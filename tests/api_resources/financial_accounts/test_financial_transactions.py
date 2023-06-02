# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import FinancialTransaction
from lithic._utils import parse_datetime
from lithic.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestFinancialTransactions:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        financial_transaction = client.financial_accounts.financial_transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        financial_transaction = client.financial_accounts.financial_transactions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        financial_transaction = client.financial_accounts.financial_transactions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            category="ACH",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            result="APPROVED",
            starting_after="string",
            status="DECLINED",
        )
        assert_matches_type(SyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])


class TestAsyncFinancialTransactions:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        financial_transaction = await client.financial_accounts.financial_transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        financial_transaction = await client.financial_accounts.financial_transactions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        financial_transaction = await client.financial_accounts.financial_transactions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            category="ACH",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            result="APPROVED",
            starting_after="string",
            status="DECLINED",
        )
        assert_matches_type(AsyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])
