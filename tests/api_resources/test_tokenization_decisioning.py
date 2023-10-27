# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import TokenizationSecret, TokenizationDecisioningRotateSecretResponse
from lithic._client import Lithic, AsyncLithic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestTokenizationDecisioning:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve_secret(self, client: Lithic) -> None:
        tokenization_decisioning = client.tokenization_decisioning.retrieve_secret()
        assert_matches_type(TokenizationSecret, tokenization_decisioning, path=["response"])

    @parametrize
    def test_raw_response_retrieve_secret(self, client: Lithic) -> None:
        response = client.tokenization_decisioning.with_raw_response.retrieve_secret()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization_decisioning = response.parse()
        assert_matches_type(TokenizationSecret, tokenization_decisioning, path=["response"])

    @parametrize
    def test_method_rotate_secret(self, client: Lithic) -> None:
        tokenization_decisioning = client.tokenization_decisioning.rotate_secret()
        assert_matches_type(TokenizationDecisioningRotateSecretResponse, tokenization_decisioning, path=["response"])

    @parametrize
    def test_raw_response_rotate_secret(self, client: Lithic) -> None:
        response = client.tokenization_decisioning.with_raw_response.rotate_secret()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization_decisioning = response.parse()
        assert_matches_type(TokenizationDecisioningRotateSecretResponse, tokenization_decisioning, path=["response"])


class TestAsyncTokenizationDecisioning:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve_secret(self, client: AsyncLithic) -> None:
        tokenization_decisioning = await client.tokenization_decisioning.retrieve_secret()
        assert_matches_type(TokenizationSecret, tokenization_decisioning, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_secret(self, client: AsyncLithic) -> None:
        response = await client.tokenization_decisioning.with_raw_response.retrieve_secret()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization_decisioning = response.parse()
        assert_matches_type(TokenizationSecret, tokenization_decisioning, path=["response"])

    @parametrize
    async def test_method_rotate_secret(self, client: AsyncLithic) -> None:
        tokenization_decisioning = await client.tokenization_decisioning.rotate_secret()
        assert_matches_type(TokenizationDecisioningRotateSecretResponse, tokenization_decisioning, path=["response"])

    @parametrize
    async def test_raw_response_rotate_secret(self, client: AsyncLithic) -> None:
        response = await client.tokenization_decisioning.with_raw_response.rotate_secret()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization_decisioning = response.parse()
        assert_matches_type(TokenizationDecisioningRotateSecretResponse, tokenization_decisioning, path=["response"])
