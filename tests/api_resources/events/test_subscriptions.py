# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import EventSubscription
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage
from lithic.types.events import SubscriptionRetrieveSecretResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestSubscriptions:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.create(
            url="https://example.com",
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.create(
            url="https://example.com",
            description="string",
            disabled=True,
            event_types=["card.created", "card.created", "card.created"],
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.retrieve(
            "string",
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.update(
            "string",
            url="https://example.com",
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.update(
            "string",
            url="https://example.com",
            description="string",
            disabled=True,
            event_types=["card.created", "card.created", "card.created"],
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.list()
        assert_matches_type(SyncCursorPage[EventSubscription], subscription, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.list(
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(SyncCursorPage[EventSubscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_method_delete(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.delete(
            "string",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_method_recover(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.recover(
            "string",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_method_recover_with_all_params(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.recover(
            "string",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_method_replay_missing(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.replay_missing(
            "string",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_method_replay_missing_with_all_params(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.replay_missing(
            "string",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert subscription is None

    @parametrize
    def test_method_retrieve_secret(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.retrieve_secret(
            "string",
        )
        assert_matches_type(SubscriptionRetrieveSecretResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_method_rotate_secret(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.rotate_secret(
            "string",
        )
        assert subscription is None


class TestAsyncSubscriptions:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.create(
            url="https://example.com",
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.create(
            url="https://example.com",
            description="string",
            disabled=True,
            event_types=["card.created", "card.created", "card.created"],
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.retrieve(
            "string",
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.update(
            "string",
            url="https://example.com",
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.update(
            "string",
            url="https://example.com",
            description="string",
            disabled=True,
            event_types=["card.created", "card.created", "card.created"],
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.list()
        assert_matches_type(AsyncCursorPage[EventSubscription], subscription, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.list(
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(AsyncCursorPage[EventSubscription], subscription, path=["response"])

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_delete(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.delete(
            "string",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_recover(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.recover(
            "string",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_recover_with_all_params(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.recover(
            "string",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_replay_missing(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.replay_missing(
            "string",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_replay_missing_with_all_params(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.replay_missing(
            "string",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert subscription is None

    @parametrize
    async def test_method_retrieve_secret(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.retrieve_secret(
            "string",
        )
        assert_matches_type(SubscriptionRetrieveSecretResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_rotate_secret(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.rotate_secret(
            "string",
        )
        assert subscription is None
