# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import MessageAttempt, EventSubscription
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.events import (
    SubscriptionRetrieveSecretResponse,
    subscription_list_params,
    subscription_create_params,
    subscription_update_params,
    subscription_recover_params,
    subscription_list_attempts_params,
    subscription_replay_missing_params,
    subscription_send_simulated_example_params,
)

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["Subscriptions", "AsyncSubscriptions"]


class Subscriptions(SyncAPIResource):
    with_raw_response: SubscriptionsWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = SubscriptionsWithRawResponse(self)

    def create(
        self,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        event_types: List[
            Literal[
                "account_holder.created",
                "account_holder.updated",
                "account_holder.verification",
                "card.created",
                "card.shipped",
                "card_transaction.updated",
                "digital_wallet.tokenization_approval_request",
                "digital_wallet.tokenization_result",
                "digital_wallet.tokenization_two_factor_authentication_code",
                "dispute.updated",
                "dispute_evidence.upload_failed",
                "three_ds_authentication.created",
                "payment_transaction.created",
                "payment_transaction.updated",
                "transfer_transaction.created",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/event_subscriptions",
            body=maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "disabled": disabled,
                    "event_types": event_types,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventSubscription:
        """
        Get an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/event_subscriptions/{event_subscription_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    def update(
        self,
        event_subscription_token: str,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        event_types: List[
            Literal[
                "account_holder.created",
                "account_holder.updated",
                "account_holder.verification",
                "card.created",
                "card.shipped",
                "card_transaction.updated",
                "digital_wallet.tokenization_approval_request",
                "digital_wallet.tokenization_result",
                "digital_wallet.tokenization_two_factor_authentication_code",
                "dispute.updated",
                "dispute_evidence.upload_failed",
                "three_ds_authentication.created",
                "payment_transaction.created",
                "payment_transaction.updated",
                "transfer_transaction.created",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/event_subscriptions/{event_subscription_token}",
            body=maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "disabled": disabled,
                    "event_types": event_types,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[EventSubscription]:
        """
        List all the event subscriptions.

        Args:
          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/event_subscriptions",
            page=SyncCursorPage[EventSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._delete(
            f"/event_subscriptions/{event_subscription_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def list_attempts(
        self,
        event_subscription_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["FAILED", "PENDING", "SENDING", "SUCCESS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[MessageAttempt]:
        """
        List all the message attempts for a given event subscription.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/event_subscriptions/{event_subscription_token}/attempts",
            page=SyncCursorPage[MessageAttempt],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    subscription_list_attempts_params.SubscriptionListAttemptsParams,
                ),
            ),
            model=MessageAttempt,
        )

    def recover(
        self,
        event_subscription_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Resend all failed messages since a given time.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/event_subscriptions/{event_subscription_token}/recover",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                    },
                    subscription_recover_params.SubscriptionRecoverParams,
                ),
            ),
            cast_to=NoneType,
        )

    def replay_missing(
        self,
        event_subscription_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """Replays messages to the endpoint.

        Only messages that were created after `begin`
        will be sent. Messages that were previously sent to the endpoint are not resent.
        Message will be retried if endpoint responds with a non-2xx status code. See
        [Retry Schedule](https://docs.lithic.com/docs/events-api#retry-schedule) for
        details.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/event_subscriptions/{event_subscription_token}/replay_missing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                    },
                    subscription_replay_missing_params.SubscriptionReplayMissingParams,
                ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionRetrieveSecretResponse:
        """
        Get the secret for an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/event_subscriptions/{event_subscription_token}/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """Rotate the secret for an event subscription.

        The previous secret will be valid
        for the next 24 hours.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/event_subscriptions/{event_subscription_token}/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def send_simulated_example(
        self,
        event_subscription_token: str,
        *,
        event_type: Literal[
            "account_holder.created",
            "account_holder.updated",
            "account_holder.verification",
            "card.created",
            "card.shipped",
            "card_transaction.updated",
            "digital_wallet.tokenization_approval_request",
            "digital_wallet.tokenization_result",
            "digital_wallet.tokenization_two_factor_authentication_code",
            "dispute.updated",
            "dispute_evidence.upload_failed",
            "three_ds_authentication.created",
            "payment_transaction.created",
            "payment_transaction.updated",
            "transfer_transaction.created",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Send an example message for event.

        Args:
          event_type: Event type to send example message for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/simulate/event_subscriptions/{event_subscription_token}/send_example",
            body=maybe_transform(
                {"event_type": event_type},
                subscription_send_simulated_example_params.SubscriptionSendSimulatedExampleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncSubscriptions(AsyncAPIResource):
    with_raw_response: AsyncSubscriptionsWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncSubscriptionsWithRawResponse(self)

    async def create(
        self,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        event_types: List[
            Literal[
                "account_holder.created",
                "account_holder.updated",
                "account_holder.verification",
                "card.created",
                "card.shipped",
                "card_transaction.updated",
                "digital_wallet.tokenization_approval_request",
                "digital_wallet.tokenization_result",
                "digital_wallet.tokenization_two_factor_authentication_code",
                "dispute.updated",
                "dispute_evidence.upload_failed",
                "three_ds_authentication.created",
                "payment_transaction.created",
                "payment_transaction.updated",
                "transfer_transaction.created",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/event_subscriptions",
            body=maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "disabled": disabled,
                    "event_types": event_types,
                },
                subscription_create_params.SubscriptionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EventSubscription:
        """
        Get an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/event_subscriptions/{event_subscription_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EventSubscription,
        )

    async def update(
        self,
        event_subscription_token: str,
        *,
        url: str,
        description: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        event_types: List[
            Literal[
                "account_holder.created",
                "account_holder.updated",
                "account_holder.verification",
                "card.created",
                "card.shipped",
                "card_transaction.updated",
                "digital_wallet.tokenization_approval_request",
                "digital_wallet.tokenization_result",
                "digital_wallet.tokenization_two_factor_authentication_code",
                "dispute.updated",
                "dispute_evidence.upload_failed",
                "three_ds_authentication.created",
                "payment_transaction.created",
                "payment_transaction.updated",
                "transfer_transaction.created",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/event_subscriptions/{event_subscription_token}",
            body=maybe_transform(
                {
                    "url": url,
                    "description": description,
                    "disabled": disabled,
                    "event_types": event_types,
                },
                subscription_update_params.SubscriptionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[EventSubscription, AsyncCursorPage[EventSubscription]]:
        """
        List all the event subscriptions.

        Args:
          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/event_subscriptions",
            page=AsyncCursorPage[EventSubscription],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Delete an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._delete(
            f"/event_subscriptions/{event_subscription_token}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def list_attempts(
        self,
        event_subscription_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["FAILED", "PENDING", "SENDING", "SUCCESS"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[MessageAttempt, AsyncCursorPage[MessageAttempt]]:
        """
        List all the message attempts for a given event subscription.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/event_subscriptions/{event_subscription_token}/attempts",
            page=AsyncCursorPage[MessageAttempt],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    subscription_list_attempts_params.SubscriptionListAttemptsParams,
                ),
            ),
            model=MessageAttempt,
        )

    async def recover(
        self,
        event_subscription_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Resend all failed messages since a given time.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/event_subscriptions/{event_subscription_token}/recover",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                    },
                    subscription_recover_params.SubscriptionRecoverParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def replay_missing(
        self,
        event_subscription_token: str,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """Replays messages to the endpoint.

        Only messages that were created after `begin`
        will be sent. Messages that were previously sent to the endpoint are not resent.
        Message will be retried if endpoint responds with a non-2xx status code. See
        [Retry Schedule](https://docs.lithic.com/docs/events-api#retry-schedule) for
        details.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/event_subscriptions/{event_subscription_token}/replay_missing",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                    },
                    subscription_replay_missing_params.SubscriptionReplayMissingParams,
                ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubscriptionRetrieveSecretResponse:
        """
        Get the secret for an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/event_subscriptions/{event_subscription_token}/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """Rotate the secret for an event subscription.

        The previous secret will be valid
        for the next 24 hours.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/event_subscriptions/{event_subscription_token}/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def send_simulated_example(
        self,
        event_subscription_token: str,
        *,
        event_type: Literal[
            "account_holder.created",
            "account_holder.updated",
            "account_holder.verification",
            "card.created",
            "card.shipped",
            "card_transaction.updated",
            "digital_wallet.tokenization_approval_request",
            "digital_wallet.tokenization_result",
            "digital_wallet.tokenization_two_factor_authentication_code",
            "dispute.updated",
            "dispute_evidence.upload_failed",
            "three_ds_authentication.created",
            "payment_transaction.created",
            "payment_transaction.updated",
            "transfer_transaction.created",
        ]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Send an example message for event.

        Args:
          event_type: Event type to send example message for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/simulate/event_subscriptions/{event_subscription_token}/send_example",
            body=maybe_transform(
                {"event_type": event_type},
                subscription_send_simulated_example_params.SubscriptionSendSimulatedExampleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class SubscriptionsWithRawResponse:
    def __init__(self, subscriptions: Subscriptions) -> None:
        self.create = to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = to_raw_response_wrapper(
            subscriptions.delete,
        )
        self.list_attempts = to_raw_response_wrapper(
            subscriptions.list_attempts,
        )
        self.recover = to_raw_response_wrapper(
            subscriptions.recover,
        )
        self.replay_missing = to_raw_response_wrapper(
            subscriptions.replay_missing,
        )
        self.retrieve_secret = to_raw_response_wrapper(
            subscriptions.retrieve_secret,
        )
        self.rotate_secret = to_raw_response_wrapper(
            subscriptions.rotate_secret,
        )
        self.send_simulated_example = to_raw_response_wrapper(
            subscriptions.send_simulated_example,
        )


class AsyncSubscriptionsWithRawResponse:
    def __init__(self, subscriptions: AsyncSubscriptions) -> None:
        self.create = async_to_raw_response_wrapper(
            subscriptions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            subscriptions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            subscriptions.update,
        )
        self.list = async_to_raw_response_wrapper(
            subscriptions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            subscriptions.delete,
        )
        self.list_attempts = async_to_raw_response_wrapper(
            subscriptions.list_attempts,
        )
        self.recover = async_to_raw_response_wrapper(
            subscriptions.recover,
        )
        self.replay_missing = async_to_raw_response_wrapper(
            subscriptions.replay_missing,
        )
        self.retrieve_secret = async_to_raw_response_wrapper(
            subscriptions.retrieve_secret,
        )
        self.rotate_secret = async_to_raw_response_wrapper(
            subscriptions.rotate_secret,
        )
        self.send_simulated_example = async_to_raw_response_wrapper(
            subscriptions.send_simulated_example,
        )
