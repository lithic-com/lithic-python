# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.financial_accounts.statements import (
    LineItemListResponse,
    line_item_list_params,
)

if TYPE_CHECKING:
    from ...._client import Lithic, AsyncLithic

__all__ = ["LineItems", "AsyncLineItems"]


class LineItems(SyncAPIResource):
    with_raw_response: LineItemsWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = LineItemsWithRawResponse(self)

    def list(
        self,
        statement_token: str,
        *,
        financial_account_token: str,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[LineItemListResponse]:
        """
        List the line items for a given statement within a given financial account.

        Args:
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
            f"/financial_accounts/{financial_account_token}/statements/{statement_token}/line_items",
            page=SyncCursorPage[LineItemListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    line_item_list_params.LineItemListParams,
                ),
            ),
            model=LineItemListResponse,
        )


class AsyncLineItems(AsyncAPIResource):
    with_raw_response: AsyncLineItemsWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncLineItemsWithRawResponse(self)

    def list(
        self,
        statement_token: str,
        *,
        financial_account_token: str,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[LineItemListResponse, AsyncCursorPage[LineItemListResponse]]:
        """
        List the line items for a given statement within a given financial account.

        Args:
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
            f"/financial_accounts/{financial_account_token}/statements/{statement_token}/line_items",
            page=AsyncCursorPage[LineItemListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    line_item_list_params.LineItemListParams,
                ),
            ),
            model=LineItemListResponse,
        )


class LineItemsWithRawResponse:
    def __init__(self, line_items: LineItems) -> None:
        self.list = to_raw_response_wrapper(
            line_items.list,
        )


class AsyncLineItemsWithRawResponse:
    def __init__(self, line_items: AsyncLineItems) -> None:
        self.list = async_to_raw_response_wrapper(
            line_items.list,
        )
