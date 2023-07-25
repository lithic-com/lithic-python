# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import Payment, PaymentCreateResponse, PaymentSimulateReleaseResponse
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


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
            method_attributes={"sec_code": "PPD"},
            type="PAYMENT",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        payment = client.payments.create(
            amount=1,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            method="ACH_NEXT_DAY",
            method_attributes={"sec_code": "PPD"},
            type="PAYMENT",
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            memo="string",
            user_defined_id="string",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        payment = client.payments.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        payment = client.payments.list()
        assert_matches_type(SyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        payment = client.payments.list(
            ending_before="string",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            result="APPROVED",
            starting_after="string",
            status="PENDING",
        )
        assert_matches_type(SyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    def test_method_simulate_release(self, client: Lithic) -> None:
        payment = client.payments.simulate_release(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentSimulateReleaseResponse, payment, path=["response"])


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
            method_attributes={"sec_code": "PPD"},
            type="PAYMENT",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncLithic) -> None:
        payment = await client.payments.create(
            amount=1,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            method="ACH_NEXT_DAY",
            method_attributes={"sec_code": "PPD"},
            type="PAYMENT",
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            memo="string",
            user_defined_id="string",
        )
        assert_matches_type(PaymentCreateResponse, payment, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        payment = await client.payments.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        payment = await client.payments.list()
        assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        payment = await client.payments.list(
            ending_before="string",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            result="APPROVED",
            starting_after="string",
            status="PENDING",
        )
        assert_matches_type(AsyncCursorPage[Payment], payment, path=["response"])

    @parametrize
    async def test_method_simulate_release(self, client: AsyncLithic) -> None:
        payment = await client.payments.simulate_release(
            payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PaymentSimulateReleaseResponse, payment, path=["response"])
