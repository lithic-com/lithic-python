# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import FinancialAccount
from lithic.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFinancialAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        financial_account = client.financial_accounts.list()
        assert_matches_type(SyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        financial_account = client.financial_accounts.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ISSUING",
        )
        assert_matches_type(SyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.financial_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(SyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.financial_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = response.parse()
            assert_matches_type(SyncSinglePage[FinancialAccount], financial_account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFinancialAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        financial_account = await async_client.financial_accounts.list()
        assert_matches_type(AsyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        financial_account = await async_client.financial_accounts.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ISSUING",
        )
        assert_matches_type(AsyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(AsyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = await response.parse()
            assert_matches_type(AsyncSinglePage[FinancialAccount], financial_account, path=["response"])

        assert cast(Any, response.is_closed) is True
