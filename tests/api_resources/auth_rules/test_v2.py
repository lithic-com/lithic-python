# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.pagination import SyncCursorPage, AsyncCursorPage
from lithic.types.auth_rules import (
    V2ListResponse,
    V2ApplyResponse,
    V2DraftResponse,
    V2CreateResponse,
    V2ReportResponse,
    V2UpdateResponse,
    V2PromoteResponse,
    V2RetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestV2:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.create(
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.create(
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            parameters={
                "conditions": [
                    {
                        "attribute": "MCC",
                        "operation": "IS_ONE_OF",
                        "value": "string",
                    }
                ]
            },
            type="CONDITIONAL_BLOCK",
        )
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.create(
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.create(
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2CreateResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.create(
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.create(
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            parameters={
                "conditions": [
                    {
                        "attribute": "MCC",
                        "operation": "IS_ONE_OF",
                        "value": "string",
                    }
                ]
            },
            type="CONDITIONAL_BLOCK",
        )
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.create(
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.create(
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2CreateResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.create(
            program_level=True,
        )
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.create(
            program_level=True,
            excluded_card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            parameters={
                "conditions": [
                    {
                        "attribute": "MCC",
                        "operation": "IS_ONE_OF",
                        "value": "string",
                    }
                ]
            },
            type="CONDITIONAL_BLOCK",
        )
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.create(
            program_level=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.create(
            program_level=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2CreateResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2RetrieveResponse, v2, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2RetrieveResponse, v2, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2RetrieveResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.v2.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update_overload_1(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            state="INACTIVE",
        )
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    def test_raw_response_update_overload_1(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_1(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2UpdateResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_1(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.v2.with_raw_response.update(
                auth_rule_token="",
            )

    @parametrize
    def test_method_update_overload_2(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            state="INACTIVE",
        )
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    def test_raw_response_update_overload_2(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_2(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2UpdateResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_2(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.v2.with_raw_response.update(
                auth_rule_token="",
            )

    @parametrize
    def test_method_update_overload_3(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            excluded_card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            program_level=True,
            state="INACTIVE",
        )
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    def test_raw_response_update_overload_3(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    def test_streaming_response_update_overload_3(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2UpdateResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_overload_3(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.v2.with_raw_response.update(
                auth_rule_token="",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.list()
        assert_matches_type(SyncCursorPage[V2ListResponse], v2, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(SyncCursorPage[V2ListResponse], v2, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(SyncCursorPage[V2ListResponse], v2, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(SyncCursorPage[V2ListResponse], v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v2 is None

    @parametrize
    def test_raw_response_delete(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @parametrize
    def test_streaming_response_delete(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.v2.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_apply_overload_1(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    def test_raw_response_apply_overload_1(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    def test_streaming_response_apply_overload_1(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ApplyResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_apply_overload_1(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.v2.with_raw_response.apply(
                auth_rule_token="",
                account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    def test_method_apply_overload_2(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    def test_raw_response_apply_overload_2(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    def test_streaming_response_apply_overload_2(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ApplyResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_apply_overload_2(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.v2.with_raw_response.apply(
                auth_rule_token="",
                card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    def test_method_apply_overload_3(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            program_level=True,
        )
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    def test_method_apply_with_all_params_overload_3(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            program_level=True,
            excluded_card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    def test_raw_response_apply_overload_3(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            program_level=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    def test_streaming_response_apply_overload_3(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            program_level=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ApplyResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_apply_overload_3(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.v2.with_raw_response.apply(
                auth_rule_token="",
                program_level=True,
            )

    @parametrize
    def test_method_draft(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.draft(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2DraftResponse, v2, path=["response"])

    @parametrize
    def test_method_draft_with_all_params(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.draft(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parameters={
                "conditions": [
                    {
                        "attribute": "MCC",
                        "operation": "IS_ONE_OF",
                        "value": "string",
                    }
                ]
            },
        )
        assert_matches_type(V2DraftResponse, v2, path=["response"])

    @parametrize
    def test_raw_response_draft(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.draft(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2DraftResponse, v2, path=["response"])

    @parametrize
    def test_streaming_response_draft(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.draft(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2DraftResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_draft(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.v2.with_raw_response.draft(
                auth_rule_token="",
            )

    @parametrize
    def test_method_promote(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2PromoteResponse, v2, path=["response"])

    @parametrize
    def test_raw_response_promote(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2PromoteResponse, v2, path=["response"])

    @parametrize
    def test_streaming_response_promote(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2PromoteResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_promote(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.v2.with_raw_response.promote(
                "",
            )

    @parametrize
    def test_method_report(self, client: Lithic) -> None:
        v2 = client.auth_rules.v2.report(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2ReportResponse, v2, path=["response"])

    @parametrize
    def test_raw_response_report(self, client: Lithic) -> None:
        response = client.auth_rules.v2.with_raw_response.report(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ReportResponse, v2, path=["response"])

    @parametrize
    def test_streaming_response_report(self, client: Lithic) -> None:
        with client.auth_rules.v2.with_streaming_response.report(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = response.parse()
            assert_matches_type(V2ReportResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_report(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.v2.with_raw_response.report(
                "",
            )


class TestAsyncV2:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.create(
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.create(
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            parameters={
                "conditions": [
                    {
                        "attribute": "MCC",
                        "operation": "IS_ONE_OF",
                        "value": "string",
                    }
                ]
            },
            type="CONDITIONAL_BLOCK",
        )
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.create(
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.create(
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2CreateResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.create(
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.create(
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            parameters={
                "conditions": [
                    {
                        "attribute": "MCC",
                        "operation": "IS_ONE_OF",
                        "value": "string",
                    }
                ]
            },
            type="CONDITIONAL_BLOCK",
        )
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.create(
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.create(
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2CreateResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.create(
            program_level=True,
        )
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.create(
            program_level=True,
            excluded_card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            parameters={
                "conditions": [
                    {
                        "attribute": "MCC",
                        "operation": "IS_ONE_OF",
                        "value": "string",
                    }
                ]
            },
            type="CONDITIONAL_BLOCK",
        )
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.create(
            program_level=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2CreateResponse, v2, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.create(
            program_level=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2CreateResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2RetrieveResponse, v2, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2RetrieveResponse, v2, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2RetrieveResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.v2.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            state="INACTIVE",
        )
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2UpdateResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.v2.with_raw_response.update(
                auth_rule_token="",
            )

    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            state="INACTIVE",
        )
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2UpdateResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.v2.with_raw_response.update(
                auth_rule_token="",
            )

    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            excluded_card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            program_level=True,
            state="INACTIVE",
        )
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2UpdateResponse, v2, path=["response"])

    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.update(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2UpdateResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.v2.with_raw_response.update(
                auth_rule_token="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.list()
        assert_matches_type(AsyncCursorPage[V2ListResponse], v2, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(AsyncCursorPage[V2ListResponse], v2, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(AsyncCursorPage[V2ListResponse], v2, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(AsyncCursorPage[V2ListResponse], v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert v2 is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert v2 is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert v2 is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.v2.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_apply_overload_1(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    async def test_raw_response_apply_overload_1(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    async def test_streaming_response_apply_overload_1(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ApplyResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_apply_overload_1(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.v2.with_raw_response.apply(
                auth_rule_token="",
                account_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    async def test_method_apply_overload_2(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    async def test_raw_response_apply_overload_2(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    async def test_streaming_response_apply_overload_2(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ApplyResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_apply_overload_2(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.v2.with_raw_response.apply(
                auth_rule_token="",
                card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    async def test_method_apply_overload_3(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            program_level=True,
        )
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    async def test_method_apply_with_all_params_overload_3(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            program_level=True,
            excluded_card_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    async def test_raw_response_apply_overload_3(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            program_level=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ApplyResponse, v2, path=["response"])

    @parametrize
    async def test_streaming_response_apply_overload_3(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.apply(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            program_level=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ApplyResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_apply_overload_3(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.v2.with_raw_response.apply(
                auth_rule_token="",
                program_level=True,
            )

    @parametrize
    async def test_method_draft(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.draft(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2DraftResponse, v2, path=["response"])

    @parametrize
    async def test_method_draft_with_all_params(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.draft(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            parameters={
                "conditions": [
                    {
                        "attribute": "MCC",
                        "operation": "IS_ONE_OF",
                        "value": "string",
                    }
                ]
            },
        )
        assert_matches_type(V2DraftResponse, v2, path=["response"])

    @parametrize
    async def test_raw_response_draft(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.draft(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2DraftResponse, v2, path=["response"])

    @parametrize
    async def test_streaming_response_draft(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.draft(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2DraftResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_draft(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.v2.with_raw_response.draft(
                auth_rule_token="",
            )

    @parametrize
    async def test_method_promote(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2PromoteResponse, v2, path=["response"])

    @parametrize
    async def test_raw_response_promote(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2PromoteResponse, v2, path=["response"])

    @parametrize
    async def test_streaming_response_promote(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.promote(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2PromoteResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_promote(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.v2.with_raw_response.promote(
                "",
            )

    @parametrize
    async def test_method_report(self, async_client: AsyncLithic) -> None:
        v2 = await async_client.auth_rules.v2.report(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(V2ReportResponse, v2, path=["response"])

    @parametrize
    async def test_raw_response_report(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.with_raw_response.report(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        v2 = response.parse()
        assert_matches_type(V2ReportResponse, v2, path=["response"])

    @parametrize
    async def test_streaming_response_report(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.with_streaming_response.report(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            v2 = await response.parse()
            assert_matches_type(V2ReportResponse, v2, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_report(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.v2.with_raw_response.report(
                "",
            )
