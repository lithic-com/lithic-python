# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from .... import _legacy_response
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from .line_items import (
    LineItems,
    AsyncLineItems,
    LineItemsWithRawResponse,
    AsyncLineItemsWithRawResponse,
    LineItemsWithStreamingResponse,
    AsyncLineItemsWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.financial_accounts import statement_list_params
from ....types.financial_accounts.statement import Statement

__all__ = ["Statements", "AsyncStatements"]


class Statements(SyncAPIResource):
    @cached_property
    def line_items(self) -> LineItems:
        return LineItems(self._client)

    @cached_property
    def with_raw_response(self) -> StatementsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return StatementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatementsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return StatementsWithStreamingResponse(self)

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
          financial_account_token: Globally unique identifier for financial account.

          statement_token: Globally unique identifier for statements.

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
        return self._get(
            f"/v1/financial_accounts/{financial_account_token}/statements/{statement_token}",
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
        include_initial_statements: bool | NotGiven = NOT_GIVEN,
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
          financial_account_token: Globally unique identifier for financial account.

          begin: Date string in RFC 3339 format. Only entries created after the specified date
              will be included.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          include_initial_statements: Whether to include the initial statement. It is not included by default.

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
        return self._get_api_list(
            f"/v1/financial_accounts/{financial_account_token}/statements",
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
                        "include_initial_statements": include_initial_statements,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    statement_list_params.StatementListParams,
                ),
            ),
            model=Statement,
        )


class AsyncStatements(AsyncAPIResource):
    @cached_property
    def line_items(self) -> AsyncLineItems:
        return AsyncLineItems(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStatementsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatementsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncStatementsWithStreamingResponse(self)

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
          financial_account_token: Globally unique identifier for financial account.

          statement_token: Globally unique identifier for statements.

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
        return await self._get(
            f"/v1/financial_accounts/{financial_account_token}/statements/{statement_token}",
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
        include_initial_statements: bool | NotGiven = NOT_GIVEN,
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
          financial_account_token: Globally unique identifier for financial account.

          begin: Date string in RFC 3339 format. Only entries created after the specified date
              will be included.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          include_initial_statements: Whether to include the initial statement. It is not included by default.

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
        return self._get_api_list(
            f"/v1/financial_accounts/{financial_account_token}/statements",
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
                        "include_initial_statements": include_initial_statements,
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
        self._statements = statements

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            statements.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            statements.list,
        )

    @cached_property
    def line_items(self) -> LineItemsWithRawResponse:
        return LineItemsWithRawResponse(self._statements.line_items)


class AsyncStatementsWithRawResponse:
    def __init__(self, statements: AsyncStatements) -> None:
        self._statements = statements

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            statements.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            statements.list,
        )

    @cached_property
    def line_items(self) -> AsyncLineItemsWithRawResponse:
        return AsyncLineItemsWithRawResponse(self._statements.line_items)


class StatementsWithStreamingResponse:
    def __init__(self, statements: Statements) -> None:
        self._statements = statements

        self.retrieve = to_streamed_response_wrapper(
            statements.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            statements.list,
        )

    @cached_property
    def line_items(self) -> LineItemsWithStreamingResponse:
        return LineItemsWithStreamingResponse(self._statements.line_items)


class AsyncStatementsWithStreamingResponse:
    def __init__(self, statements: AsyncStatements) -> None:
        self._statements = statements

        self.retrieve = async_to_streamed_response_wrapper(
            statements.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            statements.list,
        )

    @cached_property
    def line_items(self) -> AsyncLineItemsWithStreamingResponse:
        return AsyncLineItemsWithStreamingResponse(self._statements.line_items)
