# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import CardProgram
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardPrograms:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        card_program = client.card_programs.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardProgram, card_program, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.card_programs.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_program = response.parse()
        assert_matches_type(CardProgram, card_program, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.card_programs.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_program = response.parse()
            assert_matches_type(CardProgram, card_program, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_program_token` but received ''"):
            client.card_programs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        card_program = client.card_programs.list()
        assert_matches_type(SyncCursorPage[CardProgram], card_program, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        card_program = client.card_programs.list(
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(SyncCursorPage[CardProgram], card_program, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.card_programs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_program = response.parse()
        assert_matches_type(SyncCursorPage[CardProgram], card_program, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.card_programs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_program = response.parse()
            assert_matches_type(SyncCursorPage[CardProgram], card_program, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCardPrograms:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        card_program = await async_client.card_programs.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardProgram, card_program, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.card_programs.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_program = response.parse()
        assert_matches_type(CardProgram, card_program, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.card_programs.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_program = await response.parse()
            assert_matches_type(CardProgram, card_program, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_program_token` but received ''"):
            await async_client.card_programs.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        card_program = await async_client.card_programs.list()
        assert_matches_type(AsyncCursorPage[CardProgram], card_program, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        card_program = await async_client.card_programs.list(
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(AsyncCursorPage[CardProgram], card_program, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.card_programs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_program = response.parse()
        assert_matches_type(AsyncCursorPage[CardProgram], card_program, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.card_programs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_program = await response.parse()
            assert_matches_type(AsyncCursorPage[CardProgram], card_program, path=["response"])

        assert cast(Any, response.is_closed) is True
