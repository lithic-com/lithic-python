# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from lithic.types import Event
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestEvents:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        resource = client.events.retrieve(
            "string",
        )
        assert isinstance(resource, Event)

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        resource = client.events.list()
        assert isinstance(resource, SyncCursorPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        resource = client.events.list(
            begin="2019-12-27T18:11:19.117Z",
            end="2019-12-27T18:11:19.117Z",
            page_size=1,
            starting_after="string",
            ending_before="string",
            event_types=["dispute.updated", "dispute.updated", "dispute.updated"],
        )
        assert isinstance(resource, SyncCursorPage)

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
        resource = await client.events.retrieve(
            "string",
        )
        assert isinstance(resource, Event)

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        resource = await client.events.list()
        assert isinstance(resource, AsyncCursorPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        resource = await client.events.list(
            begin="2019-12-27T18:11:19.117Z",
            end="2019-12-27T18:11:19.117Z",
            page_size=1,
            starting_after="string",
            ending_before="string",
            event_types=["dispute.updated", "dispute.updated", "dispute.updated"],
        )
        assert isinstance(resource, AsyncCursorPage)

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    async def test_method_resend(self) -> None:
        await self.strict_client.events.resend(
            "string",
            event_subscription_token="string",
        )
