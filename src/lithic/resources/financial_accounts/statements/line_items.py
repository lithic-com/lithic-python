# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .... import _legacy_response
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.financial_accounts.statements import LineItemListResponse, line_item_list_params

__all__ = ["LineItems", "AsyncLineItems"]


class LineItems(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LineItemsWithRawResponse:
        return LineItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LineItemsWithStreamingResponse:
        return LineItemsWithStreamingResponse(self)

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
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        if not statement_token:
            raise ValueError(f"Expected a non-empty value for `statement_token` but received {statement_token!r}")
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
    @cached_property
    def with_raw_response(self) -> AsyncLineItemsWithRawResponse:
        return AsyncLineItemsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLineItemsWithStreamingResponse:
        return AsyncLineItemsWithStreamingResponse(self)

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
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        if not statement_token:
            raise ValueError(f"Expected a non-empty value for `statement_token` but received {statement_token!r}")
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
        self._line_items = line_items

        self.list = _legacy_response.to_raw_response_wrapper(
            line_items.list,
        )


class AsyncLineItemsWithRawResponse:
    def __init__(self, line_items: AsyncLineItems) -> None:
        self._line_items = line_items

        self.list = _legacy_response.async_to_raw_response_wrapper(
            line_items.list,
        )


class LineItemsWithStreamingResponse:
    def __init__(self, line_items: LineItems) -> None:
        self._line_items = line_items

        self.list = to_streamed_response_wrapper(
            line_items.list,
        )


class AsyncLineItemsWithStreamingResponse:
    def __init__(self, line_items: AsyncLineItems) -> None:
        self._line_items = line_items

        self.list = async_to_streamed_response_wrapper(
            line_items.list,
        )
