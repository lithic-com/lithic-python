# File generated from our OpenAPI spec by Stainless.
import os
import pytest
from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage

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
                "individual": {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "zwjzvcblafxl",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-213-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
                "tos_timestamp": "2022-03-08 08:00:00",
                "workflow": "KYC_PRECHECKED",
            }
        )
        assert isinstance(resource, AccountHolder)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.account_holders.create(
            {
                "business_entity": {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "cahv",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dba_business_name": "goblbtmtnbksgvjeuuv",
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "parent_company": "rhzrkc",
                    "phone_numbers": ["+12124007676", "+12124007676", "+12124007676"],
                },
                "beneficial_owner_entities": [
                    {
                        "address": {
                            "address1": "123 Old Forest Way",
                            "address2": "rmx",
                            "city": "Omaha",
                            "country": "USA",
                            "postal_code": "68022",
                            "state": "NE",
                        },
                        "dba_business_name": "sklelbtpog",
                        "government_id": "114-123-1513",
                        "legal_business_name": "Acme, Inc.",
                        "parent_company": "w",
                        "phone_numbers": ["+12124007676", "+12124007676", "+12124007676"],
                    },
                    {
                        "address": {
                            "address1": "123 Old Forest Way",
                            "address2": "pvmieybteoit",
                            "city": "Omaha",
                            "country": "USA",
                            "postal_code": "68022",
                            "state": "NE",
                        },
                        "dba_business_name": "crwfvqxyd",
                        "government_id": "114-123-1513",
                        "legal_business_name": "Acme, Inc.",
                        "parent_company": "c",
                        "phone_numbers": ["+12124007676", "+12124007676", "+12124007676"],
                    },
                    {
                        "address": {
                            "address1": "123 Old Forest Way",
                            "address2": "dskclwoldm",
                            "city": "Omaha",
                            "country": "USA",
                            "postal_code": "68022",
                            "state": "NE",
                        },
                        "dba_business_name": "mvjm",
                        "government_id": "114-123-1513",
                        "legal_business_name": "Acme, Inc.",
                        "parent_company": "vvaromyoplfhsgjrrva",
                        "phone_numbers": ["+12124007676", "+12124007676", "+12124007676"],
                    },
                ],
                "beneficial_owner_individuals": [
                    {
                        "address": {
                            "address1": "123 Old Forest Way",
                            "address2": "qmartkmsdzoc",
                            "city": "Omaha",
                            "country": "USA",
                            "postal_code": "68022",
                            "state": "NE",
                        },
                        "dob": "1991-03-08 08:00:00",
                        "email": "tom@middle-earth.com",
                        "first_name": "Tom",
                        "government_id": "111-213-1412",
                        "last_name": "Bombadil",
                        "phone_number": "+12124007676",
                    },
                    {
                        "address": {
                            "address1": "123 Old Forest Way",
                            "address2": "b",
                            "city": "Omaha",
                            "country": "USA",
                            "postal_code": "68022",
                            "state": "NE",
                        },
                        "dob": "1991-03-08 08:00:00",
                        "email": "tom@middle-earth.com",
                        "first_name": "Tom",
                        "government_id": "111-213-1412",
                        "last_name": "Bombadil",
                        "phone_number": "+12124007676",
                    },
                    {
                        "address": {
                            "address1": "123 Old Forest Way",
                            "address2": "pztunoxchsmrz",
                            "city": "Omaha",
                            "country": "USA",
                            "postal_code": "68022",
                            "state": "NE",
                        },
                        "dob": "1991-03-08 08:00:00",
                        "email": "tom@middle-earth.com",
                        "first_name": "Tom",
                        "government_id": "111-213-1412",
                        "last_name": "Bombadil",
                        "phone_number": "+12124007676",
                    },
                ],
                "control_person": {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "i",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-213-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
                "kyb_passed_timestamp": "2022-03-08 08:00:00",
                "nature_of_business": "Software company selling solutions to the restaurant industry",
                "tos_timestamp": "2022-03-08 08:00:00",
                "website_url": "www.mybusiness.com",
                "workflow": "KYB_PRECHECKED",
            }
        )
        assert isinstance(resource, AccountHolder)

    def test_method_retrieve(self) -> None:
        resource = self.client.account_holders.retrieve(
            "38465ca6-07c2-495a-9b28-61f732eae81a",
        )
        assert isinstance(resource, AccountHolder)

    def test_method_create_webhook(self) -> None:
        resource = self.client.account_holders.create_webhook({"url": "inmivbdgd"})
        assert isinstance(resource, AccountHolderCreateWebhookResponse)

    def test_method_create_webhook_with_optional_params(self) -> None:
        resource = self.client.account_holders.create_webhook({"url": "lg"})
        assert isinstance(resource, AccountHolderCreateWebhookResponse)

    def test_method_list_documents(self) -> None:
        resource = self.client.account_holders.list_documents(
            "0c4e6054-5fd8-48a8-817c-f6611278f755",
        )
        assert isinstance(resource, AccountHolderListDocumentsResponse)

    def test_method_resubmit(self) -> None:
        resource = self.client.account_holders.resubmit(
            "c1c93379-b46e-439f-baad-f0e408619f23",
            {
                "workflow": "KYC_ADVANCED",
                "tos_timestamp": "2022-03-08 08:00:00",
                "individual": {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "jifzcogqhkqt",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-213-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
            },
        )
        assert isinstance(resource, AccountHolder)

    def test_method_resubmit_with_optional_params(self) -> None:
        resource = self.client.account_holders.resubmit(
            "c1c93379-b46e-439f-baad-f0e408619f23",
            {
                "workflow": "KYC_ADVANCED",
                "tos_timestamp": "2022-03-08 08:00:00",
                "individual": {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "kjtaz",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-213-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
            },
        )
        assert isinstance(resource, AccountHolder)

    def test_method_retrieve_document(self) -> None:
        resource = self.client.account_holders.retrieve_document(
            "52872896-44a6-40de-a0f2-7ce0cb4fcddb",
            "5ff6adb5-7e12-4ffa-91d2-1d9408b10915",
        )
        assert isinstance(resource, AccountHolderDocument)

    def test_method_upload_document(self) -> None:
        resource = self.client.account_holders.upload_document(
            "35ea558b-9a3f-494a-b416-e70e790fe858", {"document_type": "PASSPORT_CARD"}
        )
        assert isinstance(resource, AccountHolderDocument)

    def test_method_upload_document_with_optional_params(self) -> None:
        resource = self.client.account_holders.upload_document(
            "35ea558b-9a3f-494a-b416-e70e790fe858", {"document_type": "COMMERCIAL_LICENCE"}
        )
        assert isinstance(resource, AccountHolderDocument)


class TestAsyncAccountHolders:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.account_holders.create(
            {
                "individual": {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "xysfcbskwj",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-213-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
                "tos_timestamp": "2022-03-08 08:00:00",
                "workflow": "KYC_BASIC",
            }
        )
        assert isinstance(resource, AccountHolder)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.account_holders.create(
            {
                "business_entity": {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "amxbrnxnppvvijjxkktk",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dba_business_name": "kgcymxq",
                    "government_id": "114-123-1513",
                    "legal_business_name": "Acme, Inc.",
                    "parent_company": "hqxhmfh",
                    "phone_numbers": ["+12124007676", "+12124007676", "+12124007676"],
                },
                "beneficial_owner_entities": [
                    {
                        "address": {
                            "address1": "123 Old Forest Way",
                            "address2": "kikwuvt",
                            "city": "Omaha",
                            "country": "USA",
                            "postal_code": "68022",
                            "state": "NE",
                        },
                        "dba_business_name": "mynkvgsdnhtdic",
                        "government_id": "114-123-1513",
                        "legal_business_name": "Acme, Inc.",
                        "parent_company": "ppjboresrof",
                        "phone_numbers": ["+12124007676", "+12124007676", "+12124007676"],
                    },
                    {
                        "address": {
                            "address1": "123 Old Forest Way",
                            "address2": "hctpoqipos",
                            "city": "Omaha",
                            "country": "USA",
                            "postal_code": "68022",
                            "state": "NE",
                        },
                        "dba_business_name": "cxzpdgctnulfev",
                        "government_id": "114-123-1513",
                        "legal_business_name": "Acme, Inc.",
                        "parent_company": "mwutgdie",
                        "phone_numbers": ["+12124007676", "+12124007676", "+12124007676"],
                    },
                    {
                        "address": {
                            "address1": "123 Old Forest Way",
                            "address2": "oroulrjfnmkvarbadcqj",
                            "city": "Omaha",
                            "country": "USA",
                            "postal_code": "68022",
                            "state": "NE",
                        },
                        "dba_business_name": "ydmjhujtf",
                        "government_id": "114-123-1513",
                        "legal_business_name": "Acme, Inc.",
                        "parent_company": "k",
                        "phone_numbers": ["+12124007676", "+12124007676", "+12124007676"],
                    },
                ],
                "beneficial_owner_individuals": [
                    {
                        "address": {
                            "address1": "123 Old Forest Way",
                            "address2": "fivzlehfymimxb",
                            "city": "Omaha",
                            "country": "USA",
                            "postal_code": "68022",
                            "state": "NE",
                        },
                        "dob": "1991-03-08 08:00:00",
                        "email": "tom@middle-earth.com",
                        "first_name": "Tom",
                        "government_id": "111-213-1412",
                        "last_name": "Bombadil",
                        "phone_number": "+12124007676",
                    },
                    {
                        "address": {
                            "address1": "123 Old Forest Way",
                            "address2": "",
                            "city": "Omaha",
                            "country": "USA",
                            "postal_code": "68022",
                            "state": "NE",
                        },
                        "dob": "1991-03-08 08:00:00",
                        "email": "tom@middle-earth.com",
                        "first_name": "Tom",
                        "government_id": "111-213-1412",
                        "last_name": "Bombadil",
                        "phone_number": "+12124007676",
                    },
                    {
                        "address": {
                            "address1": "123 Old Forest Way",
                            "address2": "svmllpatbki",
                            "city": "Omaha",
                            "country": "USA",
                            "postal_code": "68022",
                            "state": "NE",
                        },
                        "dob": "1991-03-08 08:00:00",
                        "email": "tom@middle-earth.com",
                        "first_name": "Tom",
                        "government_id": "111-213-1412",
                        "last_name": "Bombadil",
                        "phone_number": "+12124007676",
                    },
                ],
                "control_person": {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "yuqujepuf",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-213-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
                "kyb_passed_timestamp": "2022-03-08 08:00:00",
                "nature_of_business": "Software company selling solutions to the restaurant industry",
                "tos_timestamp": "2022-03-08 08:00:00",
                "website_url": "www.mybusiness.com",
                "workflow": "KYB_BASIC",
            }
        )
        assert isinstance(resource, AccountHolder)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.account_holders.retrieve(
            "2e55d487-4ef2-4da5-8fdf-16aa96a40164",
        )
        assert isinstance(resource, AccountHolder)

    async def test_method_create_webhook(self) -> None:
        resource = await self.client.account_holders.create_webhook({"url": "hdkoeayacmqvlxl"})
        assert isinstance(resource, AccountHolderCreateWebhookResponse)

    async def test_method_create_webhook_with_optional_params(self) -> None:
        resource = await self.client.account_holders.create_webhook({"url": "jywphc"})
        assert isinstance(resource, AccountHolderCreateWebhookResponse)

    async def test_method_list_documents(self) -> None:
        resource = await self.client.account_holders.list_documents(
            "01e9dc42-851f-41ed-967a-9f0310a02bee",
        )
        assert isinstance(resource, AccountHolderListDocumentsResponse)

    async def test_method_resubmit(self) -> None:
        resource = await self.client.account_holders.resubmit(
            "677698dd-7a33-46c3-ac21-9f34b65a49fe",
            {
                "workflow": "KYC_ADVANCED",
                "tos_timestamp": "2022-03-08 08:00:00",
                "individual": {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-213-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
            },
        )
        assert isinstance(resource, AccountHolder)

    async def test_method_resubmit_with_optional_params(self) -> None:
        resource = await self.client.account_holders.resubmit(
            "677698dd-7a33-46c3-ac21-9f34b65a49fe",
            {
                "workflow": "KYC_ADVANCED",
                "tos_timestamp": "2022-03-08 08:00:00",
                "individual": {
                    "address": {
                        "address1": "123 Old Forest Way",
                        "address2": "qobjtqficcqbtxrnbfho",
                        "city": "Omaha",
                        "country": "USA",
                        "postal_code": "68022",
                        "state": "NE",
                    },
                    "dob": "1991-03-08 08:00:00",
                    "email": "tom@middle-earth.com",
                    "first_name": "Tom",
                    "government_id": "111-213-1412",
                    "last_name": "Bombadil",
                    "phone_number": "+12124007676",
                },
            },
        )
        assert isinstance(resource, AccountHolder)

    async def test_method_retrieve_document(self) -> None:
        resource = await self.client.account_holders.retrieve_document(
            "7f43c928-90f8-4e03-a0cf-5e4e669b9326",
            "1db2ced7-f6c4-4cee-8dc6-d4ef4d5c9a7c",
        )
        assert isinstance(resource, AccountHolderDocument)

    async def test_method_upload_document(self) -> None:
        resource = await self.client.account_holders.upload_document(
            "e46b7298-63fc-41d3-95a2-74ecc850efd9", {"document_type": "VISA"}
        )
        assert isinstance(resource, AccountHolderDocument)

    async def test_method_upload_document_with_optional_params(self) -> None:
        resource = await self.client.account_holders.upload_document(
            "e46b7298-63fc-41d3-95a2-74ecc850efd9", {"document_type": "COMMERCIAL_LICENCE"}
        )
        assert isinstance(resource, AccountHolderDocument)
