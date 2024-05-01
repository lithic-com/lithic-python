# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    AccountHolder,
    AccountHolderDocument,
    AccountHolderCreateResponse,
    AccountHolderUpdateResponse,
    AccountHolderListDocumentsResponse,
)
from lithic.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountHolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            },
            nature_of_business="Software company selling solutions to the restaurant industry",
            tos_timestamp="2018-05-29T21:16:05Z",
            workflow="KYB_BASIC",
        )
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

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
            external_id="string",
            kyb_passed_timestamp="2018-05-29T21:16:05Z",
            website_url="www.mybusiness.com",
        )
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Lithic) -> None:
        response = client.account_holders.with_raw_response.create(
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
            },
            nature_of_business="Software company selling solutions to the restaurant industry",
            tos_timestamp="2018-05-29T21:16:05Z",
            workflow="KYB_BASIC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Lithic) -> None:
        with client.account_holders.with_streaming_response.create(
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
            },
            nature_of_business="Software company selling solutions to the restaurant industry",
            tos_timestamp="2018-05-29T21:16:05Z",
            workflow="KYB_BASIC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = response.parse()
            assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

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
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

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
            external_id="string",
            kyc_passed_timestamp="string",
        )
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Lithic) -> None:
        response = client.account_holders.with_raw_response.create(
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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Lithic) -> None:
        with client.account_holders.with_streaming_response.create(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = response.parse()
            assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Lithic) -> None:
        account_holder = client.account_holders.create(
            address={
                "address1": "123 Old Forest Way",
                "city": "Omaha",
                "country": "USA",
                "postal_code": "68022",
                "state": "NE",
            },
            email="string",
            first_name="string",
            kyc_exemption_type="AUTHORIZED_USER",
            last_name="string",
            phone_number="string",
            workflow="KYC_EXEMPT",
        )
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Lithic) -> None:
        account_holder = client.account_holders.create(
            address={
                "address1": "123 Old Forest Way",
                "address2": "string",
                "city": "Omaha",
                "country": "USA",
                "postal_code": "68022",
                "state": "NE",
            },
            email="string",
            first_name="string",
            kyc_exemption_type="AUTHORIZED_USER",
            last_name="string",
            phone_number="string",
            workflow="KYC_EXEMPT",
            business_account_token="string",
            external_id="string",
        )
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Lithic) -> None:
        response = client.account_holders.with_raw_response.create(
            address={
                "address1": "123 Old Forest Way",
                "city": "Omaha",
                "country": "USA",
                "postal_code": "68022",
                "state": "NE",
            },
            email="string",
            first_name="string",
            kyc_exemption_type="AUTHORIZED_USER",
            last_name="string",
            phone_number="string",
            workflow="KYC_EXEMPT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Lithic) -> None:
        with client.account_holders.with_streaming_response.create(
            address={
                "address1": "123 Old Forest Way",
                "city": "Omaha",
                "country": "USA",
                "postal_code": "68022",
                "state": "NE",
            },
            email="string",
            first_name="string",
            kyc_exemption_type="AUTHORIZED_USER",
            last_name="string",
            phone_number="string",
            workflow="KYC_EXEMPT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = response.parse()
            assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        account_holder = client.account_holders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.account_holders.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.account_holders.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = response.parse()
            assert_matches_type(AccountHolder, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            client.account_holders.with_raw_response.retrieve(
                "",
            )

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
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.account_holders.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderUpdateResponse, account_holder, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.account_holders.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = response.parse()
            assert_matches_type(AccountHolderUpdateResponse, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            client.account_holders.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        account_holder = client.account_holders.list()
        assert_matches_type(SyncSinglePage[AccountHolder], account_holder, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        account_holder = client.account_holders.list(
            ending_before="string",
            external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            starting_after="string",
        )
        assert_matches_type(SyncSinglePage[AccountHolder], account_holder, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.account_holders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(SyncSinglePage[AccountHolder], account_holder, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.account_holders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = response.parse()
            assert_matches_type(SyncSinglePage[AccountHolder], account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_documents(self, client: Lithic) -> None:
        account_holder = client.account_holders.list_documents(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolderListDocumentsResponse, account_holder, path=["response"])

    @parametrize
    def test_raw_response_list_documents(self, client: Lithic) -> None:
        response = client.account_holders.with_raw_response.list_documents(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderListDocumentsResponse, account_holder, path=["response"])

    @parametrize
    def test_streaming_response_list_documents(self, client: Lithic) -> None:
        with client.account_holders.with_streaming_response.list_documents(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = response.parse()
            assert_matches_type(AccountHolderListDocumentsResponse, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_documents(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            client.account_holders.with_raw_response.list_documents(
                "",
            )

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
    def test_raw_response_resubmit(self, client: Lithic) -> None:
        response = client.account_holders.with_raw_response.resubmit(
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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    def test_streaming_response_resubmit(self, client: Lithic) -> None:
        with client.account_holders.with_streaming_response.resubmit(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = response.parse()
            assert_matches_type(AccountHolder, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resubmit(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            client.account_holders.with_raw_response.resubmit(
                "",
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

    @parametrize
    def test_method_retrieve_document(self, client: Lithic) -> None:
        account_holder = client.account_holders.retrieve_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

    @parametrize
    def test_raw_response_retrieve_document(self, client: Lithic) -> None:
        response = client.account_holders.with_raw_response.retrieve_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_document(self, client: Lithic) -> None:
        with client.account_holders.with_streaming_response.retrieve_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = response.parse()
            assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_document(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            client.account_holders.with_raw_response.retrieve_document(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_holder_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_token` but received ''"):
            client.account_holders.with_raw_response.retrieve_document(
                "",
                account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_upload_document(self, client: Lithic) -> None:
        account_holder = client.account_holders.upload_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_type="drivers_license",
        )
        assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

    @parametrize
    def test_raw_response_upload_document(self, client: Lithic) -> None:
        response = client.account_holders.with_raw_response.upload_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_type="drivers_license",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

    @parametrize
    def test_streaming_response_upload_document(self, client: Lithic) -> None:
        with client.account_holders.with_streaming_response.upload_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_type="drivers_license",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = response.parse()
            assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_upload_document(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            client.account_holders.with_raw_response.upload_document(
                "",
                document_type="drivers_license",
            )


class TestAsyncAccountHolders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.create(
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
            },
            nature_of_business="Software company selling solutions to the restaurant industry",
            tos_timestamp="2018-05-29T21:16:05Z",
            workflow="KYB_BASIC",
        )
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.create(
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
            external_id="string",
            kyb_passed_timestamp="2018-05-29T21:16:05Z",
            website_url="www.mybusiness.com",
        )
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_holders.with_raw_response.create(
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
            },
            nature_of_business="Software company selling solutions to the restaurant industry",
            tos_timestamp="2018-05-29T21:16:05Z",
            workflow="KYB_BASIC",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncLithic) -> None:
        async with async_client.account_holders.with_streaming_response.create(
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
            },
            nature_of_business="Software company selling solutions to the restaurant industry",
            tos_timestamp="2018-05-29T21:16:05Z",
            workflow="KYB_BASIC",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = await response.parse()
            assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.create(
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
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.create(
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
            external_id="string",
            kyc_passed_timestamp="string",
        )
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_holders.with_raw_response.create(
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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncLithic) -> None:
        async with async_client.account_holders.with_streaming_response.create(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = await response.parse()
            assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.create(
            address={
                "address1": "123 Old Forest Way",
                "city": "Omaha",
                "country": "USA",
                "postal_code": "68022",
                "state": "NE",
            },
            email="string",
            first_name="string",
            kyc_exemption_type="AUTHORIZED_USER",
            last_name="string",
            phone_number="string",
            workflow="KYC_EXEMPT",
        )
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.create(
            address={
                "address1": "123 Old Forest Way",
                "address2": "string",
                "city": "Omaha",
                "country": "USA",
                "postal_code": "68022",
                "state": "NE",
            },
            email="string",
            first_name="string",
            kyc_exemption_type="AUTHORIZED_USER",
            last_name="string",
            phone_number="string",
            workflow="KYC_EXEMPT",
            business_account_token="string",
            external_id="string",
        )
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_holders.with_raw_response.create(
            address={
                "address1": "123 Old Forest Way",
                "city": "Omaha",
                "country": "USA",
                "postal_code": "68022",
                "state": "NE",
            },
            email="string",
            first_name="string",
            kyc_exemption_type="AUTHORIZED_USER",
            last_name="string",
            phone_number="string",
            workflow="KYC_EXEMPT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncLithic) -> None:
        async with async_client.account_holders.with_streaming_response.create(
            address={
                "address1": "123 Old Forest Way",
                "city": "Omaha",
                "country": "USA",
                "postal_code": "68022",
                "state": "NE",
            },
            email="string",
            first_name="string",
            kyc_exemption_type="AUTHORIZED_USER",
            last_name="string",
            phone_number="string",
            workflow="KYC_EXEMPT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = await response.parse()
            assert_matches_type(AccountHolderCreateResponse, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_holders.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.account_holders.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = await response.parse()
            assert_matches_type(AccountHolder, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            await async_client.account_holders.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolderUpdateResponse, account_holder, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            business_account_token="string",
            email="string",
            phone_number="string",
        )
        assert_matches_type(AccountHolderUpdateResponse, account_holder, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_holders.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderUpdateResponse, account_holder, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLithic) -> None:
        async with async_client.account_holders.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = await response.parse()
            assert_matches_type(AccountHolderUpdateResponse, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            await async_client.account_holders.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.list()
        assert_matches_type(AsyncSinglePage[AccountHolder], account_holder, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.list(
            ending_before="string",
            external_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=0,
            starting_after="string",
        )
        assert_matches_type(AsyncSinglePage[AccountHolder], account_holder, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_holders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AsyncSinglePage[AccountHolder], account_holder, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.account_holders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = await response.parse()
            assert_matches_type(AsyncSinglePage[AccountHolder], account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_documents(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.list_documents(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolderListDocumentsResponse, account_holder, path=["response"])

    @parametrize
    async def test_raw_response_list_documents(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_holders.with_raw_response.list_documents(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderListDocumentsResponse, account_holder, path=["response"])

    @parametrize
    async def test_streaming_response_list_documents(self, async_client: AsyncLithic) -> None:
        async with async_client.account_holders.with_streaming_response.list_documents(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = await response.parse()
            assert_matches_type(AccountHolderListDocumentsResponse, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_documents(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            await async_client.account_holders.with_raw_response.list_documents(
                "",
            )

    @parametrize
    async def test_method_resubmit(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.resubmit(
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
    async def test_raw_response_resubmit(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_holders.with_raw_response.resubmit(
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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolder, account_holder, path=["response"])

    @parametrize
    async def test_streaming_response_resubmit(self, async_client: AsyncLithic) -> None:
        async with async_client.account_holders.with_streaming_response.resubmit(
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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = await response.parse()
            assert_matches_type(AccountHolder, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resubmit(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            await async_client.account_holders.with_raw_response.resubmit(
                "",
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

    @parametrize
    async def test_method_retrieve_document(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.retrieve_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_document(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_holders.with_raw_response.retrieve_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_document(self, async_client: AsyncLithic) -> None:
        async with async_client.account_holders.with_streaming_response.retrieve_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = await response.parse()
            assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_document(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            await async_client.account_holders.with_raw_response.retrieve_document(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_holder_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_token` but received ''"):
            await async_client.account_holders.with_raw_response.retrieve_document(
                "",
                account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_upload_document(self, async_client: AsyncLithic) -> None:
        account_holder = await async_client.account_holders.upload_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_type="drivers_license",
        )
        assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

    @parametrize
    async def test_raw_response_upload_document(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_holders.with_raw_response.upload_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_type="drivers_license",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_holder = response.parse()
        assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

    @parametrize
    async def test_streaming_response_upload_document(self, async_client: AsyncLithic) -> None:
        async with async_client.account_holders.with_streaming_response.upload_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_type="drivers_license",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_holder = await response.parse()
            assert_matches_type(AccountHolderDocument, account_holder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_upload_document(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            await async_client.account_holders.with_raw_response.upload_document(
                "",
                document_type="drivers_license",
            )
