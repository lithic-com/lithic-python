# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ...types import event_list_params, event_list_attempts_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncCursorPage, AsyncCursorPage
from ...types.event import Event
from .subscriptions import (
    Subscriptions,
    AsyncSubscriptions,
    SubscriptionsWithRawResponse,
    AsyncSubscriptionsWithRawResponse,
    SubscriptionsWithStreamingResponse,
    AsyncSubscriptionsWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.message_attempt import MessageAttempt

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    @cached_property
    def subscriptions(self) -> Subscriptions:
        return Subscriptions(self._client)

    @cached_property
    def with_raw_response(self) -> EventsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return EventsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return EventsWithStreamingResponse(self)

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
        if not event_token:
            raise ValueError(f"Expected a non-empty value for `event_token` but received {event_token!r}")
        return self._get(
            f"/v1/events/{event_token}",
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
                "auth_rules.performance_report.created",
                "balance.updated",
                "book_transfer_transaction.created",
                "card.created",
                "card.renewed",
                "card.reissued",
                "card.converted",
                "card.shipped",
                "card_transaction.updated",
                "digital_wallet.tokenization_approval_request",
                "digital_wallet.tokenization_result",
                "digital_wallet.tokenization_two_factor_authentication_code",
                "digital_wallet.tokenization_two_factor_authentication_code_sent",
                "digital_wallet.tokenization_updated",
                "dispute.updated",
                "dispute_evidence.upload_failed",
                "external_bank_account.created",
                "external_bank_account.updated",
                "external_payment.created",
                "external_payment.updated",
                "financial_account.created",
                "financial_account.updated",
                "loan_tape.created",
                "loan_tape.updated",
                "management_operation.created",
                "management_operation.updated",
                "payment_transaction.created",
                "payment_transaction.updated",
                "internal_transaction.created",
                "internal_transaction.updated",
                "settlement_report.updated",
                "statements.created",
                "three_ds_authentication.created",
                "three_ds_authentication.updated",
                "tokenization.approval_request",
                "tokenization.result",
                "tokenization.two_factor_authentication_code",
                "tokenization.two_factor_authentication_code_sent",
                "tokenization.updated",
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
            "/v1/events",
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
        if not event_token:
            raise ValueError(f"Expected a non-empty value for `event_token` but received {event_token!r}")
        return self._get_api_list(
            f"/v1/events/{event_token}/attempts",
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
            f"/v1/events/{event_token}/event_subscriptions/{event_subscription_token}/resend",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )


class AsyncEvents(AsyncAPIResource):
    @cached_property
    def subscriptions(self) -> AsyncSubscriptions:
        return AsyncSubscriptions(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEventsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncEventsWithStreamingResponse(self)

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
        if not event_token:
            raise ValueError(f"Expected a non-empty value for `event_token` but received {event_token!r}")
        return await self._get(
            f"/v1/events/{event_token}",
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
                "auth_rules.performance_report.created",
                "balance.updated",
                "book_transfer_transaction.created",
                "card.created",
                "card.renewed",
                "card.reissued",
                "card.converted",
                "card.shipped",
                "card_transaction.updated",
                "digital_wallet.tokenization_approval_request",
                "digital_wallet.tokenization_result",
                "digital_wallet.tokenization_two_factor_authentication_code",
                "digital_wallet.tokenization_two_factor_authentication_code_sent",
                "digital_wallet.tokenization_updated",
                "dispute.updated",
                "dispute_evidence.upload_failed",
                "external_bank_account.created",
                "external_bank_account.updated",
                "external_payment.created",
                "external_payment.updated",
                "financial_account.created",
                "financial_account.updated",
                "loan_tape.created",
                "loan_tape.updated",
                "management_operation.created",
                "management_operation.updated",
                "payment_transaction.created",
                "payment_transaction.updated",
                "internal_transaction.created",
                "internal_transaction.updated",
                "settlement_report.updated",
                "statements.created",
                "three_ds_authentication.created",
                "three_ds_authentication.updated",
                "tokenization.approval_request",
                "tokenization.result",
                "tokenization.two_factor_authentication_code",
                "tokenization.two_factor_authentication_code_sent",
                "tokenization.updated",
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
            "/v1/events",
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
        if not event_token:
            raise ValueError(f"Expected a non-empty value for `event_token` but received {event_token!r}")
        return self._get_api_list(
            f"/v1/events/{event_token}/attempts",
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
            f"/v1/events/{event_token}/event_subscriptions/{event_subscription_token}/resend",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )


class EventsWithRawResponse:
    def __init__(self, events: Events) -> None:
        self._events = events

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            events.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            events.list,
        )
        self.list_attempts = _legacy_response.to_raw_response_wrapper(
            events.list_attempts,
        )

    @cached_property
    def subscriptions(self) -> SubscriptionsWithRawResponse:
        return SubscriptionsWithRawResponse(self._events.subscriptions)


class AsyncEventsWithRawResponse:
    def __init__(self, events: AsyncEvents) -> None:
        self._events = events

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            events.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            events.list,
        )
        self.list_attempts = _legacy_response.async_to_raw_response_wrapper(
            events.list_attempts,
        )

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsWithRawResponse:
        return AsyncSubscriptionsWithRawResponse(self._events.subscriptions)


class EventsWithStreamingResponse:
    def __init__(self, events: Events) -> None:
        self._events = events

        self.retrieve = to_streamed_response_wrapper(
            events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            events.list,
        )
        self.list_attempts = to_streamed_response_wrapper(
            events.list_attempts,
        )

    @cached_property
    def subscriptions(self) -> SubscriptionsWithStreamingResponse:
        return SubscriptionsWithStreamingResponse(self._events.subscriptions)


class AsyncEventsWithStreamingResponse:
    def __init__(self, events: AsyncEvents) -> None:
        self._events = events

        self.retrieve = async_to_streamed_response_wrapper(
            events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            events.list,
        )
        self.list_attempts = async_to_streamed_response_wrapper(
            events.list_attempts,
        )

    @cached_property
    def subscriptions(self) -> AsyncSubscriptionsWithStreamingResponse:
        return AsyncSubscriptionsWithStreamingResponse(self._events.subscriptions)
