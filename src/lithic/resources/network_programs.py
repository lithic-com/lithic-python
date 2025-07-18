# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from .. import _legacy_response
from ..types import network_program_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncSinglePage, AsyncSinglePage
from .._base_client import AsyncPaginator, make_request_options
from ..types.network_program import NetworkProgram

__all__ = ["NetworkPrograms", "AsyncNetworkPrograms"]


class NetworkPrograms(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NetworkProgramsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return NetworkProgramsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworkProgramsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return NetworkProgramsWithStreamingResponse(self)

    def retrieve(
        self,
        network_program_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkProgram:
        """
        Get network program.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network_program_token:
            raise ValueError(
                f"Expected a non-empty value for `network_program_token` but received {network_program_token!r}"
            )
        return self._get(
            f"/v1/network_programs/{network_program_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkProgram,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[NetworkProgram]:
        """List network programs.

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          page_size: Page size (for pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/network_programs",
            page=SyncSinglePage[NetworkProgram],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "page_size": page_size,
                    },
                    network_program_list_params.NetworkProgramListParams,
                ),
            ),
            model=NetworkProgram,
        )


class AsyncNetworkPrograms(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNetworkProgramsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworkProgramsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworkProgramsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncNetworkProgramsWithStreamingResponse(self)

    async def retrieve(
        self,
        network_program_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkProgram:
        """
        Get network program.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not network_program_token:
            raise ValueError(
                f"Expected a non-empty value for `network_program_token` but received {network_program_token!r}"
            )
        return await self._get(
            f"/v1/network_programs/{network_program_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkProgram,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[NetworkProgram, AsyncSinglePage[NetworkProgram]]:
        """List network programs.

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          page_size: Page size (for pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/network_programs",
            page=AsyncSinglePage[NetworkProgram],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "page_size": page_size,
                    },
                    network_program_list_params.NetworkProgramListParams,
                ),
            ),
            model=NetworkProgram,
        )


class NetworkProgramsWithRawResponse:
    def __init__(self, network_programs: NetworkPrograms) -> None:
        self._network_programs = network_programs

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            network_programs.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            network_programs.list,
        )


class AsyncNetworkProgramsWithRawResponse:
    def __init__(self, network_programs: AsyncNetworkPrograms) -> None:
        self._network_programs = network_programs

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            network_programs.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            network_programs.list,
        )


class NetworkProgramsWithStreamingResponse:
    def __init__(self, network_programs: NetworkPrograms) -> None:
        self._network_programs = network_programs

        self.retrieve = to_streamed_response_wrapper(
            network_programs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            network_programs.list,
        )


class AsyncNetworkProgramsWithStreamingResponse:
    def __init__(self, network_programs: AsyncNetworkPrograms) -> None:
        self._network_programs = network_programs

        self.retrieve = async_to_streamed_response_wrapper(
            network_programs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            network_programs.list,
        )
