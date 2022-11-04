# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload
from typing_extensions import Literal

from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from .._utils import required_args
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.transaction import Transaction
from ..types.transaction_list_params import TransactionListParams
from ..types.transaction_simulate_void_params import TransactionSimulateVoidParams
from ..types.transaction_simulate_return_params import TransactionSimulateReturnParams
from ..types.transaction_simulate_void_response import TransactionSimulateVoidResponse
from ..types.transaction_simulate_clearing_params import (
    TransactionSimulateClearingParams,
)
from ..types.transaction_simulate_return_response import (
    TransactionSimulateReturnResponse,
)
from ..types.transaction_simulate_clearing_response import (
    TransactionSimulateClearingResponse,
)
from ..types.transaction_simulate_authorization_params import (
    TransactionSimulateAuthorizationParams,
)
from ..types.transaction_simulate_authorization_response import (
    TransactionSimulateAuthorizationResponse,
)

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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """
        Get specific transaction.

        _Note that the events.amount field returned via this endpoint became a signed
        field on September 27, 2022. Please refer to
        [this page](https://docs.lithic.com/docs/guide-to-lithic-api-changes-march-2022)
        for more information._
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/transactions/{transaction_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Transaction,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Transaction]:
        """
        List transactions.

        _Note that the events.amount field returned via this endpoint became a signed
        field on September 27, 2022. Please refer to
        [this page](https://docs.lithic.com/docs/guide-to-lithic-api-changes-march-2022)
        for more information._

        Args:
          account_token: Only required for multi-account users. Returns transactions associated with this
              account. Only applicable if using account holder enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          card_token: Filters transactions associated with a specific card.

          result: List specific transactions. Filters include `APPROVED`, and `DECLINED`.

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
        ...

    @overload
    def list(
        self,
        query: TransactionListParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Transaction]:
        """
        List transactions.

        _Note that the events.amount field returned via this endpoint became a signed
        field on September 27, 2022. Please refer to
        [this page](https://docs.lithic.com/docs/guide-to-lithic-api-changes-march-2022)
        for more information._
        """
        ...

    def list(
        self,
        query: TransactionListParams | None = None,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Transaction]:
        """
        List transactions.

        _Note that the events.amount field returned via this endpoint became a signed
        field on September 27, 2022. Please refer to
        [this page](https://docs.lithic.com/docs/guide-to-lithic-api-changes-march-2022)
        for more information._

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_token: Only required for multi-account users. Returns transactions associated with this
              account. Only applicable if using account holder enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          card_token: Filters transactions associated with a specific card.

          result: List specific transactions. Filters include `APPROVED`, and `DECLINED`.

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
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionListParams type.
            query = cast(
                Any,
                {
                    "account_token": account_token,
                    "card_token": card_token,
                    "result": result,
                    "begin": begin,
                    "end": end,
                    "page": page,
                    "page_size": page_size,
                },
            )

        return self._get_api_list(
            "/transactions",
            page=SyncPage[Transaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=Transaction,
        )

    @overload
    def simulate_authorization(
        self,
        *,
        amount: int,
        descriptor: str,
        pan: str,
        status: Literal[
            "AUTHORIZATION", "CREDIT_AUTHORIZATION", "FINANCIAL_AUTHORIZATION", "FINANCIAL_CREDIT_AUTHORIZATION"
        ]
        | NotGiven = NOT_GIVEN,
        merchant_currency: str | NotGiven = NOT_GIVEN,
        merchant_amount: int | NotGiven = NOT_GIVEN,
        partial_approval_capable: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateAuthorizationResponse:
        """
        Simulates an authorization request from the payment network as if it came from a
        merchant acquirer. If you're configured for ASA, simulating auths requires your
        ASA client to be set up properly (respond with a valid JSON to the ASA request).

        Args:
          amount: Amount (in cents) to authorize.

          descriptor: Merchant descriptor.

          pan: Sixteen digit card number.

          status: Type of event to simulate.

              - `CREDIT` indicates funds flow towards the user rather than towards the
                merchant.
              - `FINANCIAL` indicates that this is a single message transaction that completes
                immediately if approved.

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
        ...

    @overload
    def simulate_authorization(
        self,
        body: TransactionSimulateAuthorizationParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateAuthorizationResponse:
        """
        Simulates an authorization request from the payment network as if it came from a
        merchant acquirer. If you're configured for ASA, simulating auths requires your
        ASA client to be set up properly (respond with a valid JSON to the ASA request).
        """
        ...

    @required_args(["body"], ["amount", "descriptor", "pan"])
    def simulate_authorization(
        self,
        body: TransactionSimulateAuthorizationParams | None = None,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        pan: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "AUTHORIZATION", "CREDIT_AUTHORIZATION", "FINANCIAL_AUTHORIZATION", "FINANCIAL_CREDIT_AUTHORIZATION"
        ]
        | NotGiven = NOT_GIVEN,
        merchant_currency: str | NotGiven = NOT_GIVEN,
        merchant_amount: int | NotGiven = NOT_GIVEN,
        partial_approval_capable: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateAuthorizationResponse:
        """
        Simulates an authorization request from the payment network as if it came from a
        merchant acquirer. If you're configured for ASA, simulating auths requires your
        ASA client to be set up properly (respond with a valid JSON to the ASA request).

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          amount: Amount (in cents) to authorize.

          descriptor: Merchant descriptor.

          pan: Sixteen digit card number.

          status: Type of event to simulate.

              - `CREDIT` indicates funds flow towards the user rather than towards the
                merchant.
              - `FINANCIAL` indicates that this is a single message transaction that completes
                immediately if approved.

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
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionSimulateAuthorizationParams type.
            body = cast(
                Any,
                {
                    "amount": amount,
                    "descriptor": descriptor,
                    "pan": pan,
                    "status": status,
                    "merchant_currency": merchant_currency,
                    "merchant_amount": merchant_amount,
                    "partial_approval_capable": partial_approval_capable,
                },
            )

        return self._post(
            "/simulate/authorize",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=TransactionSimulateAuthorizationResponse,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    def simulate_clearing(
        self,
        body: TransactionSimulateClearingParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer
        pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.
        """
        ...

    @required_args(["body"], ["token"])
    def simulate_clearing(
        self,
        body: TransactionSimulateClearingParams | None = None,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer
        pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionSimulateClearingParams type.
            body = cast(
                Any,
                {
                    "amount": amount,
                    "token": token,
                },
            )

        return self._post(
            "/simulate/clearing",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=TransactionSimulateClearingResponse,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    def simulate_return(
        self,
        body: TransactionSimulateReturnParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately
        and do not spend time in a `PENDING` state.
        """
        ...

    @required_args(["body"], ["amount", "descriptor", "pan"])
    def simulate_return(
        self,
        body: TransactionSimulateReturnParams | None = None,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        pan: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately
        and do not spend time in a `PENDING` state.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          amount: Amount (in cents) to authorize.

          descriptor: Merchant descriptor.

          pan: Sixteen digit card number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionSimulateReturnParams type.
            body = cast(
                Any,
                {
                    "amount": amount,
                    "descriptor": descriptor,
                    "pan": pan,
                },
            )

        return self._post(
            "/simulate/return",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=TransactionSimulateReturnResponse,
        )

    @overload
    def simulate_void(
        self,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent
        the full amount will be voided. Cannot be used on partially completed
        transactions, but can be used on partially voided transactions.

        Args:
          amount: Amount (in cents) to void. Typically this will match the original authorization,
              but may be less.

          token: The transaction token returned from the /v1/simulate/authorize response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def simulate_void(
        self,
        body: TransactionSimulateVoidParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent
        the full amount will be voided. Cannot be used on partially completed
        transactions, but can be used on partially voided transactions.
        """
        ...

    @required_args(["body"], ["token"])
    def simulate_void(
        self,
        body: TransactionSimulateVoidParams | None = None,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent
        the full amount will be voided. Cannot be used on partially completed
        transactions, but can be used on partially voided transactions.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          amount: Amount (in cents) to void. Typically this will match the original authorization,
              but may be less.

          token: The transaction token returned from the /v1/simulate/authorize response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionSimulateVoidParams type.
            body = cast(
                Any,
                {
                    "amount": amount,
                    "token": token,
                },
            )

        return self._post(
            "/simulate/void",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """
        Get specific transaction.

        _Note that the events.amount field returned via this endpoint became a signed
        field on September 27, 2022. Please refer to
        [this page](https://docs.lithic.com/docs/guide-to-lithic-api-changes-march-2022)
        for more information._
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/transactions/{transaction_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Transaction,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Transaction, AsyncPage[Transaction]]:
        """
        List transactions.

        _Note that the events.amount field returned via this endpoint became a signed
        field on September 27, 2022. Please refer to
        [this page](https://docs.lithic.com/docs/guide-to-lithic-api-changes-march-2022)
        for more information._

        Args:
          account_token: Only required for multi-account users. Returns transactions associated with this
              account. Only applicable if using account holder enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          card_token: Filters transactions associated with a specific card.

          result: List specific transactions. Filters include `APPROVED`, and `DECLINED`.

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
        ...

    @overload
    def list(
        self,
        query: TransactionListParams = {},
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Transaction, AsyncPage[Transaction]]:
        """
        List transactions.

        _Note that the events.amount field returned via this endpoint became a signed
        field on September 27, 2022. Please refer to
        [this page](https://docs.lithic.com/docs/guide-to-lithic-api-changes-march-2022)
        for more information._
        """
        ...

    def list(
        self,
        query: TransactionListParams | None = None,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Transaction, AsyncPage[Transaction]]:
        """
        List transactions.

        _Note that the events.amount field returned via this endpoint became a signed
        field on September 27, 2022. Please refer to
        [this page](https://docs.lithic.com/docs/guide-to-lithic-api-changes-march-2022)
        for more information._

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          account_token: Only required for multi-account users. Returns transactions associated with this
              account. Only applicable if using account holder enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          card_token: Filters transactions associated with a specific card.

          result: List specific transactions. Filters include `APPROVED`, and `DECLINED`.

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
        if query is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionListParams type.
            query = cast(
                Any,
                {
                    "account_token": account_token,
                    "card_token": card_token,
                    "result": result,
                    "begin": begin,
                    "end": end,
                    "page": page,
                    "page_size": page_size,
                },
            )

        return self._get_api_list(
            "/transactions",
            page=AsyncPage[Transaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=Transaction,
        )

    @overload
    async def simulate_authorization(
        self,
        *,
        amount: int,
        descriptor: str,
        pan: str,
        status: Literal[
            "AUTHORIZATION", "CREDIT_AUTHORIZATION", "FINANCIAL_AUTHORIZATION", "FINANCIAL_CREDIT_AUTHORIZATION"
        ]
        | NotGiven = NOT_GIVEN,
        merchant_currency: str | NotGiven = NOT_GIVEN,
        merchant_amount: int | NotGiven = NOT_GIVEN,
        partial_approval_capable: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateAuthorizationResponse:
        """
        Simulates an authorization request from the payment network as if it came from a
        merchant acquirer. If you're configured for ASA, simulating auths requires your
        ASA client to be set up properly (respond with a valid JSON to the ASA request).

        Args:
          amount: Amount (in cents) to authorize.

          descriptor: Merchant descriptor.

          pan: Sixteen digit card number.

          status: Type of event to simulate.

              - `CREDIT` indicates funds flow towards the user rather than towards the
                merchant.
              - `FINANCIAL` indicates that this is a single message transaction that completes
                immediately if approved.

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
        ...

    @overload
    async def simulate_authorization(
        self,
        body: TransactionSimulateAuthorizationParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateAuthorizationResponse:
        """
        Simulates an authorization request from the payment network as if it came from a
        merchant acquirer. If you're configured for ASA, simulating auths requires your
        ASA client to be set up properly (respond with a valid JSON to the ASA request).
        """
        ...

    @required_args(["body"], ["amount", "descriptor", "pan"])
    async def simulate_authorization(
        self,
        body: TransactionSimulateAuthorizationParams | None = None,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        pan: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "AUTHORIZATION", "CREDIT_AUTHORIZATION", "FINANCIAL_AUTHORIZATION", "FINANCIAL_CREDIT_AUTHORIZATION"
        ]
        | NotGiven = NOT_GIVEN,
        merchant_currency: str | NotGiven = NOT_GIVEN,
        merchant_amount: int | NotGiven = NOT_GIVEN,
        partial_approval_capable: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateAuthorizationResponse:
        """
        Simulates an authorization request from the payment network as if it came from a
        merchant acquirer. If you're configured for ASA, simulating auths requires your
        ASA client to be set up properly (respond with a valid JSON to the ASA request).

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          amount: Amount (in cents) to authorize.

          descriptor: Merchant descriptor.

          pan: Sixteen digit card number.

          status: Type of event to simulate.

              - `CREDIT` indicates funds flow towards the user rather than towards the
                merchant.
              - `FINANCIAL` indicates that this is a single message transaction that completes
                immediately if approved.

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
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionSimulateAuthorizationParams type.
            body = cast(
                Any,
                {
                    "amount": amount,
                    "descriptor": descriptor,
                    "pan": pan,
                    "status": status,
                    "merchant_currency": merchant_currency,
                    "merchant_amount": merchant_amount,
                    "partial_approval_capable": partial_approval_capable,
                },
            )

        return await self._post(
            "/simulate/authorize",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=TransactionSimulateAuthorizationResponse,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    async def simulate_clearing(
        self,
        body: TransactionSimulateClearingParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer
        pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.
        """
        ...

    @required_args(["body"], ["token"])
    async def simulate_clearing(
        self,
        body: TransactionSimulateClearingParams | None = None,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer
        pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionSimulateClearingParams type.
            body = cast(
                Any,
                {
                    "amount": amount,
                    "token": token,
                },
            )

        return await self._post(
            "/simulate/clearing",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=TransactionSimulateClearingResponse,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    async def simulate_return(
        self,
        body: TransactionSimulateReturnParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately
        and do not spend time in a `PENDING` state.
        """
        ...

    @required_args(["body"], ["amount", "descriptor", "pan"])
    async def simulate_return(
        self,
        body: TransactionSimulateReturnParams | None = None,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        descriptor: str | NotGiven = NOT_GIVEN,
        pan: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately
        and do not spend time in a `PENDING` state.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          amount: Amount (in cents) to authorize.

          descriptor: Merchant descriptor.

          pan: Sixteen digit card number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionSimulateReturnParams type.
            body = cast(
                Any,
                {
                    "amount": amount,
                    "descriptor": descriptor,
                    "pan": pan,
                },
            )

        return await self._post(
            "/simulate/return",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=TransactionSimulateReturnResponse,
        )

    @overload
    async def simulate_void(
        self,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent
        the full amount will be voided. Cannot be used on partially completed
        transactions, but can be used on partially voided transactions.

        Args:
          amount: Amount (in cents) to void. Typically this will match the original authorization,
              but may be less.

          token: The transaction token returned from the /v1/simulate/authorize response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def simulate_void(
        self,
        body: TransactionSimulateVoidParams,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent
        the full amount will be voided. Cannot be used on partially completed
        transactions, but can be used on partially voided transactions.
        """
        ...

    @required_args(["body"], ["token"])
    async def simulate_void(
        self,
        body: TransactionSimulateVoidParams | None = None,
        *,
        amount: int | NotGiven = NOT_GIVEN,
        token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent
        the full amount will be voided. Cannot be used on partially completed
        transactions, but can be used on partially voided transactions.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          amount: Amount (in cents) to void. Typically this will match the original authorization,
              but may be less.

          token: The transaction token returned from the /v1/simulate/authorize response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        if body is not None:
            warnings.warn(
                "Passing parameters as a dictionary is deprecated and will be removed in the future",
                DeprecationWarning,
                stacklevel=2,
            )
        else:
            # cast to Any is required because the NotGiven types make this expression incompatible
            # with the standard TransactionSimulateVoidParams type.
            body = cast(
                Any,
                {
                    "amount": amount,
                    "token": token,
                },
            )

        return await self._post(
            "/simulate/void",
            body=body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=TransactionSimulateVoidResponse,
        )
