# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from lithic import Lithic, AsyncLithic
from lithic.types.account_holder import *
from lithic.types.account_holder_document import *
from lithic.types.account_holder_create_webhook_response import *
from lithic.types.account_holder_list_documents_response import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccountHolders:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.account_holders.create(
            {
                "business_entity": {
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
                "beneficial_owner_entities": [
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
                "beneficial_owner_individuals": [
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
                "control_person": {
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
                "nature_of_business": "Software company selling solutions to the restaurant industry",
                "tos_timestamp": "2022-03-08 08:00:00",
                "website_url": "www.mybusiness.com",
                "workflow": "KYB_BASIC",
            },
        )
        assert isinstance(resource, AccountHolder)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.account_holders.create(
            {
                "business_entity": {
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
                "beneficial_owner_entities": [
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
                "beneficial_owner_individuals": [
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
                "control_person": {
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
                "kyb_passed_timestamp": "2022-03-08 08:00:00",
                "nature_of_business": "Software company selling solutions to the restaurant industry",
                "tos_timestamp": "2022-03-08 08:00:00",
                "website_url": "www.mybusiness.com",
                "workflow": "KYB_BASIC",
            },
        )
        assert isinstance(resource, AccountHolder)

    def test_method_retrieve(self) -> None:
        resource = self.client.account_holders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AccountHolder)

    def test_method_create_webhook(self) -> None:
        resource = self.client.account_holders.create_webhook(
            {"url": "string"},
        )
        assert isinstance(resource, AccountHolderCreateWebhookResponse)

    def test_method_create_webhook_with_optional_params(self) -> None:
        resource = self.client.account_holders.create_webhook(
            {"url": "string"},
        )
        assert isinstance(resource, AccountHolderCreateWebhookResponse)

    def test_method_list_documents(self) -> None:
        resource = self.client.account_holders.list_documents(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AccountHolderListDocumentsResponse)

    def test_method_resubmit(self) -> None:
        resource = self.client.account_holders.resubmit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "workflow": "KYC_ADVANCED",
                "tos_timestamp": "2022-03-08 08:00:00",
                "individual": {
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
            },
        )
        assert isinstance(resource, AccountHolder)

    def test_method_resubmit_with_optional_params(self) -> None:
        resource = self.client.account_holders.resubmit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "workflow": "KYC_ADVANCED",
                "tos_timestamp": "2022-03-08 08:00:00",
                "individual": {
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
            },
        )
        assert isinstance(resource, AccountHolder)

    def test_method_retrieve_document(self) -> None:
        resource = self.client.account_holders.retrieve_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AccountHolderDocument)

    def test_method_upload_document(self) -> None:
        resource = self.client.account_holders.upload_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {"document_type": "COMMERCIAL_LICENSE"},
        )
        assert isinstance(resource, AccountHolderDocument)

    def test_method_upload_document_with_optional_params(self) -> None:
        resource = self.client.account_holders.upload_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {"document_type": "COMMERCIAL_LICENSE"},
        )
        assert isinstance(resource, AccountHolderDocument)


class TestAsyncAccountHolders:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.account_holders.create(
            {
                "business_entity": {
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
                "beneficial_owner_entities": [
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
                "beneficial_owner_individuals": [
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
                "control_person": {
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
                "nature_of_business": "Software company selling solutions to the restaurant industry",
                "tos_timestamp": "2022-03-08 08:00:00",
                "website_url": "www.mybusiness.com",
                "workflow": "KYB_BASIC",
            },
        )
        assert isinstance(resource, AccountHolder)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.account_holders.create(
            {
                "business_entity": {
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
                "beneficial_owner_entities": [
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
                "beneficial_owner_individuals": [
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
                "control_person": {
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
                "kyb_passed_timestamp": "2022-03-08 08:00:00",
                "nature_of_business": "Software company selling solutions to the restaurant industry",
                "tos_timestamp": "2022-03-08 08:00:00",
                "website_url": "www.mybusiness.com",
                "workflow": "KYB_BASIC",
            },
        )
        assert isinstance(resource, AccountHolder)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.account_holders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AccountHolder)

    async def test_method_create_webhook(self) -> None:
        resource = await self.client.account_holders.create_webhook(
            {"url": "string"},
        )
        assert isinstance(resource, AccountHolderCreateWebhookResponse)

    async def test_method_create_webhook_with_optional_params(self) -> None:
        resource = await self.client.account_holders.create_webhook(
            {"url": "string"},
        )
        assert isinstance(resource, AccountHolderCreateWebhookResponse)

    async def test_method_list_documents(self) -> None:
        resource = await self.client.account_holders.list_documents(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AccountHolderListDocumentsResponse)

    async def test_method_resubmit(self) -> None:
        resource = await self.client.account_holders.resubmit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "workflow": "KYC_ADVANCED",
                "tos_timestamp": "2022-03-08 08:00:00",
                "individual": {
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
            },
        )
        assert isinstance(resource, AccountHolder)

    async def test_method_resubmit_with_optional_params(self) -> None:
        resource = await self.client.account_holders.resubmit(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "workflow": "KYC_ADVANCED",
                "tos_timestamp": "2022-03-08 08:00:00",
                "individual": {
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
            },
        )
        assert isinstance(resource, AccountHolder)

    async def test_method_retrieve_document(self) -> None:
        resource = await self.client.account_holders.retrieve_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AccountHolderDocument)

    async def test_method_upload_document(self) -> None:
        resource = await self.client.account_holders.upload_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {"document_type": "COMMERCIAL_LICENSE"},
        )
        assert isinstance(resource, AccountHolderDocument)

    async def test_method_upload_document_with_optional_params(self) -> None:
        resource = await self.client.account_holders.upload_document(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {"document_type": "COMMERCIAL_LICENSE"},
        )
        assert isinstance(resource, AccountHolderDocument)
