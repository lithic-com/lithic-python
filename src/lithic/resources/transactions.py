# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

from ..types import (
    Transaction,
    TransactionSimulateVoidResponse,
    TransactionSimulateReturnResponse,
    TransactionSimulateClearingResponse,
    TransactionSimulateAuthorizationResponse,
    TransactionSimulateReturnReversalResponse,
    TransactionSimulateCreditAuthorizationResponse,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["Transactions", "AsyncTransactions"]


class Transactions(SyncAPIResource):
    def retrieve(
        self,
        transaction_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Transaction:
        """Get specific transaction."""
        return self._get(
            f"/transactions/{transaction_token}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Transaction,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        card_token: str | NotGiven = NOT_GIVEN,
        result: Literal["APPROVED", "DECLINED"] | NotGiven = NOT_GIVEN,
        begin: str | NotGiven = NOT_GIVEN,
        end: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[Transaction]:
        """
        List transactions.

        Args:
          account_token: Filters for transactions associated with a specific account.

          card_token: Filters for transactions associated with a specific card.

          result: Filters for transactions using transaction result field. Can filter by
              `APPROVED`, and `DECLINED`.

          begin: Date string in 8601 format. Only entries created after the specified date will
              be included. UTC time zone.

          end: Date string in 8601 format. Only entries created before the specified date will
              be included. UTC time zone.

          page: Page (for pagination).

          page_size: Page size (for pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/transactions",
            page=SyncPage[Transaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "account_token": account_token,
                    "card_token": card_token,
                    "result": result,
                    "begin": begin,
                    "end": end,
                    "page": page,
                    "page_size": page_size,
                },
            ),
            model=Transaction,
        )

    def simulate_authorization(
        self,
        *,
        amount: int,
        descriptor: str,
        pan: str,
        status: Literal[
            "AUTHORIZATION",
            "BALANCE_INQUIRY",
            "CREDIT_AUTHORIZATION",
            "FINANCIAL_AUTHORIZATION",
            "FINANCIAL_CREDIT_AUTHORIZATION",
        ]
        | NotGiven = NOT_GIVEN,
        merchant_acceptor_id: str | NotGiven = NOT_GIVEN,
        merchant_currency: str | NotGiven = NOT_GIVEN,
        merchant_amount: int | NotGiven = NOT_GIVEN,
        partial_approval_capable: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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

          merchant_acceptor_id: Unique identifier to identify the payment card acceptor.

          merchant_currency: 3-digit alphabetic ISO 4217 currency code.

          merchant_amount: Amount of the transaction to be simulated in currency specified in
              merchant_currency, including any acquirer fees.

          partial_approval_capable: Set to true if the terminal is capable of partial approval otherwise false.
              Partial approval is when part of a transaction is approved and another payment
              must be used for the remainder.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/simulate/authorize",
            body={
                "amount": amount,
                "descriptor": descriptor,
                "pan": pan,
                "status": status,
                "merchant_acceptor_id": merchant_acceptor_id,
                "merchant_currency": merchant_currency,
                "merchant_amount": merchant_amount,
                "partial_approval_capable": partial_approval_capable,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=TransactionSimulateAuthorizationResponse,
        )

    def simulate_clearing(
        self,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer
        pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.

        Args:
          amount: Amount (in cents) to complete. Typically this will match the original
              authorization, but may be more or less.

              If no amount is supplied to this endpoint, the amount of the transaction will be
              captured. Any transaction that has any amount completed at all do not have
              access to this behavior.

          token: The transaction token returned from the /v1/simulate/authorize response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/simulate/clearing",
            body={
                "amount": amount,
                "token": token,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=TransactionSimulateClearingResponse,
        )

    def simulate_credit_authorization(
        self,
        *,
        amount: int,
        descriptor: str,
        pan: str,
        merchant_acceptor_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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

          merchant_acceptor_id: Unique identifier to identify the payment card acceptor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/simulate/credit_authorization_advice",
            body={
                "amount": amount,
                "descriptor": descriptor,
                "pan": pan,
                "merchant_acceptor_id": merchant_acceptor_id,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
        """
        return self._post(
            "/simulate/return",
            body={
                "amount": amount,
                "descriptor": descriptor,
                "pan": pan,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
        """
        return self._post(
            "/simulate/return_reversal",
            body={"token": token},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=TransactionSimulateReturnReversalResponse,
        )

    def simulate_void(
        self,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        token: str,
        type: Literal["AUTHORIZATION_EXPIRY", "AUTHORIZATION_REVERSAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent
        the full amount will be voided. Cannot be used on partially completed
        transactions, but can be used on partially voided transactions. _Note that
        simulating an authorization expiry on credit authorizations or credit
        authorization advice is not currently supported but will be added soon._

        Args:
          amount: Amount (in cents) to void. Typically this will match the original authorization,
              but may be less.

          token: The transaction token returned from the /v1/simulate/authorize response.

          type: Type of event to simulate. Defaults to `AUTHORIZATION_REVERSAL`.

              - `AUTHORIZATION_EXPIRY` indicates authorization has expired and been reversed
                by Lithic.
              - `AUTHORIZATION_REVERSAL` indicates authorization was reversed by the merchant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/simulate/void",
            body={
                "amount": amount,
                "token": token,
                "type": type,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=TransactionSimulateVoidResponse,
        )


class AsyncTransactions(AsyncAPIResource):
    async def retrieve(
        self,
        transaction_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Transaction:
        """Get specific transaction."""
        return await self._get(
            f"/transactions/{transaction_token}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Transaction,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        card_token: str | NotGiven = NOT_GIVEN,
        result: Literal["APPROVED", "DECLINED"] | NotGiven = NOT_GIVEN,
        begin: str | NotGiven = NOT_GIVEN,
        end: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[Transaction, AsyncPage[Transaction]]:
        """
        List transactions.

        Args:
          account_token: Filters for transactions associated with a specific account.

          card_token: Filters for transactions associated with a specific card.

          result: Filters for transactions using transaction result field. Can filter by
              `APPROVED`, and `DECLINED`.

          begin: Date string in 8601 format. Only entries created after the specified date will
              be included. UTC time zone.

          end: Date string in 8601 format. Only entries created before the specified date will
              be included. UTC time zone.

          page: Page (for pagination).

          page_size: Page size (for pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/transactions",
            page=AsyncPage[Transaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "account_token": account_token,
                    "card_token": card_token,
                    "result": result,
                    "begin": begin,
                    "end": end,
                    "page": page,
                    "page_size": page_size,
                },
            ),
            model=Transaction,
        )

    async def simulate_authorization(
        self,
        *,
        amount: int,
        descriptor: str,
        pan: str,
        status: Literal[
            "AUTHORIZATION",
            "BALANCE_INQUIRY",
            "CREDIT_AUTHORIZATION",
            "FINANCIAL_AUTHORIZATION",
            "FINANCIAL_CREDIT_AUTHORIZATION",
        ]
        | NotGiven = NOT_GIVEN,
        merchant_acceptor_id: str | NotGiven = NOT_GIVEN,
        merchant_currency: str | NotGiven = NOT_GIVEN,
        merchant_amount: int | NotGiven = NOT_GIVEN,
        partial_approval_capable: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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

          merchant_acceptor_id: Unique identifier to identify the payment card acceptor.

          merchant_currency: 3-digit alphabetic ISO 4217 currency code.

          merchant_amount: Amount of the transaction to be simulated in currency specified in
              merchant_currency, including any acquirer fees.

          partial_approval_capable: Set to true if the terminal is capable of partial approval otherwise false.
              Partial approval is when part of a transaction is approved and another payment
              must be used for the remainder.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/simulate/authorize",
            body={
                "amount": amount,
                "descriptor": descriptor,
                "pan": pan,
                "status": status,
                "merchant_acceptor_id": merchant_acceptor_id,
                "merchant_currency": merchant_currency,
                "merchant_amount": merchant_amount,
                "partial_approval_capable": partial_approval_capable,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=TransactionSimulateAuthorizationResponse,
        )

    async def simulate_clearing(
        self,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer
        pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.

        Args:
          amount: Amount (in cents) to complete. Typically this will match the original
              authorization, but may be more or less.

              If no amount is supplied to this endpoint, the amount of the transaction will be
              captured. Any transaction that has any amount completed at all do not have
              access to this behavior.

          token: The transaction token returned from the /v1/simulate/authorize response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/simulate/clearing",
            body={
                "amount": amount,
                "token": token,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=TransactionSimulateClearingResponse,
        )

    async def simulate_credit_authorization(
        self,
        *,
        amount: int,
        descriptor: str,
        pan: str,
        merchant_acceptor_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
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

          merchant_acceptor_id: Unique identifier to identify the payment card acceptor.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/simulate/credit_authorization_advice",
            body={
                "amount": amount,
                "descriptor": descriptor,
                "pan": pan,
                "merchant_acceptor_id": merchant_acceptor_id,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
        """
        return await self._post(
            "/simulate/return",
            body={
                "amount": amount,
                "descriptor": descriptor,
                "pan": pan,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
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
        """
        return await self._post(
            "/simulate/return_reversal",
            body={"token": token},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=TransactionSimulateReturnReversalResponse,
        )

    async def simulate_void(
        self,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        token: str,
        type: Literal["AUTHORIZATION_EXPIRY", "AUTHORIZATION_REVERSAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent
        the full amount will be voided. Cannot be used on partially completed
        transactions, but can be used on partially voided transactions. _Note that
        simulating an authorization expiry on credit authorizations or credit
        authorization advice is not currently supported but will be added soon._

        Args:
          amount: Amount (in cents) to void. Typically this will match the original authorization,
              but may be less.

          token: The transaction token returned from the /v1/simulate/authorize response.

          type: Type of event to simulate. Defaults to `AUTHORIZATION_REVERSAL`.

              - `AUTHORIZATION_EXPIRY` indicates authorization has expired and been reversed
                by Lithic.
              - `AUTHORIZATION_REVERSAL` indicates authorization was reversed by the merchant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/simulate/void",
            body={
                "amount": amount,
                "token": token,
                "type": type,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=TransactionSimulateVoidResponse,
        )
