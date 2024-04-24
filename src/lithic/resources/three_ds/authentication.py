# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.three_ds import authentication_simulate_params
from ...types.three_ds.authentication_retrieve_response import AuthenticationRetrieveResponse
from ...types.three_ds.authentication_simulate_response import AuthenticationSimulateResponse

__all__ = ["Authentication", "AsyncAuthentication"]


class Authentication(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthenticationWithRawResponse:
        return AuthenticationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticationWithStreamingResponse:
        return AuthenticationWithStreamingResponse(self)

    def retrieve(
        self,
        three_ds_authentication_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationRetrieveResponse:
        """
        Get 3DS Authentication by token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not three_ds_authentication_token:
            raise ValueError(
                f"Expected a non-empty value for `three_ds_authentication_token` but received {three_ds_authentication_token!r}"
            )
        return self._get(
            f"/three_ds_authentication/{three_ds_authentication_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationRetrieveResponse,
        )

    def simulate(
        self,
        *,
        merchant: authentication_simulate_params.Merchant,
        pan: str,
        transaction: authentication_simulate_params.Transaction,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationSimulateResponse:
        """
        Simulates a 3DS authentication request from the payment network as if it came
        from an ACS. If you're configured for 3DS Customer Decisioning, simulating
        authentications requires your customer decisioning endpoint to be set up
        properly (respond with a valid JSON).

        Args:
          pan: Sixteen digit card number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/three_ds_authentication/simulate",
            body=maybe_transform(
                {
                    "merchant": merchant,
                    "pan": pan,
                    "transaction": transaction,
                },
                authentication_simulate_params.AuthenticationSimulateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationSimulateResponse,
        )


class AsyncAuthentication(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthenticationWithRawResponse:
        return AsyncAuthenticationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticationWithStreamingResponse:
        return AsyncAuthenticationWithStreamingResponse(self)

    async def retrieve(
        self,
        three_ds_authentication_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationRetrieveResponse:
        """
        Get 3DS Authentication by token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not three_ds_authentication_token:
            raise ValueError(
                f"Expected a non-empty value for `three_ds_authentication_token` but received {three_ds_authentication_token!r}"
            )
        return await self._get(
            f"/three_ds_authentication/{three_ds_authentication_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationRetrieveResponse,
        )

    async def simulate(
        self,
        *,
        merchant: authentication_simulate_params.Merchant,
        pan: str,
        transaction: authentication_simulate_params.Transaction,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationSimulateResponse:
        """
        Simulates a 3DS authentication request from the payment network as if it came
        from an ACS. If you're configured for 3DS Customer Decisioning, simulating
        authentications requires your customer decisioning endpoint to be set up
        properly (respond with a valid JSON).

        Args:
          pan: Sixteen digit card number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/three_ds_authentication/simulate",
            body=await async_maybe_transform(
                {
                    "merchant": merchant,
                    "pan": pan,
                    "transaction": transaction,
                },
                authentication_simulate_params.AuthenticationSimulateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationSimulateResponse,
        )


class AuthenticationWithRawResponse:
    def __init__(self, authentication: Authentication) -> None:
        self._authentication = authentication

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            authentication.retrieve,
        )
        self.simulate = _legacy_response.to_raw_response_wrapper(
            authentication.simulate,
        )


class AsyncAuthenticationWithRawResponse:
    def __init__(self, authentication: AsyncAuthentication) -> None:
        self._authentication = authentication

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            authentication.retrieve,
        )
        self.simulate = _legacy_response.async_to_raw_response_wrapper(
            authentication.simulate,
        )


class AuthenticationWithStreamingResponse:
    def __init__(self, authentication: Authentication) -> None:
        self._authentication = authentication

        self.retrieve = to_streamed_response_wrapper(
            authentication.retrieve,
        )
        self.simulate = to_streamed_response_wrapper(
            authentication.simulate,
        )


class AsyncAuthenticationWithStreamingResponse:
    def __init__(self, authentication: AsyncAuthentication) -> None:
        self._authentication = authentication

        self.retrieve = async_to_streamed_response_wrapper(
            authentication.retrieve,
        )
        self.simulate = async_to_streamed_response_wrapper(
            authentication.simulate,
        )
