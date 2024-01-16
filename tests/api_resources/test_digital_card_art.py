# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import DigitalCardArt
from lithic._client import Lithic, AsyncLithic
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestDigitalCardArt:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        digital_card_art = client.digital_card_art.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DigitalCardArt, digital_card_art, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.digital_card_art.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_art = response.parse()
        assert_matches_type(DigitalCardArt, digital_card_art, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.digital_card_art.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_art = response.parse()
            assert_matches_type(DigitalCardArt, digital_card_art, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `digital_card_art_token` but received ''"
        ):
            client.digital_card_art.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        digital_card_art = client.digital_card_art.list()
        assert_matches_type(SyncCursorPage[DigitalCardArt], digital_card_art, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        digital_card_art = client.digital_card_art.list(
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(SyncCursorPage[DigitalCardArt], digital_card_art, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.digital_card_art.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_art = response.parse()
        assert_matches_type(SyncCursorPage[DigitalCardArt], digital_card_art, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.digital_card_art.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_art = response.parse()
            assert_matches_type(SyncCursorPage[DigitalCardArt], digital_card_art, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDigitalCardArt:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        digital_card_art = await client.digital_card_art.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DigitalCardArt, digital_card_art, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncLithic) -> None:
        response = await client.digital_card_art.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_art = response.parse()
        assert_matches_type(DigitalCardArt, digital_card_art, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncLithic) -> None:
        async with client.digital_card_art.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_art = await response.parse()
            assert_matches_type(DigitalCardArt, digital_card_art, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `digital_card_art_token` but received ''"
        ):
            await client.digital_card_art.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        digital_card_art = await client.digital_card_art.list()
        assert_matches_type(AsyncCursorPage[DigitalCardArt], digital_card_art, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        digital_card_art = await client.digital_card_art.list(
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(AsyncCursorPage[DigitalCardArt], digital_card_art, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncLithic) -> None:
        response = await client.digital_card_art.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        digital_card_art = response.parse()
        assert_matches_type(AsyncCursorPage[DigitalCardArt], digital_card_art, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncLithic) -> None:
        async with client.digital_card_art.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            digital_card_art = await response.parse()
            assert_matches_type(AsyncCursorPage[DigitalCardArt], digital_card_art, path=["response"])

        assert cast(Any, response.is_closed) is True
