# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic._utils import parse_date, parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage
from lithic.types.reports.settlement import (
    NetworkTotalListResponse,
    NetworkTotalRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNetworkTotals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        network_total = client.reports.settlement.network_totals.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NetworkTotalRetrieveResponse, network_total, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.reports.settlement.network_totals.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_total = response.parse()
        assert_matches_type(NetworkTotalRetrieveResponse, network_total, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.reports.settlement.network_totals.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_total = response.parse()
            assert_matches_type(NetworkTotalRetrieveResponse, network_total, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            client.reports.settlement.network_totals.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        network_total = client.reports.settlement.network_totals.list()
        assert_matches_type(SyncCursorPage[NetworkTotalListResponse], network_total, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        network_total = client.reports.settlement.network_totals.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            institution_id="institution_id",
            network="VISA",
            page_size=1,
            report_date=parse_date("2019-12-27"),
            report_date_begin=parse_date("2019-12-27"),
            report_date_end=parse_date("2019-12-27"),
            settlement_institution_id="settlement_institution_id",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[NetworkTotalListResponse], network_total, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.reports.settlement.network_totals.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_total = response.parse()
        assert_matches_type(SyncCursorPage[NetworkTotalListResponse], network_total, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.reports.settlement.network_totals.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_total = response.parse()
            assert_matches_type(SyncCursorPage[NetworkTotalListResponse], network_total, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNetworkTotals:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        network_total = await async_client.reports.settlement.network_totals.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(NetworkTotalRetrieveResponse, network_total, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.reports.settlement.network_totals.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_total = response.parse()
        assert_matches_type(NetworkTotalRetrieveResponse, network_total, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.reports.settlement.network_totals.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_total = await response.parse()
            assert_matches_type(NetworkTotalRetrieveResponse, network_total, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token` but received ''"):
            await async_client.reports.settlement.network_totals.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        network_total = await async_client.reports.settlement.network_totals.list()
        assert_matches_type(AsyncCursorPage[NetworkTotalListResponse], network_total, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        network_total = await async_client.reports.settlement.network_totals.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            institution_id="institution_id",
            network="VISA",
            page_size=1,
            report_date=parse_date("2019-12-27"),
            report_date_begin=parse_date("2019-12-27"),
            report_date_end=parse_date("2019-12-27"),
            settlement_institution_id="settlement_institution_id",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[NetworkTotalListResponse], network_total, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.reports.settlement.network_totals.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network_total = response.parse()
        assert_matches_type(AsyncCursorPage[NetworkTotalListResponse], network_total, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.reports.settlement.network_totals.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network_total = await response.parse()
            assert_matches_type(AsyncCursorPage[NetworkTotalListResponse], network_total, path=["response"])

        assert cast(Any, response.is_closed) is True
