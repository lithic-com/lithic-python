# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Dict
from .._core import Timeout, make_request_options
from .._resource import SyncAPIResource, AsyncAPIResource
from .._models import StringModel, NoneModel
from ..pagination import SyncPage, AsyncPage
from ..types.auth_rule import *
from ..types.auth_rule_create_response import *
from ..types.auth_rule_retrieve_response import *
from ..types.auth_rule_update_response import *
from ..types.auth_rule_list_response import *
from ..types.auth_rule_apply_response import *
from ..types.auth_rule_remove_response import *
from ..types.auth_rule_create_params import *
from ..types.auth_rule_update_params import *
from ..types.auth_rule_list_params import *
from ..types.auth_rule_apply_params import *
from ..types.auth_rule_remove_params import *

__all__ = ["AuthRules", "AsyncAuthRules"]


class AuthRules(SyncAPIResource):
    def create(
        self,
        body: AuthRuleCreateParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AuthRuleCreateResponse:
        """Creates an authorization rule (Auth Rule) and applies it at the
        program, account, or card level."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.post("/auth_rules", model=AuthRuleCreateResponse, body=body, options=options)

    def retrieve(
        self,
        id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AuthRuleRetrieveResponse:
        """Detail the properties and entities (program, accounts, and cards)
        associated with an existing authorization rule (Auth Rule)."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.get(f"/auth_rules/{id}", model=AuthRuleRetrieveResponse, options=options)

    def update(
        self,
        id: str,
        body: AuthRuleUpdateParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AuthRuleUpdateResponse:
        """Update the properties associated with an existing authorization rule
        (Auth Rule)."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.put(f"/auth_rules/{id}", model=AuthRuleUpdateResponse, body=body, options=options)

    def list(
        self,
        query: Optional[AuthRuleListParams] = None,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AuthRuleListResponse:
        """Return all of the Auth Rules under the program."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.get("/auth_rules", model=AuthRuleListResponse, query=query, options=options)

    def apply(
        self,
        id: str,
        body: AuthRuleApplyParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AuthRuleApplyResponse:
        """Applies an existing authorization rule (Auth Rule) to an program,
        account, or card level."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.post(f"/auth_rules/{id}/apply", model=AuthRuleApplyResponse, body=body, options=options)

    def remove(
        self,
        body: AuthRuleRemoveParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AuthRuleRemoveResponse:
        """Remove an existing authorization rule (Auth Rule) from an program,
        account, or card-level."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.delete("/auth_rules/remove", model=AuthRuleRemoveResponse, body=body, options=options)


class AsyncAuthRules(AsyncAPIResource):
    async def create(
        self,
        body: AuthRuleCreateParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AuthRuleCreateResponse:
        """Creates an authorization rule (Auth Rule) and applies it at the
        program, account, or card level."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.post("/auth_rules", model=AuthRuleCreateResponse, body=body, options=options)

    async def retrieve(
        self,
        id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AuthRuleRetrieveResponse:
        """Detail the properties and entities (program, accounts, and cards)
        associated with an existing authorization rule (Auth Rule)."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.get(f"/auth_rules/{id}", model=AuthRuleRetrieveResponse, options=options)

    async def update(
        self,
        id: str,
        body: AuthRuleUpdateParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AuthRuleUpdateResponse:
        """Update the properties associated with an existing authorization rule
        (Auth Rule)."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.put(f"/auth_rules/{id}", model=AuthRuleUpdateResponse, body=body, options=options)

    async def list(
        self,
        query: Optional[AuthRuleListParams] = None,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AuthRuleListResponse:
        """Return all of the Auth Rules under the program."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.get("/auth_rules", model=AuthRuleListResponse, query=query, options=options)

    async def apply(
        self,
        id: str,
        body: AuthRuleApplyParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AuthRuleApplyResponse:
        """Applies an existing authorization rule (Auth Rule) to an program,
        account, or card level."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.post(f"/auth_rules/{id}/apply", model=AuthRuleApplyResponse, body=body, options=options)

    async def remove(
        self,
        body: AuthRuleRemoveParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AuthRuleRemoveResponse:
        """Remove an existing authorization rule (Auth Rule) from an program,
        account, or card-level."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.delete("/auth_rules/remove", model=AuthRuleRemoveResponse, body=body, options=options)
