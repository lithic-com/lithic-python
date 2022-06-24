# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.account import *
from ..types.account_list_params import AccountListParams
from ..types.account_update_params import AccountUpdateParams

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(SyncAPIResource):
    def retrieve(
        self,
        account_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Account:
        """Get account configuration such as spend limits."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/accounts/{account_token}",
            options=options,
            cast_to=Account,
        )

    def update(
        self,
        account_token: str,
        body: AccountUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Account:
        """Update account configuration such as spend limits and verification address.

        Can only be run on accounts that are part of the program managed by this API
        key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._patch(
            f"/accounts/{account_token}",
            body=body,
            options=options,
            cast_to=Account,
        )

    def list(
        self,
        query: AccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Account]:
        """List account configurations."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/accounts",
            page=SyncPage[Account],
            query=query,
            options=options,
            model=Account,
        )


class AsyncAccounts(AsyncAPIResource):
    async def retrieve(
        self,
        account_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Account:
        """Get account configuration such as spend limits."""
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/accounts/{account_token}",
            options=options,
            cast_to=Account,
        )

    async def update(
        self,
        account_token: str,
        body: AccountUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Account:
        """Update account configuration such as spend limits and verification address.

        Can only be run on accounts that are part of the program managed by this API
        key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._patch(
            f"/accounts/{account_token}",
            body=body,
            options=options,
            cast_to=Account,
        )

    def list(
        self,
        query: AccountListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Account, AsyncPage[Account]]:
        """List account configurations."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/accounts",
            page=AsyncPage[Account],
            query=query,
            options=options,
            model=Account,
        )
