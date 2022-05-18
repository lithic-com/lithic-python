from __future__ import annotations
import time
from typing import Any, TypeVar, Union, Optional, Type, Generic, Generator, Iterator, AsyncIterator, Mapping, cast
from ._types import Query
from ._core import RequestOptions, FinalRequestOptions

import anyio
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
from ._types import ModelT
from .exceptions import make_status_error, APITimeoutError, APIConnectionError, APIResponseValidationError


Item = TypeVar("Item")


# TODO: make base page type vars covariant
SyncPageT = TypeVar("SyncPageT", bound="BaseSyncPage[Any]")
AsyncPageT = TypeVar("AsyncPageT", bound="BaseAsyncPage[Any]")


class BaseSyncPage(BasePage[ModelT, Mapping[str, object]], Generic[ModelT]):
    _client: SyncAPIClient = pydantic.PrivateAttr()

    def _set_private_attributes(
        self,
        client: SyncAPIClient,
        model: Type[ModelT],
        options: FinalRequestOptions,
    ) -> None:
        self._model = model
        self._client = client
        self._options = options

    # Pydantic uses a custom `__iter__` method to support casting BaseModels
    # to dictionaries. e.g. dict(model).
    # As we want to support `for item in page`, this is inherently incompatible
    # with the default pydantic behaviour. It is not possible to support both
    # use cases at once. Fortunately, this is not a big deal as all other pydantic
    # methods should continue to work as expected as there is an alternative method
    # to cast a model to a dictionary, model.dict(), which is used internally
    # by pydantic.
    def __iter__(self) -> Iterator[ModelT]:  # type: ignore
        for page in self.iter_pages():
            for item in page._get_page_items():
                yield item

    def iter_pages(self: SyncPageT) -> Iterator[SyncPageT]:
        page = self
        while True:
            yield page
            if page.has_next_page():
                page = page.get_next_page()
            else:
                return

    def get_next_page(self: SyncPageT) -> SyncPageT:
        page_params = self._next_page_params()
        params = self._options.get("params", {}) or {}

        # this explicit type hint is required as the FinalRequestOptions
        # TypedDict is incompatible with dict which is what mypy infers options
        # to be.
        options: Mapping[str, object] = {**self._options, "params": {**params, **page_params}}
        return self._client.request_api_list(
            self._model,
            page=self.__class__,
            # TODO: validate that what we pass is actually valid at runtime
            options=options,  # type: ignore
        )


class AsyncPaginator(Generic[ModelT, AsyncPageT]):
    def __init__(
        self,
        client: AsyncAPIClient,
        options: FinalRequestOptions,
        page_cls: Type[AsyncPageT],
        model: Type[ModelT],
    ) -> None:
        self._model = model
        self._client = client
        self._options = options
        self._page_cls = page_cls

    def __await__(self) -> Generator[Any, None, AsyncPageT]:
        return self._get_page().__await__()

    async def _get_page(self) -> AsyncPageT:
        page = await self._client.request(self._page_cls, self._options)
        page._set_private_attributes(  # pyright: ignore[reportPrivateUsage]
            model=self._model,
            options=self._options,
            client=self._client,
        )
        return page

    async def __aiter__(self) -> AsyncIterator[ModelT]:
        # https://github.com/microsoft/pyright/issues/3464
        page = cast(
            AsyncPageT,
            await self,  # type: ignore
        )
        async for item in page:
            yield item


