# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import Event, MessageAttempt
from lithic._utils import parse_datetime
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

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    async def test_method_resend(self) -> None:
        await self.strict_client.events.resend(
            "string",
            event_subscription_token="string",
        )
