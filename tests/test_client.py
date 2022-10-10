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

    def test_copy(self) -> None:
        copied = self.client.copy()
        assert id(copied) != id(self.client)

        copied = self.client.copy(api_key="my new api key")
        assert copied.api_key == "my new api key"
        assert self.client.api_key == api_key

    def test_copy_default_options(self) -> None:
        # options that have a default are overriden correctly
        copied = self.client.copy(max_retries=7)
        assert copied.max_retries == 7
        assert self.client.max_retries == 2

        copied2 = copied.copy(max_retries=6)
        assert copied2.max_retries == 6
        assert copied.max_retries == 7

        # timeout
        assert isinstance(self.client.timeout, httpx.Timeout)
        copied = self.client.copy(timeout=None)
        assert copied.timeout is None
        assert isinstance(self.client.timeout, httpx.Timeout)


class TestAsyncLithic:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_raw_response(self) -> None:
        response = await self.client.get("/accounts", cast_to=httpx.Response)
        assert response.status_code == 200
        assert isinstance(response, httpx.Response)

    def test_copy(self) -> None:
        copied = self.client.copy()
        assert id(copied) != id(self.client)

        copied = self.client.copy(api_key="my new api key")
        assert copied.api_key == "my new api key"
        assert self.client.api_key == api_key

    def test_copy_default_options(self) -> None:
        # options that have a default are overriden correctly
        copied = self.client.copy(max_retries=7)
        assert copied.max_retries == 7
        assert self.client.max_retries == 2

        copied2 = copied.copy(max_retries=6)
        assert copied2.max_retries == 6
        assert copied.max_retries == 7

        # timeout
        assert isinstance(self.client.timeout, httpx.Timeout)
        copied = self.client.copy(timeout=None)
        assert copied.timeout is None
        assert isinstance(self.client.timeout, httpx.Timeout)
