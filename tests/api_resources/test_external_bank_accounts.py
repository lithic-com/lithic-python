# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    ExternalBankAccountListResponse,
    ExternalBankAccountCreateResponse,
    ExternalBankAccountUpdateResponse,
    ExternalBankAccountRetrieveResponse,
)
from lithic._utils import parse_date
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestExternalBankAccounts:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_overload_1(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.create(
            owner="x",
            owner_type="INDIVIDUAL",
            processor_token="x",
            verification_method="MANUAL",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.create(
            owner="x",
            owner_type="INDIVIDUAL",
            processor_token="x",
            verification_method="MANUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="x",
            dob=parse_date("2019-12-27"),
            doing_business_as="string",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_method_create_overload_2(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.create(
            account_number="string",
            country="USD",
            currency="USD",
            owner="x",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="MANUAL",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.create(
            account_number="string",
            country="USD",
            currency="USD",
            owner="x",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="MANUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "x",
                "address2": "x",
                "city": "x",
                "state": "xx",
                "postal_code": "11201",
                "country": "USD",
            },
            company_id="x",
            dob=parse_date("2019-12-27"),
            doing_business_as="string",
            name="x",
            verification_enforcement=True,
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountRetrieveResponse, external_bank_account, path=["response"])

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountUpdateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "x",
                "address2": "x",
                "city": "x",
                "state": "xx",
                "postal_code": "11201",
                "country": "USD",
            },
            company_id="x",
            dob=parse_date("2019-12-27"),
            doing_business_as="string",
            name="x",
            owner="x",
            owner_type="INDIVIDUAL",
        )
        assert_matches_type(ExternalBankAccountUpdateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.list()
        assert_matches_type(SyncCursorPage[ExternalBankAccountListResponse], external_bank_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_types=["CHECKING", "CHECKING", "CHECKING"],
            countries=["string", "string", "string"],
            ending_before="string",
            owner_types=["INDIVIDUAL", "INDIVIDUAL", "INDIVIDUAL"],
            page_size=1,
            starting_after="string",
            states=["ENABLED", "ENABLED", "ENABLED"],
            verification_states=["PENDING", "PENDING", "PENDING"],
        )
        assert_matches_type(SyncCursorPage[ExternalBankAccountListResponse], external_bank_account, path=["response"])


class TestAsyncExternalBankAccounts:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_overload_1(self, client: AsyncLithic) -> None:
        external_bank_account = await client.external_bank_accounts.create(
            owner="x",
            owner_type="INDIVIDUAL",
            processor_token="x",
            verification_method="MANUAL",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, client: AsyncLithic) -> None:
        external_bank_account = await client.external_bank_accounts.create(
            owner="x",
            owner_type="INDIVIDUAL",
            processor_token="x",
            verification_method="MANUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="x",
            dob=parse_date("2019-12-27"),
            doing_business_as="string",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_method_create_overload_2(self, client: AsyncLithic) -> None:
        external_bank_account = await client.external_bank_accounts.create(
            account_number="string",
            country="USD",
            currency="USD",
            owner="x",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="MANUAL",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, client: AsyncLithic) -> None:
        external_bank_account = await client.external_bank_accounts.create(
            account_number="string",
            country="USD",
            currency="USD",
            owner="x",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="MANUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "x",
                "address2": "x",
                "city": "x",
                "state": "xx",
                "postal_code": "11201",
                "country": "USD",
            },
            company_id="x",
            dob=parse_date("2019-12-27"),
            doing_business_as="string",
            name="x",
            verification_enforcement=True,
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        external_bank_account = await client.external_bank_accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountRetrieveResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncLithic) -> None:
        external_bank_account = await client.external_bank_accounts.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountUpdateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncLithic) -> None:
        external_bank_account = await client.external_bank_accounts.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "x",
                "address2": "x",
                "city": "x",
                "state": "xx",
                "postal_code": "11201",
                "country": "USD",
            },
            company_id="x",
            dob=parse_date("2019-12-27"),
            doing_business_as="string",
            name="x",
            owner="x",
            owner_type="INDIVIDUAL",
        )
        assert_matches_type(ExternalBankAccountUpdateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        external_bank_account = await client.external_bank_accounts.list()
        assert_matches_type(AsyncCursorPage[ExternalBankAccountListResponse], external_bank_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        external_bank_account = await client.external_bank_accounts.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_types=["CHECKING", "CHECKING", "CHECKING"],
            countries=["string", "string", "string"],
            ending_before="string",
            owner_types=["INDIVIDUAL", "INDIVIDUAL", "INDIVIDUAL"],
            page_size=1,
            starting_after="string",
            states=["ENABLED", "ENABLED", "ENABLED"],
            verification_states=["PENDING", "PENDING", "PENDING"],
        )
        assert_matches_type(AsyncCursorPage[ExternalBankAccountListResponse], external_bank_account, path=["response"])
