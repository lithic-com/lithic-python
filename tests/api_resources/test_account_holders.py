# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    AccountHolder,
    AccountHolderDocument,
    AccountHolderUpdateResponse,
    AccountHolderListDocumentsResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccountHolders:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create_overload_1(self, client: Lithic) -> None:
        account_holder = client.account_holders.create(
            beneficial_owner_entities=[
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "phone_numbers": ["+12124007676"],
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "phone_numbers": ["+12124007676"],
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "phone_numbers": ["+12124007676"],
                },
            ],
            beneficial_owner_individuals=[
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-23-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-23-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-23-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
            ],
            business_entity={
                "address": {
                    "address1": "123 Old Forest Way",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "government_id": "114-123-1513",
                "legal_business_name": "Acme, Inc.",
                "phone_numbers": ["+12124007676"],
            },
            control_person={
                "address": {
                    "address1": "123 Old Forest Way",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "dob": "1991-03-08 08:00:00",
                "email": "tom@middle-earth.com",
                "first_name": "Tom",
                "government_id": "111-23-1412",
                "last_name": "Bombadil",
                "phone_number": "+12124007676",
            },
            nature_of_business="Software company selling solutions to the restaurant industry",
            tos_timestamp="2018-05-29T21:16:05Z",
            workflow="KYB_BASIC",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Lithic) -> None:
        account_holder = client.account_holders.create(
            beneficial_owner_entities=[
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "string",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dba_business_name": "string",
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "parent_company": "string",
                    "phone_numbers": ["+12124007676"],
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "string",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dba_business_name": "string",
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "parent_company": "string",
                    "phone_numbers": ["+12124007676"],
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "string",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dba_business_name": "string",
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "parent_company": "string",
                    "phone_numbers": ["+12124007676"],
                },
            ],
            beneficial_owner_individuals=[
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "string",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-23-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "string",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-23-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "string",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-23-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
            ],
            business_entity={
                "address": {
                    "address1": "123 Old Forest Way",
                    "address2": "string",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "dba_business_name": "string",
                "government_id": "114-123-1513",
                "legal_business_name": "Acme, Inc.",
                "parent_company": "string",
                "phone_numbers": ["+12124007676"],
            },
            control_person={
                "address": {
                    "address1": "123 Old Forest Way",
                    "address2": "string",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "dob": "1991-03-08 08:00:00",
                "email": "tom@middle-earth.com",
                "first_name": "Tom",
                "government_id": "111-23-1412",
                "last_name": "Bombadil",
                "phone_number": "+12124007676",
            },
            nature_of_business="Software company selling solutions to the restaurant industry",
            tos_timestamp="2018-05-29T21:16:05Z",
            workflow="KYB_BASIC",
            kyb_passed_timestamp="2018-05-29T21:16:05Z",
            website_url="www.mybusiness.com",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    def test_method_create_overload_2(self, client: Lithic) -> None:
        account_holder = client.account_holders.create(
            individual={
                "address": {
                    "address1": "123 Old Forest Way",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "dob": "1991-03-08 08:00:00",
                "email": "tom@middle-earth.com",
                "first_name": "Tom",
                "government_id": "111-23-1412",
                "last_name": "Bombadil",
                "phone_number": "+12124007676",
            },
            tos_timestamp="string",
            workflow="KYC_ADVANCED",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Lithic) -> None:
        account_holder = client.account_holders.create(
            individual={
                "address": {
                    "address1": "123 Old Forest Way",
                    "address2": "string",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "dob": "1991-03-08 08:00:00",
                "email": "tom@middle-earth.com",
                "first_name": "Tom",
                "government_id": "111-23-1412",
                "last_name": "Bombadil",
                "phone_number": "+12124007676",
            },
            tos_timestamp="string",
            workflow="KYC_ADVANCED",
            kyc_passed_timestamp="string",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    def test_method_create_overload_3(self, client: Lithic) -> None:
        account_holder = client.account_holders.create(
            email="string",
            first_name="string",
            kyc_exemption_type="AUTHORIZED_USER",
            last_name="string",
            phone_number="string",
            workflow="KYC_EXEMPT",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Lithic) -> None:
        account_holder = client.account_holders.create(
            email="string",
            first_name="string",
            kyc_exemption_type="AUTHORIZED_USER",
            last_name="string",
            phone_number="string",
            workflow="KYC_EXEMPT",
            address={
                "address1": "123 Old Forest Way",
                "address2": "string",
                "city": "Omaha",
                "country": "USA",
                "postal_code": "68022",
                "state": "NE",
            },
            business_account_token="string",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        account_holder = client.account_holders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        account_holder = client.account_holders.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolderUpdateResponse, account_holder, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        account_holder = client.account_holders.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            business_account_token="string",
            email="string",
            phone_number="string",
        )
        assert_matches_type(AccountHolderUpdateResponse, account_holder, path=["response"])

    @parametrize
    def test_method_list_documents(self, client: Lithic) -> None:
        account_holder = client.account_holders.list_documents(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolderListDocumentsResponse, account_holder, path=["response"])

    @parametrize
    def test_method_resubmit(self, client: Lithic) -> None:
        account_holder = client.account_holders.resubmit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            individual={
                "address": {
                    "address1": "123 Old Forest Way",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "dob": "1991-03-08 08:00:00",
                "email": "tom@middle-earth.com",
                "first_name": "Tom",
                "government_id": "111-23-1412",
                "last_name": "Bombadil",
                "phone_number": "+12124007676",
            },
            tos_timestamp="2018-05-29T21:16:05Z",
            workflow="KYC_ADVANCED",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    def test_method_retrieve_document(self, client: Lithic) -> None:
        account_holder = client.account_holders.retrieve_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

    @parametrize
    def test_method_upload_document(self, client: Lithic) -> None:
        account_holder = client.account_holders.upload_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_type="commercial_license",
        )
        assert_matches_type(AccountHolderDocument, account_holder, path=["response"])


class TestAsyncAccountHolders:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create_overload_1(self, client: AsyncLithic) -> None:
        account_holder = await client.account_holders.create(
            beneficial_owner_entities=[
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "phone_numbers": ["+12124007676"],
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "phone_numbers": ["+12124007676"],
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "phone_numbers": ["+12124007676"],
                },
            ],
            beneficial_owner_individuals=[
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-23-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-23-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-23-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
            ],
            business_entity={
                "address": {
                    "address1": "123 Old Forest Way",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "government_id": "114-123-1513",
                "legal_business_name": "Acme, Inc.",
                "phone_numbers": ["+12124007676"],
            },
            control_person={
                "address": {
                    "address1": "123 Old Forest Way",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "dob": "1991-03-08 08:00:00",
                "email": "tom@middle-earth.com",
                "first_name": "Tom",
                "government_id": "111-23-1412",
                "last_name": "Bombadil",
                "phone_number": "+12124007676",
            },
            nature_of_business="Software company selling solutions to the restaurant industry",
            tos_timestamp="2018-05-29T21:16:05Z",
            workflow="KYB_BASIC",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, client: AsyncLithic) -> None:
        account_holder = await client.account_holders.create(
            beneficial_owner_entities=[
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "string",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dba_business_name": "string",
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "parent_company": "string",
                    "phone_numbers": ["+12124007676"],
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "string",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dba_business_name": "string",
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "parent_company": "string",
                    "phone_numbers": ["+12124007676"],
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "string",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dba_business_name": "string",
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "parent_company": "string",
                    "phone_numbers": ["+12124007676"],
                },
            ],
            beneficial_owner_individuals=[
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "string",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-23-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "string",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-23-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
                {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "string",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-23-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
            ],
            business_entity={
                "address": {
                    "address1": "123 Old Forest Way",
                    "address2": "string",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "dba_business_name": "string",
                "government_id": "114-123-1513",
                "legal_business_name": "Acme, Inc.",
                "parent_company": "string",
                "phone_numbers": ["+12124007676"],
            },
            control_person={
                "address": {
                    "address1": "123 Old Forest Way",
                    "address2": "string",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "dob": "1991-03-08 08:00:00",
                "email": "tom@middle-earth.com",
                "first_name": "Tom",
                "government_id": "111-23-1412",
                "last_name": "Bombadil",
                "phone_number": "+12124007676",
            },
            nature_of_business="Software company selling solutions to the restaurant industry",
            tos_timestamp="2018-05-29T21:16:05Z",
            workflow="KYB_BASIC",
            kyb_passed_timestamp="2018-05-29T21:16:05Z",
            website_url="www.mybusiness.com",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    async def test_method_create_overload_2(self, client: AsyncLithic) -> None:
        account_holder = await client.account_holders.create(
            individual={
                "address": {
                    "address1": "123 Old Forest Way",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "dob": "1991-03-08 08:00:00",
                "email": "tom@middle-earth.com",
                "first_name": "Tom",
                "government_id": "111-23-1412",
                "last_name": "Bombadil",
                "phone_number": "+12124007676",
            },
            tos_timestamp="string",
            workflow="KYC_ADVANCED",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, client: AsyncLithic) -> None:
        account_holder = await client.account_holders.create(
            individual={
                "address": {
                    "address1": "123 Old Forest Way",
                    "address2": "string",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "dob": "1991-03-08 08:00:00",
                "email": "tom@middle-earth.com",
                "first_name": "Tom",
                "government_id": "111-23-1412",
                "last_name": "Bombadil",
                "phone_number": "+12124007676",
            },
            tos_timestamp="string",
            workflow="KYC_ADVANCED",
            kyc_passed_timestamp="string",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    async def test_method_create_overload_3(self, client: AsyncLithic) -> None:
        account_holder = await client.account_holders.create(
            email="string",
            first_name="string",
            kyc_exemption_type="AUTHORIZED_USER",
            last_name="string",
            phone_number="string",
            workflow="KYC_EXEMPT",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, client: AsyncLithic) -> None:
        account_holder = await client.account_holders.create(
            email="string",
            first_name="string",
            kyc_exemption_type="AUTHORIZED_USER",
            last_name="string",
            phone_number="string",
            workflow="KYC_EXEMPT",
            address={
                "address1": "123 Old Forest Way",
                "address2": "string",
                "city": "Omaha",
                "country": "USA",
                "postal_code": "68022",
                "state": "NE",
            },
            business_account_token="string",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        account_holder = await client.account_holders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncLithic) -> None:
        account_holder = await client.account_holders.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolderUpdateResponse, account_holder, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncLithic) -> None:
        account_holder = await client.account_holders.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            business_account_token="string",
            email="string",
            phone_number="string",
        )
        assert_matches_type(AccountHolderUpdateResponse, account_holder, path=["response"])

    @parametrize
    async def test_method_list_documents(self, client: AsyncLithic) -> None:
        account_holder = await client.account_holders.list_documents(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolderListDocumentsResponse, account_holder, path=["response"])

    @parametrize
    async def test_method_resubmit(self, client: AsyncLithic) -> None:
        account_holder = await client.account_holders.resubmit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            individual={
                "address": {
                    "address1": "123 Old Forest Way",
                    "city": "Omaha",
                    "country": "USA",
                    "postal_code": "68022",
                    "state": "NE",
                },
                "dob": "1991-03-08 08:00:00",
                "email": "tom@middle-earth.com",
                "first_name": "Tom",
                "government_id": "111-23-1412",
                "last_name": "Bombadil",
                "phone_number": "+12124007676",
            },
            tos_timestamp="2018-05-29T21:16:05Z",
            workflow="KYC_ADVANCED",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    async def test_method_retrieve_document(self, client: AsyncLithic) -> None:
        account_holder = await client.account_holders.retrieve_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

    @parametrize
    async def test_method_upload_document(self, client: AsyncLithic) -> None:
        account_holder = await client.account_holders.upload_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_type="commercial_license",
        )
        assert_matches_type(AccountHolderDocument, account_holder, path=["response"])
