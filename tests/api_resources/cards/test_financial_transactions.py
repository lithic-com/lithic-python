# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import FinancialTransaction
from lithic._utils import parse_datetime
from lithic.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFinancialTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        financial_transaction = client.cards.financial_transactions.retrieve(
            financial_transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.cards.financial_transactions.with_raw_response.retrieve(
            financial_transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_transaction = response.parse()
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.cards.financial_transactions.with_streaming_response.retrieve(
            financial_transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_transaction = response.parse()
            assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.financial_transactions.with_raw_response.retrieve(
                financial_transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                card_token="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_transaction_token` but received ''"
        ):
            client.cards.financial_transactions.with_raw_response.retrieve(
                financial_transaction_token="",
                card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        financial_transaction = client.cards.financial_transactions.list(
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        financial_transaction = client.cards.financial_transactions.list(
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            category="CARD",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            result="APPROVED",
            starting_after="starting_after",
            status="DECLINED",
        )
        assert_matches_type(SyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.cards.financial_transactions.with_raw_response.list(
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_transaction = response.parse()
        assert_matches_type(SyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.cards.financial_transactions.with_streaming_response.list(
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_transaction = response.parse()
            assert_matches_type(SyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.financial_transactions.with_raw_response.list(
                card_token="",
            )


class TestAsyncFinancialTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        financial_transaction = await async_client.cards.financial_transactions.retrieve(
            financial_transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.cards.financial_transactions.with_raw_response.retrieve(
            financial_transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_transaction = response.parse()
        assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.cards.financial_transactions.with_streaming_response.retrieve(
            financial_transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_transaction = await response.parse()
            assert_matches_type(FinancialTransaction, financial_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.financial_transactions.with_raw_response.retrieve(
                financial_transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                card_token="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_transaction_token` but received ''"
        ):
            await async_client.cards.financial_transactions.with_raw_response.retrieve(
                financial_transaction_token="",
                card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        financial_transaction = await async_client.cards.financial_transactions.list(
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        financial_transaction = await async_client.cards.financial_transactions.list(
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            category="CARD",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            result="APPROVED",
            starting_after="starting_after",
            status="DECLINED",
        )
        assert_matches_type(AsyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.cards.financial_transactions.with_raw_response.list(
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_transaction = response.parse()
        assert_matches_type(AsyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.cards.financial_transactions.with_streaming_response.list(
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_transaction = await response.parse()
            assert_matches_type(AsyncSinglePage[FinancialTransaction], financial_transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.financial_transactions.with_raw_response.list(
                card_token="",
            )
