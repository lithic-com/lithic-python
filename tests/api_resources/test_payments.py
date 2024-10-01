# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    Payment,
    PaymentRetryResponse,
    PaymentCreateResponse,
    PaymentSimulateActionResponse,
    PaymentSimulateReturnResponse,
    PaymentSimulateReceiptResponse,
    PaymentSimulateReleaseResponse,
)
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        payment = client.payments.create(
            amount=1,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            method="ACH_NEXT_DAY",
            method_attributes={"sec_code": "CCD"},
            type="COLLECTION",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        payment = client.payments.create(
            amount=1,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            method="ACH_NEXT_DAY",
            method_attributes={"sec_code": "CCD"},
            type="COLLECTION",
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            memo="memo",
            user_defined_id="user_defined_id",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.payments.with_raw_response.create(
            amount=1,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            method="ACH_NEXT_DAY",
            method_attributes={"sec_code": "CCD"},
            type="COLLECTION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.payments.with_streaming_response.create(
            amount=1,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            method="ACH_NEXT_DAY",
            method_attributes={"sec_code": "CCD"},
            type="COLLECTION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentCreateResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        payment = client.payments.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.payments.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.payments.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_token` but received ''"):
            client.payments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        payment = client.payments.list()
        assert_matches_type(SyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        payment = client.payments.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            business_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category="ACH",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            result="APPROVED",
            starting_after="starting_after",
            status="DECLINED",
        )
        assert_matches_type(SyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(SyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(SyncCursorPage[Payment], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retry(self, client: Lithic) -> None:
        payment = client.payments.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentRetryResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_retry(self, client: Lithic) -> None:
        response = client.payments.with_raw_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentRetryResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_retry(self, client: Lithic) -> None:
        with client.payments.with_streaming_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentRetryResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retry(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_token` but received ''"):
            client.payments.with_raw_response.retry(
                "",
            )

    @parametrize
    def test_method_simulate_action(self, client: Lithic) -> None:
        payment = client.payments.simulate_action(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="ACH_ORIGINATION_REVIEWED",
        )
        assert_matches_type(PaymentSimulateActionResponse, payment, path=["response"])

    @parametrize
    def test_method_simulate_action_with_all_params(self, client: Lithic) -> None:
        payment = client.payments.simulate_action(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="ACH_ORIGINATION_REVIEWED",
            decline_reason="PROGRAM_TRANSACTION_LIMIT_EXCEEDED",
            return_reason_code="return_reason_code",
        )
        assert_matches_type(PaymentSimulateActionResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_simulate_action(self, client: Lithic) -> None:
        response = client.payments.with_raw_response.simulate_action(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="ACH_ORIGINATION_REVIEWED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSimulateActionResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_simulate_action(self, client: Lithic) -> None:
        with client.payments.with_streaming_response.simulate_action(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="ACH_ORIGINATION_REVIEWED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentSimulateActionResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_simulate_action(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_token` but received ''"):
            client.payments.with_raw_response.simulate_action(
                payment_token="",
                event_type="ACH_ORIGINATION_REVIEWED",
            )

    @parametrize
    def test_method_simulate_receipt(self, client: Lithic) -> None:
        payment = client.payments.simulate_receipt(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt_type="RECEIPT_CREDIT",
        )
        assert_matches_type(PaymentSimulateReceiptResponse, payment, path=["response"])

    @parametrize
    def test_method_simulate_receipt_with_all_params(self, client: Lithic) -> None:
        payment = client.payments.simulate_receipt(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt_type="RECEIPT_CREDIT",
            memo="memo",
        )
        assert_matches_type(PaymentSimulateReceiptResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_simulate_receipt(self, client: Lithic) -> None:
        response = client.payments.with_raw_response.simulate_receipt(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt_type="RECEIPT_CREDIT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSimulateReceiptResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_simulate_receipt(self, client: Lithic) -> None:
        with client.payments.with_streaming_response.simulate_receipt(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt_type="RECEIPT_CREDIT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentSimulateReceiptResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_simulate_release(self, client: Lithic) -> None:
        payment = client.payments.simulate_release(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentSimulateReleaseResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_simulate_release(self, client: Lithic) -> None:
        response = client.payments.with_raw_response.simulate_release(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSimulateReleaseResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_simulate_release(self, client: Lithic) -> None:
        with client.payments.with_streaming_response.simulate_release(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentSimulateReleaseResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_simulate_return(self, client: Lithic) -> None:
        payment = client.payments.simulate_return(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentSimulateReturnResponse, payment, path=["response"])

    @parametrize
    def test_method_simulate_return_with_all_params(self, client: Lithic) -> None:
        payment = client.payments.simulate_return(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            return_reason_code="R12",
        )
        assert_matches_type(PaymentSimulateReturnResponse, payment, path=["response"])

    @parametrize
    def test_raw_response_simulate_return(self, client: Lithic) -> None:
        response = client.payments.with_raw_response.simulate_return(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSimulateReturnResponse, payment, path=["response"])

    @parametrize
    def test_streaming_response_simulate_return(self, client: Lithic) -> None:
        with client.payments.with_streaming_response.simulate_return(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentSimulateReturnResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        payment = await async_client.payments.create(
            amount=1,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            method="ACH_NEXT_DAY",
            method_attributes={"sec_code": "CCD"},
            type="COLLECTION",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        payment = await async_client.payments.create(
            amount=1,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            method="ACH_NEXT_DAY",
            method_attributes={"sec_code": "CCD"},
            type="COLLECTION",
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            memo="memo",
            user_defined_id="user_defined_id",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.payments.with_raw_response.create(
            amount=1,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            method="ACH_NEXT_DAY",
            method_attributes={"sec_code": "CCD"},
            type="COLLECTION",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.payments.with_streaming_response.create(
            amount=1,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            method="ACH_NEXT_DAY",
            method_attributes={"sec_code": "CCD"},
            type="COLLECTION",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentCreateResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        payment = await async_client.payments.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.payments.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.payments.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_token` but received ''"):
            await async_client.payments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        payment = await async_client.payments.list()
        assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        payment = await async_client.payments.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            business_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category="ACH",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            result="APPROVED",
            starting_after="starting_after",
            status="DECLINED",
        )
        assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retry(self, async_client: AsyncLithic) -> None:
        payment = await async_client.payments.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentRetryResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncLithic) -> None:
        response = await async_client.payments.with_raw_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentRetryResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncLithic) -> None:
        async with async_client.payments.with_streaming_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentRetryResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retry(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_token` but received ''"):
            await async_client.payments.with_raw_response.retry(
                "",
            )

    @parametrize
    async def test_method_simulate_action(self, async_client: AsyncLithic) -> None:
        payment = await async_client.payments.simulate_action(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="ACH_ORIGINATION_REVIEWED",
        )
        assert_matches_type(PaymentSimulateActionResponse, payment, path=["response"])

    @parametrize
    async def test_method_simulate_action_with_all_params(self, async_client: AsyncLithic) -> None:
        payment = await async_client.payments.simulate_action(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="ACH_ORIGINATION_REVIEWED",
            decline_reason="PROGRAM_TRANSACTION_LIMIT_EXCEEDED",
            return_reason_code="return_reason_code",
        )
        assert_matches_type(PaymentSimulateActionResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_simulate_action(self, async_client: AsyncLithic) -> None:
        response = await async_client.payments.with_raw_response.simulate_action(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="ACH_ORIGINATION_REVIEWED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSimulateActionResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_simulate_action(self, async_client: AsyncLithic) -> None:
        async with async_client.payments.with_streaming_response.simulate_action(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            event_type="ACH_ORIGINATION_REVIEWED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentSimulateActionResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_simulate_action(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_token` but received ''"):
            await async_client.payments.with_raw_response.simulate_action(
                payment_token="",
                event_type="ACH_ORIGINATION_REVIEWED",
            )

    @parametrize
    async def test_method_simulate_receipt(self, async_client: AsyncLithic) -> None:
        payment = await async_client.payments.simulate_receipt(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt_type="RECEIPT_CREDIT",
        )
        assert_matches_type(PaymentSimulateReceiptResponse, payment, path=["response"])

    @parametrize
    async def test_method_simulate_receipt_with_all_params(self, async_client: AsyncLithic) -> None:
        payment = await async_client.payments.simulate_receipt(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt_type="RECEIPT_CREDIT",
            memo="memo",
        )
        assert_matches_type(PaymentSimulateReceiptResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_simulate_receipt(self, async_client: AsyncLithic) -> None:
        response = await async_client.payments.with_raw_response.simulate_receipt(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt_type="RECEIPT_CREDIT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSimulateReceiptResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_simulate_receipt(self, async_client: AsyncLithic) -> None:
        async with async_client.payments.with_streaming_response.simulate_receipt(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            receipt_type="RECEIPT_CREDIT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentSimulateReceiptResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_simulate_release(self, async_client: AsyncLithic) -> None:
        payment = await async_client.payments.simulate_release(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentSimulateReleaseResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_simulate_release(self, async_client: AsyncLithic) -> None:
        response = await async_client.payments.with_raw_response.simulate_release(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSimulateReleaseResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_simulate_release(self, async_client: AsyncLithic) -> None:
        async with async_client.payments.with_streaming_response.simulate_release(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentSimulateReleaseResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_simulate_return(self, async_client: AsyncLithic) -> None:
        payment = await async_client.payments.simulate_return(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentSimulateReturnResponse, payment, path=["response"])

    @parametrize
    async def test_method_simulate_return_with_all_params(self, async_client: AsyncLithic) -> None:
        payment = await async_client.payments.simulate_return(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            return_reason_code="R12",
        )
        assert_matches_type(PaymentSimulateReturnResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_simulate_return(self, async_client: AsyncLithic) -> None:
        response = await async_client.payments.with_raw_response.simulate_return(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSimulateReturnResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_simulate_return(self, async_client: AsyncLithic) -> None:
        async with async_client.payments.with_streaming_response.simulate_return(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentSimulateReturnResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True
