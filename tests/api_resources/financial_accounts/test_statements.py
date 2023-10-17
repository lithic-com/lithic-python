# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic._utils import parse_date
from lithic.pagination import SyncCursorPage, AsyncCursorPage
from lithic.types.financial_accounts import Statement

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestStatements:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        statement = client.financial_accounts.statements.retrieve(
            "string",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Statement, statement, path=["response"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        statement = client.financial_accounts.statements.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[Statement], statement, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        statement = client.financial_accounts.statements.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_date("2019-12-27"),
            end=parse_date("2019-12-27"),
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(SyncCursorPage[Statement], statement, path=["response"])


class TestAsyncStatements:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        statement = await client.financial_accounts.statements.retrieve(
            "string",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Statement, statement, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        statement = await client.financial_accounts.statements.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[Statement], statement, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        statement = await client.financial_accounts.statements.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_date("2019-12-27"),
            end=parse_date("2019-12-27"),
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(AsyncCursorPage[Statement], statement, path=["response"])
