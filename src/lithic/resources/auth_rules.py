# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from .. import _legacy_response
from ..types import (
    auth_rule_list_params,
    auth_rule_apply_params,
    auth_rule_create_params,
    auth_rule_remove_params,
    auth_rule_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ..types.auth_rule import AuthRule
from ..types.auth_rule_remove_response import AuthRuleRemoveResponse
from ..types.auth_rule_retrieve_response import AuthRuleRetrieveResponse

__all__ = ["AuthRules", "AsyncAuthRules"]


class AuthRules(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthRulesWithRawResponse:
        return AuthRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthRulesWithStreamingResponse:
        return AuthRulesWithStreamingResponse(self)

    def create(
        self,
        *,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        allowed_countries: List[str] | NotGiven = NOT_GIVEN,
        allowed_mcc: List[str] | NotGiven = NOT_GIVEN,
        blocked_countries: List[str] | NotGiven = NOT_GIVEN,
        blocked_mcc: List[str] | NotGiven = NOT_GIVEN,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRule:
        """
        Creates an authorization rule (Auth Rule) and applies it at the program,
        account, or card level.

        Args:
          account_tokens: Array of account_token(s) identifying the accounts that the Auth Rule applies
              to. Note that only this field or `card_tokens` can be provided for a given Auth
              Rule.

          allowed_countries: Countries in which the Auth Rule permits transactions. Note that Lithic
              maintains a list of countries in which all transactions are blocked; "allowing"
              those countries in an Auth Rule does not override the Lithic-wide restrictions.

          allowed_mcc: Merchant category codes for which the Auth Rule permits transactions.

          blocked_countries: Countries in which the Auth Rule automatically declines transactions.

          blocked_mcc: Merchant category codes for which the Auth Rule automatically declines
              transactions.

          card_tokens: Array of card_token(s) identifying the cards that the Auth Rule applies to. Note
              that only this field or `account_tokens` can be provided for a given Auth Rule.

          program_level: Boolean indicating whether the Auth Rule is applied at the program level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth_rules",
            body=maybe_transform(
                {
                    "account_tokens": account_tokens,
                    "allowed_countries": allowed_countries,
                    "allowed_mcc": allowed_mcc,
                    "blocked_countries": blocked_countries,
                    "blocked_mcc": blocked_mcc,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                },
                auth_rule_create_params.AuthRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthRule,
        )

    def retrieve(
        self,
        auth_rule_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRuleRetrieveResponse:
        """
        Detail the properties and entities (program, accounts, and cards) associated
        with an existing authorization rule (Auth Rule).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._get(
            f"/auth_rules/{auth_rule_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthRuleRetrieveResponse,
        )

    def update(
        self,
        auth_rule_token: str,
        *,
        allowed_countries: List[str] | NotGiven = NOT_GIVEN,
        allowed_mcc: List[str] | NotGiven = NOT_GIVEN,
        blocked_countries: List[str] | NotGiven = NOT_GIVEN,
        blocked_mcc: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRule:
        """
        Update the properties associated with an existing authorization rule (Auth
        Rule).

        Args:
          allowed_countries: Array of country codes for which the Auth Rule will permit transactions. Note
              that only this field or `blocked_countries` can be used for a given Auth Rule.

          allowed_mcc: Array of merchant category codes for which the Auth Rule will permit
              transactions. Note that only this field or `blocked_mcc` can be used for a given
              Auth Rule.

          blocked_countries: Array of country codes for which the Auth Rule will automatically decline
              transactions. Note that only this field or `allowed_countries` can be used for a
              given Auth Rule.

          blocked_mcc: Array of merchant category codes for which the Auth Rule will automatically
              decline transactions. Note that only this field or `allowed_mcc` can be used for
              a given Auth Rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._put(
            f"/auth_rules/{auth_rule_token}",
            body=maybe_transform(
                {
                    "allowed_countries": allowed_countries,
                    "allowed_mcc": allowed_mcc,
                    "blocked_countries": blocked_countries,
                    "blocked_mcc": blocked_mcc,
                },
                auth_rule_update_params.AuthRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthRule,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[AuthRule]:
        """
        Return all of the Auth Rules under the program.

        Args:
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
            "/auth_rules",
            page=SyncCursorPage[AuthRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    auth_rule_list_params.AuthRuleListParams,
                ),
            ),
            model=AuthRule,
        )

    def apply(
        self,
        auth_rule_token: str,
        *,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRule:
        """
        Applies an existing authorization rule (Auth Rule) to an program, account, or
        card level.

        Args:
          account_tokens: Array of account_token(s) identifying the accounts that the Auth Rule applies
              to. Note that only this field or `card_tokens` can be provided for a given Auth
              Rule.

          card_tokens: Array of card_token(s) identifying the cards that the Auth Rule applies to. Note
              that only this field or `account_tokens` can be provided for a given Auth Rule.

          program_level: Boolean indicating whether the Auth Rule is applied at the program level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._post(
            f"/auth_rules/{auth_rule_token}/apply",
            body=maybe_transform(
                {
                    "account_tokens": account_tokens,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                },
                auth_rule_apply_params.AuthRuleApplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthRule,
        )

    def remove(
        self,
        *,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRuleRemoveResponse:
        """
        Remove an existing authorization rule (Auth Rule) from an program, account, or
        card-level.

        Args:
          account_tokens: Array of account_token(s) identifying the accounts that the Auth Rule applies
              to. Note that only this field or `card_tokens` can be provided for a given Auth
              Rule.

          card_tokens: Array of card_token(s) identifying the cards that the Auth Rule applies to. Note
              that only this field or `account_tokens` can be provided for a given Auth Rule.

          program_level: Boolean indicating whether the Auth Rule is applied at the program level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/auth_rules/remove",
            body=maybe_transform(
                {
                    "account_tokens": account_tokens,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                },
                auth_rule_remove_params.AuthRuleRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthRuleRemoveResponse,
        )


class AsyncAuthRules(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthRulesWithRawResponse:
        return AsyncAuthRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthRulesWithStreamingResponse:
        return AsyncAuthRulesWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        allowed_countries: List[str] | NotGiven = NOT_GIVEN,
        allowed_mcc: List[str] | NotGiven = NOT_GIVEN,
        blocked_countries: List[str] | NotGiven = NOT_GIVEN,
        blocked_mcc: List[str] | NotGiven = NOT_GIVEN,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRule:
        """
        Creates an authorization rule (Auth Rule) and applies it at the program,
        account, or card level.

        Args:
          account_tokens: Array of account_token(s) identifying the accounts that the Auth Rule applies
              to. Note that only this field or `card_tokens` can be provided for a given Auth
              Rule.

          allowed_countries: Countries in which the Auth Rule permits transactions. Note that Lithic
              maintains a list of countries in which all transactions are blocked; "allowing"
              those countries in an Auth Rule does not override the Lithic-wide restrictions.

          allowed_mcc: Merchant category codes for which the Auth Rule permits transactions.

          blocked_countries: Countries in which the Auth Rule automatically declines transactions.

          blocked_mcc: Merchant category codes for which the Auth Rule automatically declines
              transactions.

          card_tokens: Array of card_token(s) identifying the cards that the Auth Rule applies to. Note
              that only this field or `account_tokens` can be provided for a given Auth Rule.

          program_level: Boolean indicating whether the Auth Rule is applied at the program level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth_rules",
            body=await async_maybe_transform(
                {
                    "account_tokens": account_tokens,
                    "allowed_countries": allowed_countries,
                    "allowed_mcc": allowed_mcc,
                    "blocked_countries": blocked_countries,
                    "blocked_mcc": blocked_mcc,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                },
                auth_rule_create_params.AuthRuleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthRule,
        )

    async def retrieve(
        self,
        auth_rule_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRuleRetrieveResponse:
        """
        Detail the properties and entities (program, accounts, and cards) associated
        with an existing authorization rule (Auth Rule).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._get(
            f"/auth_rules/{auth_rule_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthRuleRetrieveResponse,
        )

    async def update(
        self,
        auth_rule_token: str,
        *,
        allowed_countries: List[str] | NotGiven = NOT_GIVEN,
        allowed_mcc: List[str] | NotGiven = NOT_GIVEN,
        blocked_countries: List[str] | NotGiven = NOT_GIVEN,
        blocked_mcc: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRule:
        """
        Update the properties associated with an existing authorization rule (Auth
        Rule).

        Args:
          allowed_countries: Array of country codes for which the Auth Rule will permit transactions. Note
              that only this field or `blocked_countries` can be used for a given Auth Rule.

          allowed_mcc: Array of merchant category codes for which the Auth Rule will permit
              transactions. Note that only this field or `blocked_mcc` can be used for a given
              Auth Rule.

          blocked_countries: Array of country codes for which the Auth Rule will automatically decline
              transactions. Note that only this field or `allowed_countries` can be used for a
              given Auth Rule.

          blocked_mcc: Array of merchant category codes for which the Auth Rule will automatically
              decline transactions. Note that only this field or `allowed_mcc` can be used for
              a given Auth Rule.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._put(
            f"/auth_rules/{auth_rule_token}",
            body=await async_maybe_transform(
                {
                    "allowed_countries": allowed_countries,
                    "allowed_mcc": allowed_mcc,
                    "blocked_countries": blocked_countries,
                    "blocked_mcc": blocked_mcc,
                },
                auth_rule_update_params.AuthRuleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthRule,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AuthRule, AsyncCursorPage[AuthRule]]:
        """
        Return all of the Auth Rules under the program.

        Args:
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
            "/auth_rules",
            page=AsyncCursorPage[AuthRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    auth_rule_list_params.AuthRuleListParams,
                ),
            ),
            model=AuthRule,
        )

    async def apply(
        self,
        auth_rule_token: str,
        *,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRule:
        """
        Applies an existing authorization rule (Auth Rule) to an program, account, or
        card level.

        Args:
          account_tokens: Array of account_token(s) identifying the accounts that the Auth Rule applies
              to. Note that only this field or `card_tokens` can be provided for a given Auth
              Rule.

          card_tokens: Array of card_token(s) identifying the cards that the Auth Rule applies to. Note
              that only this field or `account_tokens` can be provided for a given Auth Rule.

          program_level: Boolean indicating whether the Auth Rule is applied at the program level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._post(
            f"/auth_rules/{auth_rule_token}/apply",
            body=await async_maybe_transform(
                {
                    "account_tokens": account_tokens,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                },
                auth_rule_apply_params.AuthRuleApplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthRule,
        )

    async def remove(
        self,
        *,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthRuleRemoveResponse:
        """
        Remove an existing authorization rule (Auth Rule) from an program, account, or
        card-level.

        Args:
          account_tokens: Array of account_token(s) identifying the accounts that the Auth Rule applies
              to. Note that only this field or `card_tokens` can be provided for a given Auth
              Rule.

          card_tokens: Array of card_token(s) identifying the cards that the Auth Rule applies to. Note
              that only this field or `account_tokens` can be provided for a given Auth Rule.

          program_level: Boolean indicating whether the Auth Rule is applied at the program level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/auth_rules/remove",
            body=await async_maybe_transform(
                {
                    "account_tokens": account_tokens,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                },
                auth_rule_remove_params.AuthRuleRemoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthRuleRemoveResponse,
        )


class AuthRulesWithRawResponse:
    def __init__(self, auth_rules: AuthRules) -> None:
        self._auth_rules = auth_rules

        self.create = _legacy_response.to_raw_response_wrapper(
            auth_rules.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            auth_rules.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            auth_rules.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            auth_rules.list,
        )
        self.apply = _legacy_response.to_raw_response_wrapper(
            auth_rules.apply,
        )
        self.remove = _legacy_response.to_raw_response_wrapper(
            auth_rules.remove,
        )


class AsyncAuthRulesWithRawResponse:
    def __init__(self, auth_rules: AsyncAuthRules) -> None:
        self._auth_rules = auth_rules

        self.create = _legacy_response.async_to_raw_response_wrapper(
            auth_rules.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            auth_rules.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            auth_rules.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            auth_rules.list,
        )
        self.apply = _legacy_response.async_to_raw_response_wrapper(
            auth_rules.apply,
        )
        self.remove = _legacy_response.async_to_raw_response_wrapper(
            auth_rules.remove,
        )


class AuthRulesWithStreamingResponse:
    def __init__(self, auth_rules: AuthRules) -> None:
        self._auth_rules = auth_rules

        self.create = to_streamed_response_wrapper(
            auth_rules.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            auth_rules.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            auth_rules.update,
        )
        self.list = to_streamed_response_wrapper(
            auth_rules.list,
        )
        self.apply = to_streamed_response_wrapper(
            auth_rules.apply,
        )
        self.remove = to_streamed_response_wrapper(
            auth_rules.remove,
        )


class AsyncAuthRulesWithStreamingResponse:
    def __init__(self, auth_rules: AsyncAuthRules) -> None:
        self._auth_rules = auth_rules

        self.create = async_to_streamed_response_wrapper(
            auth_rules.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            auth_rules.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            auth_rules.update,
        )
        self.list = async_to_streamed_response_wrapper(
            auth_rules.list,
        )
        self.apply = async_to_streamed_response_wrapper(
            auth_rules.apply,
        )
        self.remove = async_to_streamed_response_wrapper(
            auth_rules.remove,
        )
