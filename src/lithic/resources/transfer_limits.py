# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from .. import _legacy_response
from ..types import transfer_limit_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncSinglePage, AsyncSinglePage
from .._base_client import AsyncPaginator, make_request_options
from ..types.transfer_limits_response import Data

__all__ = ["TransferLimits", "AsyncTransferLimits"]


class TransferLimits(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransferLimitsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return TransferLimitsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransferLimitsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return TransferLimitsWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[Data]:
        """
        Get transfer limits for a specified date

        Args:
          date: Date for which to retrieve transfer limits (ISO 8601 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/transfer_limits",
            page=SyncSinglePage[Data],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, transfer_limit_list_params.TransferLimitListParams),
            ),
            model=Data,
        )


class AsyncTransferLimits(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransferLimitsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransferLimitsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransferLimitsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncTransferLimitsWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Data, AsyncSinglePage[Data]]:
        """
        Get transfer limits for a specified date

        Args:
          date: Date for which to retrieve transfer limits (ISO 8601 format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/transfer_limits",
            page=AsyncSinglePage[Data],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, transfer_limit_list_params.TransferLimitListParams),
            ),
            model=Data,
        )


class TransferLimitsWithRawResponse:
    def __init__(self, transfer_limits: TransferLimits) -> None:
        self._transfer_limits = transfer_limits

        self.list = _legacy_response.to_raw_response_wrapper(
            transfer_limits.list,
        )


class AsyncTransferLimitsWithRawResponse:
    def __init__(self, transfer_limits: AsyncTransferLimits) -> None:
        self._transfer_limits = transfer_limits

        self.list = _legacy_response.async_to_raw_response_wrapper(
            transfer_limits.list,
        )


class TransferLimitsWithStreamingResponse:
    def __init__(self, transfer_limits: TransferLimits) -> None:
        self._transfer_limits = transfer_limits

        self.list = to_streamed_response_wrapper(
            transfer_limits.list,
        )


class AsyncTransferLimitsWithStreamingResponse:
    def __init__(self, transfer_limits: AsyncTransferLimits) -> None:
        self._transfer_limits = transfer_limits

        self.list = async_to_streamed_response_wrapper(
            transfer_limits.list,
        )
