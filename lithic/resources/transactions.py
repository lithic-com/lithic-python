# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Dict
from .._core import Timeout, make_request_options
from .._resource import SyncAPIResource, AsyncAPIResource
from .._models import StringModel, NoneModel
from ..pagination import SyncPage, AsyncPage
from ..types.transaction import *
from ..types.transaction_simulate_authorization_response import *
from ..types.transaction_simulate_clearing_response import *
from ..types.transaction_simulate_return_response import *
from ..types.transaction_simulate_void_response import *
from ..types.transaction_list_params import *
from ..types.transaction_simulate_authorization_params import *
from ..types.transaction_simulate_clearing_params import *
from ..types.transaction_simulate_return_params import *
from ..types.transaction_simulate_void_params import *

__all__ = ["Transactions", "AsyncTransactions"]


class Transactions(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> Transaction:
        """Get specific transaction."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.get(f"/transactions/{id}", model=Transaction, options=options)

    def list(
        self,
        query: Optional[TransactionListParams] = None,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> SyncPage[Transaction]:
        """List transactions."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.get_api_list(
            "/transactions", model=Transaction, page=SyncPage[Transaction], query=query, options=options
        )

    def simulate_authorization(
        self,
        body: TransactionSimulateAuthorizationParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> TransactionSimulateAuthorizationResponse:
        """Simulates an authorization request from the payment network as if it
        came from a merchant acquirer.

        If you're configured for ASA, simulating auths requires your ASA
        client to be set up properly (respond with a valid JSON to the
        ASA request).
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.post(
            "/simulate/authorize", model=TransactionSimulateAuthorizationResponse, body=body, options=options
        )

    def simulate_clearing(
        self,
        body: TransactionSimulateClearingParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer pending. If no
        `amount` is supplied to this endpoint, the amount of the
        transaction will be captured. Any transaction that has any
        amount completed at all do not have access to this behavior.
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.post("/simulate/clearing", model=TransactionSimulateClearingResponse, body=body, options=options)

    def simulate_return(
        self,
        body: TransactionSimulateReturnParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately and do not spend time in a
        `PENDING` state.
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.post("/simulate/return", model=TransactionSimulateReturnResponse, body=body, options=options)

    def simulate_void(
        self,
        body: TransactionSimulateVoidParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent the full amount will be voided. Cannot be
        used on partially completed transactions, but can be used on
        partially voided transactions.
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.post("/simulate/void", model=TransactionSimulateVoidResponse, body=body, options=options)


class AsyncTransactions(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> Transaction:
        """Get specific transaction."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.get(f"/transactions/{id}", model=Transaction, options=options)

    def list(
        self,
        query: Optional[TransactionListParams] = None,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AsyncPage[Transaction]:
        """List transactions."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.get_api_list(
            "/transactions", model=Transaction, page=AsyncPage[Transaction], query=query, options=options
        )

    async def simulate_authorization(
        self,
        body: TransactionSimulateAuthorizationParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> TransactionSimulateAuthorizationResponse:
        """Simulates an authorization request from the payment network as if it
        came from a merchant acquirer.

        If you're configured for ASA, simulating auths requires your ASA
        client to be set up properly (respond with a valid JSON to the
        ASA request).
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.post(
            "/simulate/authorize", model=TransactionSimulateAuthorizationResponse, body=body, options=options
        )

    async def simulate_clearing(
        self,
        body: TransactionSimulateClearingParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> TransactionSimulateClearingResponse:
        """Clears an existing authorization.

        After this event, the transaction is no longer pending. If no
        `amount` is supplied to this endpoint, the amount of the
        transaction will be captured. Any transaction that has any
        amount completed at all do not have access to this behavior.
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.post(
            "/simulate/clearing", model=TransactionSimulateClearingResponse, body=body, options=options
        )

    async def simulate_return(
        self,
        body: TransactionSimulateReturnParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> TransactionSimulateReturnResponse:
        """Returns (aka refunds) an amount back to a card.

        Returns are cleared immediately and do not spend time in a
        `PENDING` state.
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.post("/simulate/return", model=TransactionSimulateReturnResponse, body=body, options=options)

    async def simulate_void(
        self,
        body: TransactionSimulateVoidParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> TransactionSimulateVoidResponse:
        """Voids an existing, uncleared (aka pending) authorization.

        If amount is not sent the full amount will be voided. Cannot be
        used on partially completed transactions, but can be used on
        partially voided transactions.
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.post("/simulate/void", model=TransactionSimulateVoidResponse, body=body, options=options)
