# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.pagination import SyncSinglePage, AsyncSinglePage
from lithic.types.cards import AggregateBalanceListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestAggregateBalances:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        aggregate_balance = client.cards.aggregate_balances.list()
        assert_matches_type(SyncSinglePage[AggregateBalanceListResponse], aggregate_balance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        aggregate_balance = client.cards.aggregate_balances.list(
            account_token="string",
            business_account_token="string",
        )
        assert_matches_type(SyncSinglePage[AggregateBalanceListResponse], aggregate_balance, path=["response"])


class TestAsyncAggregateBalances:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        aggregate_balance = await client.cards.aggregate_balances.list()
        assert_matches_type(AsyncSinglePage[AggregateBalanceListResponse], aggregate_balance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        aggregate_balance = await client.cards.aggregate_balances.list(
            account_token="string",
            business_account_token="string",
        )
        assert_matches_type(AsyncSinglePage[AggregateBalanceListResponse], aggregate_balance, path=["response"])
