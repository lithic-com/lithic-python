# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import SettlementDetail, SettlementReport
from lithic._utils import parse_date
from lithic._client import Lithic, AsyncLithic
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestSettlement:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list_details(self, client: Lithic) -> None:
        settlement = client.reports.settlement.list_details(
            parse_date("2019-12-27"),
        )
        assert_matches_type(SyncCursorPage[SettlementDetail], settlement, path=["response"])

    @parametrize
    def test_method_list_details_with_all_params(self, client: Lithic) -> None:
        settlement = client.reports.settlement.list_details(
            parse_date("2019-12-27"),
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(SyncCursorPage[SettlementDetail], settlement, path=["response"])

    @parametrize
    def test_raw_response_list_details(self, client: Lithic) -> None:
        response = client.reports.settlement.with_raw_response.list_details(
            parse_date("2019-12-27"),
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        settlement = response.parse()
        assert_matches_type(SyncCursorPage[SettlementDetail], settlement, path=["response"])

    @parametrize
    def test_method_summary(self, client: Lithic) -> None:
        settlement = client.reports.settlement.summary(
            parse_date("2019-12-27"),
        )
        assert_matches_type(SettlementReport, settlement, path=["response"])

    @parametrize
    def test_raw_response_summary(self, client: Lithic) -> None:
        response = client.reports.settlement.with_raw_response.summary(
            parse_date("2019-12-27"),
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        settlement = response.parse()
        assert_matches_type(SettlementReport, settlement, path=["response"])


class TestAsyncSettlement:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list_details(self, client: AsyncLithic) -> None:
        settlement = await client.reports.settlement.list_details(
            parse_date("2019-12-27"),
        )
        assert_matches_type(AsyncCursorPage[SettlementDetail], settlement, path=["response"])

    @parametrize
    async def test_method_list_details_with_all_params(self, client: AsyncLithic) -> None:
        settlement = await client.reports.settlement.list_details(
            parse_date("2019-12-27"),
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(AsyncCursorPage[SettlementDetail], settlement, path=["response"])

    @parametrize
    async def test_raw_response_list_details(self, client: AsyncLithic) -> None:
        response = await client.reports.settlement.with_raw_response.list_details(
            parse_date("2019-12-27"),
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        settlement = response.parse()
        assert_matches_type(AsyncCursorPage[SettlementDetail], settlement, path=["response"])

    @parametrize
    async def test_method_summary(self, client: AsyncLithic) -> None:
        settlement = await client.reports.settlement.summary(
            parse_date("2019-12-27"),
        )
        assert_matches_type(SettlementReport, settlement, path=["response"])

    @parametrize
    async def test_raw_response_summary(self, client: AsyncLithic) -> None:
        response = await client.reports.settlement.with_raw_response.summary(
            parse_date("2019-12-27"),
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        settlement = response.parse()
        assert_matches_type(SettlementReport, settlement, path=["response"])
