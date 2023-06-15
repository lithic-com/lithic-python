# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    AuthRule,
    AuthRuleApplyResponse,
    AuthRuleCreateResponse,
    AuthRuleRemoveResponse,
    AuthRuleUpdateResponse,
    AuthRuleRetrieveResponse,
)
from lithic.pagination import SyncPage, AsyncPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAuthRules:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.create()
        assert_matches_type(AuthRuleCreateResponse, auth_rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.create(
            account_tokens=["string", "string", "string"],
            allowed_countries=["string", "string", "string"],
            allowed_mcc=["string", "string", "string"],
            blocked_countries=["string", "string", "string"],
            blocked_mcc=["string", "string", "string"],
            card_tokens=["string", "string", "string"],
            program_level=False,
        )
        assert_matches_type(AuthRuleCreateResponse, auth_rule, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRuleRetrieveResponse, auth_rule, path=["response"])

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRuleUpdateResponse, auth_rule, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_countries=["string", "string", "string"],
            allowed_mcc=["string", "string", "string"],
            blocked_countries=["string", "string", "string"],
            blocked_mcc=["string", "string", "string"],
        )
        assert_matches_type(AuthRuleUpdateResponse, auth_rule, path=["response"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.list()
        assert_matches_type(SyncPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.list(
            page=0,
            page_size=1,
        )
        assert_matches_type(SyncPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    def test_method_apply(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRuleApplyResponse, auth_rule, path=["response"])

    @parametrize
    def test_method_apply_with_all_params(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["string", "string", "string"],
            card_tokens=["string", "string", "string"],
            program_level=True,
        )
        assert_matches_type(AuthRuleApplyResponse, auth_rule, path=["response"])

    @parametrize
    def test_method_remove(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.remove()
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])

    @parametrize
    def test_method_remove_with_all_params(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.remove(
            account_tokens=["string", "string", "string"],
            card_tokens=["string", "string", "string"],
            program_level=True,
        )
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])


class TestAsyncAuthRules:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.create()
        assert_matches_type(AuthRuleCreateResponse, auth_rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.create(
            account_tokens=["string", "string", "string"],
            allowed_countries=["string", "string", "string"],
            allowed_mcc=["string", "string", "string"],
            blocked_countries=["string", "string", "string"],
            blocked_mcc=["string", "string", "string"],
            card_tokens=["string", "string", "string"],
            program_level=False,
        )
        assert_matches_type(AuthRuleCreateResponse, auth_rule, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRuleRetrieveResponse, auth_rule, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRuleUpdateResponse, auth_rule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_countries=["string", "string", "string"],
            allowed_mcc=["string", "string", "string"],
            blocked_countries=["string", "string", "string"],
            blocked_mcc=["string", "string", "string"],
        )
        assert_matches_type(AuthRuleUpdateResponse, auth_rule, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.list()
        assert_matches_type(AsyncPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.list(
            page=0,
            page_size=1,
        )
        assert_matches_type(AsyncPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    async def test_method_apply(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRuleApplyResponse, auth_rule, path=["response"])

    @parametrize
    async def test_method_apply_with_all_params(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["string", "string", "string"],
            card_tokens=["string", "string", "string"],
            program_level=True,
        )
        assert_matches_type(AuthRuleApplyResponse, auth_rule, path=["response"])

    @parametrize
    async def test_method_remove(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.remove()
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])

    @parametrize
    async def test_method_remove_with_all_params(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.remove(
            account_tokens=["string", "string", "string"],
            card_tokens=["string", "string", "string"],
            program_level=True,
        )
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])
