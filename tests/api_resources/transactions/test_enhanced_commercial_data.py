# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types.transactions import EnhancedCommercialDataRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEnhancedCommercialData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        enhanced_commercial_data = client.transactions.enhanced_commercial_data.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnhancedCommercialDataRetrieveResponse, enhanced_commercial_data, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.transactions.enhanced_commercial_data.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enhanced_commercial_data = response.parse()
        assert_matches_type(EnhancedCommercialDataRetrieveResponse, enhanced_commercial_data, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.transactions.enhanced_commercial_data.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enhanced_commercial_data = response.parse()
            assert_matches_type(EnhancedCommercialDataRetrieveResponse, enhanced_commercial_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_token` but received ''"):
            client.transactions.enhanced_commercial_data.with_raw_response.retrieve(
                "",
            )


class TestAsyncEnhancedCommercialData:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        enhanced_commercial_data = await async_client.transactions.enhanced_commercial_data.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(EnhancedCommercialDataRetrieveResponse, enhanced_commercial_data, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.transactions.enhanced_commercial_data.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        enhanced_commercial_data = response.parse()
        assert_matches_type(EnhancedCommercialDataRetrieveResponse, enhanced_commercial_data, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.transactions.enhanced_commercial_data.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            enhanced_commercial_data = await response.parse()
            assert_matches_type(EnhancedCommercialDataRetrieveResponse, enhanced_commercial_data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_token` but received ''"):
            await async_client.transactions.enhanced_commercial_data.with_raw_response.retrieve(
                "",
            )
