# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import AggregateBalance
from lithic.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAggregateBalances:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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


class TestAsyncAggregateBalances:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        aggregate_balance = await client.aggregate_balances.list()
        assert_matches_type(AsyncSinglePage[AggregateBalance], aggregate_balance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        aggregate_balance = await client.aggregate_balances.list(
            financial_account_type="ISSUING",
        )
        assert_matches_type(AsyncSinglePage[AggregateBalance], aggregate_balance, path=["response"])
