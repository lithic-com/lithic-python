# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .enhanced_commercial_data import (
    EnhancedCommercialData,
    AsyncEnhancedCommercialData,
    EnhancedCommercialDataWithRawResponse,
    AsyncEnhancedCommercialDataWithRawResponse,
    EnhancedCommercialDataWithStreamingResponse,
    AsyncEnhancedCommercialDataWithStreamingResponse,
)

__all__ = ["Events", "AsyncEvents"]


class Events(SyncAPIResource):
    @cached_property
    def enhanced_commercial_data(self) -> EnhancedCommercialData:
        return EnhancedCommercialData(self._client)

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


class AsyncEvents(AsyncAPIResource):
    @cached_property
    def enhanced_commercial_data(self) -> AsyncEnhancedCommercialData:
        return AsyncEnhancedCommercialData(self._client)

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


class EventsWithRawResponse:
    def __init__(self, events: Events) -> None:
        self._events = events

    @cached_property
    def enhanced_commercial_data(self) -> EnhancedCommercialDataWithRawResponse:
        return EnhancedCommercialDataWithRawResponse(self._events.enhanced_commercial_data)


class AsyncEventsWithRawResponse:
    def __init__(self, events: AsyncEvents) -> None:
        self._events = events

    @cached_property
    def enhanced_commercial_data(self) -> AsyncEnhancedCommercialDataWithRawResponse:
        return AsyncEnhancedCommercialDataWithRawResponse(self._events.enhanced_commercial_data)


class EventsWithStreamingResponse:
    def __init__(self, events: Events) -> None:
        self._events = events

    @cached_property
    def enhanced_commercial_data(self) -> EnhancedCommercialDataWithStreamingResponse:
        return EnhancedCommercialDataWithStreamingResponse(self._events.enhanced_commercial_data)


class AsyncEventsWithStreamingResponse:
    def __init__(self, events: AsyncEvents) -> None:
        self._events = events

    @cached_property
    def enhanced_commercial_data(self) -> AsyncEnhancedCommercialDataWithStreamingResponse:
        return AsyncEnhancedCommercialDataWithStreamingResponse(self._events.enhanced_commercial_data)
