# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import AggregateBalance
from lithic.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAggregateBalances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        aggregate_balance = client.aggregate_balances.list()
        assert_matches_type(SyncSinglePage[AggregateBalance], aggregate_balance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        aggregate_balance = client.aggregate_balances.list(
            financial_account_type="ISSUING",
        )
        assert_matches_type(SyncSinglePage[AggregateBalance], aggregate_balance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.aggregate_balances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregate_balance = response.parse()
        assert_matches_type(SyncSinglePage[AggregateBalance], aggregate_balance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.aggregate_balances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregate_balance = response.parse()
            assert_matches_type(SyncSinglePage[AggregateBalance], aggregate_balance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAggregateBalances:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        aggregate_balance = await async_client.aggregate_balances.list()
        assert_matches_type(AsyncSinglePage[AggregateBalance], aggregate_balance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        aggregate_balance = await async_client.aggregate_balances.list(
            financial_account_type="ISSUING",
        )
        assert_matches_type(AsyncSinglePage[AggregateBalance], aggregate_balance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.aggregate_balances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregate_balance = response.parse()
        assert_matches_type(AsyncSinglePage[AggregateBalance], aggregate_balance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.aggregate_balances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregate_balance = await response.parse()
            assert_matches_type(AsyncSinglePage[AggregateBalance], aggregate_balance, path=["response"])

        assert cast(Any, response.is_closed) is True
