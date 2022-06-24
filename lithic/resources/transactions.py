# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.transaction import *
from ..types.transaction_list_params import TransactionListParams
from ..types.transaction_simulate_void_params import TransactionSimulateVoidParams
from ..types.transaction_simulate_return_params import TransactionSimulateReturnParams
from ..types.transaction_simulate_void_response import *
from ..types.transaction_simulate_clearing_params import (
    TransactionSimulateClearingParams,
)
from ..types.transaction_simulate_return_response import *
from ..types.transaction_simulate_clearing_response import *
from ..types.transaction_simulate_authorization_params import (
    TransactionSimulateAuthorizationParams,
)
from ..types.transaction_simulate_authorization_response import *

__all__ = ["Transactions", "AsyncTransactions"]


class Transactions(SyncAPIResource):
    def retrieve(
        self,
        transaction_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Transaction:
        """Get specific transaction."""
        options = make_request_options(headers, max_retries, timeout)
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
        """List transactions."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/transactions",
            page=SyncPage[Transaction],
            query=query,
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
    ) -> TransactionSimulateAuthorizationResponse:
        """
        Simulates an authorization request from the payment network as if it came from a
        merchant acquirer. If you're configured for ASA, simulating auths requires your
        ASA client to be set up properly (respond with a valid JSON to the ASA request).
        """
        options = make_request_options(headers, max_retries, timeout)
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
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.
        """
        options = make_request_options(headers, max_retries, timeout)
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
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately and do not spend time in a `PENDING` state.
        """
        options = make_request_options(headers, max_retries, timeout)
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
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent the full amount will be voided. Cannot be used on
        partially completed transactions, but can be used on partially voided
        transactions.
        """
        options = make_request_options(headers, max_retries, timeout)
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
    ) -> Transaction:
        """Get specific transaction."""
        options = make_request_options(headers, max_retries, timeout)
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
        """List transactions."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/transactions",
            page=AsyncPage[Transaction],
            query=query,
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
    ) -> TransactionSimulateAuthorizationResponse:
        """
        Simulates an authorization request from the payment network as if it came from a
        merchant acquirer. If you're configured for ASA, simulating auths requires your
        ASA client to be set up properly (respond with a valid JSON to the ASA request).
        """
        options = make_request_options(headers, max_retries, timeout)
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
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.
        """
        options = make_request_options(headers, max_retries, timeout)
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
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately and do not spend time in a `PENDING` state.
        """
        options = make_request_options(headers, max_retries, timeout)
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
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent the full amount will be voided. Cannot be used on
        partially completed transactions, but can be used on partially voided
        transactions.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/simulate/void",
            body=body,
            options=options,
            cast_to=TransactionSimulateVoidResponse,
        )
