# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

from ..types import Account, account_list_params, account_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Get account configuration such as spend limits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def update(
        self,
        account_token: str,
        *,
        daily_spend_limit: int | NotGiven = NOT_GIVEN,
        lifetime_spend_limit: int | NotGiven = NOT_GIVEN,
        monthly_spend_limit: int | NotGiven = NOT_GIVEN,
        state: Literal["ACTIVE", "PAUSED"] | NotGiven = NOT_GIVEN,
        verification_address: account_update_params.VerificationAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Account:
        """Update account configuration such as spend limits and verification address.

        Can
        only be run on accounts that are part of the program managed by this API key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.

        Args:
          daily_spend_limit: Amount (in cents) for the account's daily spend limit. By default the daily
              spend limit is set to $1,250.

          lifetime_spend_limit: Amount (in cents) for the account's lifetime spend limit. Once this limit is
              reached, no transactions will be accepted on any card created for this account
              until the limit is updated. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the
              account limit. This behavior differs from the daily spend limit and the monthly
              spend limit.

          monthly_spend_limit: Amount (in cents) for the account's monthly spend limit. By default the monthly
              spend limit is set to $5,000.

          state: Account states.

          verification_address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/accounts/{account_token}",
            body=maybe_transform(
                {
                    "daily_spend_limit": daily_spend_limit,
                    "lifetime_spend_limit": lifetime_spend_limit,
                    "monthly_spend_limit": monthly_spend_limit,
                    "state": state,
                    "verification_address": verification_address,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Account,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Account]:
        """List account configurations.

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified date
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included. UTC time zone.

          page: Page (for pagination).

          page_size: Page size (for pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/accounts",
            page=SyncPage[Account],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "page": page,
                        "page_size": page_size,
                    },
                    account_list_params.AccountListParams,
                ),
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Get account configuration such as spend limits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    async def update(
        self,
        account_token: str,
        *,
        daily_spend_limit: int | NotGiven = NOT_GIVEN,
        lifetime_spend_limit: int | NotGiven = NOT_GIVEN,
        monthly_spend_limit: int | NotGiven = NOT_GIVEN,
        state: Literal["ACTIVE", "PAUSED"] | NotGiven = NOT_GIVEN,
        verification_address: account_update_params.VerificationAddress | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Account:
        """Update account configuration such as spend limits and verification address.

        Can
        only be run on accounts that are part of the program managed by this API key.

        Accounts that are in the `PAUSED` state will not be able to transact or create
        new cards.

        Args:
          daily_spend_limit: Amount (in cents) for the account's daily spend limit. By default the daily
              spend limit is set to $1,250.

          lifetime_spend_limit: Amount (in cents) for the account's lifetime spend limit. Once this limit is
              reached, no transactions will be accepted on any card created for this account
              until the limit is updated. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the
              account limit. This behavior differs from the daily spend limit and the monthly
              spend limit.

          monthly_spend_limit: Amount (in cents) for the account's monthly spend limit. By default the monthly
              spend limit is set to $5,000.

          state: Account states.

          verification_address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/accounts/{account_token}",
            body=maybe_transform(
                {
                    "daily_spend_limit": daily_spend_limit,
                    "lifetime_spend_limit": lifetime_spend_limit,
                    "monthly_spend_limit": monthly_spend_limit,
                    "state": state,
                    "verification_address": verification_address,
                },
                account_update_params.AccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Account,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Account, AsyncPage[Account]]:
        """List account configurations.

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified date
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included. UTC time zone.

          page: Page (for pagination).

          page_size: Page size (for pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/accounts",
            page=AsyncPage[Account],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "page": page,
                        "page_size": page_size,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            model=Account,
        )
