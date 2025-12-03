# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import card_bulk_order_list_params, card_bulk_order_create_params, card_bulk_order_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.card_bulk_order import CardBulkOrder

__all__ = ["CardBulkOrders", "AsyncCardBulkOrders"]


class CardBulkOrders(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardBulkOrdersWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return CardBulkOrdersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardBulkOrdersWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return CardBulkOrdersWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_product_id: str,
        shipping_address: object,
        shipping_method: Literal["BULK_EXPEDITED"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardBulkOrder:
        """Create a new bulk order for physical card shipments **[BETA]**.

        Cards can be
        added to the order via the POST /v1/cards endpoint by specifying the
        bulk_order_token. Lock the order via PATCH
        /v1/card_bulk_orders/{bulk_order_token} to prepare for shipment. Please work
        with your Customer Success Manager and card personalization bureau to ensure
        bulk shipping is supported for your program.

        Args:
          customer_product_id: Customer-specified product configuration for physical card manufacturing. This
              must be configured with Lithic before use

          shipping_address: Shipping address for all cards in this bulk order

          shipping_method: Shipping method for all cards in this bulk order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/card_bulk_orders",
            body=maybe_transform(
                {
                    "customer_product_id": customer_product_id,
                    "shipping_address": shipping_address,
                    "shipping_method": shipping_method,
                },
                card_bulk_order_create_params.CardBulkOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardBulkOrder,
        )

    def retrieve(
        self,
        bulk_order_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardBulkOrder:
        """
        Retrieve a specific bulk order by token **[BETA]**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bulk_order_token:
            raise ValueError(f"Expected a non-empty value for `bulk_order_token` but received {bulk_order_token!r}")
        return self._get(
            f"/v1/card_bulk_orders/{bulk_order_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardBulkOrder,
        )

    def update(
        self,
        bulk_order_token: str,
        *,
        status: Literal["LOCKED"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardBulkOrder:
        """Update a bulk order **[BETA]**.

        Primarily used to lock the order, preventing
        additional cards from being added

        Args:
          status: Status to update the bulk order to. Use LOCKED to finalize the order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bulk_order_token:
            raise ValueError(f"Expected a non-empty value for `bulk_order_token` but received {bulk_order_token!r}")
        return self._patch(
            f"/v1/card_bulk_orders/{bulk_order_token}",
            body=maybe_transform({"status": status}, card_bulk_order_update_params.CardBulkOrderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardBulkOrder,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CardBulkOrder]:
        """
        List bulk orders for physical card shipments **[BETA]**

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/card_bulk_orders",
            page=SyncCursorPage[CardBulkOrder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    card_bulk_order_list_params.CardBulkOrderListParams,
                ),
            ),
            model=CardBulkOrder,
        )


class AsyncCardBulkOrders(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardBulkOrdersWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardBulkOrdersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardBulkOrdersWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncCardBulkOrdersWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_product_id: str,
        shipping_address: object,
        shipping_method: Literal["BULK_EXPEDITED"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardBulkOrder:
        """Create a new bulk order for physical card shipments **[BETA]**.

        Cards can be
        added to the order via the POST /v1/cards endpoint by specifying the
        bulk_order_token. Lock the order via PATCH
        /v1/card_bulk_orders/{bulk_order_token} to prepare for shipment. Please work
        with your Customer Success Manager and card personalization bureau to ensure
        bulk shipping is supported for your program.

        Args:
          customer_product_id: Customer-specified product configuration for physical card manufacturing. This
              must be configured with Lithic before use

          shipping_address: Shipping address for all cards in this bulk order

          shipping_method: Shipping method for all cards in this bulk order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/card_bulk_orders",
            body=await async_maybe_transform(
                {
                    "customer_product_id": customer_product_id,
                    "shipping_address": shipping_address,
                    "shipping_method": shipping_method,
                },
                card_bulk_order_create_params.CardBulkOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardBulkOrder,
        )

    async def retrieve(
        self,
        bulk_order_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardBulkOrder:
        """
        Retrieve a specific bulk order by token **[BETA]**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bulk_order_token:
            raise ValueError(f"Expected a non-empty value for `bulk_order_token` but received {bulk_order_token!r}")
        return await self._get(
            f"/v1/card_bulk_orders/{bulk_order_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardBulkOrder,
        )

    async def update(
        self,
        bulk_order_token: str,
        *,
        status: Literal["LOCKED"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardBulkOrder:
        """Update a bulk order **[BETA]**.

        Primarily used to lock the order, preventing
        additional cards from being added

        Args:
          status: Status to update the bulk order to. Use LOCKED to finalize the order

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not bulk_order_token:
            raise ValueError(f"Expected a non-empty value for `bulk_order_token` but received {bulk_order_token!r}")
        return await self._patch(
            f"/v1/card_bulk_orders/{bulk_order_token}",
            body=await async_maybe_transform(
                {"status": status}, card_bulk_order_update_params.CardBulkOrderUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardBulkOrder,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CardBulkOrder, AsyncCursorPage[CardBulkOrder]]:
        """
        List bulk orders for physical card shipments **[BETA]**

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/card_bulk_orders",
            page=AsyncCursorPage[CardBulkOrder],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    card_bulk_order_list_params.CardBulkOrderListParams,
                ),
            ),
            model=CardBulkOrder,
        )


class CardBulkOrdersWithRawResponse:
    def __init__(self, card_bulk_orders: CardBulkOrders) -> None:
        self._card_bulk_orders = card_bulk_orders

        self.create = _legacy_response.to_raw_response_wrapper(
            card_bulk_orders.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            card_bulk_orders.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            card_bulk_orders.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            card_bulk_orders.list,
        )


class AsyncCardBulkOrdersWithRawResponse:
    def __init__(self, card_bulk_orders: AsyncCardBulkOrders) -> None:
        self._card_bulk_orders = card_bulk_orders

        self.create = _legacy_response.async_to_raw_response_wrapper(
            card_bulk_orders.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            card_bulk_orders.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            card_bulk_orders.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            card_bulk_orders.list,
        )


class CardBulkOrdersWithStreamingResponse:
    def __init__(self, card_bulk_orders: CardBulkOrders) -> None:
        self._card_bulk_orders = card_bulk_orders

        self.create = to_streamed_response_wrapper(
            card_bulk_orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            card_bulk_orders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            card_bulk_orders.update,
        )
        self.list = to_streamed_response_wrapper(
            card_bulk_orders.list,
        )


class AsyncCardBulkOrdersWithStreamingResponse:
    def __init__(self, card_bulk_orders: AsyncCardBulkOrders) -> None:
        self._card_bulk_orders = card_bulk_orders

        self.create = async_to_streamed_response_wrapper(
            card_bulk_orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            card_bulk_orders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            card_bulk_orders.update,
        )
        self.list = async_to_streamed_response_wrapper(
            card_bulk_orders.list,
        )
