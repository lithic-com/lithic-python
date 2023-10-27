# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import FinancialAccount
from lithic._client import Lithic, AsyncLithic
from lithic.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestFinancialAccounts:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(SyncSinglePage[FinancialAccount], financial_account, path=["response"])


class TestAsyncFinancialAccounts:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        financial_account = await client.financial_accounts.list()
        assert_matches_type(AsyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        financial_account = await client.financial_accounts.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ISSUING",
        )
        assert_matches_type(AsyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncLithic) -> None:
        response = await client.financial_accounts.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(AsyncSinglePage[FinancialAccount], financial_account, path=["response"])
