# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options

__all__ = ["EventSubscriptions", "AsyncEventSubscriptions"]


class EventSubscriptions(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventSubscriptionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return EventSubscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventSubscriptionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return EventSubscriptionsWithStreamingResponse(self)

    def resend(
        self,
        event_subscription_token: str,
        *,
        event_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Resend an event to an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_token:
            raise ValueError(f"Expected a non-empty value for `event_token` but received {event_token!r}")
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return self._post(
            f"/v1/events/{event_token}/event_subscriptions/{event_subscription_token}/resend",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEventSubscriptions(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventSubscriptionsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventSubscriptionsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventSubscriptionsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncEventSubscriptionsWithStreamingResponse(self)

    async def resend(
        self,
        event_subscription_token: str,
        *,
        event_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Resend an event to an event subscription.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_token:
            raise ValueError(f"Expected a non-empty value for `event_token` but received {event_token!r}")
        if not event_subscription_token:
            raise ValueError(
                f"Expected a non-empty value for `event_subscription_token` but received {event_subscription_token!r}"
            )
        return await self._post(
            f"/v1/events/{event_token}/event_subscriptions/{event_subscription_token}/resend",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EventSubscriptionsWithRawResponse:
    def __init__(self, event_subscriptions: EventSubscriptions) -> None:
        self._event_subscriptions = event_subscriptions

        self.resend = _legacy_response.to_raw_response_wrapper(
            event_subscriptions.resend,
        )


class AsyncEventSubscriptionsWithRawResponse:
    def __init__(self, event_subscriptions: AsyncEventSubscriptions) -> None:
        self._event_subscriptions = event_subscriptions

        self.resend = _legacy_response.async_to_raw_response_wrapper(
            event_subscriptions.resend,
        )


class EventSubscriptionsWithStreamingResponse:
    def __init__(self, event_subscriptions: EventSubscriptions) -> None:
        self._event_subscriptions = event_subscriptions

        self.resend = to_streamed_response_wrapper(
            event_subscriptions.resend,
        )


class AsyncEventSubscriptionsWithStreamingResponse:
    def __init__(self, event_subscriptions: AsyncEventSubscriptions) -> None:
        self._event_subscriptions = event_subscriptions

        self.resend = async_to_streamed_response_wrapper(
            event_subscriptions.resend,
        )
