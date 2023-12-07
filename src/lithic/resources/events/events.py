# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    Event,
    MessageAttempt,
    event_list_params,
    event_list_attempts_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncCursorPage, AsyncCursorPage
from .subscriptions import (
    Subscriptions,
    AsyncSubscriptions,
    SubscriptionsWithRawResponse,
    AsyncSubscriptionsWithRawResponse,
)
from ..._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    subscriptions: Subscriptions
    with_raw_response: EventsWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.subscriptions = Subscriptions(client)
        self.with_raw_response = EventsWithRawResponse(self)

    def retrieve(
        self,
        event_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Event:
        """
        Get an event.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/events/{event_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Event,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
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
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        with_content: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Event]:
        """List all events.

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          event_types: Event types to filter events by.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          with_content: Whether to include the event payload content in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events",
            page=SyncCursorPage[Event],
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
                        "event_types": event_types,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "with_content": with_content,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=Event,
        )

    def list_attempts(
        self,
        event_token: str,
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
        List all the message attempts for a given event.

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
            f"/events/{event_token}/attempts",
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
                    event_list_attempts_params.EventListAttemptsParams,
                ),
            ),
            model=MessageAttempt,
        )

    def resend(
        self,
        event_token: str,
        *,
        event_subscription_token: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """Resend an event to an event subscription."""
        self._post(
            f"/events/{event_token}/event_subscriptions/{event_subscription_token}/resend",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )


class AsyncEvents(AsyncAPIResource):
    subscriptions: AsyncSubscriptions
    with_raw_response: AsyncEventsWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.subscriptions = AsyncSubscriptions(client)
        self.with_raw_response = AsyncEventsWithRawResponse(self)

    async def retrieve(
        self,
        event_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Event:
        """
        Get an event.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/events/{event_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Event,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
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
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        with_content: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Event, AsyncCursorPage[Event]]:
        """List all events.

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          event_types: Event types to filter events by.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          with_content: Whether to include the event payload content in the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/events",
            page=AsyncCursorPage[Event],
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
                        "event_types": event_types,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "with_content": with_content,
                    },
                    event_list_params.EventListParams,
                ),
            ),
            model=Event,
        )

    def list_attempts(
        self,
        event_token: str,
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
        List all the message attempts for a given event.

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
            f"/events/{event_token}/attempts",
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
                    event_list_attempts_params.EventListAttemptsParams,
                ),
            ),
            model=MessageAttempt,
        )

    async def resend(
        self,
        event_token: str,
        *,
        event_subscription_token: str,
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """Resend an event to an event subscription."""
        await self._post(
            f"/events/{event_token}/event_subscriptions/{event_subscription_token}/resend",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )


class EventsWithRawResponse:
    def __init__(self, events: Events) -> None:
        self.subscriptions = SubscriptionsWithRawResponse(events.subscriptions)

        self.retrieve = to_raw_response_wrapper(
            events.retrieve,
        )
        self.list = to_raw_response_wrapper(
            events.list,
        )
        self.list_attempts = to_raw_response_wrapper(
            events.list_attempts,
        )


class AsyncEventsWithRawResponse:
    def __init__(self, events: AsyncEvents) -> None:
        self.subscriptions = AsyncSubscriptionsWithRawResponse(events.subscriptions)

        self.retrieve = async_to_raw_response_wrapper(
            events.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            events.list,
        )
        self.list_attempts = async_to_raw_response_wrapper(
            events.list_attempts,
        )
