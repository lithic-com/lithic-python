# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic._utils import parse_date
from lithic.pagination import SyncSinglePage, AsyncSinglePage
from lithic.types.transfer_limits_response import Data

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransferLimits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        transfer_limit = client.transfer_limits.list()
        assert_matches_type(SyncSinglePage[Data], transfer_limit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        transfer_limit = client.transfer_limits.list(
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(SyncSinglePage[Data], transfer_limit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.transfer_limits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer_limit = response.parse()
        assert_matches_type(SyncSinglePage[Data], transfer_limit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.transfer_limits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer_limit = response.parse()
            assert_matches_type(SyncSinglePage[Data], transfer_limit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransferLimits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        transfer_limit = await async_client.transfer_limits.list()
        assert_matches_type(AsyncSinglePage[Data], transfer_limit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        transfer_limit = await async_client.transfer_limits.list(
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(AsyncSinglePage[Data], transfer_limit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.transfer_limits.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transfer_limit = response.parse()
        assert_matches_type(AsyncSinglePage[Data], transfer_limit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.transfer_limits.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transfer_limit = await response.parse()
            assert_matches_type(AsyncSinglePage[Data], transfer_limit, path=["response"])

        assert cast(Any, response.is_closed) is True
