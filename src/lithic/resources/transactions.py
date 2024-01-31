# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    Transaction,
    TransactionSimulateVoidResponse,
    TransactionSimulateReturnResponse,
    TransactionSimulateClearingResponse,
    TransactionSimulateAuthorizationResponse,
    TransactionSimulateReturnReversalResponse,
    TransactionSimulateAuthorizationAdviceResponse,
    TransactionSimulateCreditAuthorizationResponse,
    transaction_list_params,
    transaction_simulate_void_params,
    transaction_simulate_return_params,
    transaction_simulate_clearing_params,
    transaction_simulate_authorization_params,
    transaction_simulate_return_reversal_params,
    transaction_simulate_authorization_advice_params,
    transaction_simulate_credit_authorization_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Transactions", "AsyncTransactions"]


class Transactions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionsWithRawResponse:
        return TransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsWithStreamingResponse:
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
    ) -> Transaction:
        """
        Get specific card transaction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_token:
            raise ValueError(f"Expected a non-empty value for `transaction_token` but received {transaction_token!r}")
        return self._get(
            f"/transactions/{transaction_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transaction,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        card_token: str | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        result: Literal["APPROVED", "DECLINED"] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Transaction]:
        """
        List card transactions.

        Args:
          account_token: Filters for transactions associated with a specific account.

          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          card_token: Filters for transactions associated with a specific card.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          result: Filters for transactions using transaction result field. Can filter by
              `APPROVED`, and `DECLINED`.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/transactions",
            page=SyncCursorPage[Transaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "begin": begin,
                        "card_token": card_token,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "result": result,
                        "starting_after": starting_after,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            model=Transaction,
        )

    def simulate_authorization(
        self,
        *,
        amount: int,
        descriptor: str,
        pan: str,
        mcc: str | NotGiven = NOT_GIVEN,
        merchant_acceptor_id: str | NotGiven = NOT_GIVEN,
        merchant_amount: int | NotGiven = NOT_GIVEN,
        merchant_currency: str | NotGiven = NOT_GIVEN,
        partial_approval_capable: bool | NotGiven = NOT_GIVEN,
        status: Literal[
            "AUTHORIZATION",
            "BALANCE_INQUIRY",
            "CREDIT_AUTHORIZATION",
            "FINANCIAL_AUTHORIZATION",
            "FINANCIAL_CREDIT_AUTHORIZATION",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateAuthorizationResponse:
        """
        Simulates an authorization request from the payment network as if it came from a
        merchant acquirer. If you're configured for ASA, simulating auths requires your
        ASA client to be set up properly (respond with a valid JSON to the ASA request).
        For users that are not configured for ASA, a daily transaction limit of $5000
        USD is applied by default. This limit can be modified via the
        [update account](https://docs.lithic.com/reference/patchaccountbytoken)
        endpoint.

        Args:
          amount: Amount (in cents) to authorize. For credit authorizations and financial credit
              authorizations, any value entered will be converted into a negative amount in
              the simulated transaction. For example, entering 100 in this field will appear
              as a -100 amount in the transaction. For balance inquiries, this field must be
              set to 0.

          descriptor: Merchant descriptor.

          pan: Sixteen digit card number.

          mcc: Merchant category code for the transaction to be simulated. A four-digit number
              listed in ISO 18245. Supported merchant category codes can be found
              [here](https://docs.lithic.com/docs/transactions#merchant-category-codes-mccs).

          merchant_acceptor_id: Unique identifier to identify the payment card acceptor.

          merchant_amount: Amount of the transaction to be simulated in currency specified in
              merchant_currency, including any acquirer fees.

          merchant_currency: 3-digit alphabetic ISO 4217 currency code.

          partial_approval_capable: Set to true if the terminal is capable of partial approval otherwise false.
              Partial approval is when part of a transaction is approved and another payment
              must be used for the remainder.

          status: Type of event to simulate.

              - `AUTHORIZATION` is a dual message purchase authorization, meaning a subsequent
                clearing step is required to settle the transaction.
              - `BALANCE_INQUIRY` is a $0 authorization that includes a request for the
                balance held on the card, and is most typically seen when a cardholder
                requests to view a card's balance at an ATM.
              - `CREDIT_AUTHORIZATION` is a dual message request from a merchant to authorize
                a refund or credit, meaning a subsequent clearing step is required to settle
                the transaction.
              - `FINANCIAL_AUTHORIZATION` is a single message request from a merchant to debit
                funds immediately (such as an ATM withdrawal), and no subsequent clearing is
                required to settle the transaction.
              - `FINANCIAL_CREDIT_AUTHORIZATION` is a single message request from a merchant
                to credit funds immediately, and no subsequent clearing is required to settle
                the transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/simulate/authorize",
            body=maybe_transform(
                {
                    "amount": amount,
                    "descriptor": descriptor,
                    "pan": pan,
                    "mcc": mcc,
                    "merchant_acceptor_id": merchant_acceptor_id,
                    "merchant_amount": merchant_amount,
                    "merchant_currency": merchant_currency,
                    "partial_approval_capable": partial_approval_capable,
                    "status": status,
                },
                transaction_simulate_authorization_params.TransactionSimulateAuthorizationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateAuthorizationResponse,
        )

    def simulate_authorization_advice(
        self,
        *,
        token: str,
        amount: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateAuthorizationAdviceResponse:
        """
        Simulates an authorization advice request from the payment network as if it came
        from a merchant acquirer. An authorization advice request changes the amount of
        the transaction.

        Args:
          token: The transaction token returned from the /v1/simulate/authorize response.

          amount: Amount (in cents) to authorize. This amount will override the transaction's
              amount that was originally set by /v1/simulate/authorize.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/simulate/authorization_advice",
            body=maybe_transform(
                {
                    "token": token,
                    "amount": amount,
                },
                transaction_simulate_authorization_advice_params.TransactionSimulateAuthorizationAdviceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateAuthorizationAdviceResponse,
        )

    def simulate_clearing(
        self,
        *,
        token: str,
        amount: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer
        pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.

        Args:
          token: The transaction token returned from the /v1/simulate/authorize response.

          amount: Amount (in cents) to complete. Typically this will match the original
              authorization, but may be more or less.

              If no amount is supplied to this endpoint, the amount of the transaction will be
              captured. Any transaction that has any amount completed at all do not have
              access to this behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/simulate/clearing",
            body=maybe_transform(
                {
                    "token": token,
                    "amount": amount,
                },
                transaction_simulate_clearing_params.TransactionSimulateClearingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateClearingResponse,
        )

    def simulate_credit_authorization(
        self,
        *,
        amount: int,
        descriptor: str,
        pan: str,
        mcc: str | NotGiven = NOT_GIVEN,
        merchant_acceptor_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateCreditAuthorizationResponse:
        """Simulates a credit authorization advice message from the payment network.

        This
        message indicates that a credit authorization was approved on your behalf by the
        network.

        Args:
          amount: Amount (in cents). Any value entered will be converted into a negative amount in
              the simulated transaction. For example, entering 100 in this field will appear
              as a -100 amount in the transaction.

          descriptor: Merchant descriptor.

          pan: Sixteen digit card number.

          mcc: Merchant category code for the transaction to be simulated. A four-digit number
              listed in ISO 18245. Supported merchant category codes can be found
              [here](https://docs.lithic.com/docs/transactions#merchant-category-codes-mccs).

          merchant_acceptor_id: Unique identifier to identify the payment card acceptor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/simulate/credit_authorization_advice",
            body=maybe_transform(
                {
                    "amount": amount,
                    "descriptor": descriptor,
                    "pan": pan,
                    "mcc": mcc,
                    "merchant_acceptor_id": merchant_acceptor_id,
                },
                transaction_simulate_credit_authorization_params.TransactionSimulateCreditAuthorizationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateCreditAuthorizationResponse,
        )

    def simulate_return(
        self,
        *,
        amount: int,
        descriptor: str,
        pan: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately
        and do not spend time in a `PENDING` state.

        Args:
          amount: Amount (in cents) to authorize.

          descriptor: Merchant descriptor.

          pan: Sixteen digit card number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/simulate/return",
            body=maybe_transform(
                {
                    "amount": amount,
                    "descriptor": descriptor,
                    "pan": pan,
                },
                transaction_simulate_return_params.TransactionSimulateReturnParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateReturnResponse,
        )

    def simulate_return_reversal(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateReturnReversalResponse:
        """
        Voids a settled credit transaction – i.e., a transaction with a negative amount
        and `SETTLED` status. These can be credit authorizations that have already
        cleared or financial credit authorizations.

        Args:
          token: The transaction token returned from the /v1/simulate/authorize response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/simulate/return_reversal",
            body=maybe_transform(
                {"token": token}, transaction_simulate_return_reversal_params.TransactionSimulateReturnReversalParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateReturnReversalResponse,
        )

    def simulate_void(
        self,
        *,
        token: str,
        amount: int | NotGiven = NOT_GIVEN,
        type: Literal["AUTHORIZATION_EXPIRY", "AUTHORIZATION_REVERSAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent
        the full amount will be voided. Cannot be used on partially completed
        transactions, but can be used on partially voided transactions. _Note that
        simulating an authorization expiry on credit authorizations or credit
        authorization advice is not currently supported but will be added soon._

        Args:
          token: The transaction token returned from the /v1/simulate/authorize response.

          amount: Amount (in cents) to void. Typically this will match the original authorization,
              but may be less.

          type: Type of event to simulate. Defaults to `AUTHORIZATION_REVERSAL`.

              - `AUTHORIZATION_EXPIRY` indicates authorization has expired and been reversed
                by Lithic.
              - `AUTHORIZATION_REVERSAL` indicates authorization was reversed by the merchant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/simulate/void",
            body=maybe_transform(
                {
                    "token": token,
                    "amount": amount,
                    "type": type,
                },
                transaction_simulate_void_params.TransactionSimulateVoidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateVoidResponse,
        )


class AsyncTransactions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionsWithRawResponse:
        return AsyncTransactionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsWithStreamingResponse:
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
    ) -> Transaction:
        """
        Get specific card transaction.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_token:
            raise ValueError(f"Expected a non-empty value for `transaction_token` but received {transaction_token!r}")
        return await self._get(
            f"/transactions/{transaction_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Transaction,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        card_token: str | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        result: Literal["APPROVED", "DECLINED"] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Transaction, AsyncCursorPage[Transaction]]:
        """
        List card transactions.

        Args:
          account_token: Filters for transactions associated with a specific account.

          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          card_token: Filters for transactions associated with a specific card.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          result: Filters for transactions using transaction result field. Can filter by
              `APPROVED`, and `DECLINED`.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/transactions",
            page=AsyncCursorPage[Transaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "begin": begin,
                        "card_token": card_token,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "result": result,
                        "starting_after": starting_after,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            model=Transaction,
        )

    async def simulate_authorization(
        self,
        *,
        amount: int,
        descriptor: str,
        pan: str,
        mcc: str | NotGiven = NOT_GIVEN,
        merchant_acceptor_id: str | NotGiven = NOT_GIVEN,
        merchant_amount: int | NotGiven = NOT_GIVEN,
        merchant_currency: str | NotGiven = NOT_GIVEN,
        partial_approval_capable: bool | NotGiven = NOT_GIVEN,
        status: Literal[
            "AUTHORIZATION",
            "BALANCE_INQUIRY",
            "CREDIT_AUTHORIZATION",
            "FINANCIAL_AUTHORIZATION",
            "FINANCIAL_CREDIT_AUTHORIZATION",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateAuthorizationResponse:
        """
        Simulates an authorization request from the payment network as if it came from a
        merchant acquirer. If you're configured for ASA, simulating auths requires your
        ASA client to be set up properly (respond with a valid JSON to the ASA request).
        For users that are not configured for ASA, a daily transaction limit of $5000
        USD is applied by default. This limit can be modified via the
        [update account](https://docs.lithic.com/reference/patchaccountbytoken)
        endpoint.

        Args:
          amount: Amount (in cents) to authorize. For credit authorizations and financial credit
              authorizations, any value entered will be converted into a negative amount in
              the simulated transaction. For example, entering 100 in this field will appear
              as a -100 amount in the transaction. For balance inquiries, this field must be
              set to 0.

          descriptor: Merchant descriptor.

          pan: Sixteen digit card number.

          mcc: Merchant category code for the transaction to be simulated. A four-digit number
              listed in ISO 18245. Supported merchant category codes can be found
              [here](https://docs.lithic.com/docs/transactions#merchant-category-codes-mccs).

          merchant_acceptor_id: Unique identifier to identify the payment card acceptor.

          merchant_amount: Amount of the transaction to be simulated in currency specified in
              merchant_currency, including any acquirer fees.

          merchant_currency: 3-digit alphabetic ISO 4217 currency code.

          partial_approval_capable: Set to true if the terminal is capable of partial approval otherwise false.
              Partial approval is when part of a transaction is approved and another payment
              must be used for the remainder.

          status: Type of event to simulate.

              - `AUTHORIZATION` is a dual message purchase authorization, meaning a subsequent
                clearing step is required to settle the transaction.
              - `BALANCE_INQUIRY` is a $0 authorization that includes a request for the
                balance held on the card, and is most typically seen when a cardholder
                requests to view a card's balance at an ATM.
              - `CREDIT_AUTHORIZATION` is a dual message request from a merchant to authorize
                a refund or credit, meaning a subsequent clearing step is required to settle
                the transaction.
              - `FINANCIAL_AUTHORIZATION` is a single message request from a merchant to debit
                funds immediately (such as an ATM withdrawal), and no subsequent clearing is
                required to settle the transaction.
              - `FINANCIAL_CREDIT_AUTHORIZATION` is a single message request from a merchant
                to credit funds immediately, and no subsequent clearing is required to settle
                the transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/simulate/authorize",
            body=maybe_transform(
                {
                    "amount": amount,
                    "descriptor": descriptor,
                    "pan": pan,
                    "mcc": mcc,
                    "merchant_acceptor_id": merchant_acceptor_id,
                    "merchant_amount": merchant_amount,
                    "merchant_currency": merchant_currency,
                    "partial_approval_capable": partial_approval_capable,
                    "status": status,
                },
                transaction_simulate_authorization_params.TransactionSimulateAuthorizationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateAuthorizationResponse,
        )

    async def simulate_authorization_advice(
        self,
        *,
        token: str,
        amount: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateAuthorizationAdviceResponse:
        """
        Simulates an authorization advice request from the payment network as if it came
        from a merchant acquirer. An authorization advice request changes the amount of
        the transaction.

        Args:
          token: The transaction token returned from the /v1/simulate/authorize response.

          amount: Amount (in cents) to authorize. This amount will override the transaction's
              amount that was originally set by /v1/simulate/authorize.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/simulate/authorization_advice",
            body=maybe_transform(
                {
                    "token": token,
                    "amount": amount,
                },
                transaction_simulate_authorization_advice_params.TransactionSimulateAuthorizationAdviceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateAuthorizationAdviceResponse,
        )

    async def simulate_clearing(
        self,
        *,
        token: str,
        amount: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer
        pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.

        Args:
          token: The transaction token returned from the /v1/simulate/authorize response.

          amount: Amount (in cents) to complete. Typically this will match the original
              authorization, but may be more or less.

              If no amount is supplied to this endpoint, the amount of the transaction will be
              captured. Any transaction that has any amount completed at all do not have
              access to this behavior.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/simulate/clearing",
            body=maybe_transform(
                {
                    "token": token,
                    "amount": amount,
                },
                transaction_simulate_clearing_params.TransactionSimulateClearingParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateClearingResponse,
        )

    async def simulate_credit_authorization(
        self,
        *,
        amount: int,
        descriptor: str,
        pan: str,
        mcc: str | NotGiven = NOT_GIVEN,
        merchant_acceptor_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateCreditAuthorizationResponse:
        """Simulates a credit authorization advice message from the payment network.

        This
        message indicates that a credit authorization was approved on your behalf by the
        network.

        Args:
          amount: Amount (in cents). Any value entered will be converted into a negative amount in
              the simulated transaction. For example, entering 100 in this field will appear
              as a -100 amount in the transaction.

          descriptor: Merchant descriptor.

          pan: Sixteen digit card number.

          mcc: Merchant category code for the transaction to be simulated. A four-digit number
              listed in ISO 18245. Supported merchant category codes can be found
              [here](https://docs.lithic.com/docs/transactions#merchant-category-codes-mccs).

          merchant_acceptor_id: Unique identifier to identify the payment card acceptor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/simulate/credit_authorization_advice",
            body=maybe_transform(
                {
                    "amount": amount,
                    "descriptor": descriptor,
                    "pan": pan,
                    "mcc": mcc,
                    "merchant_acceptor_id": merchant_acceptor_id,
                },
                transaction_simulate_credit_authorization_params.TransactionSimulateCreditAuthorizationParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateCreditAuthorizationResponse,
        )

    async def simulate_return(
        self,
        *,
        amount: int,
        descriptor: str,
        pan: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately
        and do not spend time in a `PENDING` state.

        Args:
          amount: Amount (in cents) to authorize.

          descriptor: Merchant descriptor.

          pan: Sixteen digit card number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/simulate/return",
            body=maybe_transform(
                {
                    "amount": amount,
                    "descriptor": descriptor,
                    "pan": pan,
                },
                transaction_simulate_return_params.TransactionSimulateReturnParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateReturnResponse,
        )

    async def simulate_return_reversal(
        self,
        *,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateReturnReversalResponse:
        """
        Voids a settled credit transaction – i.e., a transaction with a negative amount
        and `SETTLED` status. These can be credit authorizations that have already
        cleared or financial credit authorizations.

        Args:
          token: The transaction token returned from the /v1/simulate/authorize response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/simulate/return_reversal",
            body=maybe_transform(
                {"token": token}, transaction_simulate_return_reversal_params.TransactionSimulateReturnReversalParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateReturnReversalResponse,
        )

    async def simulate_void(
        self,
        *,
        token: str,
        amount: int | NotGiven = NOT_GIVEN,
        type: Literal["AUTHORIZATION_EXPIRY", "AUTHORIZATION_REVERSAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent
        the full amount will be voided. Cannot be used on partially completed
        transactions, but can be used on partially voided transactions. _Note that
        simulating an authorization expiry on credit authorizations or credit
        authorization advice is not currently supported but will be added soon._

        Args:
          token: The transaction token returned from the /v1/simulate/authorize response.

          amount: Amount (in cents) to void. Typically this will match the original authorization,
              but may be less.

          type: Type of event to simulate. Defaults to `AUTHORIZATION_REVERSAL`.

              - `AUTHORIZATION_EXPIRY` indicates authorization has expired and been reversed
                by Lithic.
              - `AUTHORIZATION_REVERSAL` indicates authorization was reversed by the merchant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/simulate/void",
            body=maybe_transform(
                {
                    "token": token,
                    "amount": amount,
                    "type": type,
                },
                transaction_simulate_void_params.TransactionSimulateVoidParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionSimulateVoidResponse,
        )


class TransactionsWithRawResponse:
    def __init__(self, transactions: Transactions) -> None:
        self._transactions = transactions

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            transactions.list,
        )
        self.simulate_authorization = _legacy_response.to_raw_response_wrapper(
            transactions.simulate_authorization,
        )
        self.simulate_authorization_advice = _legacy_response.to_raw_response_wrapper(
            transactions.simulate_authorization_advice,
        )
        self.simulate_clearing = _legacy_response.to_raw_response_wrapper(
            transactions.simulate_clearing,
        )
        self.simulate_credit_authorization = _legacy_response.to_raw_response_wrapper(
            transactions.simulate_credit_authorization,
        )
        self.simulate_return = _legacy_response.to_raw_response_wrapper(
            transactions.simulate_return,
        )
        self.simulate_return_reversal = _legacy_response.to_raw_response_wrapper(
            transactions.simulate_return_reversal,
        )
        self.simulate_void = _legacy_response.to_raw_response_wrapper(
            transactions.simulate_void,
        )


class AsyncTransactionsWithRawResponse:
    def __init__(self, transactions: AsyncTransactions) -> None:
        self._transactions = transactions

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            transactions.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            transactions.list,
        )
        self.simulate_authorization = _legacy_response.async_to_raw_response_wrapper(
            transactions.simulate_authorization,
        )
        self.simulate_authorization_advice = _legacy_response.async_to_raw_response_wrapper(
            transactions.simulate_authorization_advice,
        )
        self.simulate_clearing = _legacy_response.async_to_raw_response_wrapper(
            transactions.simulate_clearing,
        )
        self.simulate_credit_authorization = _legacy_response.async_to_raw_response_wrapper(
            transactions.simulate_credit_authorization,
        )
        self.simulate_return = _legacy_response.async_to_raw_response_wrapper(
            transactions.simulate_return,
        )
        self.simulate_return_reversal = _legacy_response.async_to_raw_response_wrapper(
            transactions.simulate_return_reversal,
        )
        self.simulate_void = _legacy_response.async_to_raw_response_wrapper(
            transactions.simulate_void,
        )


class TransactionsWithStreamingResponse:
    def __init__(self, transactions: Transactions) -> None:
        self._transactions = transactions

        self.retrieve = to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            transactions.list,
        )
        self.simulate_authorization = to_streamed_response_wrapper(
            transactions.simulate_authorization,
        )
        self.simulate_authorization_advice = to_streamed_response_wrapper(
            transactions.simulate_authorization_advice,
        )
        self.simulate_clearing = to_streamed_response_wrapper(
            transactions.simulate_clearing,
        )
        self.simulate_credit_authorization = to_streamed_response_wrapper(
            transactions.simulate_credit_authorization,
        )
        self.simulate_return = to_streamed_response_wrapper(
            transactions.simulate_return,
        )
        self.simulate_return_reversal = to_streamed_response_wrapper(
            transactions.simulate_return_reversal,
        )
        self.simulate_void = to_streamed_response_wrapper(
            transactions.simulate_void,
        )


class AsyncTransactionsWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactions) -> None:
        self._transactions = transactions

        self.retrieve = async_to_streamed_response_wrapper(
            transactions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            transactions.list,
        )
        self.simulate_authorization = async_to_streamed_response_wrapper(
            transactions.simulate_authorization,
        )
        self.simulate_authorization_advice = async_to_streamed_response_wrapper(
            transactions.simulate_authorization_advice,
        )
        self.simulate_clearing = async_to_streamed_response_wrapper(
            transactions.simulate_clearing,
        )
        self.simulate_credit_authorization = async_to_streamed_response_wrapper(
            transactions.simulate_credit_authorization,
        )
        self.simulate_return = async_to_streamed_response_wrapper(
            transactions.simulate_return,
        )
        self.simulate_return_reversal = async_to_streamed_response_wrapper(
            transactions.simulate_return_reversal,
        )
        self.simulate_void = async_to_streamed_response_wrapper(
            transactions.simulate_void,
        )
