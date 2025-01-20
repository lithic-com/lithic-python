# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import book_transfer_list_params, book_transfer_create_params, book_transfer_reverse_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.book_transfer_response import BookTransferResponse

__all__ = ["BookTransfers", "AsyncBookTransfers"]


class BookTransfers(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BookTransfersWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return BookTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BookTransfersWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return BookTransfersWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        category: Literal["ADJUSTMENT", "BALANCE_OR_FUNDING", "DERECOGNITION", "DISPUTE", "FEE", "REWARD", "TRANSFER"],
        from_financial_account_token: str,
        subtype: str,
        to_financial_account_token: str,
        type: Literal[
            "ATM_WITHDRAWAL",
            "ATM_DECLINE",
            "INTERNATIONAL_ATM_WITHDRAWAL",
            "INACTIVITY",
            "STATEMENT",
            "MONTHLY",
            "QUARTERLY",
            "ANNUAL",
            "CUSTOMER_SERVICE",
            "ACCOUNT_MAINTENANCE",
            "ACCOUNT_ACTIVATION",
            "ACCOUNT_CLOSURE",
            "CARD_REPLACEMENT",
            "CARD_DELIVERY",
            "CARD_CREATE",
            "CURRENCY_CONVERSION",
            "INTEREST",
            "LATE_PAYMENT",
            "BILL_PAYMENT",
            "CASH_BACK",
            "ACCOUNT_TO_ACCOUNT",
            "CARD_TO_CARD",
            "DISBURSE",
            "BILLING_ERROR",
            "LOSS_WRITE_OFF",
            "EXPIRED_CARD",
            "EARLY_DERECOGNITION",
            "ESCHEATMENT",
            "INACTIVITY_FEE_DOWN",
            "PROVISIONAL_CREDIT",
            "DISPUTE_WON",
            "TRANSFER",
        ],
        token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookTransferResponse:
        """
        Book transfer funds between two financial accounts or between a financial
        account and card

        Args:
          amount: Amount to be transferred in the currency’s smallest unit (e.g., cents for USD).
              This should always be a positive value.

          category: Category of the book transfer

          from_financial_account_token: Globally unique identifier for the financial account or card that will send the
              funds. Accepted type dependent on the program's use case.

          subtype: The program specific subtype code for the specified category/type.

          to_financial_account_token: Globally unique identifier for the financial account or card that will receive
              the funds. Accepted type dependent on the program's use case.

          type: Type of book_transfer

          token: Customer-provided token that will serve as an idempotency token. This token will
              become the transaction token.

          memo: Optional descriptor for the transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/book_transfers",
            body=maybe_transform(
                {
                    "amount": amount,
                    "category": category,
                    "from_financial_account_token": from_financial_account_token,
                    "subtype": subtype,
                    "to_financial_account_token": to_financial_account_token,
                    "type": type,
                    "token": token,
                    "memo": memo,
                },
                book_transfer_create_params.BookTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookTransferResponse,
        )

    def retrieve(
        self,
        book_transfer_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookTransferResponse:
        """
        Get book transfer by token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not book_transfer_token:
            raise ValueError(
                f"Expected a non-empty value for `book_transfer_token` but received {book_transfer_token!r}"
            )
        return self._get(
            f"/v1/book_transfers/{book_transfer_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookTransferResponse,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        category: Literal["BALANCE_OR_FUNDING", "FEE", "REWARD", "ADJUSTMENT", "DERECOGNITION", "DISPUTE", "INTERNAL"]
        | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        result: Literal["APPROVED", "DECLINED"] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["DECLINED", "SETTLED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[BookTransferResponse]:
        """List book transfers

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          category: Book Transfer category to be returned.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          financial_account_token: Globally unique identifier for the financial account or card that will send the
              funds. Accepted type dependent on the program's use case.

          page_size: Page size (for pagination).

          result: Book transfer result to be returned.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Book transfer status to be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/book_transfers",
            page=SyncCursorPage[BookTransferResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "begin": begin,
                        "business_account_token": business_account_token,
                        "category": category,
                        "end": end,
                        "ending_before": ending_before,
                        "financial_account_token": financial_account_token,
                        "page_size": page_size,
                        "result": result,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    book_transfer_list_params.BookTransferListParams,
                ),
            ),
            model=BookTransferResponse,
        )

    def reverse(
        self,
        book_transfer_token: str,
        *,
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookTransferResponse:
        """
        Reverse a book transfer

        Args:
          memo: Optional descriptor for the reversal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not book_transfer_token:
            raise ValueError(
                f"Expected a non-empty value for `book_transfer_token` but received {book_transfer_token!r}"
            )
        return self._post(
            f"/v1/book_transfers/{book_transfer_token}/reverse",
            body=maybe_transform({"memo": memo}, book_transfer_reverse_params.BookTransferReverseParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookTransferResponse,
        )


class AsyncBookTransfers(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBookTransfersWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBookTransfersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBookTransfersWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncBookTransfersWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        category: Literal["ADJUSTMENT", "BALANCE_OR_FUNDING", "DERECOGNITION", "DISPUTE", "FEE", "REWARD", "TRANSFER"],
        from_financial_account_token: str,
        subtype: str,
        to_financial_account_token: str,
        type: Literal[
            "ATM_WITHDRAWAL",
            "ATM_DECLINE",
            "INTERNATIONAL_ATM_WITHDRAWAL",
            "INACTIVITY",
            "STATEMENT",
            "MONTHLY",
            "QUARTERLY",
            "ANNUAL",
            "CUSTOMER_SERVICE",
            "ACCOUNT_MAINTENANCE",
            "ACCOUNT_ACTIVATION",
            "ACCOUNT_CLOSURE",
            "CARD_REPLACEMENT",
            "CARD_DELIVERY",
            "CARD_CREATE",
            "CURRENCY_CONVERSION",
            "INTEREST",
            "LATE_PAYMENT",
            "BILL_PAYMENT",
            "CASH_BACK",
            "ACCOUNT_TO_ACCOUNT",
            "CARD_TO_CARD",
            "DISBURSE",
            "BILLING_ERROR",
            "LOSS_WRITE_OFF",
            "EXPIRED_CARD",
            "EARLY_DERECOGNITION",
            "ESCHEATMENT",
            "INACTIVITY_FEE_DOWN",
            "PROVISIONAL_CREDIT",
            "DISPUTE_WON",
            "TRANSFER",
        ],
        token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookTransferResponse:
        """
        Book transfer funds between two financial accounts or between a financial
        account and card

        Args:
          amount: Amount to be transferred in the currency’s smallest unit (e.g., cents for USD).
              This should always be a positive value.

          category: Category of the book transfer

          from_financial_account_token: Globally unique identifier for the financial account or card that will send the
              funds. Accepted type dependent on the program's use case.

          subtype: The program specific subtype code for the specified category/type.

          to_financial_account_token: Globally unique identifier for the financial account or card that will receive
              the funds. Accepted type dependent on the program's use case.

          type: Type of book_transfer

          token: Customer-provided token that will serve as an idempotency token. This token will
              become the transaction token.

          memo: Optional descriptor for the transfer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/book_transfers",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "category": category,
                    "from_financial_account_token": from_financial_account_token,
                    "subtype": subtype,
                    "to_financial_account_token": to_financial_account_token,
                    "type": type,
                    "token": token,
                    "memo": memo,
                },
                book_transfer_create_params.BookTransferCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookTransferResponse,
        )

    async def retrieve(
        self,
        book_transfer_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookTransferResponse:
        """
        Get book transfer by token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not book_transfer_token:
            raise ValueError(
                f"Expected a non-empty value for `book_transfer_token` but received {book_transfer_token!r}"
            )
        return await self._get(
            f"/v1/book_transfers/{book_transfer_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookTransferResponse,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        category: Literal["BALANCE_OR_FUNDING", "FEE", "REWARD", "ADJUSTMENT", "DERECOGNITION", "DISPUTE", "INTERNAL"]
        | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        result: Literal["APPROVED", "DECLINED"] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["DECLINED", "SETTLED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BookTransferResponse, AsyncCursorPage[BookTransferResponse]]:
        """List book transfers

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          category: Book Transfer category to be returned.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          financial_account_token: Globally unique identifier for the financial account or card that will send the
              funds. Accepted type dependent on the program's use case.

          page_size: Page size (for pagination).

          result: Book transfer result to be returned.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Book transfer status to be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/book_transfers",
            page=AsyncCursorPage[BookTransferResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "begin": begin,
                        "business_account_token": business_account_token,
                        "category": category,
                        "end": end,
                        "ending_before": ending_before,
                        "financial_account_token": financial_account_token,
                        "page_size": page_size,
                        "result": result,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    book_transfer_list_params.BookTransferListParams,
                ),
            ),
            model=BookTransferResponse,
        )

    async def reverse(
        self,
        book_transfer_token: str,
        *,
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BookTransferResponse:
        """
        Reverse a book transfer

        Args:
          memo: Optional descriptor for the reversal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not book_transfer_token:
            raise ValueError(
                f"Expected a non-empty value for `book_transfer_token` but received {book_transfer_token!r}"
            )
        return await self._post(
            f"/v1/book_transfers/{book_transfer_token}/reverse",
            body=await async_maybe_transform({"memo": memo}, book_transfer_reverse_params.BookTransferReverseParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BookTransferResponse,
        )


class BookTransfersWithRawResponse:
    def __init__(self, book_transfers: BookTransfers) -> None:
        self._book_transfers = book_transfers

        self.create = _legacy_response.to_raw_response_wrapper(
            book_transfers.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            book_transfers.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            book_transfers.list,
        )
        self.reverse = _legacy_response.to_raw_response_wrapper(
            book_transfers.reverse,
        )


class AsyncBookTransfersWithRawResponse:
    def __init__(self, book_transfers: AsyncBookTransfers) -> None:
        self._book_transfers = book_transfers

        self.create = _legacy_response.async_to_raw_response_wrapper(
            book_transfers.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            book_transfers.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            book_transfers.list,
        )
        self.reverse = _legacy_response.async_to_raw_response_wrapper(
            book_transfers.reverse,
        )


class BookTransfersWithStreamingResponse:
    def __init__(self, book_transfers: BookTransfers) -> None:
        self._book_transfers = book_transfers

        self.create = to_streamed_response_wrapper(
            book_transfers.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            book_transfers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            book_transfers.list,
        )
        self.reverse = to_streamed_response_wrapper(
            book_transfers.reverse,
        )


class AsyncBookTransfersWithStreamingResponse:
    def __init__(self, book_transfers: AsyncBookTransfers) -> None:
        self._book_transfers = book_transfers

        self.create = async_to_streamed_response_wrapper(
            book_transfers.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            book_transfers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            book_transfers.list,
        )
        self.reverse = async_to_streamed_response_wrapper(
            book_transfers.reverse,
        )