class BaseAsyncPage(BasePage[ModelT, Mapping[str, object]], Generic[ModelT]):
    _client: AsyncAPIClient = pydantic.PrivateAttr()

    def _set_private_attributes(
        self,
        model: Type[ModelT],
        client: AsyncAPIClient,
        options: FinalRequestOptions,
    ) -> None:
        self._model = model
        self._client = client
        self._options = options

    async def __aiter__(self) -> AsyncIterator[ModelT]:
        async for page in self.iter_pages():
            for item in page._get_page_items():
                yield item

    async def iter_pages(self: AsyncPageT) -> AsyncIterator[AsyncPageT]:
        page = self
        while True:
            yield page
            if page.has_next_page():
                page = await page.get_next_page()
            else:
                return

    async def get_next_page(self: AsyncPageT) -> AsyncPageT:
        page_params = self._next_page_params()
        params = self._options.get("params", {}) or {}

        # this explicit type hint is required as the FinalRequestOptions
        # TypedDict is incompatible with dict which is what mypy infers options
        # to be.
        options: Mapping[str, object] = {**self._options, "params": {**params, **page_params}}
        return await self._client.request_api_list(
            self._model,
            page=self.__class__,
            # TODO: validate that what we pass is actually valid at runtime
            options=options,  # type: ignore
        )


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
        self._client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            proxies=proxies,  # type: ignore
            transport=transport,  # type: ignore
            headers={"Accept": "application/json"},
        )

    def request(self, model: Type[Rsp], options: FinalRequestOptions, remaining_retries: Optional[int] = None) -> Rsp:
        retries = self.remaining_retries(remaining_retries, options)
        req_args = self.prepare_request_args(options)

        # https://github.com/encode/httpx/discussions/2181
        request = self._client.build_request(**req_args)  # pyright: ignore[reportUnknownMemberType]

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

    def request_api_list(
        self,
        model: Type[ModelT],
        page: Type[SyncPageT],
        options: FinalRequestOptions,
    ) -> SyncPageT:
        resp = self.request(page, options)
        resp._set_private_attributes(  # pyright: ignore[reportPrivateUsage]
            client=self,
            model=model,
            options=options,
        )
        return resp

    def get(self, path: str, *, query: Query | None = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="get", url=path, params=query, **options)  # type: ignore[misc]
        return self.request(model, opts)

    def post(self, path: str, *, body: Query | None = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="post", url=path, json=body, **options)  # type: ignore[misc]
        return self.request(model, opts)

    def patch(self, path: str, *, body: Query | None = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="patch", url=path, json=body, **options)  # type: ignore[misc]
        return self.request(model, opts)

    def put(self, path: str, *, body: Query | None = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="put", url=path, json=body, **options)  # type: ignore[misc]
        return self.request(model, opts)

    def delete(self, path: str, *, body: Query | None = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="delete", url=path, json=body, **options)  # type: ignore[misc]
        return self.request(model, opts)

    def get_api_list(
        self,
        path: str,
        *,
        query: Query | None = None,
        model: Type[ModelT],
        page: Type[SyncPageT],
        options: RequestOptions,
    ) -> SyncPageT:
        opts = FinalRequestOptions(method="get", url=path, params=query, **options)  # type: ignore[misc]
        return self.request_api_list(model, page, opts)


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
        self._client = httpx.AsyncClient(
            base_url=base_url,
            timeout=timeout,
            proxies=proxies,  # type: ignore
            transport=transport,  # type: ignore
            headers={"Accept": "application/json"},
        )

    async def request(
        self, model: Type[Rsp], options: FinalRequestOptions, remaining_retries: Optional[int] = None
    ) -> Rsp:
        retries = self.remaining_retries(remaining_retries, options)
        req_args = self.prepare_request_args(options)

        # https://github.com/encode/httpx/discussions/2181
        request = self._client.build_request(**req_args)  # pyright: ignore[reportUnknownMemberType]

        try:
            response = await self._client.send(request)
            response.raise_for_status()
        except httpx.HTTPStatusError as err:  # thrown on 4xx and 5xx status code
            if retries > 0 and self.should_retry(err.response):
                return await self.retry_request(options, model, retries, err.response.headers)
            raise make_status_error(request, err.response)
        except httpx.ConnectTimeout as err:
            if retries > 0:
                return await self.retry_request(options, model, retries)
            raise APITimeoutError(request=request) from err
        except httpx.ReadTimeout as err:
            # We explicitly do not retry on ReadTimeout errors as this means
            # that the server processing the request has taken 60 seconds
            # (our default timeout). This likely indicates that something
            # is not working as expected on the server side.
            raise
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
        await anyio.sleep(timeout)
        return await self.request(
            options=options,
            model=model,
            remaining_retries=remaining,
        )

    def request_api_list(
        self,
        model: Type[ModelT],
        page: Type[AsyncPageT],
        options: FinalRequestOptions,
    ) -> AsyncPaginator[ModelT, AsyncPageT]:
        return AsyncPaginator(client=self, options=options, page_cls=page, model=model)

    async def get(self, path: str, *, query: Query | None = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="get", url=path, params=query, **options)  # type: ignore[misc]
        return await self.request(model, opts)

    async def post(self, path: str, *, body: Query | None = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="post", url=path, json=body, **options)  # type: ignore[misc]
        return await self.request(model, opts)

    async def patch(self, path: str, *, body: Query | None = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="patch", url=path, json=body, **options)  # type: ignore[misc]
        return await self.request(model, opts)

    async def put(self, path: str, *, body: Query | None = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="put", url=path, json=body, **options)  # type: ignore[misc]
        return await self.request(model, opts)

    async def delete(self, path: str, *, body: Query | None = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="delete", url=path, json=body, **options)  # type: ignore[misc]
        return await self.request(model, opts)

    def get_api_list(
        self,
        path: str,
        *,
        query: Query | None = None,
        model: Type[ModelT],
        page: Type[AsyncPageT],
        options: RequestOptions,
    ) -> AsyncPaginator[ModelT, AsyncPageT]:
        opts = FinalRequestOptions(method="get", url=path, params=query, **options)  # type: ignore[misc]
        return self.request_api_list(model, page, opts)
