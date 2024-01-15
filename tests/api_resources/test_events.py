# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import Event, MessageAttempt
from lithic._utils import parse_datetime
from lithic._client import Lithic, AsyncLithic
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestEvents:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        event = client.events.retrieve(
            "string",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.events.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.events.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        event = client.events.list()
        assert_matches_type(SyncCursorPage[Event], event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        event = client.events.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            event_types=["account_holder.created", "account_holder.updated", "account_holder.verification"],
            page_size=1,
            starting_after="string",
            with_content=True,
        )
        assert_matches_type(SyncCursorPage[Event], event, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncCursorPage[Event], event, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncCursorPage[Event], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_attempts(self, client: Lithic) -> None:
        event = client.events.list_attempts(
            "string",
        )
        assert_matches_type(SyncCursorPage[MessageAttempt], event, path=["response"])

    @parametrize
    def test_method_list_attempts_with_all_params(self, client: Lithic) -> None:
        event = client.events.list_attempts(
            "string",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            page_size=1,
            starting_after="string",
            status="FAILED",
        )
        assert_matches_type(SyncCursorPage[MessageAttempt], event, path=["response"])

    @parametrize
    def test_raw_response_list_attempts(self, client: Lithic) -> None:
        response = client.events.with_raw_response.list_attempts(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncCursorPage[MessageAttempt], event, path=["response"])

    @parametrize
    def test_streaming_response_list_attempts(self, client: Lithic) -> None:
        with client.events.with_streaming_response.list_attempts(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncCursorPage[MessageAttempt], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    def test_method_resend(self) -> None:
        self.strict_client.events.resend(
            "string",
            event_subscription_token="string",
        )


class TestAsyncEvents:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        event = await client.events.retrieve(
            "string",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncLithic) -> None:
        response = await client.events.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncLithic) -> None:
        async with client.events.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        event = await client.events.list()
        assert_matches_type(AsyncCursorPage[Event], event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        event = await client.events.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            event_types=["account_holder.created", "account_holder.updated", "account_holder.verification"],
            page_size=1,
            starting_after="string",
            with_content=True,
        )
        assert_matches_type(AsyncCursorPage[Event], event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, client: AsyncLithic) -> None:
        response = await client.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(AsyncCursorPage[Event], event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, client: AsyncLithic) -> None:
        async with client.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncCursorPage[Event], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_attempts(self, client: AsyncLithic) -> None:
        event = await client.events.list_attempts(
            "string",
        )
        assert_matches_type(AsyncCursorPage[MessageAttempt], event, path=["response"])

    @parametrize
    async def test_method_list_attempts_with_all_params(self, client: AsyncLithic) -> None:
        event = await client.events.list_attempts(
            "string",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            page_size=1,
            starting_after="string",
            status="FAILED",
        )
        assert_matches_type(AsyncCursorPage[MessageAttempt], event, path=["response"])

    @parametrize
    async def test_raw_response_list_attempts(self, client: AsyncLithic) -> None:
        response = await client.events.with_raw_response.list_attempts(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(AsyncCursorPage[MessageAttempt], event, path=["response"])

    @parametrize
    async def test_streaming_response_list_attempts(self, client: AsyncLithic) -> None:
        async with client.events.with_streaming_response.list_attempts(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncCursorPage[MessageAttempt], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    async def test_method_resend(self) -> None:
        await self.strict_client.events.resend(
            "string",
            event_subscription_token="string",
        )
