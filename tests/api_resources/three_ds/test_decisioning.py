# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types.three_ds import (
    DecisioningRetrieveSecretResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDecisioning:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_challenge_response(self, client: Lithic) -> None:
        decisioning = client.three_ds.decisioning.challenge_response(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            challenge_response="APPROVE",
        )
        assert decisioning is None

    @parametrize
    def test_raw_response_challenge_response(self, client: Lithic) -> None:
        response = client.three_ds.decisioning.with_raw_response.challenge_response(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            challenge_response="APPROVE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        decisioning = response.parse()
        assert decisioning is None

    @parametrize
    def test_streaming_response_challenge_response(self, client: Lithic) -> None:
        with client.three_ds.decisioning.with_streaming_response.challenge_response(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            challenge_response="APPROVE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            decisioning = response.parse()
            assert decisioning is None

        assert cast(Any, response.is_closed) is True

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
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_challenge_response(self, async_client: AsyncLithic) -> None:
        decisioning = await async_client.three_ds.decisioning.challenge_response(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            challenge_response="APPROVE",
        )
        assert decisioning is None

    @parametrize
    async def test_raw_response_challenge_response(self, async_client: AsyncLithic) -> None:
        response = await async_client.three_ds.decisioning.with_raw_response.challenge_response(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            challenge_response="APPROVE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        decisioning = response.parse()
        assert decisioning is None

    @parametrize
    async def test_streaming_response_challenge_response(self, async_client: AsyncLithic) -> None:
        async with async_client.three_ds.decisioning.with_streaming_response.challenge_response(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            challenge_response="APPROVE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            decisioning = await response.parse()
            assert decisioning is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_secret(self, async_client: AsyncLithic) -> None:
        decisioning = await async_client.three_ds.decisioning.retrieve_secret()
        assert_matches_type(DecisioningRetrieveSecretResponse, decisioning, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_secret(self, async_client: AsyncLithic) -> None:
        response = await async_client.three_ds.decisioning.with_raw_response.retrieve_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        decisioning = response.parse()
        assert_matches_type(DecisioningRetrieveSecretResponse, decisioning, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_secret(self, async_client: AsyncLithic) -> None:
        async with async_client.three_ds.decisioning.with_streaming_response.retrieve_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            decisioning = await response.parse()
            assert_matches_type(DecisioningRetrieveSecretResponse, decisioning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_rotate_secret(self, async_client: AsyncLithic) -> None:
        decisioning = await async_client.three_ds.decisioning.rotate_secret()
        assert decisioning is None

    @parametrize
    async def test_raw_response_rotate_secret(self, async_client: AsyncLithic) -> None:
        response = await async_client.three_ds.decisioning.with_raw_response.rotate_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        decisioning = response.parse()
        assert decisioning is None

    @parametrize
    async def test_streaming_response_rotate_secret(self, async_client: AsyncLithic) -> None:
        async with async_client.three_ds.decisioning.with_streaming_response.rotate_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            decisioning = await response.parse()
            assert decisioning is None

        assert cast(Any, response.is_closed) is True
