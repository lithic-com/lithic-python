# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union, Optional

from .._types import Timeout, NotGiven
from .._models import NoneModel, StringModel
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import AsyncPaginator, make_request_options
from ..types.auth_rule import *
from ..types.auth_rule_list_params import *
from ..types.auth_rule_apply_params import *
from ..types.auth_rule_create_params import *
from ..types.auth_rule_list_response import *
from ..types.auth_rule_remove_params import *
from ..types.auth_rule_update_params import *
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
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthRuleCreateResponse:
        """
        Creates an authorization rule (Auth Rule) and applies it at the program,
        account, or card level.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post("/auth_rules", model=AuthRuleCreateResponse, body=body, options=options)

    def retrieve(
        self,
        id: str,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthRuleRetrieveResponse:
        """
        Detail the properties and entities (program, accounts, and cards) associated
        with an existing authorization rule (Auth Rule).
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._get(f"/auth_rules/{id}", model=AuthRuleRetrieveResponse, options=options)

    def update(
        self,
        id: str,
        body: AuthRuleUpdateParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthRuleUpdateResponse:
        """
        Update the properties associated with an existing authorization rule (Auth
        Rule).
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._put(f"/auth_rules/{id}", model=AuthRuleUpdateResponse, body=body, options=options)

    def list(
        self,
        query: AuthRuleListParams = {},
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthRuleListResponse:
        """Return all of the Auth Rules under the program."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get("/auth_rules", model=AuthRuleListResponse, query=query, options=options)

    def apply(
        self,
        id: str,
        body: AuthRuleApplyParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthRuleApplyResponse:
        """
        Applies an existing authorization rule (Auth Rule) to an program, account, or
        card level.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(f"/auth_rules/{id}/apply", model=AuthRuleApplyResponse, body=body, options=options)

    def remove(
        self,
        body: AuthRuleRemoveParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthRuleRemoveResponse:
        """
        Remove an existing authorization rule (Auth Rule) from an program, account, or
        card-level.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._delete("/auth_rules/remove", model=AuthRuleRemoveResponse, body=body, options=options)


class AsyncAuthRules(AsyncAPIResource):
    async def create(
        self,
        body: AuthRuleCreateParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthRuleCreateResponse:
        """
        Creates an authorization rule (Auth Rule) and applies it at the program,
        account, or card level.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post("/auth_rules", model=AuthRuleCreateResponse, body=body, options=options)

    async def retrieve(
        self,
        id: str,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthRuleRetrieveResponse:
        """
        Detail the properties and entities (program, accounts, and cards) associated
        with an existing authorization rule (Auth Rule).
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(f"/auth_rules/{id}", model=AuthRuleRetrieveResponse, options=options)

    async def update(
        self,
        id: str,
        body: AuthRuleUpdateParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthRuleUpdateResponse:
        """
        Update the properties associated with an existing authorization rule (Auth
        Rule).
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._put(f"/auth_rules/{id}", model=AuthRuleUpdateResponse, body=body, options=options)

    async def list(
        self,
        query: AuthRuleListParams = {},
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthRuleListResponse:
        """Return all of the Auth Rules under the program."""
        options = make_request_options(headers, max_retries, timeout)
        return await self._get("/auth_rules", model=AuthRuleListResponse, query=query, options=options)

    async def apply(
        self,
        id: str,
        body: AuthRuleApplyParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthRuleApplyResponse:
        """
        Applies an existing authorization rule (Auth Rule) to an program, account, or
        card level.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(f"/auth_rules/{id}/apply", model=AuthRuleApplyResponse, body=body, options=options)

    async def remove(
        self,
        body: AuthRuleRemoveParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthRuleRemoveResponse:
        """
        Remove an existing authorization rule (Auth Rule) from an program, account, or
        card-level.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._delete("/auth_rules/remove", model=AuthRuleRemoveResponse, body=body, options=options)
