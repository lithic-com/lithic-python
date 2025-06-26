# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types.fraud import TransactionReportResponse, TransactionRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        transaction = client.fraud.transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.fraud.transactions.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.fraud.transactions.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_token` but received ''"):
            client.fraud.transactions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_report(self, client: Lithic) -> None:
        transaction = client.fraud.transactions.report(
            transaction_token="00000000-0000-0000-0000-000000000000",
            fraud_status="SUSPECTED_FRAUD",
        )
        assert_matches_type(TransactionReportResponse, transaction, path=["response"])

    @parametrize
    def test_method_report_with_all_params(self, client: Lithic) -> None:
        transaction = client.fraud.transactions.report(
            transaction_token="00000000-0000-0000-0000-000000000000",
            fraud_status="SUSPECTED_FRAUD",
            comment="comment",
            fraud_type="FIRST_PARTY_FRAUD",
        )
        assert_matches_type(TransactionReportResponse, transaction, path=["response"])

    @parametrize
    def test_raw_response_report(self, client: Lithic) -> None:
        response = client.fraud.transactions.with_raw_response.report(
            transaction_token="00000000-0000-0000-0000-000000000000",
            fraud_status="SUSPECTED_FRAUD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionReportResponse, transaction, path=["response"])

    @parametrize
    def test_streaming_response_report(self, client: Lithic) -> None:
        with client.fraud.transactions.with_streaming_response.report(
            transaction_token="00000000-0000-0000-0000-000000000000",
            fraud_status="SUSPECTED_FRAUD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionReportResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_report(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_token` but received ''"):
            client.fraud.transactions.with_raw_response.report(
                transaction_token="",
                fraud_status="SUSPECTED_FRAUD",
            )


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        transaction = await async_client.fraud.transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.fraud.transactions.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.fraud.transactions.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionRetrieveResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_token` but received ''"):
            await async_client.fraud.transactions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_report(self, async_client: AsyncLithic) -> None:
        transaction = await async_client.fraud.transactions.report(
            transaction_token="00000000-0000-0000-0000-000000000000",
            fraud_status="SUSPECTED_FRAUD",
        )
        assert_matches_type(TransactionReportResponse, transaction, path=["response"])

    @parametrize
    async def test_method_report_with_all_params(self, async_client: AsyncLithic) -> None:
        transaction = await async_client.fraud.transactions.report(
            transaction_token="00000000-0000-0000-0000-000000000000",
            fraud_status="SUSPECTED_FRAUD",
            comment="comment",
            fraud_type="FIRST_PARTY_FRAUD",
        )
        assert_matches_type(TransactionReportResponse, transaction, path=["response"])

    @parametrize
    async def test_raw_response_report(self, async_client: AsyncLithic) -> None:
        response = await async_client.fraud.transactions.with_raw_response.report(
            transaction_token="00000000-0000-0000-0000-000000000000",
            fraud_status="SUSPECTED_FRAUD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionReportResponse, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_report(self, async_client: AsyncLithic) -> None:
        async with async_client.fraud.transactions.with_streaming_response.report(
            transaction_token="00000000-0000-0000-0000-000000000000",
            fraud_status="SUSPECTED_FRAUD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionReportResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_report(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_token` but received ''"):
            await async_client.fraud.transactions.with_raw_response.report(
                transaction_token="",
                fraud_status="SUSPECTED_FRAUD",
            )
