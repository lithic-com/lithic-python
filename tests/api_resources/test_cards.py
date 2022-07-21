# File generated from our OpenAPI spec by Stainless.
import os

from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage
from lithic.types.card import *
from lithic.types.embed_request_param import *
from lithic.types.card_provision_response import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCards:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.cards.create(
            {"type": "MERCHANT_LOCKED"},
        )
        assert isinstance(resource, Card)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.cards.create(
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "card_program_token": "00000000-0000-0000-1000-000000000000",
                "exp_month": "06",
                "exp_year": "2027",
                "funding_token": "ecbd1d58-0299-48b3-84da-6ed7f5bf9ec1",
                "memo": "New Card",
                "spend_limit": 0,
                "spend_limit_duration": "ANNUALLY",
                "state": "OPEN",
                "type": "MERCHANT_LOCKED",
                "pin": "string",
                "product_id": "1",
                "shipping_address": {
                    "first_name": "Michael",
                    "last_name": "Bluth",
                    "line2_text": "The Bluth Company",
                    "address1": "5 Broad Street",
                    "address2": "Unit 25A",
                    "city": "NEW YORK",
                    "state": "NY",
                    "postal_code": "10001-1809",
                    "country": "USA",
                    "email": "johnny@appleseed.com",
                    "phone_number": "+12124007676",
                },
                "shipping_method": "STANDARD",
            },
        )
        assert isinstance(resource, Card)

    def test_method_retrieve(self) -> None:
        resource = self.client.cards.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, Card)

    def test_method_update(self) -> None:
        resource = self.client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, Card)

    def test_method_update_with_optional_params(self) -> None:
        resource = self.client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "funding_token": "ecbd1d58-0299-48b3-84da-6ed7f5bf9ec1",
                "memo": "New Card",
                "spend_limit": 0,
                "spend_limit_duration": "ANNUALLY",
                "auth_rule_token": "string",
                "state": "CLOSED",
                "pin": "string",
            },
        )
        assert isinstance(resource, Card)

    def test_method_list(self) -> None:
        resource = self.client.cards.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.cards.list(
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "begin": "2019-12-27T18:11:19.117Z",
                "end": "2019-12-27T18:11:19.117Z",
                "page": 0,
                "page_size": 1,
            },
        )
        assert isinstance(resource, SyncPage)

    def test_method_embed(self) -> None:
        resource = self.client.cards.embed()
        assert isinstance(resource, str)

    def test_method_embed_with_optional_params(self) -> None:
        resource = self.client.cards.embed(
            {
                "embed_request": "string",
                "hmac": "string",
            },
        )
        assert isinstance(resource, str)

    def test_get_embed_html(self) -> None:
        html = self.client.cards.get_embed_html({"token": "foo"})
        assert "html" in html

    def test_get_embed_url(self) -> None:
        url = self.client.cards.get_embed_url({"token": "foo"})
        params = set(  # pyright: ignore[reportUnknownVariableType]
            url.params.keys()  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
        )
        assert "hmac" in params
        assert "embed_request" in params

    def test_method_provision(self) -> None:
        resource = self.client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, CardProvisionResponse)

    def test_method_provision_with_optional_params(self) -> None:
        resource = self.client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "digital_wallet": "APPLE_PAY",
                "nonce": "U3RhaW5sZXNzIHJvY2tz",
                "nonce_signature": "U3RhaW5sZXNzIHJvY2tz",
                "certificate": "U3RhaW5sZXNzIHJvY2tz",
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
        )
        assert isinstance(resource, CardProvisionResponse)

    def test_method_reissue(self) -> None:
        resource = self.client.cards.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, Card)

    def test_method_reissue_with_optional_params(self) -> None:
        resource = self.client.cards.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "shipping_address": {
                    "first_name": "Michael",
                    "last_name": "Bluth",
                    "line2_text": "The Bluth Company",
                    "address1": "5 Broad Street",
                    "address2": "Unit 25A",
                    "city": "NEW YORK",
                    "state": "NY",
                    "postal_code": "10001-1809",
                    "country": "USA",
                    "email": "johnny@appleseed.com",
                    "phone_number": "+12124007676",
                },
                "shipping_method": "STANDARD",
                "product_id": "string",
            },
        )
        assert isinstance(resource, Card)


