# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.three_ds import (
    AuthenticationRetrieveResponse,
    AuthenticationSimulateResponse,
    authentication_simulate_params,
)

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["Authentication", "AsyncAuthentication"]


class Authentication(SyncAPIResource):
    with_raw_response: AuthenticationWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = AuthenticationWithRawResponse(self)

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
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AuthenticationSimulateResponse,
        )


class AsyncAuthentication(AsyncAPIResource):
    with_raw_response: AsyncAuthenticationWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncAuthenticationWithRawResponse(self)

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
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=AuthenticationSimulateResponse,
        )


class AuthenticationWithRawResponse:
    def __init__(self, authentication: Authentication) -> None:
        self.retrieve = to_raw_response_wrapper(
            authentication.retrieve,
        )
        self.simulate = to_raw_response_wrapper(
            authentication.simulate,
        )


class AsyncAuthenticationWithRawResponse:
    def __init__(self, authentication: AsyncAuthentication) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            authentication.retrieve,
        )
        self.simulate = async_to_raw_response_wrapper(
            authentication.simulate,
        )
