# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import warnings
from typing import Any, List, Union, Optional, cast, overload
from typing_extensions import Literal

from .._types import NOT_GIVEN, Body, Query, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.auth_rule import AuthRule
from ..types.auth_rule_list_params import AuthRuleListParams
from ..types.auth_rule_apply_params import AuthRuleApplyParams
from ..types.auth_rule_create_params import AuthRuleCreateParams
from ..types.auth_rule_remove_params import AuthRuleRemoveParams
from ..types.auth_rule_update_params import AuthRuleUpdateParams
from ..types.auth_rule_apply_response import AuthRuleApplyResponse
from ..types.auth_rule_create_response import AuthRuleCreateResponse
from ..types.auth_rule_remove_response import AuthRuleRemoveResponse
from ..types.auth_rule_update_response import AuthRuleUpdateResponse
from ..types.auth_rule_retrieve_response import AuthRuleRetrieveResponse

__all__ = ["AuthRules", "AsyncAuthRules"]


class AuthRules(SyncAPIResource):
    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    def create(
        self,
        body: AuthRuleCreateParams,
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
    ) -> AuthRuleCreateResponse:
        """
        Creates an authorization rule (Auth Rule) and applies it at the program,
        account, or card level.
        """
        ...

    def create(
        self,
        body: AuthRuleCreateParams | None = None,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AuthRuleCreateResponse:
        """
        Creates an authorization rule (Auth Rule) and applies it at the program,
        account, or card level.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard AuthRuleCreateParams type.
            body = cast(
                Any,
                {
                    "allowed_mcc": allowed_mcc,
                    "blocked_mcc": blocked_mcc,
                    "allowed_countries": allowed_countries,
                    "blocked_countries": blocked_countries,
                    "avs_type": avs_type,
                    "account_tokens": account_tokens,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                },
            )

        return self._post(
            "/auth_rules",
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AuthRuleRetrieveResponse:
        """
        Detail the properties and entities (program, accounts, and cards) associated
        with an existing authorization rule (Auth Rule).
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return self._get(
            f"/auth_rules/{auth_rule_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=AuthRuleRetrieveResponse,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    def update(
        self,
        auth_rule_token: str,
        body: AuthRuleUpdateParams,
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
    ) -> AuthRuleUpdateResponse:
        """
        Update the properties associated with an existing authorization rule (Auth
        Rule).
        """
        ...

    def update(
        self,
        auth_rule_token: str,
        body: AuthRuleUpdateParams | None = None,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AuthRuleUpdateResponse:
        """
        Update the properties associated with an existing authorization rule (Auth
        Rule).

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard AuthRuleUpdateParams type.
            body = cast(
                Any,
                {
                    "allowed_mcc": allowed_mcc,
                    "blocked_mcc": blocked_mcc,
                    "allowed_countries": allowed_countries,
                    "blocked_countries": blocked_countries,
                    "avs_type": avs_type,
                },
            )

        return self._put(
            f"/auth_rules/{auth_rule_token}",
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
            cast_to=AuthRuleUpdateResponse,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        ...

    @overload
    def list(
        self,
        query: AuthRuleListParams = {},
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
    ) -> SyncPage[AuthRule]:
        """Return all of the Auth Rules under the program."""
        ...

    def list(
        self,
        query: AuthRuleListParams | None = None,
        *,
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
    ) -> SyncPage[AuthRule]:
        """
        Return all of the Auth Rules under the program.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard AuthRuleListParams type.
            query = cast(
                Any,
                {
                    "page": page,
                    "page_size": page_size,
                },
            )

        return self._get_api_list(
            "/auth_rules",
            page=SyncPage[AuthRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=AuthRule,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    def apply(
        self,
        auth_rule_token: str,
        body: AuthRuleApplyParams,
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
    ) -> AuthRuleApplyResponse:
        """
        Applies an existing authorization rule (Auth Rule) to an program, account, or
        card level.
        """
        ...

    def apply(
        self,
        auth_rule_token: str,
        body: AuthRuleApplyParams | None = None,
        *,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
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
    ) -> AuthRuleApplyResponse:
        """
        Applies an existing authorization rule (Auth Rule) to an program, account, or
        card level.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard AuthRuleApplyParams type.
            body = cast(
                Any,
                {
                    "card_tokens": card_tokens,
                    "account_tokens": account_tokens,
                    "program_level": program_level,
                },
            )

        return self._post(
            f"/auth_rules/{auth_rule_token}/apply",
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
            cast_to=AuthRuleApplyResponse,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    def remove(
        self,
        body: AuthRuleRemoveParams,
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
    ) -> AuthRuleRemoveResponse:
        """
        Remove an existing authorization rule (Auth Rule) from an program, account, or
        card-level.
        """
        ...

    def remove(
        self,
        body: AuthRuleRemoveParams | None = None,
        *,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
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
    ) -> AuthRuleRemoveResponse:
        """
        Remove an existing authorization rule (Auth Rule) from an program, account, or
        card-level.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard AuthRuleRemoveParams type.
            body = cast(
                Any,
                {
                    "card_tokens": card_tokens,
                    "account_tokens": account_tokens,
                    "program_level": program_level,
                },
            )

        return self._delete(
            "/auth_rules/remove",
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
            cast_to=AuthRuleRemoveResponse,
        )


class AsyncAuthRules(AsyncAPIResource):
    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    async def create(
        self,
        body: AuthRuleCreateParams,
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
    ) -> AuthRuleCreateResponse:
        """
        Creates an authorization rule (Auth Rule) and applies it at the program,
        account, or card level.
        """
        ...

    async def create(
        self,
        body: AuthRuleCreateParams | None = None,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AuthRuleCreateResponse:
        """
        Creates an authorization rule (Auth Rule) and applies it at the program,
        account, or card level.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard AuthRuleCreateParams type.
            body = cast(
                Any,
                {
                    "allowed_mcc": allowed_mcc,
                    "blocked_mcc": blocked_mcc,
                    "allowed_countries": allowed_countries,
                    "blocked_countries": blocked_countries,
                    "avs_type": avs_type,
                    "account_tokens": account_tokens,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                },
            )

        return await self._post(
            "/auth_rules",
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AuthRuleRetrieveResponse:
        """
        Detail the properties and entities (program, accounts, and cards) associated
        with an existing authorization rule (Auth Rule).
        """
        if query is not None:
            warnings.warn(
                "The `query` argument is deprecated. Please use `extra_query` instead",
                DeprecationWarning,
                stacklevel=3,
            )

        return await self._get(
            f"/auth_rules/{auth_rule_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            cast_to=AuthRuleRetrieveResponse,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    async def update(
        self,
        auth_rule_token: str,
        body: AuthRuleUpdateParams,
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
    ) -> AuthRuleUpdateResponse:
        """
        Update the properties associated with an existing authorization rule (Auth
        Rule).
        """
        ...

    async def update(
        self,
        auth_rule_token: str,
        body: AuthRuleUpdateParams | None = None,
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
    ) -> AuthRuleUpdateResponse:
        """
        Update the properties associated with an existing authorization rule (Auth
        Rule).

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard AuthRuleUpdateParams type.
            body = cast(
                Any,
                {
                    "allowed_mcc": allowed_mcc,
                    "blocked_mcc": blocked_mcc,
                    "allowed_countries": allowed_countries,
                    "blocked_countries": blocked_countries,
                    "avs_type": avs_type,
                },
            )

        return await self._put(
            f"/auth_rules/{auth_rule_token}",
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
            cast_to=AuthRuleUpdateResponse,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        ...

    @overload
    def list(
        self,
        query: AuthRuleListParams = {},
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
    ) -> AsyncPaginator[AuthRule, AsyncPage[AuthRule]]:
        """Return all of the Auth Rules under the program."""
        ...

    def list(
        self,
        query: AuthRuleListParams | None = None,
        *,
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
    ) -> AsyncPaginator[AuthRule, AsyncPage[AuthRule]]:
        """
        Return all of the Auth Rules under the program.

        Args:
          query: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard AuthRuleListParams type.
            query = cast(
                Any,
                {
                    "page": page,
                    "page_size": page_size,
                },
            )

        return self._get_api_list(
            "/auth_rules",
            page=AsyncPage[AuthRule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                headers=headers,
                max_retries=max_retries,
                timeout=timeout,
                query=query,
            ),
            model=AuthRule,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    async def apply(
        self,
        auth_rule_token: str,
        body: AuthRuleApplyParams,
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
    ) -> AuthRuleApplyResponse:
        """
        Applies an existing authorization rule (Auth Rule) to an program, account, or
        card level.
        """
        ...

    async def apply(
        self,
        auth_rule_token: str,
        body: AuthRuleApplyParams | None = None,
        *,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
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
    ) -> AuthRuleApplyResponse:
        """
        Applies an existing authorization rule (Auth Rule) to an program, account, or
        card level.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard AuthRuleApplyParams type.
            body = cast(
                Any,
                {
                    "card_tokens": card_tokens,
                    "account_tokens": account_tokens,
                    "program_level": program_level,
                },
            )

        return await self._post(
            f"/auth_rules/{auth_rule_token}/apply",
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
            cast_to=AuthRuleApplyResponse,
        )

    @overload
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
        # deprecated options params
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        query: Optional[Query] = None,
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
        ...

    @overload
    async def remove(
        self,
        body: AuthRuleRemoveParams,
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
    ) -> AuthRuleRemoveResponse:
        """
        Remove an existing authorization rule (Auth Rule) from an program, account, or
        card-level.
        """
        ...

    async def remove(
        self,
        body: AuthRuleRemoveParams | None = None,
        *,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
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
    ) -> AuthRuleRemoveResponse:
        """
        Remove an existing authorization rule (Auth Rule) from an program, account, or
        card-level.

        Args:
          body: Deprecated TypedDict parameter, this is being replaced with explicit kwargs
              instead.

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
            # with the standard AuthRuleRemoveParams type.
            body = cast(
                Any,
                {
                    "card_tokens": card_tokens,
                    "account_tokens": account_tokens,
                    "program_level": program_level,
                },
            )

        return await self._delete(
            "/auth_rules/remove",
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
            cast_to=AuthRuleRemoveResponse,
        )
