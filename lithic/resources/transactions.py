# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union, Optional

from .._types import NOT_GIVEN, Query, Headers, Timeout, NotGiven
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
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """Get specific transaction.

        _Note that the events.amount field returned via this endpoint is changing and
        will become a signed field. Debits will appear as positive amounts and credits
        will appear as negative amounts. This is already reflected in Sandbox as of
        August 30, 2022 at 17:00 UTC and will be updated in Production on September 27,
        2022 at 17:00 UTC. Please refer to
        [this page](https://docs.lithic.com/docs/guide-to-lithic-api-changes-march-2022)
        for more information._
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get(
            f"/transactions/{transaction_token}",
            options=options,
            cast_to=Transaction,
        )

    def list(
        self,
        query: TransactionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Transaction]:
        """List transactions.

        _Note that the events.amount field returned via this endpoint is changing and
        will become a signed field. Debits will appear as positive amounts and credits
        will appear as negative amounts. This is already reflected in Sandbox as of
        August 30, 2022 at 17:00 UTC and will be updated in Production on September 27,
        2022 at 17:00 UTC. Please refer to
        [this page](https://docs.lithic.com/docs/guide-to-lithic-api-changes-march-2022)
        for more information._
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/transactions",
            page=SyncPage[Transaction],
            options=options,
            model=Transaction,
        )

    def simulate_authorization(
        self,
        body: TransactionSimulateAuthorizationParams,
        *,
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
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/simulate/authorize",
            body=body,
            options=options,
            cast_to=TransactionSimulateAuthorizationResponse,
        )

    def simulate_clearing(
        self,
        body: TransactionSimulateClearingParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/simulate/clearing",
            body=body,
            options=options,
            cast_to=TransactionSimulateClearingResponse,
        )

    def simulate_return(
        self,
        body: TransactionSimulateReturnParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately and do not spend time in a `PENDING` state.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/simulate/return",
            body=body,
            options=options,
            cast_to=TransactionSimulateReturnResponse,
        )

    def simulate_void(
        self,
        body: TransactionSimulateVoidParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent the full amount will be voided. Cannot be used on
        partially completed transactions, but can be used on partially voided
        transactions.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._post(
            "/simulate/void",
            body=body,
            options=options,
            cast_to=TransactionSimulateVoidResponse,
        )


class AsyncTransactions(AsyncAPIResource):
    async def retrieve(
        self,
        transaction_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> Transaction:
        """Get specific transaction.

        _Note that the events.amount field returned via this endpoint is changing and
        will become a signed field. Debits will appear as positive amounts and credits
        will appear as negative amounts. This is already reflected in Sandbox as of
        August 30, 2022 at 17:00 UTC and will be updated in Production on September 27,
        2022 at 17:00 UTC. Please refer to
        [this page](https://docs.lithic.com/docs/guide-to-lithic-api-changes-march-2022)
        for more information._
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._get(
            f"/transactions/{transaction_token}",
            options=options,
            cast_to=Transaction,
        )

    def list(
        self,
        query: TransactionListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Transaction, AsyncPage[Transaction]]:
        """List transactions.

        _Note that the events.amount field returned via this endpoint is changing and
        will become a signed field. Debits will appear as positive amounts and credits
        will appear as negative amounts. This is already reflected in Sandbox as of
        August 30, 2022 at 17:00 UTC and will be updated in Production on September 27,
        2022 at 17:00 UTC. Please refer to
        [this page](https://docs.lithic.com/docs/guide-to-lithic-api-changes-march-2022)
        for more information._
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return self._get_api_list(
            "/transactions",
            page=AsyncPage[Transaction],
            options=options,
            model=Transaction,
        )

    async def simulate_authorization(
        self,
        body: TransactionSimulateAuthorizationParams,
        *,
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
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/simulate/authorize",
            body=body,
            options=options,
            cast_to=TransactionSimulateAuthorizationResponse,
        )

    async def simulate_clearing(
        self,
        body: TransactionSimulateClearingParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/simulate/clearing",
            body=body,
            options=options,
            cast_to=TransactionSimulateClearingResponse,
        )

    async def simulate_return(
        self,
        body: TransactionSimulateReturnParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately and do not spend time in a `PENDING` state.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/simulate/return",
            body=body,
            options=options,
            cast_to=TransactionSimulateReturnResponse,
        )

    async def simulate_void(
        self,
        body: TransactionSimulateVoidParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent the full amount will be voided. Cannot be used on
        partially completed transactions, but can be used on partially voided
        transactions.
        """
        options = make_request_options(headers, max_retries, timeout, query)
        return await self._post(
            "/simulate/void",
            body=body,
            options=options,
            cast_to=TransactionSimulateVoidResponse,
        )
