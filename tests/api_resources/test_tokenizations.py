# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import TokenizationSimulateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestTokenizations:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_simulate(self, client: Lithic) -> None:
        tokenization = client.tokenizations.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
        )
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

    @parametrize
    def test_method_simulate_with_all_params(self, client: Lithic) -> None:
        tokenization = client.tokenizations.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
            account_score=5,
            device_score=5,
            wallet_recommended_decision="APPROVED",
        )
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])


class TestAsyncTokenizations:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_simulate(self, client: AsyncLithic) -> None:
        tokenization = await client.tokenizations.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
        )
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

    @parametrize
    async def test_method_simulate_with_all_params(self, client: AsyncLithic) -> None:
        tokenization = await client.tokenizations.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
            account_score=5,
            device_score=5,
            wallet_recommended_decision="APPROVED",
        )
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])
