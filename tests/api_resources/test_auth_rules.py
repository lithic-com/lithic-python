# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    AuthRuleRemoveResponse,
    AuthRuleRetrieveResponse,
    AuthRuleMigrateV1ToV2Response,
)
from lithic.pagination import SyncCursorPage, AsyncCursorPage
from lithic.types.shared import AuthRule

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthRules:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            blocked_countries=["CAN", "USA"],
            blocked_mcc=["5811", "5812"],
            card_tokens=["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
            program_level=False,
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.auth_rules.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.auth_rules.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = response.parse()
            assert_matches_type(AuthRule, auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRuleRetrieveResponse, auth_rule, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.auth_rules.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = response.parse()
            assert_matches_type(AuthRuleRetrieveResponse, auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_countries=["USA"],
            allowed_mcc=["3000", "3001"],
            blocked_countries=["string", "string", "string"],
            blocked_mcc=["string", "string", "string"],
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.auth_rules.with_raw_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.auth_rules.with_streaming_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = response.parse()
            assert_matches_type(AuthRule, auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.with_raw_response.update(
                auth_rule_token="",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.list()
        assert_matches_type(SyncCursorPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.list(
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(SyncCursorPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.auth_rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(SyncCursorPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.auth_rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = response.parse()
            assert_matches_type(SyncCursorPage[AuthRule], auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_apply(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_method_apply_with_all_params(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["string", "string", "string"],
            card_tokens=["1336a403-2447-4b36-a009-6fbb852ee675", "df942c4e-9130-4ab5-b067-778a2c55b357"],
            program_level=True,
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_raw_response_apply(self, client: Lithic) -> None:
        response = client.auth_rules.with_raw_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    def test_streaming_response_apply(self, client: Lithic) -> None:
        with client.auth_rules.with_streaming_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = response.parse()
            assert_matches_type(AuthRule, auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_apply(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.with_raw_response.apply(
                auth_rule_token="",
            )

    @parametrize
    def test_method_migrate_v1_to_v2(self, client: Lithic) -> None:
        auth_rule = client.auth_rules.migrate_v1_to_v2(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRuleMigrateV1ToV2Response, auth_rule, path=["response"])

    @parametrize
    def test_raw_response_migrate_v1_to_v2(self, client: Lithic) -> None:
        response = client.auth_rules.with_raw_response.migrate_v1_to_v2(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRuleMigrateV1ToV2Response, auth_rule, path=["response"])

    @parametrize
    def test_streaming_response_migrate_v1_to_v2(self, client: Lithic) -> None:
        with client.auth_rules.with_streaming_response.migrate_v1_to_v2(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = response.parse()
            assert_matches_type(AuthRuleMigrateV1ToV2Response, auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_migrate_v1_to_v2(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.with_raw_response.migrate_v1_to_v2(
                "",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])

    @parametrize
    def test_streaming_response_remove(self, client: Lithic) -> None:
        with client.auth_rules.with_streaming_response.remove() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = response.parse()
            assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuthRules:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        auth_rule = await async_client.auth_rules.create()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        auth_rule = await async_client.auth_rules.create(
            account_tokens=["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
            allowed_countries=["MEX"],
            allowed_mcc=["3000"],
            blocked_countries=["CAN", "USA"],
            blocked_mcc=["5811", "5812"],
            card_tokens=["3fa85f64-5717-4562-b3fc-2c963f66afa6"],
            program_level=False,
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = await response.parse()
            assert_matches_type(AuthRule, auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        auth_rule = await async_client.auth_rules.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRuleRetrieveResponse, auth_rule, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRuleRetrieveResponse, auth_rule, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = await response.parse()
            assert_matches_type(AuthRuleRetrieveResponse, auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLithic) -> None:
        auth_rule = await async_client.auth_rules.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLithic) -> None:
        auth_rule = await async_client.auth_rules.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            allowed_countries=["USA"],
            allowed_mcc=["3000", "3001"],
            blocked_countries=["string", "string", "string"],
            blocked_mcc=["string", "string", "string"],
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.with_raw_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.with_streaming_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = await response.parse()
            assert_matches_type(AuthRule, auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.with_raw_response.update(
                auth_rule_token="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        auth_rule = await async_client.auth_rules.list()
        assert_matches_type(AsyncCursorPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        auth_rule = await async_client.auth_rules.list(
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(AsyncCursorPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AsyncCursorPage[AuthRule], auth_rule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = await response.parse()
            assert_matches_type(AsyncCursorPage[AuthRule], auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_apply(self, async_client: AsyncLithic) -> None:
        auth_rule = await async_client.auth_rules.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_method_apply_with_all_params(self, async_client: AsyncLithic) -> None:
        auth_rule = await async_client.auth_rules.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["string", "string", "string"],
            card_tokens=["1336a403-2447-4b36-a009-6fbb852ee675", "df942c4e-9130-4ab5-b067-778a2c55b357"],
            program_level=True,
        )
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_raw_response_apply(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.with_raw_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRule, auth_rule, path=["response"])

    @parametrize
    async def test_streaming_response_apply(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.with_streaming_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = await response.parse()
            assert_matches_type(AuthRule, auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_apply(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.with_raw_response.apply(
                auth_rule_token="",
            )

    @parametrize
    async def test_method_migrate_v1_to_v2(self, async_client: AsyncLithic) -> None:
        auth_rule = await async_client.auth_rules.migrate_v1_to_v2(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthRuleMigrateV1ToV2Response, auth_rule, path=["response"])

    @parametrize
    async def test_raw_response_migrate_v1_to_v2(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.with_raw_response.migrate_v1_to_v2(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRuleMigrateV1ToV2Response, auth_rule, path=["response"])

    @parametrize
    async def test_streaming_response_migrate_v1_to_v2(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.with_streaming_response.migrate_v1_to_v2(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = await response.parse()
            assert_matches_type(AuthRuleMigrateV1ToV2Response, auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_migrate_v1_to_v2(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.with_raw_response.migrate_v1_to_v2(
                "",
            )

    @parametrize
    async def test_method_remove(self, async_client: AsyncLithic) -> None:
        auth_rule = await async_client.auth_rules.remove()
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])

    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncLithic) -> None:
        auth_rule = await async_client.auth_rules.remove(
            account_tokens=["string", "string", "string"],
            card_tokens=["string", "string", "string"],
            program_level=False,
        )
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])

    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.with_raw_response.remove()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_rule = response.parse()
        assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])

    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.with_streaming_response.remove() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_rule = await response.parse()
            assert_matches_type(AuthRuleRemoveResponse, auth_rule, path=["response"])

        assert cast(Any, response.is_closed) is True