class TestAsyncCards:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.cards.create(
            {"type": "MERCHANT_LOCKED"},
        )
        assert isinstance(resource, Card)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.cards.create(
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "card_program_token": "00000000-0000-0000-1000-000000000000",
                "exp_month": "06",
                "exp_year": "2027",
                "funding_token": "ecbd1d58-0299-48b3-84da-6ed7f5bf9ec1",
                "memo": "New Card",
                "spend_limit": 0,
                "spend_limit_duration": "ANNUALLY",
                "state": "OPEN",
                "type": "MERCHANT_LOCKED",
                "pin": "string",
                "product_id": "1",
                "shipping_address": {
                    "first_name": "Michael",
                    "last_name": "Bluth",
                    "line2_text": "The Bluth Company",
                    "address1": "5 Broad Street",
                    "address2": "Unit 25A",
                    "city": "NEW YORK",
                    "state": "NY",
                    "postal_code": "10001-1809",
                    "country": "USA",
                    "email": "johnny@appleseed.com",
                    "phone_number": "+12124007676",
                },
                "shipping_method": "STANDARD",
            },
        )
        assert isinstance(resource, Card)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.cards.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, Card)

    async def test_method_update(self) -> None:
        resource = await self.client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, Card)

    async def test_method_update_with_optional_params(self) -> None:
        resource = await self.client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "funding_token": "ecbd1d58-0299-48b3-84da-6ed7f5bf9ec1",
                "memo": "New Card",
                "spend_limit": 0,
                "spend_limit_duration": "ANNUALLY",
                "auth_rule_token": "string",
                "state": "CLOSED",
                "pin": "string",
            },
        )
        assert isinstance(resource, Card)

    async def test_method_list(self) -> None:
        resource = await self.client.cards.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.cards.list(
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "begin": "2019-12-27T18:11:19.117Z",
                "end": "2019-12-27T18:11:19.117Z",
                "page": 0,
                "page_size": 1,
            },
        )
        assert isinstance(resource, AsyncPage)

    async def test_method_embed(self) -> None:
        resource = await self.client.cards.embed()
        assert isinstance(resource, str)

    async def test_method_embed_with_optional_params(self) -> None:
        resource = await self.client.cards.embed(
            {
                "embed_request": "string",
                "hmac": "string",
            },
        )
        assert isinstance(resource, str)

    async def test_get_embed_html(self) -> None:
        html = await self.client.cards.get_embed_html({"token": "foo"})
        assert "html" in html

    def test_get_embed_url(self) -> None:
        url = self.client.cards.get_embed_url({"token": "foo"})
        params = set(  # pyright: ignore[reportUnknownVariableType]
            url.params.keys()  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
        )
        assert "hmac" in params
        assert "embed_request" in params

    async def test_method_provision(self) -> None:
        resource = await self.client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, CardProvisionResponse)

    async def test_method_provision_with_optional_params(self) -> None:
        resource = await self.client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "digital_wallet": "APPLE_PAY",
                "nonce": "U3RhaW5sZXNzIHJvY2tz",
                "nonce_signature": "U3RhaW5sZXNzIHJvY2tz",
                "certificate": "U3RhaW5sZXNzIHJvY2tz",
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
        )
        assert isinstance(resource, CardProvisionResponse)

    async def test_method_reissue(self) -> None:
        resource = await self.client.cards.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, Card)

    async def test_method_reissue_with_optional_params(self) -> None:
        resource = await self.client.cards.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "shipping_address": {
                    "first_name": "Michael",
                    "last_name": "Bluth",
                    "line2_text": "The Bluth Company",
                    "address1": "5 Broad Street",
                    "address2": "Unit 25A",
                    "city": "NEW YORK",
                    "state": "NY",
                    "postal_code": "10001-1809",
                    "country": "USA",
                    "email": "johnny@appleseed.com",
                    "phone_number": "+12124007676",
                },
                "shipping_method": "STANDARD",
                "product_id": "string",
            },
        )
        assert isinstance(resource, Card)
