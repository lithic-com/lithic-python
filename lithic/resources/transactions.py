# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union, Optional

from .._types import Timeout, NotGiven
from .._models import NoneModel, StringModel
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.transaction import *
from ..types.transaction_list_params import *
from ..types.transaction_simulate_void_params import *
from ..types.transaction_simulate_return_params import *
from ..types.transaction_simulate_void_response import *
from ..types.transaction_simulate_clearing_params import *
from ..types.transaction_simulate_return_response import *
from ..types.transaction_simulate_clearing_response import *
from ..types.transaction_simulate_authorization_params import *
from ..types.transaction_simulate_authorization_response import *

__all__ = ["Transactions", "AsyncTransactions"]


class Transactions(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> Transaction:
        """Get specific transaction."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get(f"/transactions/{id}", model=Transaction, options=options)

    def list(
        self,
        query: TransactionListParams = {},
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> SyncPage[Transaction]:
        """List transactions."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/transactions", model=Transaction, page=SyncPage[Transaction], query=query, options=options
        )

    def simulate_authorization(
        self,
        body: TransactionSimulateAuthorizationParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> TransactionSimulateAuthorizationResponse:
        """
        Simulates an authorization request from the payment network as if it came from a
        merchant acquirer. If you're configured for ASA, simulating auths requires your
        ASA client to be set up properly (respond with a valid JSON to the ASA request).
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/simulate/authorize", model=TransactionSimulateAuthorizationResponse, body=body, options=options
        )

    def simulate_clearing(
        self,
        body: TransactionSimulateClearingParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post("/simulate/clearing", model=TransactionSimulateClearingResponse, body=body, options=options)

    def simulate_return(
        self,
        body: TransactionSimulateReturnParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately and do not spend time in a `PENDING` state.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post("/simulate/return", model=TransactionSimulateReturnResponse, body=body, options=options)

    def simulate_void(
        self,
        body: TransactionSimulateVoidParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent the full amount will be voided. Cannot be used on
        partially completed transactions, but can be used on partially voided
        transactions.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post("/simulate/void", model=TransactionSimulateVoidResponse, body=body, options=options)


class AsyncTransactions(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> Transaction:
        """Get specific transaction."""
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(f"/transactions/{id}", model=Transaction, options=options)

    def list(
        self,
        query: TransactionListParams = {},
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AsyncPaginator[Transaction, AsyncPage[Transaction]]:
        """List transactions."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/transactions", model=Transaction, page=AsyncPage[Transaction], query=query, options=options
        )

    async def simulate_authorization(
        self,
        body: TransactionSimulateAuthorizationParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> TransactionSimulateAuthorizationResponse:
        """
        Simulates an authorization request from the payment network as if it came from a
        merchant acquirer. If you're configured for ASA, simulating auths requires your
        ASA client to be set up properly (respond with a valid JSON to the ASA request).
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/simulate/authorize", model=TransactionSimulateAuthorizationResponse, body=body, options=options
        )

    async def simulate_clearing(
        self,
        body: TransactionSimulateClearingParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer pending.

        If no `amount` is supplied to this endpoint, the amount of the transaction will
        be captured. Any transaction that has any amount completed at all do not have
        access to this behavior.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/simulate/clearing", model=TransactionSimulateClearingResponse, body=body, options=options
        )

    async def simulate_return(
        self,
        body: TransactionSimulateReturnParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately and do not spend time in a `PENDING` state.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post("/simulate/return", model=TransactionSimulateReturnResponse, body=body, options=options)

    async def simulate_void(
        self,
        body: TransactionSimulateVoidParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent the full amount will be voided. Cannot be used on
        partially completed transactions, but can be used on partially voided
        transactions.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post("/simulate/void", model=TransactionSimulateVoidResponse, body=body, options=options)
