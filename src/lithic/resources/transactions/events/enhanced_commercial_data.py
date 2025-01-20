# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .... import _legacy_response
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...._base_client import make_request_options
from ....types.transactions.events.enhanced_data import EnhancedData

__all__ = ["EnhancedCommercialData", "AsyncEnhancedCommercialData"]


class EnhancedCommercialData(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EnhancedCommercialDataWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return EnhancedCommercialDataWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EnhancedCommercialDataWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return EnhancedCommercialDataWithStreamingResponse(self)

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
    ) -> EnhancedData:
        """Get L2/L3 enhanced commercial data associated with a transaction event.

        Not
        available in sandbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_token:
            raise ValueError(f"Expected a non-empty value for `event_token` but received {event_token!r}")
        return self._get(
            f"/v1/transactions/events/{event_token}/enhanced_commercial_data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnhancedData,
        )


class AsyncEnhancedCommercialData(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEnhancedCommercialDataWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEnhancedCommercialDataWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEnhancedCommercialDataWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncEnhancedCommercialDataWithStreamingResponse(self)

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
    ) -> EnhancedData:
        """Get L2/L3 enhanced commercial data associated with a transaction event.

        Not
        available in sandbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_token:
            raise ValueError(f"Expected a non-empty value for `event_token` but received {event_token!r}")
        return await self._get(
            f"/v1/transactions/events/{event_token}/enhanced_commercial_data",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EnhancedData,
        )


class EnhancedCommercialDataWithRawResponse:
    def __init__(self, enhanced_commercial_data: EnhancedCommercialData) -> None:
        self._enhanced_commercial_data = enhanced_commercial_data

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            enhanced_commercial_data.retrieve,
        )


class AsyncEnhancedCommercialDataWithRawResponse:
    def __init__(self, enhanced_commercial_data: AsyncEnhancedCommercialData) -> None:
        self._enhanced_commercial_data = enhanced_commercial_data

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            enhanced_commercial_data.retrieve,
        )


class EnhancedCommercialDataWithStreamingResponse:
    def __init__(self, enhanced_commercial_data: EnhancedCommercialData) -> None:
        self._enhanced_commercial_data = enhanced_commercial_data

        self.retrieve = to_streamed_response_wrapper(
            enhanced_commercial_data.retrieve,
        )


class AsyncEnhancedCommercialDataWithStreamingResponse:
    def __init__(self, enhanced_commercial_data: AsyncEnhancedCommercialData) -> None:
        self._enhanced_commercial_data = enhanced_commercial_data

        self.retrieve = async_to_streamed_response_wrapper(
            enhanced_commercial_data.retrieve,
        )
