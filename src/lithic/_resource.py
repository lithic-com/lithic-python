# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._client import Lithic, AsyncLithic


class SyncAPIResource:
    _client: Lithic

    def __init__(self, client: Lithic) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list


class AsyncAPIResource:
    _client: AsyncLithic

    def __init__(self, client: AsyncLithic) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list
