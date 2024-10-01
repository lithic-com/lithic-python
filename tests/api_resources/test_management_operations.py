# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    ManagementOperationTransaction,
)
from lithic._utils import parse_date, parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestManagementOperations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        management_operation = client.management_operations.create(
            amount=0,
            category="MANAGEMENT_FEE",
            direction="CREDIT",
            effective_date=parse_date("2019-12-27"),
            event_type="CASH_BACK",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        management_operation = client.management_operations.create(
            amount=0,
            category="MANAGEMENT_FEE",
            direction="CREDIT",
            effective_date=parse_date("2019-12-27"),
            event_type="CASH_BACK",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            memo="memo",
            subtype="subtype",
            user_defined_id="user_defined_id",
        )
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.management_operations.with_raw_response.create(
            amount=0,
            category="MANAGEMENT_FEE",
            direction="CREDIT",
            effective_date=parse_date("2019-12-27"),
            event_type="CASH_BACK",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        management_operation = response.parse()
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.management_operations.with_streaming_response.create(
            amount=0,
            category="MANAGEMENT_FEE",
            direction="CREDIT",
            effective_date=parse_date("2019-12-27"),
            event_type="CASH_BACK",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            management_operation = response.parse()
            assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        management_operation = client.management_operations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.management_operations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        management_operation = response.parse()
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.management_operations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            management_operation = response.parse()
            assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `management_operation_token` but received ''"
        ):
            client.management_operations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        management_operation = client.management_operations.list()
        assert_matches_type(SyncCursorPage[ManagementOperationTransaction], management_operation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        management_operation = client.management_operations.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            business_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category="MANAGEMENT_FEE",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            starting_after="starting_after",
            status="PENDING",
        )
        assert_matches_type(SyncCursorPage[ManagementOperationTransaction], management_operation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.management_operations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        management_operation = response.parse()
        assert_matches_type(SyncCursorPage[ManagementOperationTransaction], management_operation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.management_operations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            management_operation = response.parse()
            assert_matches_type(SyncCursorPage[ManagementOperationTransaction], management_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_reverse(self, client: Lithic) -> None:
        management_operation = client.management_operations.reverse(
            management_operation_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    def test_method_reverse_with_all_params(self, client: Lithic) -> None:
        management_operation = client.management_operations.reverse(
            management_operation_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
            memo="memo",
        )
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    def test_raw_response_reverse(self, client: Lithic) -> None:
        response = client.management_operations.with_raw_response.reverse(
            management_operation_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        management_operation = response.parse()
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    def test_streaming_response_reverse(self, client: Lithic) -> None:
        with client.management_operations.with_streaming_response.reverse(
            management_operation_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            management_operation = response.parse()
            assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reverse(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `management_operation_token` but received ''"
        ):
            client.management_operations.with_raw_response.reverse(
                management_operation_token="",
                effective_date=parse_date("2019-12-27"),
            )


class TestAsyncManagementOperations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        management_operation = await async_client.management_operations.create(
            amount=0,
            category="MANAGEMENT_FEE",
            direction="CREDIT",
            effective_date=parse_date("2019-12-27"),
            event_type="CASH_BACK",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        management_operation = await async_client.management_operations.create(
            amount=0,
            category="MANAGEMENT_FEE",
            direction="CREDIT",
            effective_date=parse_date("2019-12-27"),
            event_type="CASH_BACK",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            memo="memo",
            subtype="subtype",
            user_defined_id="user_defined_id",
        )
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.management_operations.with_raw_response.create(
            amount=0,
            category="MANAGEMENT_FEE",
            direction="CREDIT",
            effective_date=parse_date("2019-12-27"),
            event_type="CASH_BACK",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        management_operation = response.parse()
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.management_operations.with_streaming_response.create(
            amount=0,
            category="MANAGEMENT_FEE",
            direction="CREDIT",
            effective_date=parse_date("2019-12-27"),
            event_type="CASH_BACK",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            management_operation = await response.parse()
            assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        management_operation = await async_client.management_operations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.management_operations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        management_operation = response.parse()
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.management_operations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            management_operation = await response.parse()
            assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `management_operation_token` but received ''"
        ):
            await async_client.management_operations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        management_operation = await async_client.management_operations.list()
        assert_matches_type(AsyncCursorPage[ManagementOperationTransaction], management_operation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        management_operation = await async_client.management_operations.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            business_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category="MANAGEMENT_FEE",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            starting_after="starting_after",
            status="PENDING",
        )
        assert_matches_type(AsyncCursorPage[ManagementOperationTransaction], management_operation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.management_operations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        management_operation = response.parse()
        assert_matches_type(AsyncCursorPage[ManagementOperationTransaction], management_operation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.management_operations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            management_operation = await response.parse()
            assert_matches_type(
                AsyncCursorPage[ManagementOperationTransaction], management_operation, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_reverse(self, async_client: AsyncLithic) -> None:
        management_operation = await async_client.management_operations.reverse(
            management_operation_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    async def test_method_reverse_with_all_params(self, async_client: AsyncLithic) -> None:
        management_operation = await async_client.management_operations.reverse(
            management_operation_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
            memo="memo",
        )
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    async def test_raw_response_reverse(self, async_client: AsyncLithic) -> None:
        response = await async_client.management_operations.with_raw_response.reverse(
            management_operation_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        management_operation = response.parse()
        assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

    @parametrize
    async def test_streaming_response_reverse(self, async_client: AsyncLithic) -> None:
        async with async_client.management_operations.with_streaming_response.reverse(
            management_operation_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            management_operation = await response.parse()
            assert_matches_type(ManagementOperationTransaction, management_operation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reverse(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `management_operation_token` but received ''"
        ):
            await async_client.management_operations.with_raw_response.reverse(
                management_operation_token="",
                effective_date=parse_date("2019-12-27"),
            )
