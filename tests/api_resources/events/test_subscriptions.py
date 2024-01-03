# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import MessageAttempt, EventSubscription
from lithic._utils import parse_datetime
from lithic._client import Lithic, AsyncLithic
from lithic.pagination import SyncCursorPage, AsyncCursorPage
from lithic.types.events import (
    SubscriptionRetrieveSecretResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


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
            event_types=["account_holder.created", "account_holder.updated", "account_holder.verification"],
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.events.subscriptions.with_raw_response.create(
            url="https://example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.retrieve(
            "string",
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.events.subscriptions.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
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
            event_types=["account_holder.created", "account_holder.updated", "account_holder.verification"],
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.events.subscriptions.with_raw_response.update(
            "string",
            url="https://example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
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

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.events.subscriptions.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
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
    def test_raw_response_delete(self, client: Lithic) -> None:
        response = client.events.subscriptions.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    def test_method_list_attempts(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.list_attempts(
            "string",
        )
        assert_matches_type(SyncCursorPage[MessageAttempt], subscription, path=["response"])

    @parametrize
    def test_method_list_attempts_with_all_params(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.list_attempts(
            "string",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            page_size=1,
            starting_after="string",
            status="FAILED",
        )
        assert_matches_type(SyncCursorPage[MessageAttempt], subscription, path=["response"])

    @parametrize
    def test_raw_response_list_attempts(self, client: Lithic) -> None:
        response = client.events.subscriptions.with_raw_response.list_attempts(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncCursorPage[MessageAttempt], subscription, path=["response"])

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
    def test_raw_response_recover(self, client: Lithic) -> None:
        response = client.events.subscriptions.with_raw_response.recover(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
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

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_raw_response_replay_missing(self, client: Lithic) -> None:
        response = client.events.subscriptions.with_raw_response.replay_missing(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    def test_method_retrieve_secret(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.retrieve_secret(
            "string",
        )
        assert_matches_type(SubscriptionRetrieveSecretResponse, subscription, path=["response"])

    @parametrize
    def test_raw_response_retrieve_secret(self, client: Lithic) -> None:
        response = client.events.subscriptions.with_raw_response.retrieve_secret(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionRetrieveSecretResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_method_rotate_secret(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.rotate_secret(
            "string",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_raw_response_rotate_secret(self, client: Lithic) -> None:
        response = client.events.subscriptions.with_raw_response.rotate_secret(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    def test_method_send_simulated_example(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.send_simulated_example(
            "string",
        )
        assert subscription is None

    @parametrize
    def test_method_send_simulated_example_with_all_params(self, client: Lithic) -> None:
        subscription = client.events.subscriptions.send_simulated_example(
            "string",
            event_type="account_holder.created",
        )
        assert subscription is None

    @parametrize
    def test_raw_response_send_simulated_example(self, client: Lithic) -> None:
        response = client.events.subscriptions.with_raw_response.send_simulated_example(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
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
            event_types=["account_holder.created", "account_holder.updated", "account_holder.verification"],
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncLithic) -> None:
        response = await client.events.subscriptions.with_raw_response.create(
            url="https://example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.retrieve(
            "string",
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncLithic) -> None:
        response = await client.events.subscriptions.with_raw_response.retrieve(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
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
            event_types=["account_holder.created", "account_holder.updated", "account_holder.verification"],
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncLithic) -> None:
        response = await client.events.subscriptions.with_raw_response.update(
            "string",
            url="https://example.com",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
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

    @parametrize
    async def test_raw_response_list(self, client: AsyncLithic) -> None:
        response = await client.events.subscriptions.with_raw_response.list()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
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
    async def test_raw_response_delete(self, client: AsyncLithic) -> None:
        response = await client.events.subscriptions.with_raw_response.delete(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    async def test_method_list_attempts(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.list_attempts(
            "string",
        )
        assert_matches_type(AsyncCursorPage[MessageAttempt], subscription, path=["response"])

    @parametrize
    async def test_method_list_attempts_with_all_params(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.list_attempts(
            "string",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            page_size=1,
            starting_after="string",
            status="FAILED",
        )
        assert_matches_type(AsyncCursorPage[MessageAttempt], subscription, path=["response"])

    @parametrize
    async def test_raw_response_list_attempts(self, client: AsyncLithic) -> None:
        response = await client.events.subscriptions.with_raw_response.list_attempts(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(AsyncCursorPage[MessageAttempt], subscription, path=["response"])

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
    async def test_raw_response_recover(self, client: AsyncLithic) -> None:
        response = await client.events.subscriptions.with_raw_response.recover(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
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

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_raw_response_replay_missing(self, client: AsyncLithic) -> None:
        response = await client.events.subscriptions.with_raw_response.replay_missing(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    async def test_method_retrieve_secret(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.retrieve_secret(
            "string",
        )
        assert_matches_type(SubscriptionRetrieveSecretResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_secret(self, client: AsyncLithic) -> None:
        response = await client.events.subscriptions.with_raw_response.retrieve_secret(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionRetrieveSecretResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_rotate_secret(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.rotate_secret(
            "string",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_raw_response_rotate_secret(self, client: AsyncLithic) -> None:
        response = await client.events.subscriptions.with_raw_response.rotate_secret(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    async def test_method_send_simulated_example(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.send_simulated_example(
            "string",
        )
        assert subscription is None

    @parametrize
    async def test_method_send_simulated_example_with_all_params(self, client: AsyncLithic) -> None:
        subscription = await client.events.subscriptions.send_simulated_example(
            "string",
            event_type="account_holder.created",
        )
        assert subscription is None

    @parametrize
    async def test_raw_response_send_simulated_example(self, client: AsyncLithic) -> None:
        response = await client.events.subscriptions.with_raw_response.send_simulated_example(
            "string",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None
