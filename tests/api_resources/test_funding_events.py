# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    FundingEventListResponse,
    FundingEventRetrieveResponse,
    FundingEventRetrieveDetailsResponse,
)
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFundingEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        funding_event = client.funding_events.retrieve(
            "funding_event_token",
        )
        assert_matches_type(FundingEventRetrieveResponse, funding_event, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.funding_events.with_raw_response.retrieve(
            "funding_event_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        funding_event = response.parse()
        assert_matches_type(FundingEventRetrieveResponse, funding_event, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.funding_events.with_streaming_response.retrieve(
            "funding_event_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            funding_event = response.parse()
            assert_matches_type(FundingEventRetrieveResponse, funding_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `funding_event_token` but received ''"):
            client.funding_events.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        funding_event = client.funding_events.list()
        assert_matches_type(SyncCursorPage[FundingEventListResponse], funding_event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        funding_event = client.funding_events.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(SyncCursorPage[FundingEventListResponse], funding_event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.funding_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        funding_event = response.parse()
        assert_matches_type(SyncCursorPage[FundingEventListResponse], funding_event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.funding_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            funding_event = response.parse()
            assert_matches_type(SyncCursorPage[FundingEventListResponse], funding_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_details(self, client: Lithic) -> None:
        funding_event = client.funding_events.retrieve_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FundingEventRetrieveDetailsResponse, funding_event, path=["response"])

    @parametrize
    def test_raw_response_retrieve_details(self, client: Lithic) -> None:
        response = client.funding_events.with_raw_response.retrieve_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        funding_event = response.parse()
        assert_matches_type(FundingEventRetrieveDetailsResponse, funding_event, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_details(self, client: Lithic) -> None:
        with client.funding_events.with_streaming_response.retrieve_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            funding_event = response.parse()
            assert_matches_type(FundingEventRetrieveDetailsResponse, funding_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_details(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `funding_event_token` but received ''"):
            client.funding_events.with_raw_response.retrieve_details(
                "",
            )


class TestAsyncFundingEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        funding_event = await async_client.funding_events.retrieve(
            "funding_event_token",
        )
        assert_matches_type(FundingEventRetrieveResponse, funding_event, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.funding_events.with_raw_response.retrieve(
            "funding_event_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        funding_event = response.parse()
        assert_matches_type(FundingEventRetrieveResponse, funding_event, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.funding_events.with_streaming_response.retrieve(
            "funding_event_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            funding_event = await response.parse()
            assert_matches_type(FundingEventRetrieveResponse, funding_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `funding_event_token` but received ''"):
            await async_client.funding_events.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        funding_event = await async_client.funding_events.list()
        assert_matches_type(AsyncCursorPage[FundingEventListResponse], funding_event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        funding_event = await async_client.funding_events.list(
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(AsyncCursorPage[FundingEventListResponse], funding_event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.funding_events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        funding_event = response.parse()
        assert_matches_type(AsyncCursorPage[FundingEventListResponse], funding_event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.funding_events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            funding_event = await response.parse()
            assert_matches_type(AsyncCursorPage[FundingEventListResponse], funding_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_details(self, async_client: AsyncLithic) -> None:
        funding_event = await async_client.funding_events.retrieve_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FundingEventRetrieveDetailsResponse, funding_event, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_details(self, async_client: AsyncLithic) -> None:
        response = await async_client.funding_events.with_raw_response.retrieve_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        funding_event = response.parse()
        assert_matches_type(FundingEventRetrieveDetailsResponse, funding_event, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_details(self, async_client: AsyncLithic) -> None:
        async with async_client.funding_events.with_streaming_response.retrieve_details(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            funding_event = await response.parse()
            assert_matches_type(FundingEventRetrieveDetailsResponse, funding_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_details(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `funding_event_token` but received ''"):
            await async_client.funding_events.with_raw_response.retrieve_details(
                "",
            )
