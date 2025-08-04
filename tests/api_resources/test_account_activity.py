# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    AccountActivityListResponse,
    AccountActivityRetrieveTransactionResponse,
)
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountActivity:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        account_activity = client.account_activity.list()
        assert_matches_type(SyncCursorPage[AccountActivityListResponse], account_activity, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        account_activity = client.account_activity.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            business_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category="ACH",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            result=["APPROVED"],
            starting_after="starting_after",
            status=["DECLINED"],
        )
        assert_matches_type(SyncCursorPage[AccountActivityListResponse], account_activity, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.account_activity.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_activity = response.parse()
        assert_matches_type(SyncCursorPage[AccountActivityListResponse], account_activity, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.account_activity.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_activity = response.parse()
            assert_matches_type(SyncCursorPage[AccountActivityListResponse], account_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_transaction(self, client: Lithic) -> None:
        account_activity = client.account_activity.retrieve_transaction(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountActivityRetrieveTransactionResponse, account_activity, path=["response"])

    @parametrize
    def test_raw_response_retrieve_transaction(self, client: Lithic) -> None:
        response = client.account_activity.with_raw_response.retrieve_transaction(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_activity = response.parse()
        assert_matches_type(AccountActivityRetrieveTransactionResponse, account_activity, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_transaction(self, client: Lithic) -> None:
        with client.account_activity.with_streaming_response.retrieve_transaction(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_activity = response.parse()
            assert_matches_type(AccountActivityRetrieveTransactionResponse, account_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_transaction(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_token` but received ''"):
            client.account_activity.with_raw_response.retrieve_transaction(
                "",
            )


class TestAsyncAccountActivity:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        account_activity = await async_client.account_activity.list()
        assert_matches_type(AsyncCursorPage[AccountActivityListResponse], account_activity, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        account_activity = await async_client.account_activity.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            business_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category="ACH",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            result=["APPROVED"],
            starting_after="starting_after",
            status=["DECLINED"],
        )
        assert_matches_type(AsyncCursorPage[AccountActivityListResponse], account_activity, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_activity.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_activity = response.parse()
        assert_matches_type(AsyncCursorPage[AccountActivityListResponse], account_activity, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.account_activity.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_activity = await response.parse()
            assert_matches_type(AsyncCursorPage[AccountActivityListResponse], account_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_transaction(self, async_client: AsyncLithic) -> None:
        account_activity = await async_client.account_activity.retrieve_transaction(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountActivityRetrieveTransactionResponse, account_activity, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_transaction(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_activity.with_raw_response.retrieve_transaction(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_activity = response.parse()
        assert_matches_type(AccountActivityRetrieveTransactionResponse, account_activity, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_transaction(self, async_client: AsyncLithic) -> None:
        async with async_client.account_activity.with_streaming_response.retrieve_transaction(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_activity = await response.parse()
            assert_matches_type(AccountActivityRetrieveTransactionResponse, account_activity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_transaction(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `transaction_token` but received ''"):
            await async_client.account_activity.with_raw_response.retrieve_transaction(
                "",
            )
