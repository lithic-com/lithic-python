# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    tokenization_list_params,
    tokenization_create_params,
    tokenization_simulate_params,
    tokenization_submit_tfa_params,
    tokenization_select_tfa_method_params,
    tokenization_resend_activation_code_params,
    tokenization_update_digital_card_art_params,
    tokenization_create_payment_credentials_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.tokenization import Tokenization
from ..types.tokenization_submit_tfa_response import TokenizationSubmitTfaResponse
from ..types.tokenization_select_tfa_method_response import TokenizationSelectTfaMethodResponse
from ..types.tokenization_create_payment_credentials_response import TokenizationCreatePaymentCredentialsResponse

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

    def create(
        self,
        card_token: str,
        *,
        agent_token: str,
        type: Literal["AGENT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tokenization:
        """
        > 🚧 Beta API
        >
        > This endpoint is in beta and subject to change.

        Create a tokenization for an OPEN card. Contact your Lithic representative to
        configure tokenization for your program and card network.

        If the status is PENDING_2FA, select an available tfa_methods entry and submit
        the cardholder's authentication code. An ACTIVE tokenization can then be used to
        create payment credentials.

        Additional attempts to create the same tokenizations on a card will result in a
        409 Conflict.

        Args:
          agent_token: Globally unique identifier for the active agent configured for your program

          type: Type of tokenization to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._post(
            path_template("/v1/cards/{card_token}/tokenizations", card_token=card_token),
            body=maybe_transform(
                {
                    "agent_token": agent_token,
                    "type": type,
                },
                tokenization_create_params.TokenizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tokenization,
        )

    def retrieve(
        self,
        tokenization_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tokenization:
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
            path_template("/v1/tokenizations/{tokenization_token}", tokenization_token=tokenization_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tokenization,
        )

    def list(
        self,
        *,
        account_token: str | Omit = omit,
        begin: Union[str, date] | Omit = omit,
        card_token: str | Omit = omit,
        end: Union[str, date] | Omit = omit,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        tokenization_channel: Literal["DIGITAL_WALLET", "MERCHANT", "AGENT_PAY", "ALL"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Tokenization]:
        """
        List card tokenizations

        Args:
          account_token: Filters for tokenizations associated with a specific account.

          begin: Filter for tokenizations created on or after this date.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/tokenizations/{tokenization_token}/activate", tokenization_token=tokenization_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def create_payment_credentials(
        self,
        tokenization_token: str,
        *,
        device: tokenization_create_payment_credentials_params.Device,
        mandate: tokenization_create_payment_credentials_params.Mandate,
        type: Literal["AUTONOMOUS", "HUMAN_IN_THE_LOOP", "RECURRING"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenizationCreatePaymentCredentialsResponse:
        """
        > 🚧 Beta API
        >
        > This endpoint is in beta and subject to change.

        Create payment credentials and a purchase mandate for an ACTIVE tokenization.

        The credential value, expiration date, and CVV are only available in this
        response and cannot be retrieved later.

        Args:
          device: Device used for the purchase

          type: Type of purchase for which payment credentials are requested

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return self._post(
            path_template(
                "/v1/tokenizations/{tokenization_token}/payment_credentials", tokenization_token=tokenization_token
            ),
            body=maybe_transform(
                {
                    "device": device,
                    "mandate": mandate,
                    "type": type,
                },
                tokenization_create_payment_credentials_params.TokenizationCreatePaymentCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationCreatePaymentCredentialsResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/tokenizations/{tokenization_token}/deactivate", tokenization_token=tokenization_token),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/tokenizations/{tokenization_token}/pause", tokenization_token=tokenization_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def resend_activation_code(
        self,
        tokenization_token: str,
        *,
        activation_method_type: Literal["EMAIL_TO_CARDHOLDER_ADDRESS", "TEXT_TO_CARDHOLDER_NUMBER"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template(
                "/v1/tokenizations/{tokenization_token}/resend_activation_code", tokenization_token=tokenization_token
            ),
            body=maybe_transform(
                {"activation_method_type": activation_method_type},
                tokenization_resend_activation_code_params.TokenizationResendActivationCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def select_tfa_method(
        self,
        tokenization_token: str,
        *,
        method: Literal["SMS", "EMAIL"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenizationSelectTfaMethodResponse:
        """
        > 🚧 Beta API
        >
        > This endpoint is in beta and subject to change.

        Select an available SMS or EMAIL authentication method for a tokenization with
        status PENDING_2FA. Use a method returned in the tokenization's list of
        tfa_methods. The card network initiates delivery of the authentication code to
        the corresponding destination.

        A successful response confirms method selection, not tokenization activation.
        Submit the code using submit_tfa after the cardholder receives it.

        Args:
          method: An available method from the tokenization's list of tfa_methods

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return self._post(
            path_template(
                "/v1/tokenizations/{tokenization_token}/select_tfa_method", tokenization_token=tokenization_token
            ),
            body=maybe_transform(
                {"method": method}, tokenization_select_tfa_method_params.TokenizationSelectTfaMethodParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationSelectTfaMethodResponse,
        )

    def simulate(
        self,
        *,
        cvv: str,
        expiration_date: str,
        pan: str,
        tokenization_source: Literal["APPLE_PAY", "GOOGLE", "SAMSUNG_PAY", "MERCHANT"],
        account_score: int | Omit = omit,
        device_score: int | Omit = omit,
        entity: str | Omit = omit,
        wallet_recommended_decision: Literal["APPROVED", "DECLINED", "REQUIRE_ADDITIONAL_AUTHENTICATION"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tokenization:
        """
        This endpoint is used to simulate a card's tokenization in the Digital Wallet
        and merchant tokenization ecosystem.

        Args:
          cvv: The three or four digit CVV for the card. AMEX cards use four digit CVVs.

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
            cast_to=Tokenization,
        )

    def submit_tfa(
        self,
        tokenization_token: str,
        *,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenizationSubmitTfaResponse:
        """
        > 🚧 Beta API
        >
        > This endpoint is in beta and subject to change.

        Submit the cardholder's one-time authentication code for a tokenization with
        status PENDING_2FA. A successful select_tfa_method request must precede
        submission. Send the code as a string to preserve leading zeros.

        A successful response means that the network accepted the authentication code.
        The activation of a tokenization will occur asynchronously initiated by the card
        network.

        Args:
          value: One-time authentication code received by the cardholder, including any leading
              zeros

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return self._post(
            path_template("/v1/tokenizations/{tokenization_token}/submit_tfa", tokenization_token=tokenization_token),
            body=maybe_transform({"value": value}, tokenization_submit_tfa_params.TokenizationSubmitTfaParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationSubmitTfaResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/tokenizations/{tokenization_token}/unpause", tokenization_token=tokenization_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def update_digital_card_art(
        self,
        tokenization_token: str,
        *,
        digital_card_art_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tokenization:
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
            path_template(
                "/v1/tokenizations/{tokenization_token}/update_digital_card_art", tokenization_token=tokenization_token
            ),
            body=maybe_transform(
                {"digital_card_art_token": digital_card_art_token},
                tokenization_update_digital_card_art_params.TokenizationUpdateDigitalCardArtParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tokenization,
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

    async def create(
        self,
        card_token: str,
        *,
        agent_token: str,
        type: Literal["AGENT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tokenization:
        """
        > 🚧 Beta API
        >
        > This endpoint is in beta and subject to change.

        Create a tokenization for an OPEN card. Contact your Lithic representative to
        configure tokenization for your program and card network.

        If the status is PENDING_2FA, select an available tfa_methods entry and submit
        the cardholder's authentication code. An ACTIVE tokenization can then be used to
        create payment credentials.

        Additional attempts to create the same tokenizations on a card will result in a
        409 Conflict.

        Args:
          agent_token: Globally unique identifier for the active agent configured for your program

          type: Type of tokenization to create

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return await self._post(
            path_template("/v1/cards/{card_token}/tokenizations", card_token=card_token),
            body=await async_maybe_transform(
                {
                    "agent_token": agent_token,
                    "type": type,
                },
                tokenization_create_params.TokenizationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tokenization,
        )

    async def retrieve(
        self,
        tokenization_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tokenization:
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
            path_template("/v1/tokenizations/{tokenization_token}", tokenization_token=tokenization_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tokenization,
        )

    def list(
        self,
        *,
        account_token: str | Omit = omit,
        begin: Union[str, date] | Omit = omit,
        card_token: str | Omit = omit,
        end: Union[str, date] | Omit = omit,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        tokenization_channel: Literal["DIGITAL_WALLET", "MERCHANT", "AGENT_PAY", "ALL"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Tokenization, AsyncCursorPage[Tokenization]]:
        """
        List card tokenizations

        Args:
          account_token: Filters for tokenizations associated with a specific account.

          begin: Filter for tokenizations created on or after this date.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/tokenizations/{tokenization_token}/activate", tokenization_token=tokenization_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def create_payment_credentials(
        self,
        tokenization_token: str,
        *,
        device: tokenization_create_payment_credentials_params.Device,
        mandate: tokenization_create_payment_credentials_params.Mandate,
        type: Literal["AUTONOMOUS", "HUMAN_IN_THE_LOOP", "RECURRING"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenizationCreatePaymentCredentialsResponse:
        """
        > 🚧 Beta API
        >
        > This endpoint is in beta and subject to change.

        Create payment credentials and a purchase mandate for an ACTIVE tokenization.

        The credential value, expiration date, and CVV are only available in this
        response and cannot be retrieved later.

        Args:
          device: Device used for the purchase

          type: Type of purchase for which payment credentials are requested

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return await self._post(
            path_template(
                "/v1/tokenizations/{tokenization_token}/payment_credentials", tokenization_token=tokenization_token
            ),
            body=await async_maybe_transform(
                {
                    "device": device,
                    "mandate": mandate,
                    "type": type,
                },
                tokenization_create_payment_credentials_params.TokenizationCreatePaymentCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationCreatePaymentCredentialsResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/tokenizations/{tokenization_token}/deactivate", tokenization_token=tokenization_token),
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/tokenizations/{tokenization_token}/pause", tokenization_token=tokenization_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def resend_activation_code(
        self,
        tokenization_token: str,
        *,
        activation_method_type: Literal["EMAIL_TO_CARDHOLDER_ADDRESS", "TEXT_TO_CARDHOLDER_NUMBER"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template(
                "/v1/tokenizations/{tokenization_token}/resend_activation_code", tokenization_token=tokenization_token
            ),
            body=await async_maybe_transform(
                {"activation_method_type": activation_method_type},
                tokenization_resend_activation_code_params.TokenizationResendActivationCodeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def select_tfa_method(
        self,
        tokenization_token: str,
        *,
        method: Literal["SMS", "EMAIL"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenizationSelectTfaMethodResponse:
        """
        > 🚧 Beta API
        >
        > This endpoint is in beta and subject to change.

        Select an available SMS or EMAIL authentication method for a tokenization with
        status PENDING_2FA. Use a method returned in the tokenization's list of
        tfa_methods. The card network initiates delivery of the authentication code to
        the corresponding destination.

        A successful response confirms method selection, not tokenization activation.
        Submit the code using submit_tfa after the cardholder receives it.

        Args:
          method: An available method from the tokenization's list of tfa_methods

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return await self._post(
            path_template(
                "/v1/tokenizations/{tokenization_token}/select_tfa_method", tokenization_token=tokenization_token
            ),
            body=await async_maybe_transform(
                {"method": method}, tokenization_select_tfa_method_params.TokenizationSelectTfaMethodParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationSelectTfaMethodResponse,
        )

    async def simulate(
        self,
        *,
        cvv: str,
        expiration_date: str,
        pan: str,
        tokenization_source: Literal["APPLE_PAY", "GOOGLE", "SAMSUNG_PAY", "MERCHANT"],
        account_score: int | Omit = omit,
        device_score: int | Omit = omit,
        entity: str | Omit = omit,
        wallet_recommended_decision: Literal["APPROVED", "DECLINED", "REQUIRE_ADDITIONAL_AUTHENTICATION"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tokenization:
        """
        This endpoint is used to simulate a card's tokenization in the Digital Wallet
        and merchant tokenization ecosystem.

        Args:
          cvv: The three or four digit CVV for the card. AMEX cards use four digit CVVs.

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
            cast_to=Tokenization,
        )

    async def submit_tfa(
        self,
        tokenization_token: str,
        *,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenizationSubmitTfaResponse:
        """
        > 🚧 Beta API
        >
        > This endpoint is in beta and subject to change.

        Submit the cardholder's one-time authentication code for a tokenization with
        status PENDING_2FA. A successful select_tfa_method request must precede
        submission. Send the code as a string to preserve leading zeros.

        A successful response means that the network accepted the authentication code.
        The activation of a tokenization will occur asynchronously initiated by the card
        network.

        Args:
          value: One-time authentication code received by the cardholder, including any leading
              zeros

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tokenization_token:
            raise ValueError(f"Expected a non-empty value for `tokenization_token` but received {tokenization_token!r}")
        return await self._post(
            path_template("/v1/tokenizations/{tokenization_token}/submit_tfa", tokenization_token=tokenization_token),
            body=await async_maybe_transform(
                {"value": value}, tokenization_submit_tfa_params.TokenizationSubmitTfaParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TokenizationSubmitTfaResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
            path_template("/v1/tokenizations/{tokenization_token}/unpause", tokenization_token=tokenization_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def update_digital_card_art(
        self,
        tokenization_token: str,
        *,
        digital_card_art_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tokenization:
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
            path_template(
                "/v1/tokenizations/{tokenization_token}/update_digital_card_art", tokenization_token=tokenization_token
            ),
            body=await async_maybe_transform(
                {"digital_card_art_token": digital_card_art_token},
                tokenization_update_digital_card_art_params.TokenizationUpdateDigitalCardArtParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tokenization,
        )


class TokenizationsWithRawResponse:
    def __init__(self, tokenizations: Tokenizations) -> None:
        self._tokenizations = tokenizations

        self.create = _legacy_response.to_raw_response_wrapper(
            tokenizations.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            tokenizations.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            tokenizations.list,
        )
        self.activate = _legacy_response.to_raw_response_wrapper(
            tokenizations.activate,
        )
        self.create_payment_credentials = _legacy_response.to_raw_response_wrapper(
            tokenizations.create_payment_credentials,
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
        self.select_tfa_method = _legacy_response.to_raw_response_wrapper(
            tokenizations.select_tfa_method,
        )
        self.simulate = _legacy_response.to_raw_response_wrapper(
            tokenizations.simulate,
        )
        self.submit_tfa = _legacy_response.to_raw_response_wrapper(
            tokenizations.submit_tfa,
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

        self.create = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.list,
        )
        self.activate = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.activate,
        )
        self.create_payment_credentials = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.create_payment_credentials,
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
        self.select_tfa_method = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.select_tfa_method,
        )
        self.simulate = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.simulate,
        )
        self.submit_tfa = _legacy_response.async_to_raw_response_wrapper(
            tokenizations.submit_tfa,
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

        self.create = to_streamed_response_wrapper(
            tokenizations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tokenizations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            tokenizations.list,
        )
        self.activate = to_streamed_response_wrapper(
            tokenizations.activate,
        )
        self.create_payment_credentials = to_streamed_response_wrapper(
            tokenizations.create_payment_credentials,
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
        self.select_tfa_method = to_streamed_response_wrapper(
            tokenizations.select_tfa_method,
        )
        self.simulate = to_streamed_response_wrapper(
            tokenizations.simulate,
        )
        self.submit_tfa = to_streamed_response_wrapper(
            tokenizations.submit_tfa,
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

        self.create = async_to_streamed_response_wrapper(
            tokenizations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tokenizations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            tokenizations.list,
        )
        self.activate = async_to_streamed_response_wrapper(
            tokenizations.activate,
        )
        self.create_payment_credentials = async_to_streamed_response_wrapper(
            tokenizations.create_payment_credentials,
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
        self.select_tfa_method = async_to_streamed_response_wrapper(
            tokenizations.select_tfa_method,
        )
        self.simulate = async_to_streamed_response_wrapper(
            tokenizations.simulate,
        )
        self.submit_tfa = async_to_streamed_response_wrapper(
            tokenizations.submit_tfa,
        )
        self.unpause = async_to_streamed_response_wrapper(
            tokenizations.unpause,
        )
        self.update_digital_card_art = async_to_streamed_response_wrapper(
            tokenizations.update_digital_card_art,
        )
