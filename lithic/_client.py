from __future__ import annotations
import time
import asyncio
from typing import Any, Awaitable, Dict, TypeVar, Union, Optional, Type, Generic, Iterator, AsyncIterator
from typing_extensions import Literal
import httpx
import pydantic
from ._core import (
    Timeout,
    DEFAULT_MAX_RETRIES,
    DEFAULT_TIMEOUT,
    Transport,
    ProxiesTypes,
    BaseClient,
    BasePage,
    FinalRequestOptions,
    Rsp,
)
from .exceptions import make_status_error, APITimeoutError, APIConnectionError, APIResponseValidationError

Item = TypeVar("Item")
PageParams = TypeVar("PageParams")
TPage = TypeVar("TPage", bound="SyncPage")
TAsyncPage = TypeVar("TAsyncPage", bound="AsyncPage")


class SyncPage(BasePage[Item, PageParams], Generic[Item, TPage, PageParams]):
    _client: SyncAPIClient = pydantic.PrivateAttr()
    _tmodel: Type[Item] = pydantic.PrivateAttr()
    _tpage: Type[TPage] = pydantic.PrivateAttr()

    def _init_for_iter(self, client: SyncAPIClient, model: Type[Item], page: Type[TPage], options: FinalRequestOptions):
        self._client = client
        self._tmodel = model
        self._tpage = page
        self._options = options

    def __iter__(self) -> Iterator[Item]:
        for page in self._iter_pages():
            for item in page._get_page_items():
                yield item

    def _iter_pages(self) -> Iterator[TPage]:
        while True:
            yield self  # type: ignore
            if self.has_next_page():
                self = self.get_next_page()
            else:
                return

    def get_next_page(self) -> TPage:
        page_params = self._next_page_params()
        params = self._options.get("params", {}) or {}
        options = {**self._options, "params": {**params, **page_params}}
        return self._client.request_api_list(self._tmodel, self._tpage, options)


class AsyncPage(BasePage[Item, PageParams], Generic[Item, TAsyncPage, PageParams]):
    _client: AsyncAPIClient = pydantic.PrivateAttr()
    _tmodel: Type[Item] = pydantic.PrivateAttr()
    _tpage: Type[TAsyncPage] = pydantic.PrivateAttr()
    _awaited: bool = pydantic.PrivateAttr()

    def _init_for_iter(
        self, client: AsyncAPIClient, model: Type[Item], page: Type[TAsyncPage], options: FinalRequestOptions
    ):
        self._client = client
        self._tmodel = model
        self._tpage = page
        self._options = options
        self._awaited = False

    def __await__(self) -> Iterator[TAsyncPage]:
        async def awaitable() -> TAsyncPage:
            resp: TAsyncPage = await self._client.request(self._tpage, self._options)
            resp._init_for_iter(self._client, self._tmodel, self._tpage, self._options)
            self._awaited = True
            return resp

        return awaitable().__await__()

    async def _iter_pages(self) -> AsyncIterator[TAsyncPage]:
        while True:
            yield self
            if self.has_next_page():
                self = await self.get_next_page()
            else:
                return

    async def __aiter__(self) -> AsyncIterator[Item]:
        if not self._awaited:
            self = await self
        async for page in self._iter_pages():
            for item in page._get_page_items():
                yield item

    async def get_next_page(self) -> TAsyncPage:
        page_params = self._next_page_params()
        params = self._options.get("params", {}) or {}
        options = {**self._options, "params": {**params, **page_params}}
        return await self._client.request_api_list(self._tmodel, self._tpage, options)


