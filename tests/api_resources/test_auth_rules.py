# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    AuthRule,
    AuthRuleRemoveResponse,
    AuthRuleRetrieveResponse,
)
from lithic._client import Lithic, AsyncLithic
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestAuthRules:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.create()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.create(
            account_tokens=["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
            allowed_countries=["MEX"],
            allowed_mcc=["3000"],
            blocked_countries=["USA", "CAN"],
            blocked_mcc=["5811", "5812"],
            card_tokens=["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
            program_level=False,
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.auth_rules.with_raw_response.create()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRuleRetrieveResponse, auth_rule, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.auth_rules.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRuleRetrieveResponse, auth_rule, path=["response"])

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_countries=["USA"],
            allowed_mcc=["3000", "3001"],
            blocked_countries=["string", "string", "string"],
            blocked_mcc=["string", "string", "string"],
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.auth_rules.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.list()
        assert_matches_type(SyncCursorPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.list(
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(SyncCursorPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.auth_rules.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(SyncCursorPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    def test_method_apply(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_method_apply_with_all_params(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["string", "string", "string"],
            card_tokens=["df942c4e-9130-4ab5-b067-778a2c55b357", "1336a403-2447-4b36-a009-6fbb852ee675"],
            program_level=True,
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_raw_response_apply(self, client: Lithic) -> None:
        response = client.auth_rules.with_raw_response.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_method_remove(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.remove()
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])

    @parametrize
    def test_method_remove_with_all_params(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.remove(
            account_tokens=["string", "string", "string"],
            card_tokens=["string", "string", "string"],
            program_level=False,
        )
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])

    @parametrize
    def test_raw_response_remove(self, client: Lithic) -> None:
        response = client.auth_rules.with_raw_response.remove()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])


class TestAsyncAuthRules:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.create()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.create(
            account_tokens=["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
            allowed_countries=["MEX"],
            allowed_mcc=["3000"],
            blocked_countries=["USA", "CAN"],
            blocked_mcc=["5811", "5812"],
            card_tokens=["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
            program_level=False,
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncLithic) -> None:
        response = await client.auth_rules.with_raw_response.create()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRuleRetrieveResponse, auth_rule, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncLithic) -> None:
        response = await client.auth_rules.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRuleRetrieveResponse, auth_rule, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_countries=["USA"],
            allowed_mcc=["3000", "3001"],
            blocked_countries=["string", "string", "string"],
            blocked_mcc=["string", "string", "string"],
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncLithic) -> None:
        response = await client.auth_rules.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.list()
        assert_matches_type(AsyncCursorPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.list(
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(AsyncCursorPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncLithic) -> None:
        response = await client.auth_rules.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AsyncCursorPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    async def test_method_apply(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_method_apply_with_all_params(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["string", "string", "string"],
            card_tokens=["df942c4e-9130-4ab5-b067-778a2c55b357", "1336a403-2447-4b36-a009-6fbb852ee675"],
            program_level=True,
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_raw_response_apply(self, client: AsyncLithic) -> None:
        response = await client.auth_rules.with_raw_response.apply(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_method_remove(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.remove()
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])

    @parametrize
    async def test_method_remove_with_all_params(self, client: AsyncLithic) -> None:
        auth_rule = await client.auth_rules.remove(
            account_tokens=["string", "string", "string"],
            card_tokens=["string", "string", "string"],
            program_level=False,
        )
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, client: AsyncLithic) -> None:
        response = await client.auth_rules.with_raw_response.remove()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])
