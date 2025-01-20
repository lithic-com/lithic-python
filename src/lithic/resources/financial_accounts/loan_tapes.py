# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.financial_accounts import loan_tape_list_params
from ...types.financial_accounts.loan_tape import LoanTape

__all__ = ["LoanTapes", "AsyncLoanTapes"]


class LoanTapes(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoanTapesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return LoanTapesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoanTapesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return LoanTapesWithStreamingResponse(self)

    def retrieve(
        self,
        loan_tape_token: str,
        *,
        financial_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoanTape:
        """
        Get a specific loan tape for a given financial account.

        Args:
          financial_account_token: Globally unique identifier for financial account.

          loan_tape_token: Globally unique identifier for loan tape.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        if not loan_tape_token:
            raise ValueError(f"Expected a non-empty value for `loan_tape_token` but received {loan_tape_token!r}")
        return self._get(
            f"/v1/financial_accounts/{financial_account_token}/loan_tapes/{loan_tape_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoanTape,
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
    ) -> SyncCursorPage[LoanTape]:
        """
        List the loan tapes for a given financial account.

        Args:
          financial_account_token: Globally unique identifier for financial account.

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
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        return self._get_api_list(
            f"/v1/financial_accounts/{financial_account_token}/loan_tapes",
            page=SyncCursorPage[LoanTape],
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
                    loan_tape_list_params.LoanTapeListParams,
                ),
            ),
            model=LoanTape,
        )


class AsyncLoanTapes(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoanTapesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoanTapesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoanTapesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncLoanTapesWithStreamingResponse(self)

    async def retrieve(
        self,
        loan_tape_token: str,
        *,
        financial_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LoanTape:
        """
        Get a specific loan tape for a given financial account.

        Args:
          financial_account_token: Globally unique identifier for financial account.

          loan_tape_token: Globally unique identifier for loan tape.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        if not loan_tape_token:
            raise ValueError(f"Expected a non-empty value for `loan_tape_token` but received {loan_tape_token!r}")
        return await self._get(
            f"/v1/financial_accounts/{financial_account_token}/loan_tapes/{loan_tape_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoanTape,
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
    ) -> AsyncPaginator[LoanTape, AsyncCursorPage[LoanTape]]:
        """
        List the loan tapes for a given financial account.

        Args:
          financial_account_token: Globally unique identifier for financial account.

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
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        return self._get_api_list(
            f"/v1/financial_accounts/{financial_account_token}/loan_tapes",
            page=AsyncCursorPage[LoanTape],
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
                    loan_tape_list_params.LoanTapeListParams,
                ),
            ),
            model=LoanTape,
        )


class LoanTapesWithRawResponse:
    def __init__(self, loan_tapes: LoanTapes) -> None:
        self._loan_tapes = loan_tapes

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            loan_tapes.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            loan_tapes.list,
        )


class AsyncLoanTapesWithRawResponse:
    def __init__(self, loan_tapes: AsyncLoanTapes) -> None:
        self._loan_tapes = loan_tapes

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            loan_tapes.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            loan_tapes.list,
        )


class LoanTapesWithStreamingResponse:
    def __init__(self, loan_tapes: LoanTapes) -> None:
        self._loan_tapes = loan_tapes

        self.retrieve = to_streamed_response_wrapper(
            loan_tapes.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            loan_tapes.list,
        )


class AsyncLoanTapesWithStreamingResponse:
    def __init__(self, loan_tapes: AsyncLoanTapes) -> None:
        self._loan_tapes = loan_tapes

        self.retrieve = async_to_streamed_response_wrapper(
            loan_tapes.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            loan_tapes.list,
        )
