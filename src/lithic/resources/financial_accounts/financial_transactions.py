# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import FinancialTransaction
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.financial_accounts import financial_transaction_list_params

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["FinancialTransactions", "AsyncFinancialTransactions"]


class FinancialTransactions(SyncAPIResource):
    with_raw_response: FinancialTransactionsWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = FinancialTransactionsWithRawResponse(self)

    def retrieve(
        self,
        financial_transaction_token: str,
        *,
        financial_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialTransaction:
        """
        Get the financial transaction for the provided token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/financial_accounts/{financial_account_token}/financial_transactions/{financial_transaction_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialTransaction,
        )

    def list(
        self,
        financial_account_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        category: Literal["ACH", "CARD", "TRANSFER"] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        result: Literal["APPROVED", "DECLINED"] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["DECLINED", "EXPIRED", "PENDING", "RETURNED", "SETTLED", "VOIDED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[FinancialTransaction]:
        """
        List the financial transactions for a given financial account.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          category: Financial Transaction category to be returned.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          result: Financial Transaction result to be returned.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Financial Transaction status to be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/financial_accounts/{financial_account_token}/financial_transactions",
            page=SyncSinglePage[FinancialTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "category": category,
                        "end": end,
                        "ending_before": ending_before,
                        "result": result,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    financial_transaction_list_params.FinancialTransactionListParams,
                ),
            ),
            model=FinancialTransaction,
        )


class AsyncFinancialTransactions(AsyncAPIResource):
    with_raw_response: AsyncFinancialTransactionsWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncFinancialTransactionsWithRawResponse(self)

    async def retrieve(
        self,
        financial_transaction_token: str,
        *,
        financial_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialTransaction:
        """
        Get the financial transaction for the provided token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/financial_accounts/{financial_account_token}/financial_transactions/{financial_transaction_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialTransaction,
        )

    def list(
        self,
        financial_account_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        category: Literal["ACH", "CARD", "TRANSFER"] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        result: Literal["APPROVED", "DECLINED"] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["DECLINED", "EXPIRED", "PENDING", "RETURNED", "SETTLED", "VOIDED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[FinancialTransaction, AsyncSinglePage[FinancialTransaction]]:
        """
        List the financial transactions for a given financial account.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          category: Financial Transaction category to be returned.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          result: Financial Transaction result to be returned.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Financial Transaction status to be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/financial_accounts/{financial_account_token}/financial_transactions",
            page=AsyncSinglePage[FinancialTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "category": category,
                        "end": end,
                        "ending_before": ending_before,
                        "result": result,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    financial_transaction_list_params.FinancialTransactionListParams,
                ),
            ),
            model=FinancialTransaction,
        )


class FinancialTransactionsWithRawResponse:
    def __init__(self, financial_transactions: FinancialTransactions) -> None:
        self.retrieve = to_raw_response_wrapper(
            financial_transactions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            financial_transactions.list,
        )


class AsyncFinancialTransactionsWithRawResponse:
    def __init__(self, financial_transactions: AsyncFinancialTransactions) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            financial_transactions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            financial_transactions.list,
        )
