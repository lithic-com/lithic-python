# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List
from typing_extensions import Literal

from ...types import Event
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncCursorPage, AsyncCursorPage
from .subscriptions import Subscriptions, AsyncSubscriptions
from ..._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    subscriptions: Subscriptions

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.subscriptions = Subscriptions(client)

    def retrieve(
        self,
        event_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Event:
        """Get an event."""
        return self._get(
            f"/events/{event_token}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Event,
        )

    def list(
        self,
        *,
        begin: str | NotGiven = NOT_GIVEN,
        end: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        event_types: List[Literal["dispute.updated", "digital_wallet.token_approval_request"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncCursorPage[Event]:
        """List all events.

        Args:
          begin: Date string in 8601 format.

        Only entries created after the specified date will
              be included. UTC time zone.

          end: Date string in 8601 format. Only entries created before the specified date will
              be included. UTC time zone.

          page_size: Page size (for pagination).

          starting_after: The unique identifier of the last item in the previous page. Used to retrieve
              the next page.

          ending_before: The unique identifier of the first item in the previous page. Used to retrieve
              the previous page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/events",
            page=SyncCursorPage[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "begin": begin,
                    "end": end,
                    "page_size": page_size,
                    "starting_after": starting_after,
                    "ending_before": ending_before,
                    "event_types": event_types,
                },
            ),
            model=Event,
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

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.subscriptions = AsyncSubscriptions(client)

    async def retrieve(
        self,
        event_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> Event:
        """Get an event."""
        return await self._get(
            f"/events/{event_token}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=Event,
        )

    def list(
        self,
        *,
        begin: str | NotGiven = NOT_GIVEN,
        end: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        event_types: List[Literal["dispute.updated", "digital_wallet.token_approval_request"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[Event, AsyncCursorPage[Event]]:
        """List all events.

        Args:
          begin: Date string in 8601 format.

        Only entries created after the specified date will
              be included. UTC time zone.

          end: Date string in 8601 format. Only entries created before the specified date will
              be included. UTC time zone.

          page_size: Page size (for pagination).

          starting_after: The unique identifier of the last item in the previous page. Used to retrieve
              the next page.

          ending_before: The unique identifier of the first item in the previous page. Used to retrieve
              the previous page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/events",
            page=AsyncCursorPage[Event],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "begin": begin,
                    "end": end,
                    "page_size": page_size,
                    "starting_after": starting_after,
                    "ending_before": ending_before,
                    "event_types": event_types,
                },
            ),
            model=Event,
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
