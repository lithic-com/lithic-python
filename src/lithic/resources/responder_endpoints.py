# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

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
from .._base_client import make_request_options

__all__ = ["ResponderEndpoints", "AsyncResponderEndpoints"]


class ResponderEndpoints(SyncAPIResource):
    def create(
        self,
        *,
        type: Literal["TOKENIZATION_DECISIONING"] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        type: Literal["TOKENIZATION_DECISIONING"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        type: Literal["TOKENIZATION_DECISIONING"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
    async def create(
        self,
        *,
        type: Literal["TOKENIZATION_DECISIONING"] | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        type: Literal["TOKENIZATION_DECISIONING"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        type: Literal["TOKENIZATION_DECISIONING"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
