# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options
from ..types.api_status import *

__all__ = ["StatusResource", "AsyncStatusResource"]


class StatusResource(SyncAPIResource):
    def retrieve(
        self,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> APIStatus:
        options = make_request_options(headers, max_retries, timeout)
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
    ) -> APIStatus:
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            "/status",
            options=options,
            cast_to=APIStatus,
        )
