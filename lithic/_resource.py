from typing import Type, Generic, List, TypeVar
from ._core import FinalRequestOptions, RequestOptions, Rsp, Req
from ._client import SyncAPIClient, AsyncAPIClient, SyncPage, Item, TPage, TAsyncPage


class SyncAPIResource:
    _client: SyncAPIClient

    def __init__(self, client: SyncAPIClient):
        self._client = client

    def get(self, path: str, *, query: Req = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="get", url=path, params=query, **options)  # type: ignore[misc]
        return self._client.request(model, opts)

    def post(self, path: str, *, body: Req = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="post", url=path, json=body, **options)  # type: ignore[misc]
        return self._client.request(model, opts)

    def patch(self, path: str, *, body: Req = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="patch", url=path, json=body, **options)  # type: ignore[misc]
        return self._client.request(model, opts)

    def put(self, path: str, *, body: Req = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="put", url=path, json=body, **options)  # type: ignore[misc]
        return self._client.request(model, opts)

    def delete(self, path: str, *, body: Req = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="delete", url=path, json=body, **options)  # type: ignore[misc]
        return self._client.request(model, opts)

    def get_api_list(
        self, path: str, *, query: Req = None, model: Type[Item], page: Type[TPage], options: RequestOptions
    ) -> TPage:
        opts = FinalRequestOptions(method="get", url=path, params=query, **options)  # type: ignore[misc]
        return self._client.request_api_list(model, page, opts)


class AsyncAPIResource:
    _client: AsyncAPIClient

    def __init__(self, client: AsyncAPIClient):
        self._client = client

    async def get(self, path: str, *, query: Req = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="get", url=path, params=query, **options)  # type: ignore[misc]
        return await self._client.request(model, opts)

    async def post(self, path: str, *, body: Req = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="post", url=path, json=body, **options)  # type: ignore[misc]
        return await self._client.request(model, opts)

    async def patch(self, path: str, *, body: Req = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="patch", url=path, json=body, **options)  # type: ignore[misc]
        return await self._client.request(model, opts)

    async def put(self, path: str, *, body: Req = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="put", url=path, json=body, **options)  # type: ignore[misc]
        return await self._client.request(model, opts)

    async def delete(self, path: str, *, body: Req = None, model: Type[Rsp], options: RequestOptions) -> Rsp:
        opts = FinalRequestOptions(method="delete", url=path, json=body, **options)  # type: ignore[misc]
        return await self._client.request(model, opts)

    def get_api_list(
        self, path: str, *, query: Req = None, model: Type[Item], page: Type[TAsyncPage], options: RequestOptions
    ) -> TAsyncPage:
        opts = FinalRequestOptions(method="get", url=path, params=query, **options)  # type: ignore[misc]
        return self._client.request_api_list(model, page, opts)
