# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage
from lithic.types.auth_rule_apply_response import AuthRuleApplyResponse
from lithic.types.auth_rule_create_response import AuthRuleCreateResponse
from lithic.types.auth_rule_remove_response import AuthRuleRemoveResponse
from lithic.types.auth_rule_update_response import AuthRuleUpdateResponse
from lithic.types.auth_rule_retrieve_response import AuthRuleRetrieveResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAuthRules:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        resource = client.auth_rules.create()
        assert isinstance(resource, AuthRuleCreateResponse)

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        resource = client.auth_rules.create(
            allowed_mcc=["string", "string", "string"],
            blocked_mcc=["string", "string", "string"],
            allowed_countries=["string", "string", "string"],
            blocked_countries=["string", "string", "string"],
            avs_type="ZIP_ONLY",
            account_tokens=["string", "string", "string"],
            card_tokens=["string", "string", "string"],
            program_level=False,
        )
        assert isinstance(resource, AuthRuleCreateResponse)

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        resource = client.auth_rules.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AuthRuleRetrieveResponse)

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        resource = client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AuthRuleUpdateResponse)

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        resource = client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_mcc=["string", "string", "string"],
            blocked_mcc=["string", "string", "string"],
            allowed_countries=["string", "string", "string"],
            blocked_countries=["string", "string", "string"],
            avs_type="ZIP_ONLY",
        )
        assert isinstance(resource, AuthRuleUpdateResponse)

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        resource = client.auth_rules.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        resource = client.auth_rules.list(
            page=0,
            page_size=1,
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_apply(self, client: Lithic) -> None:
        resource = client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AuthRuleApplyResponse)

    @parametrize
    def test_method_apply_with_all_params(self, client: Lithic) -> None:
        resource = client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_tokens=["string", "string", "string"],
            account_tokens=["string", "string", "string"],
            program_level=True,
        )
        assert isinstance(resource, AuthRuleApplyResponse)

    @parametrize
    def test_method_remove(self, client: Lithic) -> None:
        resource = client.auth_rules.remove()
        assert isinstance(resource, AuthRuleRemoveResponse)

    @parametrize
    def test_method_remove_with_all_params(self, client: Lithic) -> None:
        resource = client.auth_rules.remove(
            card_tokens=["string", "string", "string"],
            account_tokens=["string", "string", "string"],
            program_level=True,
        )
        assert isinstance(resource, AuthRuleRemoveResponse)


class TestAsyncAuthRules:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncLithic) -> None:
        resource = await client.auth_rules.create()
        assert isinstance(resource, AuthRuleCreateResponse)

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncLithic) -> None:
        resource = await client.auth_rules.create(
            allowed_mcc=["string", "string", "string"],
            blocked_mcc=["string", "string", "string"],
            allowed_countries=["string", "string", "string"],
            blocked_countries=["string", "string", "string"],
            avs_type="ZIP_ONLY",
            account_tokens=["string", "string", "string"],
            card_tokens=["string", "string", "string"],
            program_level=False,
        )
        assert isinstance(resource, AuthRuleCreateResponse)

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        resource = await client.auth_rules.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AuthRuleRetrieveResponse)

    @parametrize
    async def test_method_update(self, client: AsyncLithic) -> None:
        resource = await client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AuthRuleUpdateResponse)

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncLithic) -> None:
        resource = await client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_mcc=["string", "string", "string"],
            blocked_mcc=["string", "string", "string"],
            allowed_countries=["string", "string", "string"],
            blocked_countries=["string", "string", "string"],
            avs_type="ZIP_ONLY",
        )
        assert isinstance(resource, AuthRuleUpdateResponse)

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        resource = await client.auth_rules.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        resource = await client.auth_rules.list(
            page=0,
            page_size=1,
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_apply(self, client: AsyncLithic) -> None:
        resource = await client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AuthRuleApplyResponse)

    @parametrize
    async def test_method_apply_with_all_params(self, client: AsyncLithic) -> None:
        resource = await client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_tokens=["string", "string", "string"],
            account_tokens=["string", "string", "string"],
            program_level=True,
        )
        assert isinstance(resource, AuthRuleApplyResponse)

    @parametrize
    async def test_method_remove(self, client: AsyncLithic) -> None:
        resource = await client.auth_rules.remove()
        assert isinstance(resource, AuthRuleRemoveResponse)

    @parametrize
    async def test_method_remove_with_all_params(self, client: AsyncLithic) -> None:
        resource = await client.auth_rules.remove(
            card_tokens=["string", "string", "string"],
            account_tokens=["string", "string", "string"],
            program_level=True,
        )
        assert isinstance(resource, AuthRuleRemoveResponse)