class SyncAPIClient(BaseClient):
    _client: httpx.Client

    def __init__(
        self,
        *,
        version: str,
        base_url: str,
        api_key: str,
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        transport: Optional[Transport] = None,
        proxies: Optional[ProxiesTypes] = None,
        _strict_response_validation: bool,
    ) -> None:
        super().__init__(version, api_key, _strict_response_validation, max_retries, timeout)
        self._client = httpx.Client(base_url=base_url, timeout=timeout, proxies=proxies, transport=transport)

    def request(self, model: Type[Rsp], options: FinalRequestOptions, remaining_retries: Optional[int] = None) -> Rsp:
        retries = self.remaining_retries(remaining_retries, options)
        req_args = self.prepare_request_args(options)
        request = self._client.build_request(**req_args)

        try:
            response = self._client.send(request)
            response.raise_for_status()
        except httpx.HTTPStatusError as err:  # thrown on 4xx and 5xx status code
            if retries > 0 and self.should_retry(err.response):
                return self.retry_request(options, model, retries, err.response.headers)
            raise make_status_error(request, err.response)
        except httpx.TimeoutException as err:
            if retries > 0:
                return self.retry_request(options, model, retries)
            raise APITimeoutError(request=request) from err
        except Exception as err:
            if retries > 0:
                return self.retry_request(options, model, retries)
            raise APIConnectionError(request=request) from err

        try:
            rsp = self.process_response(model, options, response)
        except pydantic.ValidationError as err:
            raise APIResponseValidationError(request=request, response=response) from err

        return rsp

    def retry_request(
        self,
        options: FinalRequestOptions,
        model: Type[Rsp],
        remaining_retries: int,
        response_headers: Optional[httpx.Headers] = None,
    ) -> Rsp:
        remaining = remaining_retries - 1
        timeout = self.calculate_retry_timeout(remaining, options, response_headers)
        print(f"Retry request in {timeout} seconds")
        # In a synchronous context we are blocking the entire thread. Up to the library user to run the client in a
        # different thread if necessary.
        time.sleep(timeout)
        return self.request(
            options=options,
            model=model,
            remaining_retries=remaining,
        )

    def request_api_list(self, model: Type[Item], page: Type[TPage], options: FinalRequestOptions) -> TPage:
        resp: TPage = self.request(page, options)
        resp._init_for_iter(self, model, page, options)
        return resp


class AsyncAPIClient(BaseClient):
    _client: httpx.AsyncClient

    def __init__(
        self,
        *,
        version: str,
        base_url: str,
        api_key: str,
        _strict_response_validation: bool,
        max_retries: int = DEFAULT_MAX_RETRIES,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        transport: Optional[Transport] = None,
        proxies: Optional[ProxiesTypes] = None,
    ) -> None:
        super().__init__(version, api_key, _strict_response_validation, max_retries, timeout)
        self._client = httpx.AsyncClient(base_url=base_url, timeout=timeout, proxies=proxies, transport=transport)

    async def request(
        self, model: Type[Rsp], options: FinalRequestOptions, remaining_retries: Optional[int] = None
    ) -> Rsp:
        retries = self.remaining_retries(remaining_retries, options)
        req_args = self.prepare_request_args(options)
        request = self._client.build_request(**req_args)
        try:
            response = await self._client.send(request)
            response.raise_for_status()
        except httpx.HTTPStatusError as err:  # thrown on 4xx and 5xx status code
            if retries > 0 and self.should_retry(err.response):
                return await self.retry_request(options, model, retries, err.response.headers)
            raise make_status_error(request, err.response)
        except httpx.TimeoutException as err:
            if retries > 0:
                return await self.retry_request(options, model, retries)
            raise APITimeoutError(request=request) from err
        except Exception as err:
            if retries > 0:
                return await self.retry_request(options, model, retries)
            raise APIConnectionError(request=request) from err

        try:
            rsp = self.process_response(model, options, response)
        except pydantic.ValidationError as err:
            raise APIResponseValidationError(request=request, response=response) from err

        return rsp

    async def retry_request(
        self,
        options: FinalRequestOptions,
        model: Type[Rsp],
        remaining_retries: int,
        response_headers: Optional[httpx.Headers] = None,
    ) -> Rsp:
        remaining = remaining_retries - 1
        timeout = self.calculate_retry_timeout(remaining, options, response_headers)
        print(f"Retry request in {timeout} seconds")
        await asyncio.sleep(timeout)
        return await self.request(
            options=options,
            model=model,
            remaining_retries=remaining,
        )

    def request_api_list(self, model: Type[Item], page: Type[TAsyncPage], options: FinalRequestOptions) -> TAsyncPage:
        p = page.construct()  # construct() here is necessary to instanciate without triggering pydantic validation
        p._init_for_iter(self, model, page, options)
        return p
