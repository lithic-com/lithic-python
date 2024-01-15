# File generated from our OpenAPI spec by Stainless.

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
    PaymentSimulateReturnResponse,
    PaymentSimulateReleaseResponse,
)
from lithic._utils import parse_datetime
from lithic._client import Lithic, AsyncLithic
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestPayments:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
            method_attributes={
                "company_id": "string",
                "receipt_routing_number": "string",
                "retries": 0,
                "return_reason_code": "string",
                "sec_code": "CCD",
            },
            type="COLLECTION",
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            memo="string",
            user_defined_id="string",
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
    def test_method_list(self, client: Lithic) -> None:
        payment = client.payments.list()
        assert_matches_type(SyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        payment = client.payments.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            result="APPROVED",
            starting_after="string",
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
            return_reason_code="string",
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
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncLithic) -> None:
        payment = await client.payments.create(
            amount=1,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            method="ACH_NEXT_DAY",
            method_attributes={"sec_code": "CCD"},
            type="COLLECTION",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncLithic) -> None:
        payment = await client.payments.create(
            amount=1,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            method="ACH_NEXT_DAY",
            method_attributes={
                "company_id": "string",
                "receipt_routing_number": "string",
                "retries": 0,
                "return_reason_code": "string",
                "sec_code": "CCD",
            },
            type="COLLECTION",
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            memo="string",
            user_defined_id="string",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncLithic) -> None:
        response = await client.payments.with_raw_response.create(
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
    async def test_streaming_response_create(self, client: AsyncLithic) -> None:
        async with client.payments.with_streaming_response.create(
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
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        payment = await client.payments.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncLithic) -> None:
        response = await client.payments.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncLithic) -> None:
        async with client.payments.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        payment = await client.payments.list()
        assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        payment = await client.payments.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            result="APPROVED",
            starting_after="string",
            status="DECLINED",
        )
        assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncLithic) -> None:
        response = await client.payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncLithic) -> None:
        async with client.payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retry(self, client: AsyncLithic) -> None:
        payment = await client.payments.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentRetryResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_retry(self, client: AsyncLithic) -> None:
        response = await client.payments.with_raw_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentRetryResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_retry(self, client: AsyncLithic) -> None:
        async with client.payments.with_streaming_response.retry(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentRetryResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_simulate_release(self, client: AsyncLithic) -> None:
        payment = await client.payments.simulate_release(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentSimulateReleaseResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_simulate_release(self, client: AsyncLithic) -> None:
        response = await client.payments.with_raw_response.simulate_release(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSimulateReleaseResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_simulate_release(self, client: AsyncLithic) -> None:
        async with client.payments.with_streaming_response.simulate_release(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentSimulateReleaseResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_simulate_return(self, client: AsyncLithic) -> None:
        payment = await client.payments.simulate_return(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentSimulateReturnResponse, payment, path=["response"])

    @parametrize
    async def test_method_simulate_return_with_all_params(self, client: AsyncLithic) -> None:
        payment = await client.payments.simulate_return(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            return_reason_code="string",
        )
        assert_matches_type(PaymentSimulateReturnResponse, payment, path=["response"])

    @parametrize
    async def test_raw_response_simulate_return(self, client: AsyncLithic) -> None:
        response = await client.payments.with_raw_response.simulate_return(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentSimulateReturnResponse, payment, path=["response"])

    @parametrize
    async def test_streaming_response_simulate_return(self, client: AsyncLithic) -> None:
        async with client.payments.with_streaming_response.simulate_return(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentSimulateReturnResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True
