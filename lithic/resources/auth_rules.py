# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.auth_rule import *
from ..types.auth_rule_list_params import AuthRuleListParams
from ..types.auth_rule_apply_params import AuthRuleApplyParams
from ..types.auth_rule_create_params import AuthRuleCreateParams
from ..types.auth_rule_remove_params import AuthRuleRemoveParams
from ..types.auth_rule_update_params import AuthRuleUpdateParams
from ..types.auth_rule_apply_response import *
from ..types.auth_rule_create_response import *
from ..types.auth_rule_remove_response import *
from ..types.auth_rule_update_response import *
from ..types.auth_rule_retrieve_response import *

__all__ = ["AuthRules", "AsyncAuthRules"]


class AuthRules(SyncAPIResource):
    def create(
        self,
        body: AuthRuleCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AuthRuleCreateResponse:
        """
        Creates an authorization rule (Auth Rule) and applies it at the program,
        account, or card level.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/auth_rules",
            body=body,
            options=options,
            cast_to=AuthRuleCreateResponse,
        )

    def retrieve(
        self,
        auth_rule_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AuthRuleRetrieveResponse:
        """
        Detail the properties and entities (program, accounts, and cards) associated
        with an existing authorization rule (Auth Rule).
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/auth_rules/{auth_rule_token}",
            options=options,
            cast_to=AuthRuleRetrieveResponse,
        )

    def update(
        self,
        auth_rule_token: str,
        body: AuthRuleUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AuthRuleUpdateResponse:
        """
        Update the properties associated with an existing authorization rule (Auth
        Rule).
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._put(
            f"/auth_rules/{auth_rule_token}",
            body=body,
            options=options,
            cast_to=AuthRuleUpdateResponse,
        )

    def list(
        self,
        query: AuthRuleListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[AuthRule]:
        """Return all of the Auth Rules under the program."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/auth_rules",
            page=SyncPage[AuthRule],
            query=query,
            options=options,
            model=AuthRule,
        )

    def apply(
        self,
        auth_rule_token: str,
        body: AuthRuleApplyParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AuthRuleApplyResponse:
        """
        Applies an existing authorization rule (Auth Rule) to an program, account, or
        card level.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            f"/auth_rules/{auth_rule_token}/apply",
            body=body,
            options=options,
            cast_to=AuthRuleApplyResponse,
        )

    def remove(
        self,
        body: AuthRuleRemoveParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AuthRuleRemoveResponse:
        """
        Remove an existing authorization rule (Auth Rule) from an program, account, or
        card-level.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._delete(
            "/auth_rules/remove",
            body=body,
            options=options,
            cast_to=AuthRuleRemoveResponse,
        )


class AsyncAuthRules(AsyncAPIResource):
    async def create(
        self,
        body: AuthRuleCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AuthRuleCreateResponse:
        """
        Creates an authorization rule (Auth Rule) and applies it at the program,
        account, or card level.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/auth_rules",
            body=body,
            options=options,
            cast_to=AuthRuleCreateResponse,
        )

    async def retrieve(
        self,
        auth_rule_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AuthRuleRetrieveResponse:
        """
        Detail the properties and entities (program, accounts, and cards) associated
        with an existing authorization rule (Auth Rule).
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/auth_rules/{auth_rule_token}",
            options=options,
            cast_to=AuthRuleRetrieveResponse,
        )

    async def update(
        self,
        auth_rule_token: str,
        body: AuthRuleUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AuthRuleUpdateResponse:
        """
        Update the properties associated with an existing authorization rule (Auth
        Rule).
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._put(
            f"/auth_rules/{auth_rule_token}",
            body=body,
            options=options,
            cast_to=AuthRuleUpdateResponse,
        )

    def list(
        self,
        query: AuthRuleListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[AuthRule, AsyncPage[AuthRule]]:
        """Return all of the Auth Rules under the program."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/auth_rules",
            page=AsyncPage[AuthRule],
            query=query,
            options=options,
            model=AuthRule,
        )

    async def apply(
        self,
        auth_rule_token: str,
        body: AuthRuleApplyParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AuthRuleApplyResponse:
        """
        Applies an existing authorization rule (Auth Rule) to an program, account, or
        card level.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            f"/auth_rules/{auth_rule_token}/apply",
            body=body,
            options=options,
            cast_to=AuthRuleApplyResponse,
        )

    async def remove(
        self,
        body: AuthRuleRemoveParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AuthRuleRemoveResponse:
        """
        Remove an existing authorization rule (Auth Rule) from an program, account, or
        card-level.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._delete(
            "/auth_rules/remove",
            body=body,
            options=options,
            cast_to=AuthRuleRemoveResponse,
        )
