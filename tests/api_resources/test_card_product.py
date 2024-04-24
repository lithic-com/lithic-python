# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types.card_product_credit_detail_response import CardProductCreditDetailResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardProduct:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_credit_detail(self, client: Lithic) -> None:
        card_product = client.card_product.credit_detail()
        assert_matches_type(CardProductCreditDetailResponse, card_product, path=["response"])

    @parametrize
    def test_raw_response_credit_detail(self, client: Lithic) -> None:
        response = client.card_product.with_raw_response.credit_detail()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_product = response.parse()
        assert_matches_type(CardProductCreditDetailResponse, card_product, path=["response"])

    @parametrize
    def test_streaming_response_credit_detail(self, client: Lithic) -> None:
        with client.card_product.with_streaming_response.credit_detail() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_product = response.parse()
            assert_matches_type(CardProductCreditDetailResponse, card_product, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardProduct:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_credit_detail(self, async_client: AsyncLithic) -> None:
        card_product = await async_client.card_product.credit_detail()
        assert_matches_type(CardProductCreditDetailResponse, card_product, path=["response"])

    @parametrize
    async def test_raw_response_credit_detail(self, async_client: AsyncLithic) -> None:
        response = await async_client.card_product.with_raw_response.credit_detail()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_product = response.parse()
        assert_matches_type(CardProductCreditDetailResponse, card_product, path=["response"])

    @parametrize
    async def test_streaming_response_credit_detail(self, async_client: AsyncLithic) -> None:
        async with async_client.card_product.with_streaming_response.credit_detail() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_product = await response.parse()
            assert_matches_type(CardProductCreditDetailResponse, card_product, path=["response"])

        assert cast(Any, response.is_closed) is True
