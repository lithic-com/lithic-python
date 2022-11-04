# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, Union, Optional, cast, overload
from typing_extensions import Literal

from ..types import account_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.account import Account
from ..types.account_list_params import AccountListParams
from ..types.account_update_params import AccountUpdateParams

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(SyncAPIResource):
    def retrieve(
        self,
        account_token: str,
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
    ) -> Account:
        """Get account configuration such as spend limits."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/accounts/{account_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Account,
        )

    @overload
    def update(
        self,
        account_token: str,
        *,
        daily_spend_limit: int | NotGiven = NOT_GIVEN,
        lifetime_spend_limit: int | NotGiven = NOT_GIVEN,
        monthly_spend_limit: int | NotGiven = NOT_GIVEN,
        verification_address: account_update_params.VerificationAddress | NotGiven = NOT_GIVEN,
        state: Literal["ACTIVE", "PAUSED"] | NotGiven = NOT_GIVEN,
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
    ) -> Account:
        """Update account configuration such as spend limits and verification address.

        Can
        only be run on accounts that are part of the program managed by this API key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.

        Args:
          daily_spend_limit: Amount (in cents) for the account's new daily spend limit. Note that a spend
              limit of 0 is effectively no limit, and should only be used to reset or remove a
              prior limit. Only a limit of 1 or above will result in declined transactions due
              to checks against the account limit.

          lifetime_spend_limit: Amount (in cents) for the account's new lifetime limit. Once this limit is
              reached, no transactions will be accepted on any card created for this account
              until the limit is updated. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the
              account limit.

          monthly_spend_limit: Amount (in cents) for the account's new monthly spend limit. Note that a spend
              limit of 0 is effectively no limit, and should only be used to reset or remove a
              prior limit. Only a limit of 1 or above will result in declined transactions due
              to checks against the account limit.

          verification_address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules.

          state: Account states.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def update(
        self,
        account_token: str,
        body: AccountUpdateParams,
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
    ) -> Account:
        """Update account configuration such as spend limits and verification address.

        Can
        only be run on accounts that are part of the program managed by this API key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.
        """
        ...

    def update(
        self,
        account_token: str,
        body: AccountUpdateParams | None = None,
        *,
        daily_spend_limit: int | NotGiven = NOT_GIVEN,
        lifetime_spend_limit: int | NotGiven = NOT_GIVEN,
        monthly_spend_limit: int | NotGiven = NOT_GIVEN,
        verification_address: account_update_params.VerificationAddress | NotGiven = NOT_GIVEN,
        state: Literal["ACTIVE", "PAUSED"] | NotGiven = NOT_GIVEN,
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
    ) -> Account:
        """Update account configuration such as spend limits and verification address.

        Can
        only be run on accounts that are part of the program managed by this API key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          daily_spend_limit: Amount (in cents) for the account's new daily spend limit. Note that a spend
              limit of 0 is effectively no limit, and should only be used to reset or remove a
              prior limit. Only a limit of 1 or above will result in declined transactions due
              to checks against the account limit.

          lifetime_spend_limit: Amount (in cents) for the account's new lifetime limit. Once this limit is
              reached, no transactions will be accepted on any card created for this account
              until the limit is updated. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the
              account limit.

          monthly_spend_limit: Amount (in cents) for the account's new monthly spend limit. Note that a spend
              limit of 0 is effectively no limit, and should only be used to reset or remove a
              prior limit. Only a limit of 1 or above will result in declined transactions due
              to checks against the account limit.

          verification_address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules.

          state: Account states.

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
            # with the standard AccountUpdateParams type.
            body = cast(
                Any,
                {
                    "daily_spend_limit": daily_spend_limit,
                    "lifetime_spend_limit": lifetime_spend_limit,
                    "monthly_spend_limit": monthly_spend_limit,
                    "verification_address": verification_address,
                    "state": state,
                },
            )

        return self._patch(
            f"/accounts/{account_token}",
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
            cast_to=Account,
        )

    @overload
    def list(
        self,
        *,
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
    ) -> SyncPage[Account]:
        """List account configurations.

        Args:
          begin: Date string in 8601 format.

        Only entries created after the specified date will
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
        query: AccountListParams = {},
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
    ) -> SyncPage[Account]:
        """List account configurations."""
        ...

    def list(
        self,
        query: AccountListParams | None = None,
        *,
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
    ) -> SyncPage[Account]:
        """
        List account configurations.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard AccountListParams type.
            query = cast(
                Any,
                {
                    "begin": begin,
                    "end": end,
                    "page": page,
                    "page_size": page_size,
                },
            )

        return self._get_api_list(
            "/accounts",
            page=SyncPage[Account],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=Account,
        )


class AsyncAccounts(AsyncAPIResource):
    async def retrieve(
        self,
        account_token: str,
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
    ) -> Account:
        """Get account configuration such as spend limits."""
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/accounts/{account_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=Account,
        )

    @overload
    async def update(
        self,
        account_token: str,
        *,
        daily_spend_limit: int | NotGiven = NOT_GIVEN,
        lifetime_spend_limit: int | NotGiven = NOT_GIVEN,
        monthly_spend_limit: int | NotGiven = NOT_GIVEN,
        verification_address: account_update_params.VerificationAddress | NotGiven = NOT_GIVEN,
        state: Literal["ACTIVE", "PAUSED"] | NotGiven = NOT_GIVEN,
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
    ) -> Account:
        """Update account configuration such as spend limits and verification address.

        Can
        only be run on accounts that are part of the program managed by this API key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.

        Args:
          daily_spend_limit: Amount (in cents) for the account's new daily spend limit. Note that a spend
              limit of 0 is effectively no limit, and should only be used to reset or remove a
              prior limit. Only a limit of 1 or above will result in declined transactions due
              to checks against the account limit.

          lifetime_spend_limit: Amount (in cents) for the account's new lifetime limit. Once this limit is
              reached, no transactions will be accepted on any card created for this account
              until the limit is updated. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the
              account limit.

          monthly_spend_limit: Amount (in cents) for the account's new monthly spend limit. Note that a spend
              limit of 0 is effectively no limit, and should only be used to reset or remove a
              prior limit. Only a limit of 1 or above will result in declined transactions due
              to checks against the account limit.

          verification_address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules.

          state: Account states.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def update(
        self,
        account_token: str,
        body: AccountUpdateParams,
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
    ) -> Account:
        """Update account configuration such as spend limits and verification address.

        Can
        only be run on accounts that are part of the program managed by this API key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.
        """
        ...

    async def update(
        self,
        account_token: str,
        body: AccountUpdateParams | None = None,
        *,
        daily_spend_limit: int | NotGiven = NOT_GIVEN,
        lifetime_spend_limit: int | NotGiven = NOT_GIVEN,
        monthly_spend_limit: int | NotGiven = NOT_GIVEN,
        verification_address: account_update_params.VerificationAddress | NotGiven = NOT_GIVEN,
        state: Literal["ACTIVE", "PAUSED"] | NotGiven = NOT_GIVEN,
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
    ) -> Account:
        """Update account configuration such as spend limits and verification address.

        Can
        only be run on accounts that are part of the program managed by this API key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

          daily_spend_limit: Amount (in cents) for the account's new daily spend limit. Note that a spend
              limit of 0 is effectively no limit, and should only be used to reset or remove a
              prior limit. Only a limit of 1 or above will result in declined transactions due
              to checks against the account limit.

          lifetime_spend_limit: Amount (in cents) for the account's new lifetime limit. Once this limit is
              reached, no transactions will be accepted on any card created for this account
              until the limit is updated. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the
              account limit.

          monthly_spend_limit: Amount (in cents) for the account's new monthly spend limit. Note that a spend
              limit of 0 is effectively no limit, and should only be used to reset or remove a
              prior limit. Only a limit of 1 or above will result in declined transactions due
              to checks against the account limit.

          verification_address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules.

          state: Account states.

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
            # with the standard AccountUpdateParams type.
            body = cast(
                Any,
                {
                    "daily_spend_limit": daily_spend_limit,
                    "lifetime_spend_limit": lifetime_spend_limit,
                    "monthly_spend_limit": monthly_spend_limit,
                    "verification_address": verification_address,
                    "state": state,
                },
            )

        return await self._patch(
            f"/accounts/{account_token}",
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
            cast_to=Account,
        )

    @overload
    def list(
        self,
        *,
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
    ) -> AsyncPaginator[Account, AsyncPage[Account]]:
        """List account configurations.

        Args:
          begin: Date string in 8601 format.

        Only entries created after the specified date will
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
        query: AccountListParams = {},
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
    ) -> AsyncPaginator[Account, AsyncPage[Account]]:
        """List account configurations."""
        ...

    def list(
        self,
        query: AccountListParams | None = None,
        *,
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
    ) -> AsyncPaginator[Account, AsyncPage[Account]]:
        """
        List account configurations.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard AccountListParams type.
            query = cast(
                Any,
                {
                    "begin": begin,
                    "end": end,
                    "page": page,
                    "page_size": page_size,
                },
            )

        return self._get_api_list(
            "/accounts",
            page=AsyncPage[Account],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=Account,
        )
