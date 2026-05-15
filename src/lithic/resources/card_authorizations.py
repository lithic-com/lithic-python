# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import card_authorization_challenge_response_params
from .._types import Body, Query, Headers, NoneType, NotGiven, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import make_request_options

__all__ = ["CardAuthorizations", "AsyncCardAuthorizations"]


class CardAuthorizations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardAuthorizationsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return CardAuthorizationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardAuthorizationsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return CardAuthorizationsWithStreamingResponse(self)

    def challenge_response(
        self,
        event_token: str,
        *,
        response: Literal["APPROVE", "DECLINE"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Card program's response to Authorization Challenge.

        Programs that have
        Authorization Challenges configured as Out of Band receive a
        [card_authorization.challenge](https://docs.lithic.com/reference/post_card-authorization-challenge)
        webhook when an authorization attempt triggers a challenge. The card program
        should respond using this endpoint after the cardholder completes the challenge.

        Args:
          response: Whether the cardholder has approved or declined the issued challenge

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_token:
            raise ValueError(f"Expected a non-empty value for `event_token` but received {event_token!r}")
        return self._post(
            path_template("/v1/card_authorizations/{event_token}/challenge_response", event_token=event_token),
            body=maybe_transform(
                {"response": response},
                card_authorization_challenge_response_params.CardAuthorizationChallengeResponseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCardAuthorizations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardAuthorizationsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardAuthorizationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardAuthorizationsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncCardAuthorizationsWithStreamingResponse(self)

    async def challenge_response(
        self,
        event_token: str,
        *,
        response: Literal["APPROVE", "DECLINE"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Card program's response to Authorization Challenge.

        Programs that have
        Authorization Challenges configured as Out of Band receive a
        [card_authorization.challenge](https://docs.lithic.com/reference/post_card-authorization-challenge)
        webhook when an authorization attempt triggers a challenge. The card program
        should respond using this endpoint after the cardholder completes the challenge.

        Args:
          response: Whether the cardholder has approved or declined the issued challenge

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not event_token:
            raise ValueError(f"Expected a non-empty value for `event_token` but received {event_token!r}")
        return await self._post(
            path_template("/v1/card_authorizations/{event_token}/challenge_response", event_token=event_token),
            body=await async_maybe_transform(
                {"response": response},
                card_authorization_challenge_response_params.CardAuthorizationChallengeResponseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CardAuthorizationsWithRawResponse:
    def __init__(self, card_authorizations: CardAuthorizations) -> None:
        self._card_authorizations = card_authorizations

        self.challenge_response = _legacy_response.to_raw_response_wrapper(
            card_authorizations.challenge_response,
        )


class AsyncCardAuthorizationsWithRawResponse:
    def __init__(self, card_authorizations: AsyncCardAuthorizations) -> None:
        self._card_authorizations = card_authorizations

        self.challenge_response = _legacy_response.async_to_raw_response_wrapper(
            card_authorizations.challenge_response,
        )


class CardAuthorizationsWithStreamingResponse:
    def __init__(self, card_authorizations: CardAuthorizations) -> None:
        self._card_authorizations = card_authorizations

        self.challenge_response = to_streamed_response_wrapper(
            card_authorizations.challenge_response,
        )


class AsyncCardAuthorizationsWithStreamingResponse:
    def __init__(self, card_authorizations: AsyncCardAuthorizations) -> None:
        self._card_authorizations = card_authorizations

        self.challenge_response = async_to_streamed_response_wrapper(
            card_authorizations.challenge_response,
        )
