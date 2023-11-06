# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..types import TokenizationSecret, TokenizationDecisioningRotateSecretResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Lithic, AsyncLithic

__all__ = ["TokenizationDecisioning", "AsyncTokenizationDecisioning"]


class TokenizationDecisioning(SyncAPIResource):
    with_raw_response: TokenizationDecisioningWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = TokenizationDecisioningWithRawResponse(self)

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
            "/tokenization_decisioning/secret",
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
        idempotency_key: str | None = None,
    ) -> TokenizationDecisioningRotateSecretResponse:
        """Generate a new Tokenization Decisioning secret key.

        The old Tokenization
        Decisioning secret key will be deactivated 24 hours after a successful request
        to this endpoint.
        """
        return self._post(
            "/tokenization_decisioning/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TokenizationDecisioningRotateSecretResponse,
        )


class AsyncTokenizationDecisioning(AsyncAPIResource):
    with_raw_response: AsyncTokenizationDecisioningWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncTokenizationDecisioningWithRawResponse(self)

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
            "/tokenization_decisioning/secret",
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
        idempotency_key: str | None = None,
    ) -> TokenizationDecisioningRotateSecretResponse:
        """Generate a new Tokenization Decisioning secret key.

        The old Tokenization
        Decisioning secret key will be deactivated 24 hours after a successful request
        to this endpoint.
        """
        return await self._post(
            "/tokenization_decisioning/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=TokenizationDecisioningRotateSecretResponse,
        )


class TokenizationDecisioningWithRawResponse:
    def __init__(self, tokenization_decisioning: TokenizationDecisioning) -> None:
        self.retrieve_secret = to_raw_response_wrapper(
            tokenization_decisioning.retrieve_secret,
        )
        self.rotate_secret = to_raw_response_wrapper(
            tokenization_decisioning.rotate_secret,
        )


class AsyncTokenizationDecisioningWithRawResponse:
    def __init__(self, tokenization_decisioning: AsyncTokenizationDecisioning) -> None:
        self.retrieve_secret = async_to_raw_response_wrapper(
            tokenization_decisioning.retrieve_secret,
        )
        self.rotate_secret = async_to_raw_response_wrapper(
            tokenization_decisioning.rotate_secret,
        )
