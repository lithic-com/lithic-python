# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types.credit_products import ExtendedCredit

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtendedCredit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        extended_credit = client.credit_products.extended_credit.retrieve(
            "credit_product_token",
        )
        assert_matches_type(ExtendedCredit, extended_credit, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.credit_products.extended_credit.with_raw_response.retrieve(
            "credit_product_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extended_credit = response.parse()
        assert_matches_type(ExtendedCredit, extended_credit, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.credit_products.extended_credit.with_streaming_response.retrieve(
            "credit_product_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extended_credit = response.parse()
            assert_matches_type(ExtendedCredit, extended_credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_product_token` but received ''"):
            client.credit_products.extended_credit.with_raw_response.retrieve(
                "",
            )


class TestAsyncExtendedCredit:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        extended_credit = await async_client.credit_products.extended_credit.retrieve(
            "credit_product_token",
        )
        assert_matches_type(ExtendedCredit, extended_credit, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.credit_products.extended_credit.with_raw_response.retrieve(
            "credit_product_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extended_credit = response.parse()
        assert_matches_type(ExtendedCredit, extended_credit, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.credit_products.extended_credit.with_streaming_response.retrieve(
            "credit_product_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extended_credit = await response.parse()
            assert_matches_type(ExtendedCredit, extended_credit, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_product_token` but received ''"):
            await async_client.credit_products.extended_credit.with_raw_response.retrieve(
                "",
            )
