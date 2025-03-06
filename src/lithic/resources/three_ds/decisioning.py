# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.three_ds import ChallengeResult, decisioning_challenge_response_params
from ...types.three_ds.challenge_result import ChallengeResult
from ...types.three_ds.decisioning_retrieve_secret_response import DecisioningRetrieveSecretResponse

__all__ = ["Decisioning", "AsyncDecisioning"]


class Decisioning(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DecisioningWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return DecisioningWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DecisioningWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return DecisioningWithStreamingResponse(self)

    def challenge_response(
        self,
        *,
        token: str,
        challenge_response: ChallengeResult,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Card program's response to a 3DS Challenge Request (CReq)

        Args:
          token: Globally unique identifier for the 3DS authentication. This token is sent as
              part of the initial 3DS Decisioning Request and as part of the 3DS Challenge
              Event in the [ThreeDSAuthentication](#/components/schemas/ThreeDSAuthentication)
              object

          challenge_response: Whether the Cardholder has Approved or Declined the issued Challenge

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/three_ds_decisioning/challenge_response",
            body=maybe_transform(
                {
                    "token": token,
                    "challenge_response": challenge_response,
                },
                decisioning_challenge_response_params.DecisioningChallengeResponseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DecisioningRetrieveSecretResponse:
        """Retrieve the 3DS Decisioning HMAC secret key.

        If one does not exist for your
        program yet, calling this endpoint will create one for you. The headers (which
        you can use to verify 3DS Decisioning requests) will begin appearing shortly
        after calling this endpoint for the first time. See
        [this page](https://docs.lithic.com/docs/3ds-decisioning#3ds-decisioning-hmac-secrets)
        for more detail about verifying 3DS Decisioning requests.
        """
        return self._get(
            "/v1/three_ds_decisioning/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DecisioningRetrieveSecretResponse,
        )

    def rotate_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Generate a new 3DS Decisioning HMAC secret key.

        The old secret key will be
        deactivated 24 hours after a successful request to this endpoint. Make a
        [`GET /three_ds_decisioning/secret`](https://docs.lithic.com/reference/getthreedsdecisioningsecret)
        request to retrieve the new secret key.
        """
        return self._post(
            "/v1/three_ds_decisioning/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDecisioning(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDecisioningWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDecisioningWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDecisioningWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncDecisioningWithStreamingResponse(self)

    async def challenge_response(
        self,
        *,
        token: str,
        challenge_response: ChallengeResult,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Card program's response to a 3DS Challenge Request (CReq)

        Args:
          token: Globally unique identifier for the 3DS authentication. This token is sent as
              part of the initial 3DS Decisioning Request and as part of the 3DS Challenge
              Event in the [ThreeDSAuthentication](#/components/schemas/ThreeDSAuthentication)
              object

          challenge_response: Whether the Cardholder has Approved or Declined the issued Challenge

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/three_ds_decisioning/challenge_response",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "challenge_response": challenge_response,
                },
                decisioning_challenge_response_params.DecisioningChallengeResponseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DecisioningRetrieveSecretResponse:
        """Retrieve the 3DS Decisioning HMAC secret key.

        If one does not exist for your
        program yet, calling this endpoint will create one for you. The headers (which
        you can use to verify 3DS Decisioning requests) will begin appearing shortly
        after calling this endpoint for the first time. See
        [this page](https://docs.lithic.com/docs/3ds-decisioning#3ds-decisioning-hmac-secrets)
        for more detail about verifying 3DS Decisioning requests.
        """
        return await self._get(
            "/v1/three_ds_decisioning/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DecisioningRetrieveSecretResponse,
        )

    async def rotate_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Generate a new 3DS Decisioning HMAC secret key.

        The old secret key will be
        deactivated 24 hours after a successful request to this endpoint. Make a
        [`GET /three_ds_decisioning/secret`](https://docs.lithic.com/reference/getthreedsdecisioningsecret)
        request to retrieve the new secret key.
        """
        return await self._post(
            "/v1/three_ds_decisioning/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DecisioningWithRawResponse:
    def __init__(self, decisioning: Decisioning) -> None:
        self._decisioning = decisioning

        self.challenge_response = _legacy_response.to_raw_response_wrapper(
            decisioning.challenge_response,
        )
        self.retrieve_secret = _legacy_response.to_raw_response_wrapper(
            decisioning.retrieve_secret,
        )
        self.rotate_secret = _legacy_response.to_raw_response_wrapper(
            decisioning.rotate_secret,
        )


class AsyncDecisioningWithRawResponse:
    def __init__(self, decisioning: AsyncDecisioning) -> None:
        self._decisioning = decisioning

        self.challenge_response = _legacy_response.async_to_raw_response_wrapper(
            decisioning.challenge_response,
        )
        self.retrieve_secret = _legacy_response.async_to_raw_response_wrapper(
            decisioning.retrieve_secret,
        )
        self.rotate_secret = _legacy_response.async_to_raw_response_wrapper(
            decisioning.rotate_secret,
        )


class DecisioningWithStreamingResponse:
    def __init__(self, decisioning: Decisioning) -> None:
        self._decisioning = decisioning

        self.challenge_response = to_streamed_response_wrapper(
            decisioning.challenge_response,
        )
        self.retrieve_secret = to_streamed_response_wrapper(
            decisioning.retrieve_secret,
        )
        self.rotate_secret = to_streamed_response_wrapper(
            decisioning.rotate_secret,
        )


class AsyncDecisioningWithStreamingResponse:
    def __init__(self, decisioning: AsyncDecisioning) -> None:
        self._decisioning = decisioning

        self.challenge_response = async_to_streamed_response_wrapper(
            decisioning.challenge_response,
        )
        self.retrieve_secret = async_to_streamed_response_wrapper(
            decisioning.retrieve_secret,
        )
        self.rotate_secret = async_to_streamed_response_wrapper(
            decisioning.rotate_secret,
        )
