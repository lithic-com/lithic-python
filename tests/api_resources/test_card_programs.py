# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import CardProgram
from lithic._client import Lithic, AsyncLithic
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestCardPrograms:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_program = response.parse()
        assert_matches_type(CardProgram, card_program, path=["response"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        card_program = client.card_programs.list()
        assert_matches_type(SyncCursorPage[CardProgram], card_program, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        card_program = client.card_programs.list(
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(SyncCursorPage[CardProgram], card_program, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.card_programs.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_program = response.parse()
        assert_matches_type(SyncCursorPage[CardProgram], card_program, path=["response"])


class TestAsyncCardPrograms:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        card_program = await client.card_programs.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CardProgram, card_program, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncLithic) -> None:
        response = await client.card_programs.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_program = response.parse()
        assert_matches_type(CardProgram, card_program, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        card_program = await client.card_programs.list()
        assert_matches_type(AsyncCursorPage[CardProgram], card_program, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        card_program = await client.card_programs.list(
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(AsyncCursorPage[CardProgram], card_program, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncLithic) -> None:
        response = await client.card_programs.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_program = response.parse()
        assert_matches_type(AsyncCursorPage[CardProgram], card_program, path=["response"])
