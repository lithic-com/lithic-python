# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from ..types import (
    AuthRule,
    AuthRuleApplyResponse,
    AuthRuleCreateResponse,
    AuthRuleRemoveResponse,
    AuthRuleUpdateResponse,
    AuthRuleRetrieveResponse,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["AuthRules", "AsyncAuthRules"]


class AuthRules(SyncAPIResource):
    def create(
        self,
        *,
        allowed_mcc: List[str] | NotGiven = NOT_GIVEN,
        blocked_mcc: List[str] | NotGiven = NOT_GIVEN,
        allowed_countries: List[str] | NotGiven = NOT_GIVEN,
        blocked_countries: List[str] | NotGiven = NOT_GIVEN,
        avs_type: Literal["ZIP_ONLY"] | NotGiven = NOT_GIVEN,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AuthRuleCreateResponse:
        """
        Creates an authorization rule (Auth Rule) and applies it at the program,
        account, or card level.

        Args:
          allowed_mcc: Merchant category codes for which the Auth Rule permits transactions.

          blocked_mcc: Merchant category codes for which the Auth Rule automatically declines
              transactions.

          allowed_countries: Countries in which the Auth Rule permits transactions. Note that Lithic
              maintains a list of countries in which all transactions are blocked; "allowing"
              those countries in an Auth Rule does not override the Lithic-wide restrictions.

          blocked_countries: Countries in which the Auth Rule automatically declines transactions.

          avs_type: Address verification to confirm that postal code entered at point of transaction
              (if applicable) matches the postal code on file for a given card. Since this
              check is performed against the address submitted via the Enroll Consumer
              endpoint, it should only be used in cases where card users are enrolled with
              their own accounts. Available values:

              - `ZIP_ONLY` - AVS check is performed to confirm ZIP code entered at point of
                transaction (if applicable) matches address on file.

          account_tokens: Array of account_token(s) identifying the accounts that the Auth Rule applies
              to. Note that only this field or `card_tokens` can be provided for a given Auth
              Rule.

          card_tokens: Array of card_token(s) identifying the cards that the Auth Rule applies to. Note
              that only this field or `account_tokens` can be provided for a given Auth Rule.

          program_level: Boolean indicating whether the Auth Rule is applied at the program level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/auth_rules",
            body={
                "allowed_mcc": allowed_mcc,
                "blocked_mcc": blocked_mcc,
                "allowed_countries": allowed_countries,
                "blocked_countries": blocked_countries,
                "avs_type": avs_type,
                "account_tokens": account_tokens,
                "card_tokens": card_tokens,
                "program_level": program_level,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AuthRuleCreateResponse,
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
    ) -> AuthRuleRetrieveResponse:
        """
        Detail the properties and entities (program, accounts, and cards) associated
        with an existing authorization rule (Auth Rule).
        """
        return self._get(
            f"/auth_rules/{auth_rule_token}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AuthRuleRetrieveResponse,
        )

    def update(
        self,
        auth_rule_token: str,
        *,
        allowed_mcc: List[str] | NotGiven = NOT_GIVEN,
        blocked_mcc: List[str] | NotGiven = NOT_GIVEN,
        allowed_countries: List[str] | NotGiven = NOT_GIVEN,
        blocked_countries: List[str] | NotGiven = NOT_GIVEN,
        avs_type: Literal["ZIP_ONLY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AuthRuleUpdateResponse:
        """
        Update the properties associated with an existing authorization rule (Auth
        Rule).

        Args:
          allowed_mcc: Array of merchant category codes for which the Auth Rule will permit
              transactions. Note that only this field or `blocked_mcc` can be used for a given
              Auth Rule.

          blocked_mcc: Array of merchant category codes for which the Auth Rule will automatically
              decline transactions. Note that only this field or `allowed_mcc` can be used for
              a given Auth Rule.

          allowed_countries: Array of country codes for which the Auth Rule will permit transactions. Note
              that only this field or `blocked_countries` can be used for a given Auth Rule.

          blocked_countries: Array of country codes for which the Auth Rule will automatically decline
              transactions. Note that only this field or `allowed_countries` can be used for a
              given Auth Rule.

          avs_type: Address verification to confirm that postal code entered at point of transaction
              (if applicable) matches the postal code on file for a given card.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._put(
            f"/auth_rules/{auth_rule_token}",
            body={
                "allowed_mcc": allowed_mcc,
                "blocked_mcc": blocked_mcc,
                "allowed_countries": allowed_countries,
                "blocked_countries": blocked_countries,
                "avs_type": avs_type,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AuthRuleUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[AuthRule]:
        """
        Return all of the Auth Rules under the program.

        Args:
          page: Page (for pagination).

          page_size: Page size (for pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/auth_rules",
            page=SyncPage[AuthRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "page": page,
                    "page_size": page_size,
                },
            ),
            model=AuthRule,
        )

    def apply(
        self,
        auth_rule_token: str,
        *,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AuthRuleApplyResponse:
        """
        Applies an existing authorization rule (Auth Rule) to an program, account, or
        card level.

        Args:
          card_tokens: Array of card_token(s) identifying the cards that the Auth Rule applies to. Note
              that only this field or `account_tokens` can be provided for a given Auth Rule.

          account_tokens: Array of account_token(s) identifying the accounts that the Auth Rule applies
              to. Note that only this field or `card_tokens` can be provided for a given Auth
              Rule.

          program_level: Boolean indicating whether the Auth Rule is applied at the program level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            f"/auth_rules/{auth_rule_token}/apply",
            body={
                "card_tokens": card_tokens,
                "account_tokens": account_tokens,
                "program_level": program_level,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AuthRuleApplyResponse,
        )

    def remove(
        self,
        *,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AuthRuleRemoveResponse:
        """
        Remove an existing authorization rule (Auth Rule) from an program, account, or
        card-level.

        Args:
          card_tokens: Array of card_token(s) identifying the cards that the Auth Rule applies to. Note
              that only this field or `account_tokens` can be provided for a given Auth Rule.

          account_tokens: Array of account_token(s) identifying the accounts that the Auth Rule applies
              to. Note that only this field or `card_tokens` can be provided for a given Auth
              Rule.

          program_level: Boolean indicating whether the Auth Rule is applied at the program level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._delete(
            "/auth_rules/remove",
            body={
                "card_tokens": card_tokens,
                "account_tokens": account_tokens,
                "program_level": program_level,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AuthRuleRemoveResponse,
        )


class AsyncAuthRules(AsyncAPIResource):
    async def create(
        self,
        *,
        allowed_mcc: List[str] | NotGiven = NOT_GIVEN,
        blocked_mcc: List[str] | NotGiven = NOT_GIVEN,
        allowed_countries: List[str] | NotGiven = NOT_GIVEN,
        blocked_countries: List[str] | NotGiven = NOT_GIVEN,
        avs_type: Literal["ZIP_ONLY"] | NotGiven = NOT_GIVEN,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AuthRuleCreateResponse:
        """
        Creates an authorization rule (Auth Rule) and applies it at the program,
        account, or card level.

        Args:
          allowed_mcc: Merchant category codes for which the Auth Rule permits transactions.

          blocked_mcc: Merchant category codes for which the Auth Rule automatically declines
              transactions.

          allowed_countries: Countries in which the Auth Rule permits transactions. Note that Lithic
              maintains a list of countries in which all transactions are blocked; "allowing"
              those countries in an Auth Rule does not override the Lithic-wide restrictions.

          blocked_countries: Countries in which the Auth Rule automatically declines transactions.

          avs_type: Address verification to confirm that postal code entered at point of transaction
              (if applicable) matches the postal code on file for a given card. Since this
              check is performed against the address submitted via the Enroll Consumer
              endpoint, it should only be used in cases where card users are enrolled with
              their own accounts. Available values:

              - `ZIP_ONLY` - AVS check is performed to confirm ZIP code entered at point of
                transaction (if applicable) matches address on file.

          account_tokens: Array of account_token(s) identifying the accounts that the Auth Rule applies
              to. Note that only this field or `card_tokens` can be provided for a given Auth
              Rule.

          card_tokens: Array of card_token(s) identifying the cards that the Auth Rule applies to. Note
              that only this field or `account_tokens` can be provided for a given Auth Rule.

          program_level: Boolean indicating whether the Auth Rule is applied at the program level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/auth_rules",
            body={
                "allowed_mcc": allowed_mcc,
                "blocked_mcc": blocked_mcc,
                "allowed_countries": allowed_countries,
                "blocked_countries": blocked_countries,
                "avs_type": avs_type,
                "account_tokens": account_tokens,
                "card_tokens": card_tokens,
                "program_level": program_level,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AuthRuleCreateResponse,
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
    ) -> AuthRuleRetrieveResponse:
        """
        Detail the properties and entities (program, accounts, and cards) associated
        with an existing authorization rule (Auth Rule).
        """
        return await self._get(
            f"/auth_rules/{auth_rule_token}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AuthRuleRetrieveResponse,
        )

    async def update(
        self,
        auth_rule_token: str,
        *,
        allowed_mcc: List[str] | NotGiven = NOT_GIVEN,
        blocked_mcc: List[str] | NotGiven = NOT_GIVEN,
        allowed_countries: List[str] | NotGiven = NOT_GIVEN,
        blocked_countries: List[str] | NotGiven = NOT_GIVEN,
        avs_type: Literal["ZIP_ONLY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AuthRuleUpdateResponse:
        """
        Update the properties associated with an existing authorization rule (Auth
        Rule).

        Args:
          allowed_mcc: Array of merchant category codes for which the Auth Rule will permit
              transactions. Note that only this field or `blocked_mcc` can be used for a given
              Auth Rule.

          blocked_mcc: Array of merchant category codes for which the Auth Rule will automatically
              decline transactions. Note that only this field or `allowed_mcc` can be used for
              a given Auth Rule.

          allowed_countries: Array of country codes for which the Auth Rule will permit transactions. Note
              that only this field or `blocked_countries` can be used for a given Auth Rule.

          blocked_countries: Array of country codes for which the Auth Rule will automatically decline
              transactions. Note that only this field or `allowed_countries` can be used for a
              given Auth Rule.

          avs_type: Address verification to confirm that postal code entered at point of transaction
              (if applicable) matches the postal code on file for a given card.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._put(
            f"/auth_rules/{auth_rule_token}",
            body={
                "allowed_mcc": allowed_mcc,
                "blocked_mcc": blocked_mcc,
                "allowed_countries": allowed_countries,
                "blocked_countries": blocked_countries,
                "avs_type": avs_type,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AuthRuleUpdateResponse,
        )

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[AuthRule, AsyncPage[AuthRule]]:
        """
        Return all of the Auth Rules under the program.

        Args:
          page: Page (for pagination).

          page_size: Page size (for pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/auth_rules",
            page=AsyncPage[AuthRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "page": page,
                    "page_size": page_size,
                },
            ),
            model=AuthRule,
        )

    async def apply(
        self,
        auth_rule_token: str,
        *,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AuthRuleApplyResponse:
        """
        Applies an existing authorization rule (Auth Rule) to an program, account, or
        card level.

        Args:
          card_tokens: Array of card_token(s) identifying the cards that the Auth Rule applies to. Note
              that only this field or `account_tokens` can be provided for a given Auth Rule.

          account_tokens: Array of account_token(s) identifying the accounts that the Auth Rule applies
              to. Note that only this field or `card_tokens` can be provided for a given Auth
              Rule.

          program_level: Boolean indicating whether the Auth Rule is applied at the program level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            f"/auth_rules/{auth_rule_token}/apply",
            body={
                "card_tokens": card_tokens,
                "account_tokens": account_tokens,
                "program_level": program_level,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AuthRuleApplyResponse,
        )

    async def remove(
        self,
        *,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AuthRuleRemoveResponse:
        """
        Remove an existing authorization rule (Auth Rule) from an program, account, or
        card-level.

        Args:
          card_tokens: Array of card_token(s) identifying the cards that the Auth Rule applies to. Note
              that only this field or `account_tokens` can be provided for a given Auth Rule.

          account_tokens: Array of account_token(s) identifying the accounts that the Auth Rule applies
              to. Note that only this field or `card_tokens` can be provided for a given Auth
              Rule.

          program_level: Boolean indicating whether the Auth Rule is applied at the program level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._delete(
            "/auth_rules/remove",
            body={
                "card_tokens": card_tokens,
                "account_tokens": account_tokens,
                "program_level": program_level,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AuthRuleRemoveResponse,
        )
