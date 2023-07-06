# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import Card, CardProvisionResponse
from lithic._utils import parse_datetime
from lithic.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestCards:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        card = client.cards.create(
            type="VIRTUAL",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        card = client.cards.create(
            type="VIRTUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_program_token="00000000-0000-0000-1000-000000000000",
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            exp_month="06",
            exp_year="2027",
            memo="New Card",
            pin="string",
            product_id="1",
            shipping_address={
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
            shipping_method="STANDARD",
            spend_limit=0,
            spend_limit_duration="ANNUALLY",
            state="OPEN",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        card = client.cards.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        card = client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        card = client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth_rule_token="string",
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            memo="New Card",
            pin="string",
            spend_limit=0,
            spend_limit_duration="ANNUALLY",
            state="CLOSED",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        card = client.cards.list()
        assert_matches_type(SyncPage[Card], card, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        card = client.cards.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            page=0,
            page_size=1,
            state="OPEN",
        )
        assert_matches_type(SyncPage[Card], card, path=["response"])

    @parametrize
    def test_method_embed(self, client: Lithic) -> None:
        card = client.cards.embed(
            embed_request="string",
            hmac="string",
        )
        assert_matches_type(str, card, path=["response"])

    def test_get_embed_html(self) -> None:
        html = self.strict_client.cards.get_embed_html(token="foo")
        assert "html" in html

    def test_get_embed_url(self) -> None:
        url = self.strict_client.cards.get_embed_url(token="foo")
        params = set(  # pyright: ignore[reportUnknownVariableType]
            url.params.keys()  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
        )
        assert "hmac" in params
        assert "embed_request" in params

    @parametrize
    def test_method_provision(self, client: Lithic) -> None:
        card = client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    def test_method_provision_with_all_params(self, client: Lithic) -> None:
        card = client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            certificate="U3RhaW5sZXNzIHJvY2tz",
            digital_wallet="APPLE_PAY",
            nonce="U3RhaW5sZXNzIHJvY2tz",
            nonce_signature="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    def test_method_reissue(self, client: Lithic) -> None:
        card = client.cards.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_reissue_with_all_params(self, client: Lithic) -> None:
        card = client.cards.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            product_id="string",
            shipping_address={
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
            shipping_method="STANDARD",
        )
        assert_matches_type(Card, card, path=["response"])


class TestAsyncCards:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncLithic) -> None:
        card = await client.cards.create(
            type="VIRTUAL",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncLithic) -> None:
        card = await client.cards.create(
            type="VIRTUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_program_token="00000000-0000-0000-1000-000000000000",
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            exp_month="06",
            exp_year="2027",
            memo="New Card",
            pin="string",
            product_id="1",
            shipping_address={
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
            shipping_method="STANDARD",
            spend_limit=0,
            spend_limit_duration="ANNUALLY",
            state="OPEN",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        card = await client.cards.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncLithic) -> None:
        card = await client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncLithic) -> None:
        card = await client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth_rule_token="string",
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            memo="New Card",
            pin="string",
            spend_limit=0,
            spend_limit_duration="ANNUALLY",
            state="CLOSED",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        card = await client.cards.list()
        assert_matches_type(AsyncPage[Card], card, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        card = await client.cards.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            page=0,
            page_size=1,
            state="OPEN",
        )
        assert_matches_type(AsyncPage[Card], card, path=["response"])

    @parametrize
    async def test_method_embed(self, client: AsyncLithic) -> None:
        card = await client.cards.embed(
            embed_request="string",
            hmac="string",
        )
        assert_matches_type(str, card, path=["response"])

    async def test_get_embed_html(self) -> None:
        html = await self.strict_client.cards.get_embed_html(token="foo")
        assert "html" in html

    def test_get_embed_url(self) -> None:
        url = self.strict_client.cards.get_embed_url(token="foo")
        params = set(  # pyright: ignore[reportUnknownVariableType]
            url.params.keys()  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
        )
        assert "hmac" in params
        assert "embed_request" in params

    @parametrize
    async def test_method_provision(self, client: AsyncLithic) -> None:
        card = await client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    async def test_method_provision_with_all_params(self, client: AsyncLithic) -> None:
        card = await client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            certificate="U3RhaW5sZXNzIHJvY2tz",
            digital_wallet="APPLE_PAY",
            nonce="U3RhaW5sZXNzIHJvY2tz",
            nonce_signature="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    async def test_method_reissue(self, client: AsyncLithic) -> None:
        card = await client.cards.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_reissue_with_all_params(self, client: AsyncLithic) -> None:
        card = await client.cards.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            product_id="string",
            shipping_address={
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
            shipping_method="STANDARD",
        )
        assert_matches_type(Card, card, path=["response"])
