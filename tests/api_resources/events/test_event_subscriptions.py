# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEventSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_resend(self, client: Lithic) -> None:
        event_subscription = client.events.event_subscriptions.resend(
            event_subscription_token="event_subscription_token",
            event_token="event_token",
        )
        assert event_subscription is None

    @parametrize
    def test_raw_response_resend(self, client: Lithic) -> None:
        response = client.events.event_subscriptions.with_raw_response.resend(
            event_subscription_token="event_subscription_token",
            event_token="event_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_subscription = response.parse()
        assert event_subscription is None

    @parametrize
    def test_streaming_response_resend(self, client: Lithic) -> None:
        with client.events.event_subscriptions.with_streaming_response.resend(
            event_subscription_token="event_subscription_token",
            event_token="event_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_subscription = response.parse()
            assert event_subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resend(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_token` but received ''"):
            client.events.event_subscriptions.with_raw_response.resend(
                event_subscription_token="event_subscription_token",
                event_token="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            client.events.event_subscriptions.with_raw_response.resend(
                event_subscription_token="",
                event_token="event_token",
            )


class TestAsyncEventSubscriptions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_resend(self, async_client: AsyncLithic) -> None:
        event_subscription = await async_client.events.event_subscriptions.resend(
            event_subscription_token="event_subscription_token",
            event_token="event_token",
        )
        assert event_subscription is None

    @parametrize
    async def test_raw_response_resend(self, async_client: AsyncLithic) -> None:
        response = await async_client.events.event_subscriptions.with_raw_response.resend(
            event_subscription_token="event_subscription_token",
            event_token="event_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event_subscription = response.parse()
        assert event_subscription is None

    @parametrize
    async def test_streaming_response_resend(self, async_client: AsyncLithic) -> None:
        async with async_client.events.event_subscriptions.with_streaming_response.resend(
            event_subscription_token="event_subscription_token",
            event_token="event_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event_subscription = await response.parse()
            assert event_subscription is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resend(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_token` but received ''"):
            await async_client.events.event_subscriptions.with_raw_response.resend(
                event_subscription_token="event_subscription_token",
                event_token="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `event_subscription_token` but received ''"
        ):
            await async_client.events.event_subscriptions.with_raw_response.resend(
                event_subscription_token="",
                event_token="event_token",
            )
