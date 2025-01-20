# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    tokenization_list_params,
    tokenization_simulate_params,
    tokenization_resend_activation_code_params,
    tokenization_update_digital_card_art_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.tokenization import Tokenization
from ..types.tokenization_retrieve_response import TokenizationRetrieveResponse
from ..types.tokenization_simulate_response import TokenizationSimulateResponse
from ..types.tokenization_update_digital_card_art_response import TokenizationUpdateDigitalCardArtResponse

__all__ = ["Tokenizations", "AsyncTokenizations"]


class Tokenizations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokenizationsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return TokenizationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokenizationsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return TokenizationsWithStreamingResponse(self)

    def retrieve(
        self,
        tokenization_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenizationRetrieveResponse:
        """
        Get tokenization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return self._get(
            f"/v1/tokenizations/{tokenization_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationRetrieveResponse,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        begin: Union[str, date] | NotGiven = NOT_GIVEN,
        card_token: str | NotGiven = NOT_GIVEN,
        end: Union[str, date] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        tokenization_channel: Literal["DIGITAL_WALLET", "MERCHANT", "ALL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Tokenization]:
        """
        List card tokenizations

        Args:
          account_token: Filters for tokenizations associated with a specific account.

          begin: Filter for tokenizations created after this date.

          card_token: Filters for tokenizations associated with a specific card.

          end: Filter for tokenizations created before this date.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          tokenization_channel: Filter for tokenizations by tokenization channel. If this is not specified, only
              DIGITAL_WALLET tokenizations will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/tokenizations",
            page=SyncCursorPage[Tokenization],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "begin": begin,
                        "card_token": card_token,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "tokenization_channel": tokenization_channel,
                    },
                    tokenization_list_params.TokenizationListParams,
                ),
            ),
            model=Tokenization,
        )

    def activate(
        self,
        tokenization_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This endpoint is used to ask the card network to activate a tokenization.

        A
        successful response indicates that the request was successfully delivered to the
        card network. When the card network activates the tokenization, the state will
        be updated and a tokenization.updated event will be sent. The endpoint may only
        be used on digital wallet tokenizations with status `INACTIVE`,
        `PENDING_ACTIVATION`, or `PENDING_2FA`. This will put the tokenization in an
        active state, and transactions will be allowed. Reach out at
        [lithic.com/contact](https://lithic.com/contact) for more information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return self._post(
            f"/v1/tokenizations/{tokenization_token}/activate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def deactivate(
        self,
        tokenization_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This endpoint is used to ask the card network to deactivate a tokenization.

        A
        successful response indicates that the request was successfully delivered to the
        card network. When the card network deactivates the tokenization, the state will
        be updated and a tokenization.updated event will be sent. Authorizations
        attempted with a deactivated tokenization will be blocked and will not be
        forwarded to Lithic from the network. Deactivating the token is a permanent
        operation. If the target is a digital wallet tokenization, it will be removed
        from its device. Reach out at [lithic.com/contact](https://lithic.com/contact)
        for more information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return self._post(
            f"/v1/tokenizations/{tokenization_token}/deactivate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def pause(
        self,
        tokenization_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This endpoint is used to ask the card network to pause a tokenization.

        A
        successful response indicates that the request was successfully delivered to the
        card network. When the card network pauses the tokenization, the state will be
        updated and a tokenization.updated event will be sent. The endpoint may only be
        used on tokenizations with status `ACTIVE`. A paused token will prevent
        merchants from sending authorizations, and is a temporary status that can be
        changed. Reach out at [lithic.com/contact](https://lithic.com/contact) for more
        information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return self._post(
            f"/v1/tokenizations/{tokenization_token}/pause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def resend_activation_code(
        self,
        tokenization_token: str,
        *,
        activation_method_type: Literal["EMAIL_TO_CARDHOLDER_ADDRESS", "TEXT_TO_CARDHOLDER_NUMBER"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This endpoint is used to ask the card network to send another activation code to
        a cardholder that has already tried tokenizing a card. A successful response
        indicates that the request was successfully delivered to the card network. The
        endpoint may only be used on Mastercard digital wallet tokenizations with status
        `INACTIVE`, `PENDING_ACTIVATION`, or `PENDING_2FA`. The network will send a new
        activation code to the one of the contact methods provided in the initial
        tokenization flow. If a user fails to enter the code correctly 3 times, the
        contact method will not be eligible for resending the activation code, and the
        cardholder must restart the provision process. Reach out at
        [lithic.com/contact](https://lithic.com/contact) for more information.

        Args:
          activation_method_type: The communication method that the user has selected to use to receive the
              authentication code. Supported Values: Sms = "TEXT_TO_CARDHOLDER_NUMBER". Email
              = "EMAIL_TO_CARDHOLDER_ADDRESS"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return self._post(
            f"/v1/tokenizations/{tokenization_token}/resend_activation_code",
            body=maybe_transform(
                {"activation_method_type": activation_method_type},
                tokenization_resend_activation_code_params.TokenizationResendActivationCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def simulate(
        self,
        *,
        cvv: str,
        expiration_date: str,
        pan: str,
        tokenization_source: Literal["APPLE_PAY", "GOOGLE", "SAMSUNG_PAY", "MERCHANT"],
        account_score: int | NotGiven = NOT_GIVEN,
        device_score: int | NotGiven = NOT_GIVEN,
        entity: str | NotGiven = NOT_GIVEN,
        wallet_recommended_decision: Literal["APPROVED", "DECLINED", "REQUIRE_ADDITIONAL_AUTHENTICATION"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenizationSimulateResponse:
        """
        This endpoint is used to simulate a card's tokenization in the Digital Wallet
        and merchant tokenization ecosystem.

        Args:
          cvv: The three digit cvv for the card.

          expiration_date: The expiration date of the card in 'MM/YY' format.

          pan: The sixteen digit card number.

          tokenization_source: The source of the tokenization request.

          account_score: The account score (1-5) that represents how the Digital Wallet's view on how
              reputable an end user's account is.

          device_score: The device score (1-5) that represents how the Digital Wallet's view on how
              reputable an end user's device is.

          entity: Optional field to specify the token requestor name for a merchant token
              simulation. Ignored when tokenization_source is not MERCHANT.

          wallet_recommended_decision: The decision that the Digital Wallet's recommend

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulate/tokenizations",
            body=maybe_transform(
                {
                    "cvv": cvv,
                    "expiration_date": expiration_date,
                    "pan": pan,
                    "tokenization_source": tokenization_source,
                    "account_score": account_score,
                    "device_score": device_score,
                    "entity": entity,
                    "wallet_recommended_decision": wallet_recommended_decision,
                },
                tokenization_simulate_params.TokenizationSimulateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationSimulateResponse,
        )

    def unpause(
        self,
        tokenization_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This endpoint is used to ask the card network to unpause a tokenization.

        A
        successful response indicates that the request was successfully delivered to the
        card network. When the card network unpauses the tokenization, the state will be
        updated and a tokenization.updated event will be sent. The endpoint may only be
        used on tokenizations with status `PAUSED`. This will put the tokenization in an
        active state, and transactions may resume. Reach out at
        [lithic.com/contact](https://lithic.com/contact) for more information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return self._post(
            f"/v1/tokenizations/{tokenization_token}/unpause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_digital_card_art(
        self,
        tokenization_token: str,
        *,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenizationUpdateDigitalCardArtResponse:
        """
        This endpoint is used update the digital card art for a digital wallet
        tokenization. A successful response indicates that the card network has updated
        the tokenization's art, and the tokenization's `digital_cart_art_token` field
        was updated. The endpoint may not be used on tokenizations with status
        `DEACTIVATED`. Note that this updates the art for one specific tokenization, not
        all tokenizations for a card. New tokenizations for a card will be created with
        the art referenced in the card object's `digital_card_art_token` field. Reach
        out at [lithic.com/contact](https://lithic.com/contact) for more information.

        Args:
          digital_card_art_token: Specifies the digital card art to be displayed in the user’s digital wallet for
              a tokenization. This artwork must be approved by the network and configured by
              Lithic to use. See
              [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return self._post(
            f"/v1/tokenizations/{tokenization_token}/update_digital_card_art",
            body=maybe_transform(
                {"digital_card_art_token": digital_card_art_token},
                tokenization_update_digital_card_art_params.TokenizationUpdateDigitalCardArtParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationUpdateDigitalCardArtResponse,
        )


class AsyncTokenizations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokenizationsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTokenizationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokenizationsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncTokenizationsWithStreamingResponse(self)

    async def retrieve(
        self,
        tokenization_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenizationRetrieveResponse:
        """
        Get tokenization

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return await self._get(
            f"/v1/tokenizations/{tokenization_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationRetrieveResponse,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        begin: Union[str, date] | NotGiven = NOT_GIVEN,
        card_token: str | NotGiven = NOT_GIVEN,
        end: Union[str, date] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        tokenization_channel: Literal["DIGITAL_WALLET", "MERCHANT", "ALL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Tokenization, AsyncCursorPage[Tokenization]]:
        """
        List card tokenizations

        Args:
          account_token: Filters for tokenizations associated with a specific account.

          begin: Filter for tokenizations created after this date.

          card_token: Filters for tokenizations associated with a specific card.

          end: Filter for tokenizations created before this date.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          tokenization_channel: Filter for tokenizations by tokenization channel. If this is not specified, only
              DIGITAL_WALLET tokenizations will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/tokenizations",
            page=AsyncCursorPage[Tokenization],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "begin": begin,
                        "card_token": card_token,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "tokenization_channel": tokenization_channel,
                    },
                    tokenization_list_params.TokenizationListParams,
                ),
            ),
            model=Tokenization,
        )

    async def activate(
        self,
        tokenization_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This endpoint is used to ask the card network to activate a tokenization.

        A
        successful response indicates that the request was successfully delivered to the
        card network. When the card network activates the tokenization, the state will
        be updated and a tokenization.updated event will be sent. The endpoint may only
        be used on digital wallet tokenizations with status `INACTIVE`,
        `PENDING_ACTIVATION`, or `PENDING_2FA`. This will put the tokenization in an
        active state, and transactions will be allowed. Reach out at
        [lithic.com/contact](https://lithic.com/contact) for more information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return await self._post(
            f"/v1/tokenizations/{tokenization_token}/activate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def deactivate(
        self,
        tokenization_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This endpoint is used to ask the card network to deactivate a tokenization.

        A
        successful response indicates that the request was successfully delivered to the
        card network. When the card network deactivates the tokenization, the state will
        be updated and a tokenization.updated event will be sent. Authorizations
        attempted with a deactivated tokenization will be blocked and will not be
        forwarded to Lithic from the network. Deactivating the token is a permanent
        operation. If the target is a digital wallet tokenization, it will be removed
        from its device. Reach out at [lithic.com/contact](https://lithic.com/contact)
        for more information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return await self._post(
            f"/v1/tokenizations/{tokenization_token}/deactivate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def pause(
        self,
        tokenization_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This endpoint is used to ask the card network to pause a tokenization.

        A
        successful response indicates that the request was successfully delivered to the
        card network. When the card network pauses the tokenization, the state will be
        updated and a tokenization.updated event will be sent. The endpoint may only be
        used on tokenizations with status `ACTIVE`. A paused token will prevent
        merchants from sending authorizations, and is a temporary status that can be
        changed. Reach out at [lithic.com/contact](https://lithic.com/contact) for more
        information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return await self._post(
            f"/v1/tokenizations/{tokenization_token}/pause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def resend_activation_code(
        self,
        tokenization_token: str,
        *,
        activation_method_type: Literal["EMAIL_TO_CARDHOLDER_ADDRESS", "TEXT_TO_CARDHOLDER_NUMBER"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        This endpoint is used to ask the card network to send another activation code to
        a cardholder that has already tried tokenizing a card. A successful response
        indicates that the request was successfully delivered to the card network. The
        endpoint may only be used on Mastercard digital wallet tokenizations with status
        `INACTIVE`, `PENDING_ACTIVATION`, or `PENDING_2FA`. The network will send a new
        activation code to the one of the contact methods provided in the initial
        tokenization flow. If a user fails to enter the code correctly 3 times, the
        contact method will not be eligible for resending the activation code, and the
        cardholder must restart the provision process. Reach out at
        [lithic.com/contact](https://lithic.com/contact) for more information.

        Args:
          activation_method_type: The communication method that the user has selected to use to receive the
              authentication code. Supported Values: Sms = "TEXT_TO_CARDHOLDER_NUMBER". Email
              = "EMAIL_TO_CARDHOLDER_ADDRESS"

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return await self._post(
            f"/v1/tokenizations/{tokenization_token}/resend_activation_code",
            body=await async_maybe_transform(
                {"activation_method_type": activation_method_type},
                tokenization_resend_activation_code_params.TokenizationResendActivationCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def simulate(
        self,
        *,
        cvv: str,
        expiration_date: str,
        pan: str,
        tokenization_source: Literal["APPLE_PAY", "GOOGLE", "SAMSUNG_PAY", "MERCHANT"],
        account_score: int | NotGiven = NOT_GIVEN,
        device_score: int | NotGiven = NOT_GIVEN,
        entity: str | NotGiven = NOT_GIVEN,
        wallet_recommended_decision: Literal["APPROVED", "DECLINED", "REQUIRE_ADDITIONAL_AUTHENTICATION"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenizationSimulateResponse:
        """
        This endpoint is used to simulate a card's tokenization in the Digital Wallet
        and merchant tokenization ecosystem.

        Args:
          cvv: The three digit cvv for the card.

          expiration_date: The expiration date of the card in 'MM/YY' format.

          pan: The sixteen digit card number.

          tokenization_source: The source of the tokenization request.

          account_score: The account score (1-5) that represents how the Digital Wallet's view on how
              reputable an end user's account is.

          device_score: The device score (1-5) that represents how the Digital Wallet's view on how
              reputable an end user's device is.

          entity: Optional field to specify the token requestor name for a merchant token
              simulation. Ignored when tokenization_source is not MERCHANT.

          wallet_recommended_decision: The decision that the Digital Wallet's recommend

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulate/tokenizations",
            body=await async_maybe_transform(
                {
                    "cvv": cvv,
                    "expiration_date": expiration_date,
                    "pan": pan,
                    "tokenization_source": tokenization_source,
                    "account_score": account_score,
                    "device_score": device_score,
                    "entity": entity,
                    "wallet_recommended_decision": wallet_recommended_decision,
                },
                tokenization_simulate_params.TokenizationSimulateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationSimulateResponse,
        )

    async def unpause(
        self,
        tokenization_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """This endpoint is used to ask the card network to unpause a tokenization.

        A
        successful response indicates that the request was successfully delivered to the
        card network. When the card network unpauses the tokenization, the state will be
        updated and a tokenization.updated event will be sent. The endpoint may only be
        used on tokenizations with status `PAUSED`. This will put the tokenization in an
        active state, and transactions may resume. Reach out at
        [lithic.com/contact](https://lithic.com/contact) for more information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return await self._post(
            f"/v1/tokenizations/{tokenization_token}/unpause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_digital_card_art(
        self,
        tokenization_token: str,
        *,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenizationUpdateDigitalCardArtResponse:
        """
        This endpoint is used update the digital card art for a digital wallet
        tokenization. A successful response indicates that the card network has updated
        the tokenization's art, and the tokenization's `digital_cart_art_token` field
        was updated. The endpoint may not be used on tokenizations with status
        `DEACTIVATED`. Note that this updates the art for one specific tokenization, not
        all tokenizations for a card. New tokenizations for a card will be created with
        the art referenced in the card object's `digital_card_art_token` field. Reach
        out at [lithic.com/contact](https://lithic.com/contact) for more information.

        Args:
          digital_card_art_token: Specifies the digital card art to be displayed in the user’s digital wallet for
              a tokenization. This artwork must be approved by the network and configured by
              Lithic to use. See
              [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return await self._post(
            f"/v1/tokenizations/{tokenization_token}/update_digital_card_art",
            body=await async_maybe_transform(
                {"digital_card_art_token": digital_card_art_token},
                tokenization_update_digital_card_art_params.TokenizationUpdateDigitalCardArtParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationUpdateDigitalCardArtResponse,
        )


class TokenizationsWithRawResponse:
    def __init__(self, tokenizations: Tokenizations) -> None:
        self._tokenizations = tokenizations

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            tokenizations.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            tokenizations.list,
        )
        self.activate = _legacy_response.to_raw_response_wrapper(
            tokenizations.activate,
        )
        self.deactivate = _legacy_response.to_raw_response_wrapper(
            tokenizations.deactivate,
        )
        self.pause = _legacy_response.to_raw_response_wrapper(
            tokenizations.pause,
        )
        self.resend_activation_code = _legacy_response.to_raw_response_wrapper(
            tokenizations.resend_activation_code,
        )
        self.simulate = _legacy_response.to_raw_response_wrapper(
            tokenizations.simulate,
        )
        self.unpause = _legacy_response.to_raw_response_wrapper(
            tokenizations.unpause,
        )
        self.update_digital_card_art = _legacy_response.to_raw_response_wrapper(
            tokenizations.update_digital_card_art,
        )


class AsyncTokenizationsWithRawResponse:
    def __init__(self, tokenizations: AsyncTokenizations) -> None:
        self._tokenizations = tokenizations

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.list,
        )
        self.activate = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.activate,
        )
        self.deactivate = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.deactivate,
        )
        self.pause = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.pause,
        )
        self.resend_activation_code = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.resend_activation_code,
        )
        self.simulate = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.simulate,
        )
        self.unpause = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.unpause,
        )
        self.update_digital_card_art = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.update_digital_card_art,
        )


class TokenizationsWithStreamingResponse:
    def __init__(self, tokenizations: Tokenizations) -> None:
        self._tokenizations = tokenizations

        self.retrieve = to_streamed_response_wrapper(
            tokenizations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tokenizations.list,
        )
        self.activate = to_streamed_response_wrapper(
            tokenizations.activate,
        )
        self.deactivate = to_streamed_response_wrapper(
            tokenizations.deactivate,
        )
        self.pause = to_streamed_response_wrapper(
            tokenizations.pause,
        )
        self.resend_activation_code = to_streamed_response_wrapper(
            tokenizations.resend_activation_code,
        )
        self.simulate = to_streamed_response_wrapper(
            tokenizations.simulate,
        )
        self.unpause = to_streamed_response_wrapper(
            tokenizations.unpause,
        )
        self.update_digital_card_art = to_streamed_response_wrapper(
            tokenizations.update_digital_card_art,
        )


class AsyncTokenizationsWithStreamingResponse:
    def __init__(self, tokenizations: AsyncTokenizations) -> None:
        self._tokenizations = tokenizations

        self.retrieve = async_to_streamed_response_wrapper(
            tokenizations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tokenizations.list,
        )
        self.activate = async_to_streamed_response_wrapper(
            tokenizations.activate,
        )
        self.deactivate = async_to_streamed_response_wrapper(
            tokenizations.deactivate,
        )
        self.pause = async_to_streamed_response_wrapper(
            tokenizations.pause,
        )
        self.resend_activation_code = async_to_streamed_response_wrapper(
            tokenizations.resend_activation_code,
        )
        self.simulate = async_to_streamed_response_wrapper(
            tokenizations.simulate,
        )
        self.unpause = async_to_streamed_response_wrapper(
            tokenizations.unpause,
        )
        self.update_digital_card_art = async_to_streamed_response_wrapper(
            tokenizations.update_digital_card_art,
        )
