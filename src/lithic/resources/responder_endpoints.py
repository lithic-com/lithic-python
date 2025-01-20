# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    responder_endpoint_create_params,
    responder_endpoint_delete_params,
    responder_endpoint_check_status_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import make_request_options
from ..types.responder_endpoint_status import ResponderEndpointStatus
from ..types.responder_endpoint_create_response import ResponderEndpointCreateResponse

__all__ = ["ResponderEndpoints", "AsyncResponderEndpoints"]


class ResponderEndpoints(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResponderEndpointsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return ResponderEndpointsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResponderEndpointsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return ResponderEndpointsWithStreamingResponse(self)

    def create(
        self,
        *,
        type: Literal["AUTH_STREAM_ACCESS", "THREE_DS_DECISIONING", "TOKENIZATION_DECISIONING"] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponderEndpointCreateResponse:
        """
        Enroll a responder endpoint

        Args:
          type: The type of the endpoint.

          url: The URL for the responder endpoint (must be http(s)).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/responder_endpoints",
            body=maybe_transform(
                {
                    "type": type,
                    "url": url,
                },
                responder_endpoint_create_params.ResponderEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponderEndpointCreateResponse,
        )

    def delete(
        self,
        *,
        type: Literal["AUTH_STREAM_ACCESS", "THREE_DS_DECISIONING", "TOKENIZATION_DECISIONING"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Disenroll a responder endpoint

        Args:
          type: The type of the endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/responder_endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, responder_endpoint_delete_params.ResponderEndpointDeleteParams),
            ),
            cast_to=NoneType,
        )

    def check_status(
        self,
        *,
        type: Literal["AUTH_STREAM_ACCESS", "THREE_DS_DECISIONING", "TOKENIZATION_DECISIONING"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponderEndpointStatus:
        """
        Check the status of a responder endpoint

        Args:
          type: The type of the endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/responder_endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"type": type}, responder_endpoint_check_status_params.ResponderEndpointCheckStatusParams
                ),
            ),
            cast_to=ResponderEndpointStatus,
        )


class AsyncResponderEndpoints(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResponderEndpointsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResponderEndpointsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResponderEndpointsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncResponderEndpointsWithStreamingResponse(self)

    async def create(
        self,
        *,
        type: Literal["AUTH_STREAM_ACCESS", "THREE_DS_DECISIONING", "TOKENIZATION_DECISIONING"] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponderEndpointCreateResponse:
        """
        Enroll a responder endpoint

        Args:
          type: The type of the endpoint.

          url: The URL for the responder endpoint (must be http(s)).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/responder_endpoints",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "url": url,
                },
                responder_endpoint_create_params.ResponderEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResponderEndpointCreateResponse,
        )

    async def delete(
        self,
        *,
        type: Literal["AUTH_STREAM_ACCESS", "THREE_DS_DECISIONING", "TOKENIZATION_DECISIONING"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Disenroll a responder endpoint

        Args:
          type: The type of the endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/responder_endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"type": type}, responder_endpoint_delete_params.ResponderEndpointDeleteParams
                ),
            ),
            cast_to=NoneType,
        )

    async def check_status(
        self,
        *,
        type: Literal["AUTH_STREAM_ACCESS", "THREE_DS_DECISIONING", "TOKENIZATION_DECISIONING"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponderEndpointStatus:
        """
        Check the status of a responder endpoint

        Args:
          type: The type of the endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/responder_endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"type": type}, responder_endpoint_check_status_params.ResponderEndpointCheckStatusParams
                ),
            ),
            cast_to=ResponderEndpointStatus,
        )


class ResponderEndpointsWithRawResponse:
    def __init__(self, responder_endpoints: ResponderEndpoints) -> None:
        self._responder_endpoints = responder_endpoints

        self.create = _legacy_response.to_raw_response_wrapper(
            responder_endpoints.create,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            responder_endpoints.delete,
        )
        self.check_status = _legacy_response.to_raw_response_wrapper(
            responder_endpoints.check_status,
        )


class AsyncResponderEndpointsWithRawResponse:
    def __init__(self, responder_endpoints: AsyncResponderEndpoints) -> None:
        self._responder_endpoints = responder_endpoints

        self.create = _legacy_response.async_to_raw_response_wrapper(
            responder_endpoints.create,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            responder_endpoints.delete,
        )
        self.check_status = _legacy_response.async_to_raw_response_wrapper(
            responder_endpoints.check_status,
        )


class ResponderEndpointsWithStreamingResponse:
    def __init__(self, responder_endpoints: ResponderEndpoints) -> None:
        self._responder_endpoints = responder_endpoints

        self.create = to_streamed_response_wrapper(
            responder_endpoints.create,
        )
        self.delete = to_streamed_response_wrapper(
            responder_endpoints.delete,
        )
        self.check_status = to_streamed_response_wrapper(
            responder_endpoints.check_status,
        )


class AsyncResponderEndpointsWithStreamingResponse:
    def __init__(self, responder_endpoints: AsyncResponderEndpoints) -> None:
        self._responder_endpoints = responder_endpoints

        self.create = async_to_streamed_response_wrapper(
            responder_endpoints.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            responder_endpoints.delete,
        )
        self.check_status = async_to_streamed_response_wrapper(
            responder_endpoints.check_status,
        )
