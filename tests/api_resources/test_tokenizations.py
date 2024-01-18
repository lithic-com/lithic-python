# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import TokenizationSimulateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokenizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

    @parametrize
    def test_raw_response_simulate(self, client: Lithic) -> None:
        response = client.tokenizations.with_raw_response.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

    @parametrize
    def test_streaming_response_simulate(self, client: Lithic) -> None:
        with client.tokenizations.with_streaming_response.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = response.parse()
            assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTokenizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_simulate(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
        )
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

    @parametrize
    async def test_method_simulate_with_all_params(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
            account_score=5,
            device_score=5,
            wallet_recommended_decision="APPROVED",
        )
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

    @parametrize
    async def test_raw_response_simulate(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenizations.with_raw_response.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

    @parametrize
    async def test_streaming_response_simulate(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenizations.with_streaming_response.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = await response.parse()
            assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True
