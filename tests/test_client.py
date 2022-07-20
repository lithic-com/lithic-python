# File generated from our OpenAPI spec by Stainless.

import os

import httpx

from lithic import Lithic, AsyncLithic

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLithic:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_raw_response(self) -> None:
        response = self.client.get("/accounts", cast_to=httpx.Response)
        assert response.status_code == 200
        assert isinstance(response, httpx.Response)


class TestAsyncLithic:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_raw_response(self) -> None:
        response = await self.client.get("/accounts", cast_to=httpx.Response)
        assert response.status_code == 200
        assert isinstance(response, httpx.Response)
