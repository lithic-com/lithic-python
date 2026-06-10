# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types.transaction_monitoring import CaseActivityEntry

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        comment = client.transaction_monitoring.cases.comments.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )
        assert_matches_type(CaseActivityEntry, comment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        comment = client.transaction_monitoring.cases.comments.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
            actor_token="actor_token",
        )
        assert_matches_type(CaseActivityEntry, comment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.transaction_monitoring.cases.comments.with_raw_response.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CaseActivityEntry, comment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.transaction_monitoring.cases.comments.with_streaming_response.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CaseActivityEntry, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            client.transaction_monitoring.cases.comments.with_raw_response.create(
                case_token="",
                comment="comment",
            )

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        comment = client.transaction_monitoring.cases.comments.update(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )
        assert_matches_type(CaseActivityEntry, comment, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        comment = client.transaction_monitoring.cases.comments.update(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
            actor_token="actor_token",
        )
        assert_matches_type(CaseActivityEntry, comment, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.transaction_monitoring.cases.comments.with_raw_response.update(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CaseActivityEntry, comment, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.transaction_monitoring.cases.comments.with_streaming_response.update(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert_matches_type(CaseActivityEntry, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            client.transaction_monitoring.cases.comments.with_raw_response.update(
                comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                case_token="",
                comment="comment",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_token` but received ''"):
            client.transaction_monitoring.cases.comments.with_raw_response.update(
                comment_token="",
                case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                comment="comment",
            )

    @parametrize
    def test_method_delete(self, client: Lithic) -> None:
        comment = client.transaction_monitoring.cases.comments.delete(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert comment is None

    @parametrize
    def test_raw_response_delete(self, client: Lithic) -> None:
        response = client.transaction_monitoring.cases.comments.with_raw_response.delete(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert comment is None

    @parametrize
    def test_streaming_response_delete(self, client: Lithic) -> None:
        with client.transaction_monitoring.cases.comments.with_streaming_response.delete(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = response.parse()
            assert comment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            client.transaction_monitoring.cases.comments.with_raw_response.delete(
                comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                case_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_token` but received ''"):
            client.transaction_monitoring.cases.comments.with_raw_response.delete(
                comment_token="",
                case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncComments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        comment = await async_client.transaction_monitoring.cases.comments.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )
        assert_matches_type(CaseActivityEntry, comment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        comment = await async_client.transaction_monitoring.cases.comments.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
            actor_token="actor_token",
        )
        assert_matches_type(CaseActivityEntry, comment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.transaction_monitoring.cases.comments.with_raw_response.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CaseActivityEntry, comment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.transaction_monitoring.cases.comments.with_streaming_response.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CaseActivityEntry, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            await async_client.transaction_monitoring.cases.comments.with_raw_response.create(
                case_token="",
                comment="comment",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLithic) -> None:
        comment = await async_client.transaction_monitoring.cases.comments.update(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )
        assert_matches_type(CaseActivityEntry, comment, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLithic) -> None:
        comment = await async_client.transaction_monitoring.cases.comments.update(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
            actor_token="actor_token",
        )
        assert_matches_type(CaseActivityEntry, comment, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLithic) -> None:
        response = await async_client.transaction_monitoring.cases.comments.with_raw_response.update(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert_matches_type(CaseActivityEntry, comment, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLithic) -> None:
        async with async_client.transaction_monitoring.cases.comments.with_streaming_response.update(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert_matches_type(CaseActivityEntry, comment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            await async_client.transaction_monitoring.cases.comments.with_raw_response.update(
                comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                case_token="",
                comment="comment",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_token` but received ''"):
            await async_client.transaction_monitoring.cases.comments.with_raw_response.update(
                comment_token="",
                case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                comment="comment",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncLithic) -> None:
        comment = await async_client.transaction_monitoring.cases.comments.delete(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert comment is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLithic) -> None:
        response = await async_client.transaction_monitoring.cases.comments.with_raw_response.delete(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comment = response.parse()
        assert comment is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLithic) -> None:
        async with async_client.transaction_monitoring.cases.comments.with_streaming_response.delete(
            comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comment = await response.parse()
            assert comment is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            await async_client.transaction_monitoring.cases.comments.with_raw_response.delete(
                comment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                case_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `comment_token` but received ''"):
            await async_client.transaction_monitoring.cases.comments.with_raw_response.delete(
                comment_token="",
                case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
