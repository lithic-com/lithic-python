# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.pagination import SyncCursorPage, AsyncCursorPage
from lithic.types.financial_accounts.statements import LineItemListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestLineItems:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        line_item = client.financial_accounts.statements.line_items.list(
            "string",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[LineItemListResponse], line_item, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        line_item = client.financial_accounts.statements.line_items.list(
            "string",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(SyncCursorPage[LineItemListResponse], line_item, path=["response"])


class TestAsyncLineItems:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        line_item = await client.financial_accounts.statements.line_items.list(
            "string",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[LineItemListResponse], line_item, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        line_item = await client.financial_accounts.statements.line_items.list(
            "string",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(AsyncCursorPage[LineItemListResponse], line_item, path=["response"])
