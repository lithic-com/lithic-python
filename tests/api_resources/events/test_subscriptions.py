# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage
from lithic.types.message_attempt import MessageAttempt
from lithic.types.event_subscription import EventSubscription
from lithic.types.events.subscription_retrieve_secret_response import SubscriptionRetrieveSecretResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.events.subscriptions.with_streaming_response.create(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(EventSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.events.subscriptions.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(EventSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            client.events.subscriptions.with_raw_response.retrieve(
                "",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.events.subscriptions.with_streaming_response.update(
            "string",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(EventSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            client.events.subscriptions.with_raw_response.update(
                "",
                url="https://example.com",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncCursorPage[EventSubscription], subscription, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.events.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SyncCursorPage[EventSubscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_streaming_response_delete(self, client: Lithic) -> None:
        with client.events.subscriptions.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_path_params_delete(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            client.events.subscriptions.with_raw_response.delete(
                "",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SyncCursorPage[MessageAttempt], subscription, path=["response"])

    @parametrize
    def test_streaming_response_list_attempts(self, client: Lithic) -> None:
        with client.events.subscriptions.with_streaming_response.list_attempts(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SyncCursorPage[MessageAttempt], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_attempts(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            client.events.subscriptions.with_raw_response.list_attempts(
                "",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_streaming_response_recover(self, client: Lithic) -> None:
        with client.events.subscriptions.with_streaming_response.recover(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_path_params_recover(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            client.events.subscriptions.with_raw_response.recover(
                "",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_streaming_response_replay_missing(self, client: Lithic) -> None:
        with client.events.subscriptions.with_streaming_response.replay_missing(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_path_params_replay_missing(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            client.events.subscriptions.with_raw_response.replay_missing(
                "",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionRetrieveSecretResponse, subscription, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_secret(self, client: Lithic) -> None:
        with client.events.subscriptions.with_streaming_response.retrieve_secret(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionRetrieveSecretResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_secret(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            client.events.subscriptions.with_raw_response.retrieve_secret(
                "",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_streaming_response_rotate_secret(self, client: Lithic) -> None:
        with client.events.subscriptions.with_streaming_response.rotate_secret(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_path_params_rotate_secret(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            client.events.subscriptions.with_raw_response.rotate_secret(
                "",
            )

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

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    def test_streaming_response_send_simulated_example(self, client: Lithic) -> None:
        with client.events.subscriptions.with_streaming_response.send_simulated_example(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_send_simulated_example(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            client.events.subscriptions.with_raw_response.send_simulated_example(
                "",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.create(
            url="https://example.com",
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.create(
            url="https://example.com",
            description="string",
            disabled=True,
            event_types=["account_holder.created", "account_holder.updated", "account_holder.verification"],
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.subscriptions.with_raw_response.create(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.events.subscriptions.with_streaming_response.create(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(EventSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.retrieve(
            "string",
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.subscriptions.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.events.subscriptions.with_streaming_response.retrieve(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(EventSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            await async_client.events.subscriptions.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.update(
            "string",
            url="https://example.com",
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.update(
            "string",
            url="https://example.com",
            description="string",
            disabled=True,
            event_types=["account_holder.created", "account_holder.updated", "account_holder.verification"],
        )
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.subscriptions.with_raw_response.update(
            "string",
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(EventSubscription, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLithic) -> None:
        async with async_client.events.subscriptions.with_streaming_response.update(
            "string",
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(EventSubscription, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            await async_client.events.subscriptions.with_raw_response.update(
                "",
                url="https://example.com",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.list()
        assert_matches_type(AsyncCursorPage[EventSubscription], subscription, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.list(
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(AsyncCursorPage[EventSubscription], subscription, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.subscriptions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(AsyncCursorPage[EventSubscription], subscription, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.events.subscriptions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(AsyncCursorPage[EventSubscription], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.delete(
            "string",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.subscriptions.with_raw_response.delete(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLithic) -> None:
        async with async_client.events.subscriptions.with_streaming_response.delete(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            await async_client.events.subscriptions.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_list_attempts(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.list_attempts(
            "string",
        )
        assert_matches_type(AsyncCursorPage[MessageAttempt], subscription, path=["response"])

    @parametrize
    async def test_method_list_attempts_with_all_params(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.list_attempts(
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
    async def test_raw_response_list_attempts(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.subscriptions.with_raw_response.list_attempts(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(AsyncCursorPage[MessageAttempt], subscription, path=["response"])

    @parametrize
    async def test_streaming_response_list_attempts(self, async_client: AsyncLithic) -> None:
        async with async_client.events.subscriptions.with_streaming_response.list_attempts(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(AsyncCursorPage[MessageAttempt], subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_attempts(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            await async_client.events.subscriptions.with_raw_response.list_attempts(
                "",
            )

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_recover(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.recover(
            "string",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_recover_with_all_params(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.recover(
            "string",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_raw_response_recover(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.subscriptions.with_raw_response.recover(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_streaming_response_recover(self, async_client: AsyncLithic) -> None:
        async with async_client.events.subscriptions.with_streaming_response.recover(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_path_params_recover(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            await async_client.events.subscriptions.with_raw_response.recover(
                "",
            )

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_replay_missing(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.replay_missing(
            "string",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_replay_missing_with_all_params(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.replay_missing(
            "string",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_raw_response_replay_missing(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.subscriptions.with_raw_response.replay_missing(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_streaming_response_replay_missing(self, async_client: AsyncLithic) -> None:
        async with async_client.events.subscriptions.with_streaming_response.replay_missing(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_path_params_replay_missing(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            await async_client.events.subscriptions.with_raw_response.replay_missing(
                "",
            )

    @parametrize
    async def test_method_retrieve_secret(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.retrieve_secret(
            "string",
        )
        assert_matches_type(SubscriptionRetrieveSecretResponse, subscription, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_secret(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.subscriptions.with_raw_response.retrieve_secret(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionRetrieveSecretResponse, subscription, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_secret(self, async_client: AsyncLithic) -> None:
        async with async_client.events.subscriptions.with_streaming_response.retrieve_secret(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionRetrieveSecretResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_secret(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            await async_client.events.subscriptions.with_raw_response.retrieve_secret(
                "",
            )

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_rotate_secret(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.rotate_secret(
            "string",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_raw_response_rotate_secret(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.subscriptions.with_raw_response.rotate_secret(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_streaming_response_rotate_secret(self, async_client: AsyncLithic) -> None:
        async with async_client.events.subscriptions.with_streaming_response.rotate_secret(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_path_params_rotate_secret(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            await async_client.events.subscriptions.with_raw_response.rotate_secret(
                "",
            )

    @parametrize
    async def test_method_send_simulated_example(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.send_simulated_example(
            "string",
        )
        assert subscription is None

    @parametrize
    async def test_method_send_simulated_example_with_all_params(self, async_client: AsyncLithic) -> None:
        subscription = await async_client.events.subscriptions.send_simulated_example(
            "string",
            event_type="account_holder.created",
        )
        assert subscription is None

    @parametrize
    async def test_raw_response_send_simulated_example(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.subscriptions.with_raw_response.send_simulated_example(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @parametrize
    async def test_streaming_response_send_simulated_example(self, async_client: AsyncLithic) -> None:
        async with async_client.events.subscriptions.with_streaming_response.send_simulated_example(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_send_simulated_example(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            await async_client.events.subscriptions.with_raw_response.send_simulated_example(
                "",
            )
