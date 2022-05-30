# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union, Optional

from .._types import Timeout, NotGiven
from .._models import NoneModel, StringModel
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.account import *
from ..types.account_list_params import *
from ..types.account_update_params import *

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(SyncAPIResource):
    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> Account:
        """Get account configuration such as spend limits."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get(f"/accounts/{id}", model=Account, options=options)

    def update(
        self,
        id: str,
        body: AccountUpdateParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> Account:
        """Update account configuration such as spend limits and verification address.

        Can only be run on accounts that are part of the program managed by this API
        key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._patch(f"/accounts/{id}", model=Account, body=body, options=options)

    def list(
        self,
        query: AccountListParams = {},
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> SyncPage[Account]:
        """List account configurations."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list("/accounts", model=Account, page=SyncPage[Account], query=query, options=options)


class AsyncAccounts(AsyncAPIResource):
    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> Account:
        """Get account configuration such as spend limits."""
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(f"/accounts/{id}", model=Account, options=options)

    async def update(
        self,
        id: str,
        body: AccountUpdateParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> Account:
        """Update account configuration such as spend limits and verification address.

        Can only be run on accounts that are part of the program managed by this API
        key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._patch(f"/accounts/{id}", model=Account, body=body, options=options)

    def list(
        self,
        query: AccountListParams = {},
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AsyncPaginator[Account, AsyncPage[Account]]:
        """List account configurations."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list("/accounts", model=Account, page=AsyncPage[Account], query=query, options=options)
