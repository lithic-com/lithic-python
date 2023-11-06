# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING
from typing_extensions import Literal

import httpx

from ..types import (
    ResponderEndpointStatus,
    ResponderEndpointCreateResponse,
    responder_endpoint_create_params,
    responder_endpoint_delete_params,
    responder_endpoint_check_status_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Lithic, AsyncLithic

__all__ = ["ResponderEndpoints", "AsyncResponderEndpoints"]


class ResponderEndpoints(SyncAPIResource):
    with_raw_response: ResponderEndpointsWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = ResponderEndpointsWithRawResponse(self)

    def create(
        self,
        *,
        type: Literal["AUTH_STREAM_ACCESS", "TOKENIZATION_DECISIONING", "THREE_DS_DECISIONING"] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/responder_endpoints",
            body=maybe_transform(
                {
                    "type": type,
                    "url": url,
                },
                responder_endpoint_create_params.ResponderEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ResponderEndpointCreateResponse,
        )

    def delete(
        self,
        *,
        type: Literal["AUTH_STREAM_ACCESS", "TOKENIZATION_DECISIONING", "THREE_DS_DECISIONING"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Disenroll a responder endpoint

        Args:
          type: The type of the endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._delete(
            "/responder_endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform({"type": type}, responder_endpoint_delete_params.ResponderEndpointDeleteParams),
            ),
            cast_to=NoneType,
        )

    def check_status(
        self,
        *,
        type: Literal["AUTH_STREAM_ACCESS", "TOKENIZATION_DECISIONING", "THREE_DS_DECISIONING"],
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
            "/responder_endpoints",
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
    with_raw_response: AsyncResponderEndpointsWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncResponderEndpointsWithRawResponse(self)

    async def create(
        self,
        *,
        type: Literal["AUTH_STREAM_ACCESS", "TOKENIZATION_DECISIONING", "THREE_DS_DECISIONING"] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/responder_endpoints",
            body=maybe_transform(
                {
                    "type": type,
                    "url": url,
                },
                responder_endpoint_create_params.ResponderEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ResponderEndpointCreateResponse,
        )

    async def delete(
        self,
        *,
        type: Literal["AUTH_STREAM_ACCESS", "TOKENIZATION_DECISIONING", "THREE_DS_DECISIONING"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """
        Disenroll a responder endpoint

        Args:
          type: The type of the endpoint.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._delete(
            "/responder_endpoints",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
                query=maybe_transform({"type": type}, responder_endpoint_delete_params.ResponderEndpointDeleteParams),
            ),
            cast_to=NoneType,
        )

    async def check_status(
        self,
        *,
        type: Literal["AUTH_STREAM_ACCESS", "TOKENIZATION_DECISIONING", "THREE_DS_DECISIONING"],
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
            "/responder_endpoints",
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


class ResponderEndpointsWithRawResponse:
    def __init__(self, responder_endpoints: ResponderEndpoints) -> None:
        self.create = to_raw_response_wrapper(
            responder_endpoints.create,
        )
        self.delete = to_raw_response_wrapper(
            responder_endpoints.delete,
        )
        self.check_status = to_raw_response_wrapper(
            responder_endpoints.check_status,
        )


class AsyncResponderEndpointsWithRawResponse:
    def __init__(self, responder_endpoints: AsyncResponderEndpoints) -> None:
        self.create = async_to_raw_response_wrapper(
            responder_endpoints.create,
        )
        self.delete = async_to_raw_response_wrapper(
            responder_endpoints.delete,
        )
        self.check_status = async_to_raw_response_wrapper(
            responder_endpoints.check_status,
        )
