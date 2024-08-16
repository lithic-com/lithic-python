# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic._utils import parse_date
from lithic.pagination import SyncCursorPage, AsyncCursorPage
from lithic.types.financial_accounts import Statement

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        statement = client.financial_accounts.statements.retrieve(
            statement_token="statement_token",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Statement, statement, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.financial_accounts.statements.with_raw_response.retrieve(
            statement_token="statement_token",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = response.parse()
        assert_matches_type(Statement, statement, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.financial_accounts.statements.with_streaming_response.retrieve(
            statement_token="statement_token",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = response.parse()
            assert_matches_type(Statement, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.financial_accounts.statements.with_raw_response.retrieve(
                statement_token="statement_token",
                financial_account_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `statement_token` but received ''"):
            client.financial_accounts.statements.with_raw_response.retrieve(
                statement_token="",
                financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        statement = client.financial_accounts.statements.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[Statement], statement, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        statement = client.financial_accounts.statements.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_date("2019-12-27"),
            end=parse_date("2019-12-27"),
            ending_before="ending_before",
            include_initial_statements=True,
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(SyncCursorPage[Statement], statement, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.financial_accounts.statements.with_raw_response.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = response.parse()
        assert_matches_type(SyncCursorPage[Statement], statement, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.financial_accounts.statements.with_streaming_response.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = response.parse()
            assert_matches_type(SyncCursorPage[Statement], statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.financial_accounts.statements.with_raw_response.list(
                financial_account_token="",
            )


class TestAsyncStatements:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        statement = await async_client.financial_accounts.statements.retrieve(
            statement_token="statement_token",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Statement, statement, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.statements.with_raw_response.retrieve(
            statement_token="statement_token",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = response.parse()
        assert_matches_type(Statement, statement, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.statements.with_streaming_response.retrieve(
            statement_token="statement_token",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = await response.parse()
            assert_matches_type(Statement, statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.financial_accounts.statements.with_raw_response.retrieve(
                statement_token="statement_token",
                financial_account_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `statement_token` but received ''"):
            await async_client.financial_accounts.statements.with_raw_response.retrieve(
                statement_token="",
                financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        statement = await async_client.financial_accounts.statements.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[Statement], statement, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        statement = await async_client.financial_accounts.statements.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_date("2019-12-27"),
            end=parse_date("2019-12-27"),
            ending_before="ending_before",
            include_initial_statements=True,
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(AsyncCursorPage[Statement], statement, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.statements.with_raw_response.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        statement = response.parse()
        assert_matches_type(AsyncCursorPage[Statement], statement, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.statements.with_streaming_response.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            statement = await response.parse()
            assert_matches_type(AsyncCursorPage[Statement], statement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.financial_accounts.statements.with_raw_response.list(
                financial_account_token="",
            )
