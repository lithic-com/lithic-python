# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import Event, MessageAttempt
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        event = client.events.retrieve(
            "event_token",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.events.with_raw_response.retrieve(
            "event_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.events.with_streaming_response.retrieve(
            "event_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_token` but received ''"):
            client.events.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        event = client.events.list()
        assert_matches_type(SyncCursorPage[Event], event, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        event = client.events.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            event_types=["account_holder.created"],
            page_size=1,
            starting_after="starting_after",
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
            event_token="event_token",
        )
        assert_matches_type(SyncCursorPage[MessageAttempt], event, path=["response"])

    @parametrize
    def test_method_list_attempts_with_all_params(self, client: Lithic) -> None:
        event = client.events.list_attempts(
            event_token="event_token",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
            status="FAILED",
        )
        assert_matches_type(SyncCursorPage[MessageAttempt], event, path=["response"])

    @parametrize
    def test_raw_response_list_attempts(self, client: Lithic) -> None:
        response = client.events.with_raw_response.list_attempts(
            event_token="event_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(SyncCursorPage[MessageAttempt], event, path=["response"])

    @parametrize
    def test_streaming_response_list_attempts(self, client: Lithic) -> None:
        with client.events.with_streaming_response.list_attempts(
            event_token="event_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(SyncCursorPage[MessageAttempt], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_attempts(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_token` but received ''"):
            client.events.with_raw_response.list_attempts(
                event_token="",
            )

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    def test_method_resend(self, client: Lithic) -> None:
        client.events.resend(
            "string",
            event_subscription_token="string",
        )


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        event = await async_client.events.retrieve(
            "event_token",
        )
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.with_raw_response.retrieve(
            "event_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(Event, event, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.events.with_streaming_response.retrieve(
            "event_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(Event, event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_token` but received ''"):
            await async_client.events.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        event = await async_client.events.list()
        assert_matches_type(AsyncCursorPage[Event], event, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        event = await async_client.events.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            event_types=["account_holder.created"],
            page_size=1,
            starting_after="starting_after",
            with_content=True,
        )
        assert_matches_type(AsyncCursorPage[Event], event, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(AsyncCursorPage[Event], event, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.events.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncCursorPage[Event], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_attempts(self, async_client: AsyncLithic) -> None:
        event = await async_client.events.list_attempts(
            event_token="event_token",
        )
        assert_matches_type(AsyncCursorPage[MessageAttempt], event, path=["response"])

    @parametrize
    async def test_method_list_attempts_with_all_params(self, async_client: AsyncLithic) -> None:
        event = await async_client.events.list_attempts(
            event_token="event_token",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
            status="FAILED",
        )
        assert_matches_type(AsyncCursorPage[MessageAttempt], event, path=["response"])

    @parametrize
    async def test_raw_response_list_attempts(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.with_raw_response.list_attempts(
            event_token="event_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(AsyncCursorPage[MessageAttempt], event, path=["response"])

    @parametrize
    async def test_streaming_response_list_attempts(self, async_client: AsyncLithic) -> None:
        async with async_client.events.with_streaming_response.list_attempts(
            event_token="event_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(AsyncCursorPage[MessageAttempt], event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_attempts(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_token` but received ''"):
            await async_client.events.with_raw_response.list_attempts(
                event_token="",
            )

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    async def test_method_resend(self, async_client: AsyncLithic) -> None:
        await async_client.events.resend(
            "string",
            event_subscription_token="string",
        )
