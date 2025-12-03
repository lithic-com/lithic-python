# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    CardBulkOrder,
)
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardBulkOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        card_bulk_order = client.card_bulk_orders.create(
            customer_product_id="custom-card-design-123",
            shipping_address={
                "address1": "123 Main Street",
                "city": "NEW YORK",
                "country": "USA",
                "first_name": "Johnny",
                "last_name": "Appleseed",
                "postal_code": "10001",
                "state": "NY",
            },
            shipping_method="BULK_EXPEDITED",
        )
        assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.card_bulk_orders.with_raw_response.create(
            customer_product_id="custom-card-design-123",
            shipping_address={
                "address1": "123 Main Street",
                "city": "NEW YORK",
                "country": "USA",
                "first_name": "Johnny",
                "last_name": "Appleseed",
                "postal_code": "10001",
                "state": "NY",
            },
            shipping_method="BULK_EXPEDITED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_bulk_order = response.parse()
        assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.card_bulk_orders.with_streaming_response.create(
            customer_product_id="custom-card-design-123",
            shipping_address={
                "address1": "123 Main Street",
                "city": "NEW YORK",
                "country": "USA",
                "first_name": "Johnny",
                "last_name": "Appleseed",
                "postal_code": "10001",
                "state": "NY",
            },
            shipping_method="BULK_EXPEDITED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_bulk_order = response.parse()
            assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        card_bulk_order = client.card_bulk_orders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.card_bulk_orders.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_bulk_order = response.parse()
        assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.card_bulk_orders.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_bulk_order = response.parse()
            assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bulk_order_token` but received ''"):
            client.card_bulk_orders.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        card_bulk_order = client.card_bulk_orders.update(
            bulk_order_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="LOCKED",
        )
        assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.card_bulk_orders.with_raw_response.update(
            bulk_order_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="LOCKED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_bulk_order = response.parse()
        assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.card_bulk_orders.with_streaming_response.update(
            bulk_order_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="LOCKED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_bulk_order = response.parse()
            assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bulk_order_token` but received ''"):
            client.card_bulk_orders.with_raw_response.update(
                bulk_order_token="",
                status="LOCKED",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        card_bulk_order = client.card_bulk_orders.list()
        assert_matches_type(SyncCursorPage[CardBulkOrder], card_bulk_order, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        card_bulk_order = client.card_bulk_orders.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(SyncCursorPage[CardBulkOrder], card_bulk_order, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.card_bulk_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_bulk_order = response.parse()
        assert_matches_type(SyncCursorPage[CardBulkOrder], card_bulk_order, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.card_bulk_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_bulk_order = response.parse()
            assert_matches_type(SyncCursorPage[CardBulkOrder], card_bulk_order, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardBulkOrders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        card_bulk_order = await async_client.card_bulk_orders.create(
            customer_product_id="custom-card-design-123",
            shipping_address={
                "address1": "123 Main Street",
                "city": "NEW YORK",
                "country": "USA",
                "first_name": "Johnny",
                "last_name": "Appleseed",
                "postal_code": "10001",
                "state": "NY",
            },
            shipping_method="BULK_EXPEDITED",
        )
        assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.card_bulk_orders.with_raw_response.create(
            customer_product_id="custom-card-design-123",
            shipping_address={
                "address1": "123 Main Street",
                "city": "NEW YORK",
                "country": "USA",
                "first_name": "Johnny",
                "last_name": "Appleseed",
                "postal_code": "10001",
                "state": "NY",
            },
            shipping_method="BULK_EXPEDITED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_bulk_order = response.parse()
        assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.card_bulk_orders.with_streaming_response.create(
            customer_product_id="custom-card-design-123",
            shipping_address={
                "address1": "123 Main Street",
                "city": "NEW YORK",
                "country": "USA",
                "first_name": "Johnny",
                "last_name": "Appleseed",
                "postal_code": "10001",
                "state": "NY",
            },
            shipping_method="BULK_EXPEDITED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_bulk_order = await response.parse()
            assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        card_bulk_order = await async_client.card_bulk_orders.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.card_bulk_orders.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_bulk_order = response.parse()
        assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.card_bulk_orders.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_bulk_order = await response.parse()
            assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bulk_order_token` but received ''"):
            await async_client.card_bulk_orders.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLithic) -> None:
        card_bulk_order = await async_client.card_bulk_orders.update(
            bulk_order_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="LOCKED",
        )
        assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLithic) -> None:
        response = await async_client.card_bulk_orders.with_raw_response.update(
            bulk_order_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="LOCKED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_bulk_order = response.parse()
        assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLithic) -> None:
        async with async_client.card_bulk_orders.with_streaming_response.update(
            bulk_order_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="LOCKED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_bulk_order = await response.parse()
            assert_matches_type(CardBulkOrder, card_bulk_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bulk_order_token` but received ''"):
            await async_client.card_bulk_orders.with_raw_response.update(
                bulk_order_token="",
                status="LOCKED",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        card_bulk_order = await async_client.card_bulk_orders.list()
        assert_matches_type(AsyncCursorPage[CardBulkOrder], card_bulk_order, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        card_bulk_order = await async_client.card_bulk_orders.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(AsyncCursorPage[CardBulkOrder], card_bulk_order, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.card_bulk_orders.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_bulk_order = response.parse()
        assert_matches_type(AsyncCursorPage[CardBulkOrder], card_bulk_order, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.card_bulk_orders.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_bulk_order = await response.parse()
            assert_matches_type(AsyncCursorPage[CardBulkOrder], card_bulk_order, path=["response"])

        assert cast(Any, response.is_closed) is True
