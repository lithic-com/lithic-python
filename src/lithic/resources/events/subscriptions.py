# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from ...types import EventSubscription
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.events import (
    SubscriptionRetrieveSecretResponse,
    subscription_list_params,
    subscription_create_params,
    subscription_update_params,
)

__all__ = ["Subscriptions", "AsyncSubscriptions"]


class Subscriptions(SyncAPIResource):
    def create(
        self,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        event_types: List[Literal["dispute.updated", "digital_wallet.tokenization_approval_request"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Create a new event subscription.

        Args:
          url: URL to which event webhooks will be sent. URL must be a valid HTTPS address.

          description: Event subscription description.

          disabled: Whether the event subscription is active (false) or inactive (true).

          event_types: Indicates types of events that will be sent to this subscription. If left blank,
              all types will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/event_subscriptions",
            body=maybe_transform(
                {
                    "description": description,
                    "disabled": disabled,
                    "event_types": event_types,
                    "url": url,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=EventSubscription,
        )

    def retrieve(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> EventSubscription:
        """Get an event subscription."""
        return self._get(
            f"/event_subscriptions/{event_subscription_token}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=EventSubscription,
        )

    def update(
        self,
        event_subscription_token: str,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        event_types: List[Literal["dispute.updated", "digital_wallet.tokenization_approval_request"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Update an event subscription.

        Args:
          url: URL to which event webhooks will be sent. URL must be a valid HTTPS address.

          description: Event subscription description.

          disabled: Whether the event subscription is active (false) or inactive (true).

          event_types: Indicates types of events that will be sent to this subscription. If left blank,
              all types will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/event_subscriptions/{event_subscription_token}",
            body=maybe_transform(
                {
                    "description": description,
                    "disabled": disabled,
                    "event_types": event_types,
                    "url": url,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=EventSubscription,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncCursorPage[EventSubscription]:
        """
        List all the event subscriptions.

        Args:
          ending_before: The unique identifier of the first item in the previous page. Used to retrieve
              the previous page.

          page_size: Page size (for pagination).

          starting_after: The unique identifier of the last item in the previous page. Used to retrieve
              the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/event_subscriptions",
            page=SyncCursorPage[EventSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "ending_before": ending_before,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=EventSubscription,
        )

    def delete(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> None:
        """Delete an event subscription."""
        return self._delete(
            f"/event_subscriptions/{event_subscription_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def recover(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> None:
        """Resend all failed messages since a given time."""
        return self._post(
            f"/event_subscriptions/{event_subscription_token}/recover",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def replay_missing(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> None:
        """Replays messages to the endpoint.

        Only messages that were created after `begin`
        will be sent. Messages that were previously sent to the endpoint are not resent.
        """
        return self._post(
            f"/event_subscriptions/{event_subscription_token}/replay_missing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def retrieve_secret(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SubscriptionRetrieveSecretResponse:
        """Get the secret for an event subscription."""
        return self._get(
            f"/event_subscriptions/{event_subscription_token}/secret",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=SubscriptionRetrieveSecretResponse,
        )

    def rotate_secret(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> None:
        """Rotate the secret for an event subscription.

        The previous secret will be valid
        for the next 24 hours.
        """
        return self._post(
            f"/event_subscriptions/{event_subscription_token}/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncSubscriptions(AsyncAPIResource):
    async def create(
        self,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        event_types: List[Literal["dispute.updated", "digital_wallet.tokenization_approval_request"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Create a new event subscription.

        Args:
          url: URL to which event webhooks will be sent. URL must be a valid HTTPS address.

          description: Event subscription description.

          disabled: Whether the event subscription is active (false) or inactive (true).

          event_types: Indicates types of events that will be sent to this subscription. If left blank,
              all types will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/event_subscriptions",
            body=maybe_transform(
                {
                    "description": description,
                    "disabled": disabled,
                    "event_types": event_types,
                    "url": url,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=EventSubscription,
        )

    async def retrieve(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> EventSubscription:
        """Get an event subscription."""
        return await self._get(
            f"/event_subscriptions/{event_subscription_token}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=EventSubscription,
        )

    async def update(
        self,
        event_subscription_token: str,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        event_types: List[Literal["dispute.updated", "digital_wallet.tokenization_approval_request"]]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> EventSubscription:
        """
        Update an event subscription.

        Args:
          url: URL to which event webhooks will be sent. URL must be a valid HTTPS address.

          description: Event subscription description.

          disabled: Whether the event subscription is active (false) or inactive (true).

          event_types: Indicates types of events that will be sent to this subscription. If left blank,
              all types will be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/event_subscriptions/{event_subscription_token}",
            body=maybe_transform(
                {
                    "description": description,
                    "disabled": disabled,
                    "event_types": event_types,
                    "url": url,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=EventSubscription,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[EventSubscription, AsyncCursorPage[EventSubscription]]:
        """
        List all the event subscriptions.

        Args:
          ending_before: The unique identifier of the first item in the previous page. Used to retrieve
              the previous page.

          page_size: Page size (for pagination).

          starting_after: The unique identifier of the last item in the previous page. Used to retrieve
              the next page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/event_subscriptions",
            page=AsyncCursorPage[EventSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query=maybe_transform(
                    {
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "ending_before": ending_before,
                    },
                    subscription_list_params.SubscriptionListParams,
                ),
            ),
            model=EventSubscription,
        )

    async def delete(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> None:
        """Delete an event subscription."""
        return await self._delete(
            f"/event_subscriptions/{event_subscription_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def recover(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> None:
        """Resend all failed messages since a given time."""
        return await self._post(
            f"/event_subscriptions/{event_subscription_token}/recover",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def replay_missing(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> None:
        """Replays messages to the endpoint.

        Only messages that were created after `begin`
        will be sent. Messages that were previously sent to the endpoint are not resent.
        """
        return await self._post(
            f"/event_subscriptions/{event_subscription_token}/replay_missing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def retrieve_secret(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SubscriptionRetrieveSecretResponse:
        """Get the secret for an event subscription."""
        return await self._get(
            f"/event_subscriptions/{event_subscription_token}/secret",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=SubscriptionRetrieveSecretResponse,
        )

    async def rotate_secret(
        self,
        event_subscription_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        idempotency_key: str | None = None,
    ) -> None:
        """Rotate the secret for an event subscription.

        The previous secret will be valid
        for the next 24 hours.
        """
        return await self._post(
            f"/event_subscriptions/{event_subscription_token}/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )
