# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    Card,
    CardSpendLimits,
    CardProvisionResponse,
)
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            carrier={"qr_code_url": "string"},
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            exp_month="06",
            exp_year="2027",
            memo="New Card",
            pin="string",
            product_id="1",
            replacement_for="00000000-0000-0000-1000-000000000000",
            shipping_address={
                "address1": "5 Broad Street",
                "address2": "Unit 25A",
                "city": "NEW YORK",
                "country": "USA",
                "email": "johnny@appleseed.com",
                "first_name": "Michael",
                "last_name": "Bluth",
                "line2_text": "The Bluth Company",
                "phone_number": "+12124007676",
                "postal_code": "10001-1809",
                "state": "NY",
            },
            shipping_method="2_DAY",
            spend_limit=1000,
            spend_limit_duration="TRANSACTION",
            state="OPEN",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.cards.with_raw_response.create(
            type="VIRTUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.cards.with_streaming_response.create(
            type="VIRTUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        card = client.cards.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.cards.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.cards.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.with_raw_response.retrieve(
                "",
            )

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
            memo="Updated Name",
            pin="string",
            spend_limit=100,
            spend_limit_duration="FOREVER",
            state="OPEN",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.cards.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.cards.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.with_raw_response.update(
                "",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        card = client.cards.list()
        assert_matches_type(SyncCursorPage[Card], card, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        card = client.cards.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            page_size=1,
            starting_after="string",
            state="CLOSED",
        )
        assert_matches_type(SyncCursorPage[Card], card, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(SyncCursorPage[Card], card, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(SyncCursorPage[Card], card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_embed(self, client: Lithic) -> None:
        card = client.cards.embed(
            embed_request="string",
            hmac="string",
        )
        assert_matches_type(str, card, path=["response"])

    @parametrize
    def test_raw_response_embed(self, client: Lithic) -> None:
        response = client.cards.with_raw_response.embed(
            embed_request="string",
            hmac="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(str, card, path=["response"])

    @parametrize
    def test_streaming_response_embed(self, client: Lithic) -> None:
        with client.cards.with_streaming_response.embed(
            embed_request="string",
            hmac="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(str, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    def test_get_embed_html(self, client: Lithic) -> None:
        html = client.cards.get_embed_html(token="foo")
        assert "html" in html

    def test_get_embed_url(self, client: Lithic) -> None:
        url = client.cards.get_embed_url(token="foo")
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
            digital_wallet="GOOGLE_PAY",
            nonce="U3RhaW5sZXNzIHJvY2tz",
            nonce_signature="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    def test_raw_response_provision(self, client: Lithic) -> None:
        response = client.cards.with_raw_response.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    def test_streaming_response_provision(self, client: Lithic) -> None:
        with client.cards.with_streaming_response.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardProvisionResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_provision(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.with_raw_response.provision(
                "",
            )

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
            carrier={"qr_code_url": "https://lithic.com/activate-card/1"},
            product_id="100",
            shipping_address={
                "address1": "5 Broad Street",
                "address2": "Unit 5A",
                "city": "NEW YORK",
                "country": "USA",
                "email": "johnny@appleseed.com",
                "first_name": "Janet",
                "last_name": "Yellen",
                "line2_text": "The Bluth Company",
                "phone_number": "+12124007676",
                "postal_code": "10001",
                "state": "NY",
            },
            shipping_method="STANDARD",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_raw_response_reissue(self, client: Lithic) -> None:
        response = client.cards.with_raw_response.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_reissue(self, client: Lithic) -> None:
        with client.cards.with_streaming_response.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reissue(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.with_raw_response.reissue(
                "",
            )

    @parametrize
    def test_method_renew(self, client: Lithic) -> None:
        card = client.cards.renew(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            shipping_address={
                "address1": "5 Broad Street",
                "city": "NEW YORK",
                "country": "USA",
                "first_name": "Janet",
                "last_name": "Yellen",
                "postal_code": "10001",
                "state": "NY",
            },
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_method_renew_with_all_params(self, client: Lithic) -> None:
        card = client.cards.renew(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            shipping_address={
                "address1": "5 Broad Street",
                "address2": "Unit 5A",
                "city": "NEW YORK",
                "country": "USA",
                "email": "johnny@appleseed.com",
                "first_name": "Janet",
                "last_name": "Yellen",
                "line2_text": "The Bluth Company",
                "phone_number": "+12124007676",
                "postal_code": "10001",
                "state": "NY",
            },
            carrier={"qr_code_url": "https://lithic.com/activate-card/1"},
            exp_month="06",
            exp_year="2027",
            product_id="100",
            shipping_method="STANDARD",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_raw_response_renew(self, client: Lithic) -> None:
        response = client.cards.with_raw_response.renew(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            shipping_address={
                "address1": "5 Broad Street",
                "city": "NEW YORK",
                "country": "USA",
                "first_name": "Janet",
                "last_name": "Yellen",
                "postal_code": "10001",
                "state": "NY",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_renew(self, client: Lithic) -> None:
        with client.cards.with_streaming_response.renew(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            shipping_address={
                "address1": "5 Broad Street",
                "city": "NEW YORK",
                "country": "USA",
                "first_name": "Janet",
                "last_name": "Yellen",
                "postal_code": "10001",
                "state": "NY",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_renew(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.with_raw_response.renew(
                "",
                shipping_address={
                    "address1": "5 Broad Street",
                    "city": "NEW YORK",
                    "country": "USA",
                    "first_name": "Janet",
                    "last_name": "Yellen",
                    "postal_code": "10001",
                    "state": "NY",
                },
            )

    @parametrize
    def test_method_retrieve_spend_limits(self, client: Lithic) -> None:
        card = client.cards.retrieve_spend_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardSpendLimits, card, path=["response"])

    @parametrize
    def test_raw_response_retrieve_spend_limits(self, client: Lithic) -> None:
        response = client.cards.with_raw_response.retrieve_spend_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardSpendLimits, card, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_spend_limits(self, client: Lithic) -> None:
        with client.cards.with_streaming_response.retrieve_spend_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardSpendLimits, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_spend_limits(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            client.cards.with_raw_response.retrieve_spend_limits(
                "",
            )

    @parametrize
    def test_method_search_by_pan(self, client: Lithic) -> None:
        card = client.cards.search_by_pan(
            pan="4111111289144142",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_raw_response_search_by_pan(self, client: Lithic) -> None:
        response = client.cards.with_raw_response.search_by_pan(
            pan="4111111289144142",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    def test_streaming_response_search_by_pan(self, client: Lithic) -> None:
        with client.cards.with_streaming_response.search_by_pan(
            pan="4111111289144142",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCards:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.create(
            type="VIRTUAL",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.create(
            type="VIRTUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_program_token="00000000-0000-0000-1000-000000000000",
            carrier={"qr_code_url": "string"},
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            exp_month="06",
            exp_year="2027",
            memo="New Card",
            pin="string",
            product_id="1",
            replacement_for="00000000-0000-0000-1000-000000000000",
            shipping_address={
                "address1": "5 Broad Street",
                "address2": "Unit 25A",
                "city": "NEW YORK",
                "country": "USA",
                "email": "johnny@appleseed.com",
                "first_name": "Michael",
                "last_name": "Bluth",
                "line2_text": "The Bluth Company",
                "phone_number": "+12124007676",
                "postal_code": "10001-1809",
                "state": "NY",
            },
            shipping_method="2_DAY",
            spend_limit=1000,
            spend_limit_duration="TRANSACTION",
            state="OPEN",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.cards.with_raw_response.create(
            type="VIRTUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.cards.with_streaming_response.create(
            type="VIRTUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.cards.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.cards.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth_rule_token="string",
            digital_card_art_token="00000000-0000-0000-1000-000000000000",
            memo="Updated Name",
            pin="string",
            spend_limit=100,
            spend_limit_duration="FOREVER",
            state="OPEN",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLithic) -> None:
        response = await async_client.cards.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLithic) -> None:
        async with async_client.cards.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.with_raw_response.update(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.list()
        assert_matches_type(AsyncCursorPage[Card], card, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            page_size=1,
            starting_after="string",
            state="CLOSED",
        )
        assert_matches_type(AsyncCursorPage[Card], card, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(AsyncCursorPage[Card], card, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(AsyncCursorPage[Card], card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_embed(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.embed(
            embed_request="string",
            hmac="string",
        )
        assert_matches_type(str, card, path=["response"])

    @parametrize
    async def test_raw_response_embed(self, async_client: AsyncLithic) -> None:
        response = await async_client.cards.with_raw_response.embed(
            embed_request="string",
            hmac="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(str, card, path=["response"])

    @parametrize
    async def test_streaming_response_embed(self, async_client: AsyncLithic) -> None:
        async with async_client.cards.with_streaming_response.embed(
            embed_request="string",
            hmac="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(str, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    async def test_get_embed_html(self, async_client: AsyncLithic) -> None:
        html = await async_client.cards.get_embed_html(token="foo")
        assert "html" in html

    def test_get_embed_url(self, async_client: Lithic) -> None:
        url = async_client.cards.get_embed_url(token="foo")
        params = set(  # pyright: ignore[reportUnknownVariableType]
            url.params.keys()  # pyright: ignore[reportUnknownMemberType,reportUnknownArgumentType]
        )
        assert "hmac" in params
        assert "embed_request" in params

    @parametrize
    async def test_method_provision(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    async def test_method_provision_with_all_params(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            certificate="U3RhaW5sZXNzIHJvY2tz",
            digital_wallet="GOOGLE_PAY",
            nonce="U3RhaW5sZXNzIHJvY2tz",
            nonce_signature="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    async def test_raw_response_provision(self, async_client: AsyncLithic) -> None:
        response = await async_client.cards.with_raw_response.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardProvisionResponse, card, path=["response"])

    @parametrize
    async def test_streaming_response_provision(self, async_client: AsyncLithic) -> None:
        async with async_client.cards.with_streaming_response.provision(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardProvisionResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_provision(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.with_raw_response.provision(
                "",
            )

    @parametrize
    async def test_method_reissue(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_reissue_with_all_params(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            carrier={"qr_code_url": "https://lithic.com/activate-card/1"},
            product_id="100",
            shipping_address={
                "address1": "5 Broad Street",
                "address2": "Unit 5A",
                "city": "NEW YORK",
                "country": "USA",
                "email": "johnny@appleseed.com",
                "first_name": "Janet",
                "last_name": "Yellen",
                "line2_text": "The Bluth Company",
                "phone_number": "+12124007676",
                "postal_code": "10001",
                "state": "NY",
            },
            shipping_method="STANDARD",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_reissue(self, async_client: AsyncLithic) -> None:
        response = await async_client.cards.with_raw_response.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_reissue(self, async_client: AsyncLithic) -> None:
        async with async_client.cards.with_streaming_response.reissue(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reissue(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.with_raw_response.reissue(
                "",
            )

    @parametrize
    async def test_method_renew(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.renew(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            shipping_address={
                "address1": "5 Broad Street",
                "city": "NEW YORK",
                "country": "USA",
                "first_name": "Janet",
                "last_name": "Yellen",
                "postal_code": "10001",
                "state": "NY",
            },
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_method_renew_with_all_params(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.renew(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            shipping_address={
                "address1": "5 Broad Street",
                "address2": "Unit 5A",
                "city": "NEW YORK",
                "country": "USA",
                "email": "johnny@appleseed.com",
                "first_name": "Janet",
                "last_name": "Yellen",
                "line2_text": "The Bluth Company",
                "phone_number": "+12124007676",
                "postal_code": "10001",
                "state": "NY",
            },
            carrier={"qr_code_url": "https://lithic.com/activate-card/1"},
            exp_month="06",
            exp_year="2027",
            product_id="100",
            shipping_method="STANDARD",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_renew(self, async_client: AsyncLithic) -> None:
        response = await async_client.cards.with_raw_response.renew(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            shipping_address={
                "address1": "5 Broad Street",
                "city": "NEW YORK",
                "country": "USA",
                "first_name": "Janet",
                "last_name": "Yellen",
                "postal_code": "10001",
                "state": "NY",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_renew(self, async_client: AsyncLithic) -> None:
        async with async_client.cards.with_streaming_response.renew(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            shipping_address={
                "address1": "5 Broad Street",
                "city": "NEW YORK",
                "country": "USA",
                "first_name": "Janet",
                "last_name": "Yellen",
                "postal_code": "10001",
                "state": "NY",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_renew(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.with_raw_response.renew(
                "",
                shipping_address={
                    "address1": "5 Broad Street",
                    "city": "NEW YORK",
                    "country": "USA",
                    "first_name": "Janet",
                    "last_name": "Yellen",
                    "postal_code": "10001",
                    "state": "NY",
                },
            )

    @parametrize
    async def test_method_retrieve_spend_limits(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.retrieve_spend_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardSpendLimits, card, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_spend_limits(self, async_client: AsyncLithic) -> None:
        response = await async_client.cards.with_raw_response.retrieve_spend_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardSpendLimits, card, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_spend_limits(self, async_client: AsyncLithic) -> None:
        async with async_client.cards.with_streaming_response.retrieve_spend_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardSpendLimits, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_spend_limits(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_token` but received ''"):
            await async_client.cards.with_raw_response.retrieve_spend_limits(
                "",
            )

    @parametrize
    async def test_method_search_by_pan(self, async_client: AsyncLithic) -> None:
        card = await async_client.cards.search_by_pan(
            pan="4111111289144142",
        )
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_raw_response_search_by_pan(self, async_client: AsyncLithic) -> None:
        response = await async_client.cards.with_raw_response.search_by_pan(
            pan="4111111289144142",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(Card, card, path=["response"])

    @parametrize
    async def test_streaming_response_search_by_pan(self, async_client: AsyncLithic) -> None:
        async with async_client.cards.with_streaming_response.search_by_pan(
            pan="4111111289144142",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(Card, card, path=["response"])

        assert cast(Any, response.is_closed) is True
