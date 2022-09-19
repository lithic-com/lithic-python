# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options
from ..types.api_status import APIStatus

__all__ = ["StatusResource", "AsyncStatusResource"]


class StatusResource(SyncAPIResource):
    def retrieve(
        self,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> APIStatus:
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            "/status",
            options=options,
            cast_to=APIStatus,
        )


class AsyncStatusResource(AsyncAPIResource):
    async def retrieve(
        self,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> APIStatus:
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            "/status",
            options=options,
            cast_to=APIStatus,
        )
