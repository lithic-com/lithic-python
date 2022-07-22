# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage
from lithic.types.auth_rule import *
from lithic.types.auth_rule_apply_response import *
from lithic.types.auth_rule_create_response import *
from lithic.types.auth_rule_remove_response import *
from lithic.types.auth_rule_update_response import *
from lithic.types.auth_rule_retrieve_response import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAuthRules:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.auth_rules.create(
            {},
        )
        assert isinstance(resource, AuthRuleCreateResponse)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.auth_rules.create(
            {
                "allowed_mcc": ["string", "string", "string"],
                "blocked_mcc": ["string", "string", "string"],
                "allowed_countries": ["string", "string", "string"],
                "blocked_countries": ["string", "string", "string"],
                "avs_type": "ZIP_ONLY",
                "account_tokens": ["string", "string", "string"],
                "card_tokens": ["string", "string", "string"],
                "program_level": False,
            },
        )
        assert isinstance(resource, AuthRuleCreateResponse)

    def test_method_retrieve(self) -> None:
        resource = self.client.auth_rules.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AuthRuleRetrieveResponse)

    def test_method_update(self) -> None:
        resource = self.client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, AuthRuleUpdateResponse)

    def test_method_update_with_optional_params(self) -> None:
        resource = self.client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "allowed_mcc": ["string", "string", "string"],
                "blocked_mcc": ["string", "string", "string"],
                "allowed_countries": ["string", "string", "string"],
                "blocked_countries": ["string", "string", "string"],
                "avs_type": "ZIP_ONLY",
            },
        )
        assert isinstance(resource, AuthRuleUpdateResponse)

    def test_method_list(self) -> None:
        resource = self.client.auth_rules.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.auth_rules.list(
            {
                "page": 0,
                "page_size": 1,
            },
        )
        assert isinstance(resource, SyncPage)

    def test_method_apply(self) -> None:
        resource = self.client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, AuthRuleApplyResponse)

    def test_method_apply_with_optional_params(self) -> None:
        resource = self.client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "card_tokens": ["string", "string", "string"],
                "account_tokens": ["string", "string", "string"],
                "program_level": True,
            },
        )
        assert isinstance(resource, AuthRuleApplyResponse)

    def test_method_remove(self) -> None:
        resource = self.client.auth_rules.remove(
            {},
        )
        assert isinstance(resource, AuthRuleRemoveResponse)

    def test_method_remove_with_optional_params(self) -> None:
        resource = self.client.auth_rules.remove(
            {
                "card_tokens": ["string", "string", "string"],
                "account_tokens": ["string", "string", "string"],
                "program_level": True,
            },
        )
        assert isinstance(resource, AuthRuleRemoveResponse)


class TestAsyncAuthRules:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.auth_rules.create(
            {},
        )
        assert isinstance(resource, AuthRuleCreateResponse)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.auth_rules.create(
            {
                "allowed_mcc": ["string", "string", "string"],
                "blocked_mcc": ["string", "string", "string"],
                "allowed_countries": ["string", "string", "string"],
                "blocked_countries": ["string", "string", "string"],
                "avs_type": "ZIP_ONLY",
                "account_tokens": ["string", "string", "string"],
                "card_tokens": ["string", "string", "string"],
                "program_level": False,
            },
        )
        assert isinstance(resource, AuthRuleCreateResponse)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.auth_rules.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, AuthRuleRetrieveResponse)

    async def test_method_update(self) -> None:
        resource = await self.client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, AuthRuleUpdateResponse)

    async def test_method_update_with_optional_params(self) -> None:
        resource = await self.client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "allowed_mcc": ["string", "string", "string"],
                "blocked_mcc": ["string", "string", "string"],
                "allowed_countries": ["string", "string", "string"],
                "blocked_countries": ["string", "string", "string"],
                "avs_type": "ZIP_ONLY",
            },
        )
        assert isinstance(resource, AuthRuleUpdateResponse)

    async def test_method_list(self) -> None:
        resource = await self.client.auth_rules.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.auth_rules.list(
            {
                "page": 0,
                "page_size": 1,
            },
        )
        assert isinstance(resource, AsyncPage)

    async def test_method_apply(self) -> None:
        resource = await self.client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, AuthRuleApplyResponse)

    async def test_method_apply_with_optional_params(self) -> None:
        resource = await self.client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "card_tokens": ["string", "string", "string"],
                "account_tokens": ["string", "string", "string"],
                "program_level": True,
            },
        )
        assert isinstance(resource, AuthRuleApplyResponse)

    async def test_method_remove(self) -> None:
        resource = await self.client.auth_rules.remove(
            {},
        )
        assert isinstance(resource, AuthRuleRemoveResponse)

    async def test_method_remove_with_optional_params(self) -> None:
        resource = await self.client.auth_rules.remove(
            {
                "card_tokens": ["string", "string", "string"],
                "account_tokens": ["string", "string", "string"],
                "program_level": True,
            },
        )
        assert isinstance(resource, AuthRuleRemoveResponse)
