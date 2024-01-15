# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import FinancialTransaction
from lithic._utils import parse_datetime
from lithic._client import Lithic, AsyncLithic
from lithic.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestFinancialTransactions:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        financial_transaction = client.cards.financial_transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.cards.financial_transactions.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_transaction = response.parse()
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.cards.financial_transactions.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_transaction = response.parse()
            assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        financial_transaction = client.cards.financial_transactions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        financial_transaction = client.cards.financial_transactions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            category="CARD",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            result="APPROVED",
            starting_after="string",
            status="DECLINED",
        )
        assert_matches_type(SyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.cards.financial_transactions.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_transaction = response.parse()
        assert_matches_type(SyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.cards.financial_transactions.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_transaction = response.parse()
            assert_matches_type(SyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFinancialTransactions:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        financial_transaction = await client.cards.financial_transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncLithic) -> None:
        response = await client.cards.financial_transactions.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_transaction = response.parse()
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncLithic) -> None:
        async with client.cards.financial_transactions.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_transaction = await response.parse()
            assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        financial_transaction = await client.cards.financial_transactions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        financial_transaction = await client.cards.financial_transactions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            category="CARD",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            result="APPROVED",
            starting_after="string",
            status="DECLINED",
        )
        assert_matches_type(AsyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncLithic) -> None:
        response = await client.cards.financial_transactions.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_transaction = response.parse()
        assert_matches_type(AsyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncLithic) -> None:
        async with client.cards.financial_transactions.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_transaction = await response.parse()
            assert_matches_type(AsyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
