# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import TokenizationSecret, TokenizationDecisioningRotateSecretResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokenizationDecisioning:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_secret(self, client: Lithic) -> None:
        tokenization_decisioning = client.tokenization_decisioning.retrieve_secret()
        assert_matches_type(TokenizationSecret, tokenization_decisioning, path=["response"])

    @parametrize
    def test_raw_response_retrieve_secret(self, client: Lithic) -> None:
        response = client.tokenization_decisioning.with_raw_response.retrieve_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization_decisioning = response.parse()
        assert_matches_type(TokenizationSecret, tokenization_decisioning, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_secret(self, client: Lithic) -> None:
        with client.tokenization_decisioning.with_streaming_response.retrieve_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization_decisioning = response.parse()
            assert_matches_type(TokenizationSecret, tokenization_decisioning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_rotate_secret(self, client: Lithic) -> None:
        tokenization_decisioning = client.tokenization_decisioning.rotate_secret()
        assert_matches_type(TokenizationDecisioningRotateSecretResponse, tokenization_decisioning, path=["response"])

    @parametrize
    def test_raw_response_rotate_secret(self, client: Lithic) -> None:
        response = client.tokenization_decisioning.with_raw_response.rotate_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization_decisioning = response.parse()
        assert_matches_type(TokenizationDecisioningRotateSecretResponse, tokenization_decisioning, path=["response"])

    @parametrize
    def test_streaming_response_rotate_secret(self, client: Lithic) -> None:
        with client.tokenization_decisioning.with_streaming_response.rotate_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization_decisioning = response.parse()
            assert_matches_type(
                TokenizationDecisioningRotateSecretResponse, tokenization_decisioning, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncTokenizationDecisioning:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve_secret(self, async_client: AsyncLithic) -> None:
        tokenization_decisioning = await async_client.tokenization_decisioning.retrieve_secret()
        assert_matches_type(TokenizationSecret, tokenization_decisioning, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_secret(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenization_decisioning.with_raw_response.retrieve_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization_decisioning = response.parse()
        assert_matches_type(TokenizationSecret, tokenization_decisioning, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_secret(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenization_decisioning.with_streaming_response.retrieve_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization_decisioning = await response.parse()
            assert_matches_type(TokenizationSecret, tokenization_decisioning, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_rotate_secret(self, async_client: AsyncLithic) -> None:
        tokenization_decisioning = await async_client.tokenization_decisioning.rotate_secret()
        assert_matches_type(TokenizationDecisioningRotateSecretResponse, tokenization_decisioning, path=["response"])

    @parametrize
    async def test_raw_response_rotate_secret(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenization_decisioning.with_raw_response.rotate_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization_decisioning = response.parse()
        assert_matches_type(TokenizationDecisioningRotateSecretResponse, tokenization_decisioning, path=["response"])

    @parametrize
    async def test_streaming_response_rotate_secret(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenization_decisioning.with_streaming_response.rotate_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization_decisioning = await response.parse()
            assert_matches_type(
                TokenizationDecisioningRotateSecretResponse, tokenization_decisioning, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
