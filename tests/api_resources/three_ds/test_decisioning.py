# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic._client import Lithic, AsyncLithic
from lithic.types.three_ds import DecisioningRetrieveSecretResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestDecisioning:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve_secret(self, client: Lithic) -> None:
        decisioning = client.three_ds.decisioning.retrieve_secret()
        assert_matches_type(DecisioningRetrieveSecretResponse, decisioning, path=["response"])

    @parametrize
    def test_raw_response_retrieve_secret(self, client: Lithic) -> None:
        response = client.three_ds.decisioning.with_raw_response.retrieve_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        decisioning = response.parse()
        assert_matches_type(DecisioningRetrieveSecretResponse, decisioning, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_secret(self, client: Lithic) -> None:
        with client.three_ds.decisioning.with_streaming_response.retrieve_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            decisioning = response.parse()
            assert_matches_type(DecisioningRetrieveSecretResponse, decisioning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_rotate_secret(self, client: Lithic) -> None:
        decisioning = client.three_ds.decisioning.rotate_secret()
        assert decisioning is None

    @parametrize
    def test_raw_response_rotate_secret(self, client: Lithic) -> None:
        response = client.three_ds.decisioning.with_raw_response.rotate_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        decisioning = response.parse()
        assert decisioning is None

    @parametrize
    def test_streaming_response_rotate_secret(self, client: Lithic) -> None:
        with client.three_ds.decisioning.with_streaming_response.rotate_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            decisioning = response.parse()
            assert decisioning is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDecisioning:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve_secret(self, client: AsyncLithic) -> None:
        decisioning = await client.three_ds.decisioning.retrieve_secret()
        assert_matches_type(DecisioningRetrieveSecretResponse, decisioning, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_secret(self, client: AsyncLithic) -> None:
        response = await client.three_ds.decisioning.with_raw_response.retrieve_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        decisioning = response.parse()
        assert_matches_type(DecisioningRetrieveSecretResponse, decisioning, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_secret(self, client: AsyncLithic) -> None:
        async with client.three_ds.decisioning.with_streaming_response.retrieve_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            decisioning = await response.parse()
            assert_matches_type(DecisioningRetrieveSecretResponse, decisioning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_rotate_secret(self, client: AsyncLithic) -> None:
        decisioning = await client.three_ds.decisioning.rotate_secret()
        assert decisioning is None

    @parametrize
    async def test_raw_response_rotate_secret(self, client: AsyncLithic) -> None:
        response = await client.three_ds.decisioning.with_raw_response.rotate_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        decisioning = response.parse()
        assert decisioning is None

    @parametrize
    async def test_streaming_response_rotate_secret(self, client: AsyncLithic) -> None:
        async with client.three_ds.decisioning.with_streaming_response.rotate_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            decisioning = await response.parse()
            assert decisioning is None

        assert cast(Any, response.is_closed) is True
