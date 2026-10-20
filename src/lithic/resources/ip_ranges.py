# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import make_request_options
from ..types.ip_range_retrieve_response import IPRangeRetrieveResponse

__all__ = ["IPRanges", "AsyncIPRanges"]


class IPRanges(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPRangesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return IPRangesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPRangesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return IPRangesWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPRangeRetrieveResponse:
        """
        Returns the IP addresses Lithic sends responder requests from (Auth Stream
        Access, 3DS decisioning, and tokenization decisioning), so you can allowlist
        them in your firewall. Each environment returns its own set of addresses. Lithic
        announces new addresses at least 30 days before sending traffic from them. Event
        webhooks are not sent from these addresses
        """
        return self._get(
            "/v1/ip_ranges",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRangeRetrieveResponse,
        )


class AsyncIPRanges(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPRangesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPRangesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPRangesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncIPRangesWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPRangeRetrieveResponse:
        """
        Returns the IP addresses Lithic sends responder requests from (Auth Stream
        Access, 3DS decisioning, and tokenization decisioning), so you can allowlist
        them in your firewall. Each environment returns its own set of addresses. Lithic
        announces new addresses at least 30 days before sending traffic from them. Event
        webhooks are not sent from these addresses
        """
        return await self._get(
            "/v1/ip_ranges",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IPRangeRetrieveResponse,
        )


class IPRangesWithRawResponse:
    def __init__(self, ip_ranges: IPRanges) -> None:
        self._ip_ranges = ip_ranges

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            ip_ranges.retrieve,
        )


class AsyncIPRangesWithRawResponse:
    def __init__(self, ip_ranges: AsyncIPRanges) -> None:
        self._ip_ranges = ip_ranges

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            ip_ranges.retrieve,
        )


class IPRangesWithStreamingResponse:
    def __init__(self, ip_ranges: IPRanges) -> None:
        self._ip_ranges = ip_ranges

        self.retrieve = to_streamed_response_wrapper(
            ip_ranges.retrieve,
        )


class AsyncIPRangesWithStreamingResponse:
    def __init__(self, ip_ranges: AsyncIPRanges) -> None:
        self._ip_ranges = ip_ranges

        self.retrieve = async_to_streamed_response_wrapper(
            ip_ranges.retrieve,
        )
