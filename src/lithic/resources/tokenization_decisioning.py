# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import make_request_options
from ..types.tokenization_secret import TokenizationSecret
from ..types.tokenization_decisioning_rotate_secret_response import TokenizationDecisioningRotateSecretResponse

__all__ = ["TokenizationDecisioning", "AsyncTokenizationDecisioning"]


class TokenizationDecisioning(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokenizationDecisioningWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return TokenizationDecisioningWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokenizationDecisioningWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return TokenizationDecisioningWithStreamingResponse(self)

    def retrieve_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenizationSecret:
        """Retrieve the Tokenization Decisioning secret key.

        If one does not exist your
        program yet, calling this endpoint will create one for you. The headers of the
        Tokenization Decisioning request will contain a hmac signature which you can use
        to verify requests originate from Lithic. See
        [this page](https://docs.lithic.com/docs/events-api#verifying-webhooks) for more
        detail about verifying Tokenization Decisioning requests.
        """
        return self._get(
            "/v1/tokenization_decisioning/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationSecret,
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
    ) -> TokenizationDecisioningRotateSecretResponse:
        """Generate a new Tokenization Decisioning secret key.

        The old Tokenization
        Decisioning secret key will be deactivated 24 hours after a successful request
        to this endpoint.
        """
        return self._post(
            "/v1/tokenization_decisioning/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationDecisioningRotateSecretResponse,
        )


class AsyncTokenizationDecisioning(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokenizationDecisioningWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokenizationDecisioningWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokenizationDecisioningWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncTokenizationDecisioningWithStreamingResponse(self)

    async def retrieve_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenizationSecret:
        """Retrieve the Tokenization Decisioning secret key.

        If one does not exist your
        program yet, calling this endpoint will create one for you. The headers of the
        Tokenization Decisioning request will contain a hmac signature which you can use
        to verify requests originate from Lithic. See
        [this page](https://docs.lithic.com/docs/events-api#verifying-webhooks) for more
        detail about verifying Tokenization Decisioning requests.
        """
        return await self._get(
            "/v1/tokenization_decisioning/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationSecret,
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
    ) -> TokenizationDecisioningRotateSecretResponse:
        """Generate a new Tokenization Decisioning secret key.

        The old Tokenization
        Decisioning secret key will be deactivated 24 hours after a successful request
        to this endpoint.
        """
        return await self._post(
            "/v1/tokenization_decisioning/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationDecisioningRotateSecretResponse,
        )


class TokenizationDecisioningWithRawResponse:
    def __init__(self, tokenization_decisioning: TokenizationDecisioning) -> None:
        self._tokenization_decisioning = tokenization_decisioning

        self.retrieve_secret = _legacy_response.to_raw_response_wrapper(
            tokenization_decisioning.retrieve_secret,
        )
        self.rotate_secret = _legacy_response.to_raw_response_wrapper(
            tokenization_decisioning.rotate_secret,
        )


class AsyncTokenizationDecisioningWithRawResponse:
    def __init__(self, tokenization_decisioning: AsyncTokenizationDecisioning) -> None:
        self._tokenization_decisioning = tokenization_decisioning

        self.retrieve_secret = _legacy_response.async_to_raw_response_wrapper(
            tokenization_decisioning.retrieve_secret,
        )
        self.rotate_secret = _legacy_response.async_to_raw_response_wrapper(
            tokenization_decisioning.rotate_secret,
        )


class TokenizationDecisioningWithStreamingResponse:
    def __init__(self, tokenization_decisioning: TokenizationDecisioning) -> None:
        self._tokenization_decisioning = tokenization_decisioning

        self.retrieve_secret = to_streamed_response_wrapper(
            tokenization_decisioning.retrieve_secret,
        )
        self.rotate_secret = to_streamed_response_wrapper(
            tokenization_decisioning.rotate_secret,
        )


class AsyncTokenizationDecisioningWithStreamingResponse:
    def __init__(self, tokenization_decisioning: AsyncTokenizationDecisioning) -> None:
        self._tokenization_decisioning = tokenization_decisioning

        self.retrieve_secret = async_to_streamed_response_wrapper(
            tokenization_decisioning.retrieve_secret,
        )
        self.rotate_secret = async_to_streamed_response_wrapper(
            tokenization_decisioning.rotate_secret,
        )
