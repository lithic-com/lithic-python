# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Dict
from .._core import Timeout, make_request_options
from .._resource import SyncAPIResource, AsyncAPIResource
from .._models import StringModel, NoneModel
from ..pagination import SyncPage, AsyncPage
from ..types.api_status import *

__all__ = ["StatusResource", "AsyncStatusResource"]


class StatusResource(SyncAPIResource):
    def retrieve(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> APIStatus:
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.get("/status", model=APIStatus, options=options)


class AsyncStatusResource(AsyncAPIResource):
    async def retrieve(
        self,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> APIStatus:
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.get("/status", model=APIStatus, options=options)
