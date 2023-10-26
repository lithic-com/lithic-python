# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import DigitalCardArt
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestDigitalCardArt:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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


class TestAsyncDigitalCardArt:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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
