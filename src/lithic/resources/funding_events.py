# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import funding_event_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.funding_event_list_response import FundingEventListResponse
from ..types.funding_event_retrieve_response import FundingEventRetrieveResponse
from ..types.funding_event_retrieve_details_response import FundingEventRetrieveDetailsResponse

__all__ = ["FundingEvents", "AsyncFundingEvents"]


class FundingEvents(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FundingEventsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return FundingEventsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FundingEventsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return FundingEventsWithStreamingResponse(self)

    def retrieve(
        self,
        funding_event_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FundingEventRetrieveResponse:
        """
        Get funding event for program by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not funding_event_token:
            raise ValueError(
                f"Expected a non-empty value for `funding_event_token` but received {funding_event_token!r}"
            )
        return self._get(
            f"/v1/funding_events/{funding_event_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FundingEventRetrieveResponse,
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
    ) -> SyncCursorPage[FundingEventListResponse]:
        """
        Get all funding events for program

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
            "/v1/funding_events",
            page=SyncCursorPage[FundingEventListResponse],
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
                    funding_event_list_params.FundingEventListParams,
                ),
            ),
            model=FundingEventListResponse,
        )

    def retrieve_details(
        self,
        funding_event_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FundingEventRetrieveDetailsResponse:
        """
        Get funding event details by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not funding_event_token:
            raise ValueError(
                f"Expected a non-empty value for `funding_event_token` but received {funding_event_token!r}"
            )
        return self._get(
            f"/v1/funding_events/{funding_event_token}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FundingEventRetrieveDetailsResponse,
        )


class AsyncFundingEvents(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFundingEventsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFundingEventsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFundingEventsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncFundingEventsWithStreamingResponse(self)

    async def retrieve(
        self,
        funding_event_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FundingEventRetrieveResponse:
        """
        Get funding event for program by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not funding_event_token:
            raise ValueError(
                f"Expected a non-empty value for `funding_event_token` but received {funding_event_token!r}"
            )
        return await self._get(
            f"/v1/funding_events/{funding_event_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FundingEventRetrieveResponse,
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
    ) -> AsyncPaginator[FundingEventListResponse, AsyncCursorPage[FundingEventListResponse]]:
        """
        Get all funding events for program

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
            "/v1/funding_events",
            page=AsyncCursorPage[FundingEventListResponse],
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
                    funding_event_list_params.FundingEventListParams,
                ),
            ),
            model=FundingEventListResponse,
        )

    async def retrieve_details(
        self,
        funding_event_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FundingEventRetrieveDetailsResponse:
        """
        Get funding event details by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not funding_event_token:
            raise ValueError(
                f"Expected a non-empty value for `funding_event_token` but received {funding_event_token!r}"
            )
        return await self._get(
            f"/v1/funding_events/{funding_event_token}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FundingEventRetrieveDetailsResponse,
        )


class FundingEventsWithRawResponse:
    def __init__(self, funding_events: FundingEvents) -> None:
        self._funding_events = funding_events

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            funding_events.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            funding_events.list,
        )
        self.retrieve_details = _legacy_response.to_raw_response_wrapper(
            funding_events.retrieve_details,
        )


class AsyncFundingEventsWithRawResponse:
    def __init__(self, funding_events: AsyncFundingEvents) -> None:
        self._funding_events = funding_events

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            funding_events.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            funding_events.list,
        )
        self.retrieve_details = _legacy_response.async_to_raw_response_wrapper(
            funding_events.retrieve_details,
        )


class FundingEventsWithStreamingResponse:
    def __init__(self, funding_events: FundingEvents) -> None:
        self._funding_events = funding_events

        self.retrieve = to_streamed_response_wrapper(
            funding_events.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            funding_events.list,
        )
        self.retrieve_details = to_streamed_response_wrapper(
            funding_events.retrieve_details,
        )


class AsyncFundingEventsWithStreamingResponse:
    def __init__(self, funding_events: AsyncFundingEvents) -> None:
        self._funding_events = funding_events

        self.retrieve = async_to_streamed_response_wrapper(
            funding_events.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            funding_events.list,
        )
        self.retrieve_details = async_to_streamed_response_wrapper(
            funding_events.retrieve_details,
        )
