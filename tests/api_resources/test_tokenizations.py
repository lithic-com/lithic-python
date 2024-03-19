# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    Tokenization,
    TokenizationRetrieveResponse,
    TokenizationSimulateResponse,
)
from lithic._utils import parse_date
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokenizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        tokenization = client.tokenizations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TokenizationRetrieveResponse, tokenization, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.tokenizations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(TokenizationRetrieveResponse, tokenization, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.tokenizations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = response.parse()
            assert_matches_type(TokenizationRetrieveResponse, tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            client.tokenizations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        tokenization = client.tokenizations.list()
        assert_matches_type(SyncCursorPage[Tokenization], tokenization, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        tokenization = client.tokenizations.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_date("2019-12-27"),
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end=parse_date("2019-12-27"),
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(SyncCursorPage[Tokenization], tokenization, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.tokenizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(SyncCursorPage[Tokenization], tokenization, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.tokenizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = response.parse()
            assert_matches_type(SyncCursorPage[Tokenization], tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True

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
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TokenizationRetrieveResponse, tokenization, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenizations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(TokenizationRetrieveResponse, tokenization, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenizations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = await response.parse()
            assert_matches_type(TokenizationRetrieveResponse, tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            await async_client.tokenizations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.list()
        assert_matches_type(AsyncCursorPage[Tokenization], tokenization, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_date("2019-12-27"),
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end=parse_date("2019-12-27"),
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(AsyncCursorPage[Tokenization], tokenization, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(AsyncCursorPage[Tokenization], tokenization, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = await response.parse()
            assert_matches_type(AsyncCursorPage[Tokenization], tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True

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
