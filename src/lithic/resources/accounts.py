# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import account_list_params, account_update_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.account import Account
from ..types.account_spend_limits import AccountSpendLimits

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AccountsWithStreamingResponse(self)

    def retrieve(
        self,
        account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Get account configuration such as spend limits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return self._get(
            f"/v1/accounts/{account_token}",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """Update account configuration such as state or spend limits.

        Can only be run on
        accounts that are part of the program managed by this API key. Accounts that are
        in the `PAUSED` state will not be able to transact or create new cards.

        Args:
          daily_spend_limit: Amount (in cents) for the account's daily spend limit (e.g. 100000 would be a
              $1,000 limit). By default the daily spend limit is set to $1,250.

          lifetime_spend_limit: Amount (in cents) for the account's lifetime spend limit (e.g. 100000 would be a
              $1,000 limit). Once this limit is reached, no transactions will be accepted on
              any card created for this account until the limit is updated. Note that a spend
              limit of 0 is effectively no limit, and should only be used to reset or remove a
              prior limit. Only a limit of 1 or above will result in declined transactions due
              to checks against the account limit. This behavior differs from the daily spend
              limit and the monthly spend limit.

          monthly_spend_limit: Amount (in cents) for the account's monthly spend limit (e.g. 100000 would be a
              $1,000 limit). By default the monthly spend limit is set to $5,000.

          state: Account states.

          verification_address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules. This field is deprecated as AVS checks
              are no longer supported by Authorization Rules. The field will be removed from
              the schema in a future release.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return self._patch(
            f"/v1/accounts/{account_token}",
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Account]:
        """List account configurations.

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/accounts",
            page=SyncCursorPage[Account],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            model=Account,
        )

    def retrieve_spend_limits(
        self,
        account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountSpendLimits:
        """
        Get an Account's available spend limits, which is based on the spend limit
        configured on the Account and the amount already spent over the spend limit's
        duration. For example, if the Account has a daily spend limit of $1000
        configured, and has spent $600 in the last 24 hours, the available spend limit
        returned would be $400.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return self._get(
            f"/v1/accounts/{account_token}/spend_limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountSpendLimits,
        )


class AsyncAccounts(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncAccountsWithStreamingResponse(self)

    async def retrieve(
        self,
        account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Get account configuration such as spend limits.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return await self._get(
            f"/v1/accounts/{account_token}",
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """Update account configuration such as state or spend limits.

        Can only be run on
        accounts that are part of the program managed by this API key. Accounts that are
        in the `PAUSED` state will not be able to transact or create new cards.

        Args:
          daily_spend_limit: Amount (in cents) for the account's daily spend limit (e.g. 100000 would be a
              $1,000 limit). By default the daily spend limit is set to $1,250.

          lifetime_spend_limit: Amount (in cents) for the account's lifetime spend limit (e.g. 100000 would be a
              $1,000 limit). Once this limit is reached, no transactions will be accepted on
              any card created for this account until the limit is updated. Note that a spend
              limit of 0 is effectively no limit, and should only be used to reset or remove a
              prior limit. Only a limit of 1 or above will result in declined transactions due
              to checks against the account limit. This behavior differs from the daily spend
              limit and the monthly spend limit.

          monthly_spend_limit: Amount (in cents) for the account's monthly spend limit (e.g. 100000 would be a
              $1,000 limit). By default the monthly spend limit is set to $5,000.

          state: Account states.

          verification_address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules. This field is deprecated as AVS checks
              are no longer supported by Authorization Rules. The field will be removed from
              the schema in a future release.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return await self._patch(
            f"/v1/accounts/{account_token}",
            body=await async_maybe_transform(
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
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Account, AsyncCursorPage[Account]]:
        """List account configurations.

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/accounts",
            page=AsyncCursorPage[Account],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            model=Account,
        )

    async def retrieve_spend_limits(
        self,
        account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountSpendLimits:
        """
        Get an Account's available spend limits, which is based on the spend limit
        configured on the Account and the amount already spent over the spend limit's
        duration. For example, if the Account has a daily spend limit of $1000
        configured, and has spent $600 in the last 24 hours, the available spend limit
        returned would be $400.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return await self._get(
            f"/v1/accounts/{account_token}/spend_limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountSpendLimits,
        )


class AccountsWithRawResponse:
    def __init__(self, accounts: Accounts) -> None:
        self._accounts = accounts

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            accounts.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            accounts.list,
        )
        self.retrieve_spend_limits = _legacy_response.to_raw_response_wrapper(
            accounts.retrieve_spend_limits,
        )


class AsyncAccountsWithRawResponse:
    def __init__(self, accounts: AsyncAccounts) -> None:
        self._accounts = accounts

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            accounts.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            accounts.list,
        )
        self.retrieve_spend_limits = _legacy_response.async_to_raw_response_wrapper(
            accounts.retrieve_spend_limits,
        )


class AccountsWithStreamingResponse:
    def __init__(self, accounts: Accounts) -> None:
        self._accounts = accounts

        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )
        self.retrieve_spend_limits = to_streamed_response_wrapper(
            accounts.retrieve_spend_limits,
        )


class AsyncAccountsWithStreamingResponse:
    def __init__(self, accounts: AsyncAccounts) -> None:
        self._accounts = accounts

        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )
        self.retrieve_spend_limits = async_to_streamed_response_wrapper(
            accounts.retrieve_spend_limits,
        )
