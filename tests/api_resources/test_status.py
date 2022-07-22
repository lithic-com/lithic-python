# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from lithic import Lithic, AsyncLithic
from lithic.types.api_status import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestStatus:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_retrieve(self) -> None:
        resource = self.client.status.retrieve()
        assert isinstance(resource, APIStatus)


class TestAsyncStatus:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.status.retrieve()
        assert isinstance(resource, APIStatus)
