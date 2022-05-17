# File generated from our OpenAPI spec by Stainless.
import os
import pytest
from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage

from lithic.types.card import *
from lithic.types.card_provision_response import *


base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCards:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.cards.create({"type": "UNLOCKED"})
        assert isinstance(resource, Card)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.cards.create(
            {
                "account_token": "b0e30fca-1ce6-4972-902d-b26f814d36ad",
                "card_program_token": "00000000-0000-0000-1000-000000000000",
                "exp_month": "06",
                "exp_year": "2027",
                "funding_token": "ecbd1d58-0299-48b3-84da-6ed7f5bf9ec1",
                "memo": "New Card",
                "spend_limit": 9,
                "spend_limit_duration": "TRANSACTION",
                "state": "PAUSED",
                "type": "UNLOCKED",
                "pin": "mgs",
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
                "shipping_method": "EXPEDITED",
            }
        )
        assert isinstance(resource, Card)

    def test_method_retrieve(self) -> None:
        resource = self.client.cards.retrieve(
            "540d3d01-5478-4030-ba81-81171bdf3471",
        )
        assert isinstance(resource, Card)

    def test_method_update(self) -> None:
        resource = self.client.cards.update("719331b0-4442-4d06-91d7-4ab4bf07f52e", {})
        assert isinstance(resource, Card)

    def test_method_update_with_optional_params(self) -> None:
        resource = self.client.cards.update(
            "719331b0-4442-4d06-91d7-4ab4bf07f52e",
            {
                "account_token": "bc67d1fa-37d4-481f-ba09-53abb4fd7ff0",
                "funding_token": "ecbd1d58-0299-48b3-84da-6ed7f5bf9ec1",
                "memo": "New Card",
                "spend_limit": 5,
                "spend_limit_duration": "TRANSACTION",
                "auth_rule_token": "jdmbyd",
                "state": "PAUSED",
                "pin": "",
            },
        )
        assert isinstance(resource, Card)

    def test_method_list(self) -> None:
        resource = self.client.cards.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.cards.list(
            {
                "account_token": "3c1bd0ba-d368-4727-b595-ebccad6dec85",
                "begin": "2019-12-27T18:11:19.117Z",
                "end": "2019-12-27T18:11:19.117Z",
                "page": 13,
                "page_size": 711,
            }
        )
        assert isinstance(resource, SyncPage)

    def test_method_embed(self) -> None:
        resource = self.client.cards.embed()
        assert isinstance(resource, str)

    def test_method_embed_with_optional_params(self) -> None:
        resource = self.client.cards.embed({"embed_request": "znxr", "hmac": "kabppfxgjvjtviqnwefa"})
        assert isinstance(resource, str)

    def test_method_provision(self) -> None:
        resource = self.client.cards.provision("9e6bc870-6676-4821-ae27-9a1133f331ce", {})
        assert isinstance(resource, CardProvisionResponse)

    def test_method_provision_with_optional_params(self) -> None:
        resource = self.client.cards.provision(
            "9e6bc870-6676-4821-ae27-9a1133f331ce",
            {
                "digital_wallet": "GOOGLE_PAY",
                "nonce": "U3RhaW5sZXNzIHJvY2tz",
                "nonce_signature": "U3RhaW5sZXNzIHJvY2tz",
                "certificate": "U3RhaW5sZXNzIHJvY2tz",
                "account_token": "564922d7-3f36-403c-a398-ba8105cdf5b8",
            },
        )
        assert isinstance(resource, CardProvisionResponse)

    def test_method_reissue(self) -> None:
        resource = self.client.cards.reissue("ccdff441-7487-42e7-845d-9581c00dbd6e", {})
        assert isinstance(resource, Card)

    def test_method_reissue_with_optional_params(self) -> None:
        resource = self.client.cards.reissue(
            "ccdff441-7487-42e7-845d-9581c00dbd6e",
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
                "product_id": "bpkalgwogdhrtiefq",
            },
        )
        assert isinstance(resource, Card)


