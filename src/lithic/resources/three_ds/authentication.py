# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.three_ds import authentication_simulate_params, authentication_simulate_otp_entry_params
from ...types.three_ds.authentication_retrieve_response import AuthenticationRetrieveResponse
from ...types.three_ds.authentication_simulate_response import AuthenticationSimulateResponse

__all__ = ["Authentication", "AsyncAuthentication"]


class Authentication(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthenticationWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AuthenticationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticationWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
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
            f"/v1/three_ds_authentication/{three_ds_authentication_token}",
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
        card_expiry_check: Literal["MATCH", "MISMATCH", "NOT_PRESENT"] | NotGiven = NOT_GIVEN,
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

          card_expiry_check: When set will use the following values as part of the Simulated Authentication.
              When not set defaults to MATCH

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/three_ds_authentication/simulate",
            body=maybe_transform(
                {
                    "merchant": merchant,
                    "pan": pan,
                    "transaction": transaction,
                    "card_expiry_check": card_expiry_check,
                },
                authentication_simulate_params.AuthenticationSimulateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationSimulateResponse,
        )

    def simulate_otp_entry(
        self,
        *,
        token: str,
        otp: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Endpoint for simulating entering OTP into 3DS Challenge UI.

        A call to
        /v1/three_ds_authentication/simulate that resulted in triggered SMS-OTP
        challenge must precede. Only a single attempt is supported; upon entering OTP,
        the challenge is either approved or declined.

        Args:
          token: A unique token returned as part of a /v1/three_ds_authentication/simulate call
              that resulted in PENDING_CHALLENGE authentication result.

          otp: The OTP entered by the cardholder

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/three_ds_decisioning/simulate/enter_otp",
            body=maybe_transform(
                {
                    "token": token,
                    "otp": otp,
                },
                authentication_simulate_otp_entry_params.AuthenticationSimulateOtpEntryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAuthentication(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthenticationWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthenticationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticationWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
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
            f"/v1/three_ds_authentication/{three_ds_authentication_token}",
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
        card_expiry_check: Literal["MATCH", "MISMATCH", "NOT_PRESENT"] | NotGiven = NOT_GIVEN,
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

          card_expiry_check: When set will use the following values as part of the Simulated Authentication.
              When not set defaults to MATCH

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/three_ds_authentication/simulate",
            body=await async_maybe_transform(
                {
                    "merchant": merchant,
                    "pan": pan,
                    "transaction": transaction,
                    "card_expiry_check": card_expiry_check,
                },
                authentication_simulate_params.AuthenticationSimulateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationSimulateResponse,
        )

    async def simulate_otp_entry(
        self,
        *,
        token: str,
        otp: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Endpoint for simulating entering OTP into 3DS Challenge UI.

        A call to
        /v1/three_ds_authentication/simulate that resulted in triggered SMS-OTP
        challenge must precede. Only a single attempt is supported; upon entering OTP,
        the challenge is either approved or declined.

        Args:
          token: A unique token returned as part of a /v1/three_ds_authentication/simulate call
              that resulted in PENDING_CHALLENGE authentication result.

          otp: The OTP entered by the cardholder

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/three_ds_decisioning/simulate/enter_otp",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "otp": otp,
                },
                authentication_simulate_otp_entry_params.AuthenticationSimulateOtpEntryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
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
        self.simulate_otp_entry = _legacy_response.to_raw_response_wrapper(
            authentication.simulate_otp_entry,
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
        self.simulate_otp_entry = _legacy_response.async_to_raw_response_wrapper(
            authentication.simulate_otp_entry,
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
        self.simulate_otp_entry = to_streamed_response_wrapper(
            authentication.simulate_otp_entry,
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
        self.simulate_otp_entry = async_to_streamed_response_wrapper(
            authentication.simulate_otp_entry,
        )
