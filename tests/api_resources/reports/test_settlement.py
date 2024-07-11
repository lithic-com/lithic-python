# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import SettlementDetail, SettlementReport
from lithic._utils import parse_date
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSettlement:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_details(self, client: Lithic) -> None:
        settlement = client.reports.settlement.list_details(
            report_date=parse_date("2023-09-01"),
        )
        assert_matches_type(SyncCursorPage[SettlementDetail], settlement, path=["response"])

    @parametrize
    def test_method_list_details_with_all_params(self, client: Lithic) -> None:
        settlement = client.reports.settlement.list_details(
            report_date=parse_date("2023-09-01"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(SyncCursorPage[SettlementDetail], settlement, path=["response"])

    @parametrize
    def test_raw_response_list_details(self, client: Lithic) -> None:
        response = client.reports.settlement.with_raw_response.list_details(
            report_date=parse_date("2023-09-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        settlement = response.parse()
        assert_matches_type(SyncCursorPage[SettlementDetail], settlement, path=["response"])

    @parametrize
    def test_streaming_response_list_details(self, client: Lithic) -> None:
        with client.reports.settlement.with_streaming_response.list_details(
            report_date=parse_date("2023-09-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            settlement = response.parse()
            assert_matches_type(SyncCursorPage[SettlementDetail], settlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_details(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_date` but received ''"):
            client.reports.settlement.with_raw_response.list_details(
                report_date="",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        settlement = response.parse()
        assert_matches_type(SettlementReport, settlement, path=["response"])

    @parametrize
    def test_streaming_response_summary(self, client: Lithic) -> None:
        with client.reports.settlement.with_streaming_response.summary(
            parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            settlement = response.parse()
            assert_matches_type(SettlementReport, settlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_summary(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_date` but received ''"):
            client.reports.settlement.with_raw_response.summary(
                "",
            )


class TestAsyncSettlement:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list_details(self, async_client: AsyncLithic) -> None:
        settlement = await async_client.reports.settlement.list_details(
            report_date=parse_date("2023-09-01"),
        )
        assert_matches_type(AsyncCursorPage[SettlementDetail], settlement, path=["response"])

    @parametrize
    async def test_method_list_details_with_all_params(self, async_client: AsyncLithic) -> None:
        settlement = await async_client.reports.settlement.list_details(
            report_date=parse_date("2023-09-01"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(AsyncCursorPage[SettlementDetail], settlement, path=["response"])

    @parametrize
    async def test_raw_response_list_details(self, async_client: AsyncLithic) -> None:
        response = await async_client.reports.settlement.with_raw_response.list_details(
            report_date=parse_date("2023-09-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        settlement = response.parse()
        assert_matches_type(AsyncCursorPage[SettlementDetail], settlement, path=["response"])

    @parametrize
    async def test_streaming_response_list_details(self, async_client: AsyncLithic) -> None:
        async with async_client.reports.settlement.with_streaming_response.list_details(
            report_date=parse_date("2023-09-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            settlement = await response.parse()
            assert_matches_type(AsyncCursorPage[SettlementDetail], settlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_details(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_date` but received ''"):
            await async_client.reports.settlement.with_raw_response.list_details(
                report_date="",
            )

    @parametrize
    async def test_method_summary(self, async_client: AsyncLithic) -> None:
        settlement = await async_client.reports.settlement.summary(
            parse_date("2019-12-27"),
        )
        assert_matches_type(SettlementReport, settlement, path=["response"])

    @parametrize
    async def test_raw_response_summary(self, async_client: AsyncLithic) -> None:
        response = await async_client.reports.settlement.with_raw_response.summary(
            parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        settlement = response.parse()
        assert_matches_type(SettlementReport, settlement, path=["response"])

    @parametrize
    async def test_streaming_response_summary(self, async_client: AsyncLithic) -> None:
        async with async_client.reports.settlement.with_streaming_response.summary(
            parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            settlement = await response.parse()
            assert_matches_type(SettlementReport, settlement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_summary(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_date` but received ''"):
            await async_client.reports.settlement.with_raw_response.summary(
                "",
            )
