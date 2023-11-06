# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from datetime import date

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from .line_items import (
    LineItems,
    AsyncLineItems,
    LineItemsWithRawResponse,
    AsyncLineItemsWithRawResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.financial_accounts import Statement, statement_list_params

if TYPE_CHECKING:
    from ...._client import Lithic, AsyncLithic

__all__ = ["Statements", "AsyncStatements"]


class Statements(SyncAPIResource):
    line_items: LineItems
    with_raw_response: StatementsWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.line_items = LineItems(client)
        self.with_raw_response = StatementsWithRawResponse(self)

    def retrieve(
        self,
        statement_token: str,
        *,
        financial_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Statement:
        """
        Get a specific statement for a given financial account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/financial_accounts/{financial_account_token}/statements/{statement_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Statement,
        )

    def list(
        self,
        financial_account_token: str,
        *,
        begin: Union[str, date] | NotGiven = NOT_GIVEN,
        end: Union[str, date] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Statement]:
        """
        List the statements for a given financial account.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified date
              will be included.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included.

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
            f"/financial_accounts/{financial_account_token}/statements",
            page=SyncCursorPage[Statement],
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
                    statement_list_params.StatementListParams,
                ),
            ),
            model=Statement,
        )


class AsyncStatements(AsyncAPIResource):
    line_items: AsyncLineItems
    with_raw_response: AsyncStatementsWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.line_items = AsyncLineItems(client)
        self.with_raw_response = AsyncStatementsWithRawResponse(self)

    async def retrieve(
        self,
        statement_token: str,
        *,
        financial_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Statement:
        """
        Get a specific statement for a given financial account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/financial_accounts/{financial_account_token}/statements/{statement_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Statement,
        )

    def list(
        self,
        financial_account_token: str,
        *,
        begin: Union[str, date] | NotGiven = NOT_GIVEN,
        end: Union[str, date] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Statement, AsyncCursorPage[Statement]]:
        """
        List the statements for a given financial account.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified date
              will be included.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included.

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
            f"/financial_accounts/{financial_account_token}/statements",
            page=AsyncCursorPage[Statement],
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
                    statement_list_params.StatementListParams,
                ),
            ),
            model=Statement,
        )


class StatementsWithRawResponse:
    def __init__(self, statements: Statements) -> None:
        self.line_items = LineItemsWithRawResponse(statements.line_items)

        self.retrieve = to_raw_response_wrapper(
            statements.retrieve,
        )
        self.list = to_raw_response_wrapper(
            statements.list,
        )


class AsyncStatementsWithRawResponse:
    def __init__(self, statements: AsyncStatements) -> None:
        self.line_items = AsyncLineItemsWithRawResponse(statements.line_items)

        self.retrieve = async_to_raw_response_wrapper(
            statements.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            statements.list,
        )