class TestAsyncCards:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.cards.create({"type": "UNLOCKED"})
        assert isinstance(resource, Card)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.cards.create(
            {
                "account_token": "b32237b4-c6fd-44f8-a276-a405bc6caba1",
                "card_program_token": "00000000-0000-0000-1000-000000000000",
                "exp_month": "06",
                "exp_year": "2027",
                "funding_token": "ecbd1d58-0299-48b3-84da-6ed7f5bf9ec1",
                "memo": "New Card",
                "spend_limit": 1,
                "spend_limit_duration": "FOREVER",
                "state": "PAUSED",
                "type": "UNLOCKED",
                "pin": "lwqs",
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
            }
        )
        assert isinstance(resource, Card)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.cards.retrieve(
            "c8eb4011-151f-463c-8ace-db8ceb2b480f",
        )
        assert isinstance(resource, Card)

    async def test_method_update(self) -> None:
        resource = await self.client.cards.update("94ea9316-b0a5-420d-9e76-54395ffbbccc", {})
        assert isinstance(resource, Card)

    async def test_method_update_with_optional_params(self) -> None:
        resource = await self.client.cards.update(
            "94ea9316-b0a5-420d-9e76-54395ffbbccc",
            {
                "account_token": "6fada473-a353-4737-afff-101ad7903975",
                "funding_token": "ecbd1d58-0299-48b3-84da-6ed7f5bf9ec1",
                "memo": "New Card",
                "spend_limit": 1,
                "spend_limit_duration": "MONTHLY",
                "auth_rule_token": "rdgudygsdcppqdbwrrwy",
                "state": "PAUSED",
                "pin": "glt",
            },
        )
        assert isinstance(resource, Card)

    async def test_method_list(self) -> None:
        resource = await self.client.cards.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.cards.list(
            {
                "account_token": "8814a094-566f-4c45-bfee-612dbac03f4d",
                "begin": "2019-12-27T18:11:19.117Z",
                "end": "2019-12-27T18:11:19.117Z",
                "page": 17,
                "page_size": 833,
            }
        )
        assert isinstance(resource, AsyncPage)

    async def test_method_embed(self) -> None:
        resource = await self.client.cards.embed()
        assert isinstance(resource, str)

    async def test_method_embed_with_optional_params(self) -> None:
        resource = await self.client.cards.embed({"embed_request": "xmxefzytbbwklc", "hmac": "uhttvuccdxjvkptsq"})
        assert isinstance(resource, str)

    async def test_method_provision(self) -> None:
        resource = await self.client.cards.provision("5b7c2c71-c889-425d-9b30-ec8df8e6510d", {})
        assert isinstance(resource, CardProvisionResponse)

    async def test_method_provision_with_optional_params(self) -> None:
        resource = await self.client.cards.provision(
            "5b7c2c71-c889-425d-9b30-ec8df8e6510d",
            {
                "digital_wallet": "SAMSUNG_PAY",
                "nonce": "U3RhaW5sZXNzIHJvY2tz",
                "nonce_signature": "U3RhaW5sZXNzIHJvY2tz",
                "certificate": "U3RhaW5sZXNzIHJvY2tz",
                "account_token": "065e5dea-75ec-418d-9968-045744378c2a",
            },
        )
        assert isinstance(resource, CardProvisionResponse)

    async def test_method_reissue(self) -> None:
        resource = await self.client.cards.reissue("3a3e70f3-8b56-48a9-a9bb-e72fc2b00507", {})
        assert isinstance(resource, Card)

    async def test_method_reissue_with_optional_params(self) -> None:
        resource = await self.client.cards.reissue(
            "3a3e70f3-8b56-48a9-a9bb-e72fc2b00507",
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
                "product_id": "",
            },
        )
        assert isinstance(resource, Card)
