# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...types.fraud import transaction_report_params
from ..._base_client import make_request_options
from ...types.fraud.transaction_report_response import TransactionReportResponse
from ...types.fraud.transaction_retrieve_response import TransactionRetrieveResponse

__all__ = ["Transactions", "AsyncTransactions"]


class Transactions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return TransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return TransactionsWithStreamingResponse(self)

    def retrieve(
        self,
        transaction_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionRetrieveResponse:
        """
        Retrieve a fraud report for a specific transaction identified by its unique
        transaction token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_token:
            raise ValueError(f"Expected a non-empty value for `transaction_token` but received {transaction_token!r}")
        return self._get(
            f"/v1/fraud/transactions/{transaction_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionRetrieveResponse,
        )

    def report(
        self,
        transaction_token: str,
        *,
        fraud_status: Literal["SUSPECTED_FRAUD", "FRAUDULENT", "NOT_FRAUDULENT"],
        comment: str | NotGiven = NOT_GIVEN,
        fraud_type: Literal[
            "FIRST_PARTY_FRAUD", "ACCOUNT_TAKEOVER", "CARD_COMPROMISED", "IDENTITY_THEFT", "CARDHOLDER_MANIPULATION"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionReportResponse:
        """
        Report fraud for a specific transaction token by providing details such as fraud
        type, fraud status, and any additional comments.

        Args:
          fraud_status: The fraud status of the transaction, string (enum) supporting the following
              values:

              - `SUSPECTED_FRAUD`: The transaction is suspected to be fraudulent, but this
                hasn’t been confirmed.
              - `FRAUDULENT`: The transaction is confirmed to be fraudulent. A transaction may
                immediately be moved into this state, or be graduated into this state from the
                `SUSPECTED_FRAUD` state.
              - `NOT_FRAUDULENT`: The transaction is (explicitly) marked as not fraudulent. A
                transaction may immediately be moved into this state, or be graduated into
                this state from the `SUSPECTED_FRAUD` state.

          comment: Optional field providing additional information or context about why the
              transaction is considered fraudulent.

          fraud_type: Specifies the type or category of fraud that the transaction is suspected or
              confirmed to involve, string (enum) supporting the following values:

              - `FIRST_PARTY_FRAUD`: First-party fraud occurs when a legitimate account or
                cardholder intentionally misuses financial services for personal gain. This
                includes actions such as disputing legitimate transactions to obtain a refund,
                abusing return policies, or defaulting on credit obligations without intent to
                repay.
              - `ACCOUNT_TAKEOVER`: Account takeover fraud occurs when a fraudster gains
                unauthorized access to an existing account, modifies account settings, and
                carries out fraudulent transactions.
              - `CARD_COMPROMISED`: Card compromised fraud occurs when a fraudster gains
                access to card details without taking over the account, such as through
                physical card theft, cloning, or online data breaches.
              - `IDENTITY_THEFT`: Identity theft fraud occurs when a fraudster uses stolen
                personal information, such as Social Security numbers or addresses, to open
                accounts, apply for loans, or conduct financial transactions in someone's
                name.
              - `CARDHOLDER_MANIPULATION`: This type of fraud occurs when a fraudster
                manipulates or coerces a legitimate cardholder into unauthorized transactions,
                often through social engineering tactics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_token:
            raise ValueError(f"Expected a non-empty value for `transaction_token` but received {transaction_token!r}")
        return self._post(
            f"/v1/fraud/transactions/{transaction_token}",
            body=maybe_transform(
                {
                    "fraud_status": fraud_status,
                    "comment": comment,
                    "fraud_type": fraud_type,
                },
                transaction_report_params.TransactionReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionReportResponse,
        )


class AsyncTransactions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncTransactionsWithStreamingResponse(self)

    async def retrieve(
        self,
        transaction_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionRetrieveResponse:
        """
        Retrieve a fraud report for a specific transaction identified by its unique
        transaction token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_token:
            raise ValueError(f"Expected a non-empty value for `transaction_token` but received {transaction_token!r}")
        return await self._get(
            f"/v1/fraud/transactions/{transaction_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionRetrieveResponse,
        )

    async def report(
        self,
        transaction_token: str,
        *,
        fraud_status: Literal["SUSPECTED_FRAUD", "FRAUDULENT", "NOT_FRAUDULENT"],
        comment: str | NotGiven = NOT_GIVEN,
        fraud_type: Literal[
            "FIRST_PARTY_FRAUD", "ACCOUNT_TAKEOVER", "CARD_COMPROMISED", "IDENTITY_THEFT", "CARDHOLDER_MANIPULATION"
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionReportResponse:
        """
        Report fraud for a specific transaction token by providing details such as fraud
        type, fraud status, and any additional comments.

        Args:
          fraud_status: The fraud status of the transaction, string (enum) supporting the following
              values:

              - `SUSPECTED_FRAUD`: The transaction is suspected to be fraudulent, but this
                hasn’t been confirmed.
              - `FRAUDULENT`: The transaction is confirmed to be fraudulent. A transaction may
                immediately be moved into this state, or be graduated into this state from the
                `SUSPECTED_FRAUD` state.
              - `NOT_FRAUDULENT`: The transaction is (explicitly) marked as not fraudulent. A
                transaction may immediately be moved into this state, or be graduated into
                this state from the `SUSPECTED_FRAUD` state.

          comment: Optional field providing additional information or context about why the
              transaction is considered fraudulent.

          fraud_type: Specifies the type or category of fraud that the transaction is suspected or
              confirmed to involve, string (enum) supporting the following values:

              - `FIRST_PARTY_FRAUD`: First-party fraud occurs when a legitimate account or
                cardholder intentionally misuses financial services for personal gain. This
                includes actions such as disputing legitimate transactions to obtain a refund,
                abusing return policies, or defaulting on credit obligations without intent to
                repay.
              - `ACCOUNT_TAKEOVER`: Account takeover fraud occurs when a fraudster gains
                unauthorized access to an existing account, modifies account settings, and
                carries out fraudulent transactions.
              - `CARD_COMPROMISED`: Card compromised fraud occurs when a fraudster gains
                access to card details without taking over the account, such as through
                physical card theft, cloning, or online data breaches.
              - `IDENTITY_THEFT`: Identity theft fraud occurs when a fraudster uses stolen
                personal information, such as Social Security numbers or addresses, to open
                accounts, apply for loans, or conduct financial transactions in someone's
                name.
              - `CARDHOLDER_MANIPULATION`: This type of fraud occurs when a fraudster
                manipulates or coerces a legitimate cardholder into unauthorized transactions,
                often through social engineering tactics.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_token:
            raise ValueError(f"Expected a non-empty value for `transaction_token` but received {transaction_token!r}")
        return await self._post(
            f"/v1/fraud/transactions/{transaction_token}",
            body=await async_maybe_transform(
                {
                    "fraud_status": fraud_status,
                    "comment": comment,
                    "fraud_type": fraud_type,
                },
                transaction_report_params.TransactionReportParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionReportResponse,
        )


class TransactionsWithRawResponse:
    def __init__(self, transactions: Transactions) -> None:
        self._transactions = transactions

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.report = _legacy_response.to_raw_response_wrapper(
            transactions.report,
        )


class AsyncTransactionsWithRawResponse:
    def __init__(self, transactions: AsyncTransactions) -> None:
        self._transactions = transactions

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.report = _legacy_response.async_to_raw_response_wrapper(
            transactions.report,
        )


class TransactionsWithStreamingResponse:
    def __init__(self, transactions: Transactions) -> None:
        self._transactions = transactions

        self.retrieve = to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.report = to_streamed_response_wrapper(
            transactions.report,
        )


class AsyncTransactionsWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactions) -> None:
        self._transactions = transactions

        self.retrieve = async_to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.report = async_to_streamed_response_wrapper(
            transactions.report,
        )
