# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import Balance
from lithic._utils import parse_datetime
from lithic.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBalances:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        balance = client.balances.list()
        assert_matches_type(SyncSinglePage[Balance], balance, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        balance = client.balances.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            balance_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            business_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_type="ISSUING",
        )
        assert_matches_type(SyncSinglePage[Balance], balance, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.balances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(SyncSinglePage[Balance], balance, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.balances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = response.parse()
            assert_matches_type(SyncSinglePage[Balance], balance, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBalances:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        balance = await async_client.balances.list()
        assert_matches_type(AsyncSinglePage[Balance], balance, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        balance = await async_client.balances.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            balance_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            business_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_type="ISSUING",
        )
        assert_matches_type(AsyncSinglePage[Balance], balance, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.balances.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        balance = response.parse()
        assert_matches_type(AsyncSinglePage[Balance], balance, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.balances.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            balance = await response.parse()
            assert_matches_type(AsyncSinglePage[Balance], balance, path=["response"])

        assert cast(Any, response.is_closed) is True
