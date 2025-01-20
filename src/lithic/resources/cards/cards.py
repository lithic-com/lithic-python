# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import hmac
import json
import base64
import hashlib
from typing import Union
from datetime import datetime, timezone, timedelta
from typing_extensions import Literal

import httpx
from httpx import URL

from ... import _legacy_response
from ...types import (
    SpendLimitDuration,
    card_list_params,
    card_embed_params,
    card_renew_params,
    card_create_params,
    card_update_params,
    card_reissue_params,
    card_provision_params,
    card_get_embed_url_params,
    card_search_by_pan_params,
    card_convert_physical_params,
)
from ..._types import (
    NOT_GIVEN,
    Body,
    Query,
    Headers,
    NotGiven,
    Base64FileInput,
)
from ..._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .balances import (
    Balances,
    AsyncBalances,
    BalancesWithRawResponse,
    AsyncBalancesWithRawResponse,
    BalancesWithStreamingResponse,
    AsyncBalancesWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncCursorPage, AsyncCursorPage
from ...types.card import Card
from ..._base_client import AsyncPaginator, _merge_mappings, make_request_options
from .aggregate_balances import (
    AggregateBalances,
    AsyncAggregateBalances,
    AggregateBalancesWithRawResponse,
    AsyncAggregateBalancesWithRawResponse,
    AggregateBalancesWithStreamingResponse,
    AsyncAggregateBalancesWithStreamingResponse,
)
from .financial_transactions import (
    FinancialTransactions,
    AsyncFinancialTransactions,
    FinancialTransactionsWithRawResponse,
    AsyncFinancialTransactionsWithRawResponse,
    FinancialTransactionsWithStreamingResponse,
    AsyncFinancialTransactionsWithStreamingResponse,
)
from ...types.card_spend_limits import CardSpendLimits
from ...types.spend_limit_duration import SpendLimitDuration
from ...types.shared_params.carrier import Carrier
from ...types.card_provision_response import CardProvisionResponse
from ...types.shared_params.shipping_address import ShippingAddress

__all__ = ["Cards", "AsyncCards"]


class Cards(SyncAPIResource):
    @cached_property
    def aggregate_balances(self) -> AggregateBalances:
        return AggregateBalances(self._client)

    @cached_property
    def balances(self) -> Balances:
        return Balances(self._client)

    @cached_property
    def financial_transactions(self) -> FinancialTransactions:
        return FinancialTransactions(self._client)

    @cached_property
    def with_raw_response(self) -> CardsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return CardsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return CardsWithStreamingResponse(self)

    def create(
        self,
        *,
        type: Literal["MERCHANT_LOCKED", "PHYSICAL", "SINGLE_USE", "VIRTUAL", "UNLOCKED", "DIGITAL_WALLET"],
        account_token: str | NotGiven = NOT_GIVEN,
        card_program_token: str | NotGiven = NOT_GIVEN,
        carrier: Carrier | NotGiven = NOT_GIVEN,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        exp_month: str | NotGiven = NOT_GIVEN,
        exp_year: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        replacement_account_token: str | NotGiven = NOT_GIVEN,
        replacement_for: str | NotGiven = NOT_GIVEN,
        shipping_address: ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method: Literal["2_DAY", "EXPEDITED", "EXPRESS", "PRIORITY", "STANDARD", "STANDARD_WITH_TRACKING"]
        | NotGiven = NOT_GIVEN,
        spend_limit: int | NotGiven = NOT_GIVEN,
        spend_limit_duration: SpendLimitDuration | NotGiven = NOT_GIVEN,
        state: Literal["OPEN", "PAUSED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Create a new virtual or physical card.

        Parameters `shipping_address` and
        `product_id` only apply to physical cards.

        Args:
          type:
              Card types:

              - `VIRTUAL` - Card will authorize at any merchant and can be added to a digital
                wallet like Apple Pay or Google Pay (if the card program is digital
                wallet-enabled).
              - `PHYSICAL` - Manufactured and sent to the cardholder. We offer white label
                branding, credit, ATM, PIN debit, chip/EMV, NFC and magstripe functionality.
                Reach out at [lithic.com/contact](https://lithic.com/contact) for more
                information.
              - `SINGLE_USE` - Card is closed upon first successful authorization.
              - `MERCHANT_LOCKED` - _[Deprecated]_ Card is locked to the first merchant that
                successfully authorizes the card.
              - `UNLOCKED` - _[Deprecated]_ Similar behavior to VIRTUAL cards, please use
                VIRTUAL instead.
              - `DIGITAL_WALLET` - _[Deprecated]_ Similar behavior to VIRTUAL cards, please
                use VIRTUAL instead.

          account_token: Globally unique identifier for the account that the card will be associated
              with. Required for programs enrolling users using the
              [/account_holders endpoint](https://docs.lithic.com/docs/account-holders-kyc).
              See [Managing Your Program](doc:managing-your-program) for more information.

          card_program_token: For card programs with more than one BIN range. This must be configured with
              Lithic before use. Identifies the card program/BIN range under which to create
              the card. If omitted, will utilize the program's default `card_program_token`.
              In Sandbox, use 00000000-0000-0000-1000-000000000000 and
              00000000-0000-0000-2000-000000000000 to test creating cards on specific card
              programs.

          digital_card_art_token: Specifies the digital card art to be displayed in the user’s digital wallet
              after tokenization. This artwork must be approved by Mastercard and configured
              by Lithic to use. See
              [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).

          exp_month: Two digit (MM) expiry month. If neither `exp_month` nor `exp_year` is provided,
              an expiration date will be generated.

          exp_year: Four digit (yyyy) expiry year. If neither `exp_month` nor `exp_year` is
              provided, an expiration date will be generated.

          memo: Friendly name to identify the card.

          pin: Encrypted PIN block (in base64). Applies to cards of type `PHYSICAL` and
              `VIRTUAL`. See
              [Encrypted PIN Block](https://docs.lithic.com/docs/cards#encrypted-pin-block).

          product_id: Only applicable to cards of type `PHYSICAL`. This must be configured with Lithic
              before use. Specifies the configuration (i.e., physical card art) that the card
              should be manufactured with.

          replacement_account_token: Restricted field limited to select use cases. Lithic will reach out directly if
              this field should be used. Globally unique identifier for the replacement card's
              account. If this field is specified, `replacement_for` must also be specified.
              If `replacement_for` is specified and this field is omitted, the replacement
              card's account will be inferred from the card being replaced.

          replacement_for: Globally unique identifier for the card that this card will replace. If the card
              type is `PHYSICAL` it will be replaced by a `PHYSICAL` card. If the card type is
              `VIRTUAL` it will be replaced by a `VIRTUAL` card.

          shipping_method: Shipping method for the card. Only applies to cards of type PHYSICAL. Use of
              options besides `STANDARD` require additional permissions.

              - `STANDARD` - USPS regular mail or similar international option, with no
                tracking
              - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
                with tracking
              - `PRIORITY` - USPS Priority, 1-3 day shipping, with tracking
              - `EXPRESS` - FedEx Express, 3-day shipping, with tracking
              - `2_DAY` - FedEx 2-day shipping, with tracking
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          spend_limit: Amount (in cents) to limit approved authorizations (e.g. 100000 would be a
              $1,000 limit). Transaction requests above the spend limit will be declined. Note
              that a spend limit of 0 is effectively no limit, and should only be used to
              reset or remove a prior limit. Only a limit of 1 or above will result in
              declined transactions due to checks against the card limit.

          spend_limit_duration:
              Spend limit duration values:

              - `ANNUALLY` - Card will authorize transactions up to spend limit for the
                trailing year.
              - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
                of the card.
              - `MONTHLY` - Card will authorize transactions up to spend limit for the
                trailing month. To support recurring monthly payments, which can occur on
                different day every month, the time window we consider for monthly velocity
                starts 6 days after the current calendar date one month prior.
              - `TRANSACTION` - Card will authorize multiple transactions if each individual
                transaction is under the spend limit.

          state:
              Card state values:

              - `OPEN` - Card will approve authorizations (if they match card and account
                parameters).
              - `PAUSED` - Card will decline authorizations, but can be resumed at a later
                time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/cards",
            body=maybe_transform(
                {
                    "type": type,
                    "account_token": account_token,
                    "card_program_token": card_program_token,
                    "carrier": carrier,
                    "digital_card_art_token": digital_card_art_token,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "memo": memo,
                    "pin": pin,
                    "product_id": product_id,
                    "replacement_account_token": replacement_account_token,
                    "replacement_for": replacement_for,
                    "shipping_address": shipping_address,
                    "shipping_method": shipping_method,
                    "spend_limit": spend_limit,
                    "spend_limit_duration": spend_limit_duration,
                    "state": state,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def retrieve(
        self,
        card_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """
        Get card configuration such as spend limit and state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._get(
            f"/v1/cards/{card_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def update(
        self,
        card_token: str,
        *,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        pin_status: Literal["OK"] | NotGiven = NOT_GIVEN,
        spend_limit: int | NotGiven = NOT_GIVEN,
        spend_limit_duration: SpendLimitDuration | NotGiven = NOT_GIVEN,
        state: Literal["CLOSED", "OPEN", "PAUSED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Update the specified properties of the card.

        Unsupplied properties will remain
        unchanged.

        _Note: setting a card to a `CLOSED` state is a final action that cannot be
        undone._

        Args:
          digital_card_art_token: Specifies the digital card art to be displayed in the user’s digital wallet
              after tokenization. This artwork must be approved by Mastercard and configured
              by Lithic to use. See
              [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).

          memo: Friendly name to identify the card.

          pin: Encrypted PIN block (in base64). Only applies to cards of type `PHYSICAL` and
              `VIRTUAL`. Changing PIN also resets PIN status to `OK`. See
              [Encrypted PIN Block](https://docs.lithic.com/docs/cards#encrypted-pin-block).

          pin_status: Indicates if a card is blocked due a PIN status issue (e.g. excessive incorrect
              attempts). Can only be set to `OK` to unblock a card.

          spend_limit: Amount (in cents) to limit approved authorizations (e.g. 100000 would be a
              $1,000 limit). Transaction requests above the spend limit will be declined. Note
              that a spend limit of 0 is effectively no limit, and should only be used to
              reset or remove a prior limit. Only a limit of 1 or above will result in
              declined transactions due to checks against the card limit.

          spend_limit_duration:
              Spend limit duration values:

              - `ANNUALLY` - Card will authorize transactions up to spend limit for the
                trailing year.
              - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
                of the card.
              - `MONTHLY` - Card will authorize transactions up to spend limit for the
                trailing month. To support recurring monthly payments, which can occur on
                different day every month, the time window we consider for monthly velocity
                starts 6 days after the current calendar date one month prior.
              - `TRANSACTION` - Card will authorize multiple transactions if each individual
                transaction is under the spend limit.

          state:
              Card state values:

              - `CLOSED` - Card will no longer approve authorizations. Closing a card cannot
                be undone.
              - `OPEN` - Card will approve authorizations (if they match card and account
                parameters).
              - `PAUSED` - Card will decline authorizations, but can be resumed at a later
                time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._patch(
            f"/v1/cards/{card_token}",
            body=maybe_transform(
                {
                    "digital_card_art_token": digital_card_art_token,
                    "memo": memo,
                    "pin": pin,
                    "pin_status": pin_status,
                    "spend_limit": spend_limit,
                    "spend_limit_duration": spend_limit_duration,
                    "state": state,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        state: Literal["CLOSED", "OPEN", "PAUSED", "PENDING_ACTIVATION", "PENDING_FULFILLMENT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Card]:
        """
        List cards.

        Args:
          account_token: Returns cards associated with the specified account.

          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          state: Returns cards with the specified state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/cards",
            page=SyncCursorPage[Card],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "state": state,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            model=Card,
        )

    def convert_physical(
        self,
        card_token: str,
        *,
        shipping_address: ShippingAddress,
        carrier: Carrier | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        shipping_method: Literal["2-DAY", "EXPEDITED", "EXPRESS", "PRIORITY", "STANDARD", "STANDARD_WITH_TRACKING"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Convert a virtual card into a physical card and manufacture it.

        Customer must
        supply relevant fields for physical card creation including `product_id`,
        `carrier`, `shipping_method`, and `shipping_address`. The card token will be
        unchanged. The card's type will be altered to `PHYSICAL`. The card will be set
        to state `PENDING_FULFILLMENT` and fulfilled at next fulfillment cycle. Virtual
        cards created on card programs which do not support physical cards cannot be
        converted. The card program cannot be changed as part of the conversion. Cards
        must be in an `OPEN` state to be converted. Only applies to cards of type
        `VIRTUAL` (or existing cards with deprecated types of `DIGITAL_WALLET` and
        `UNLOCKED`).

        Args:
          shipping_address: The shipping address this card will be sent to.

          carrier: If omitted, the previous carrier will be used.

          product_id: Specifies the configuration (e.g. physical card art) that the card should be
              manufactured with, and only applies to cards of type `PHYSICAL`. This must be
              configured with Lithic before use.

          shipping_method: Shipping method for the card. Use of options besides `STANDARD` require
              additional permissions.

              - `STANDARD` - USPS regular mail or similar international option, with no
                tracking
              - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
                with tracking
              - `PRIORITY` - USPS Priority, 1-3 day shipping, with tracking
              - `EXPRESS` - FedEx Express, 3-day shipping, with tracking
              - `2_DAY` - FedEx 2-day shipping, with tracking
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._post(
            f"/v1/cards/{card_token}/convert_physical",
            body=maybe_transform(
                {
                    "shipping_address": shipping_address,
                    "carrier": carrier,
                    "product_id": product_id,
                    "shipping_method": shipping_method,
                },
                card_convert_physical_params.CardConvertPhysicalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def embed(
        self,
        *,
        embed_request: str,
        hmac: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Handling full card PANs and CVV codes requires that you comply with the Payment
        Card Industry Data Security Standards (PCI DSS). Some clients choose to reduce
        their compliance obligations by leveraging our embedded card UI solution
        documented below.

        In this setup, PANs and CVV codes are presented to the end-user via a card UI
        that we provide, optionally styled in the customer's branding using a specified
        css stylesheet. A user's browser makes the request directly to api.lithic.com,
        so card PANs and CVVs never touch the API customer's servers while full card
        data is displayed to their end-users. The response contains an HTML document
        (see Embedded Card UI or Changelog for upcoming changes in January). This means
        that the url for the request can be inserted straight into the `src` attribute
        of an iframe.

        ```html
        <iframe
          id="card-iframe"
          src="https://sandbox.lithic.com/v1/embed/card?embed_request=eyJjc3MiO...;hmac=r8tx1..."
          allow="clipboard-write"
          class="content"
        ></iframe>
        ```

        You should compute the request payload on the server side. You can render it (or
        the whole iframe) on the server or make an ajax call from your front end code,
        but **do not ever embed your API key into front end code, as doing so introduces
        a serious security vulnerability**.

        Args:
          embed_request: A base64 encoded JSON string of an EmbedRequest to specify which card to load.

          hmac: SHA256 HMAC of the embed_request JSON string with base64 digest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/html", **(extra_headers or {})}
        return self._get(
            "/v1/embed/card",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "embed_request": embed_request,
                        "hmac": hmac,
                    },
                    card_embed_params.CardEmbedParams,
                ),
            ),
            cast_to=str,
        )

    def get_embed_html(
        self,
        *,
        token: str,
        css: str | NotGiven = NOT_GIVEN,
        expiration: Union[str, datetime] | NotGiven = NOT_GIVEN,
        target_origin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Generates and executes an embed request, returning html you can serve to the
        user.

        Be aware that this html contains sensitive data whose presence on your server
        could trigger PCI DSS.

        If your company is not certified PCI compliant, we recommend using
        `get_embed_url()` instead. You would then pass that returned URL to the
        frontend, where you can load it via an iframe.
        """
        headers = _merge_mappings({"Accept": "text/html"}, extra_headers or {})
        url = self.get_embed_url(
            css=css,
            token=token,
            expiration=expiration,
            target_origin=target_origin,
        )
        return self._get(
            str(url),
            cast_to=str,
            options=make_request_options(
                extra_headers=headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    def get_embed_url(
        self,
        *,
        token: str,
        css: str | NotGiven = NOT_GIVEN,
        expiration: Union[str, datetime] | NotGiven = NOT_GIVEN,
        target_origin: str | NotGiven = NOT_GIVEN,
    ) -> URL:
        """
        Handling full card PANs and CVV codes requires that you comply with the Payment
        Card Industry Data Security Standards (PCI DSS). Some clients choose to reduce
        their compliance obligations by leveraging our embedded card UI solution
        documented below.

        In this setup, PANs and CVV codes are presented to the end-user via a card UI
        that we provide, optionally styled in the customer's branding using a specified
        css stylesheet. A user's browser makes the request directly to api.lithic.com,
        so card PANs and CVVs never touch the API customer's servers while full card
        data is displayed to their end-users. The response contains an HTML document.
        This means that the url for the request can be inserted straight into the `src`
        attribute of an iframe.

        ```html
        <iframe
          id="card-iframe"
          src="https://sandbox.lithic.com/v1/embed/card?embed_request=eyJjc3MiO...;hmac=r8tx1..."
          allow="clipboard-write"
          class="content"
        ></iframe>
        ```

        You should compute the request payload on the server side. You can render it (or
        the whole iframe) on the server or make an ajax call from your front end code,
        but **do not ever embed your API key into front end code, as doing so introduces
        a serious security vulnerability**.
        """
        # Default expiration of 1 minute from now.
        if isinstance(expiration, NotGiven):
            expiration = datetime.now(timezone.utc) + timedelta(minutes=1)

        query = maybe_transform(
            strip_not_given(
                {
                    "css": css,
                    "token": token,
                    "expiration": expiration,
                    "target_origin": target_origin,
                }
            ),
            card_get_embed_url_params.CardGetEmbedURLParams,
        )
        serialized = json.dumps(query, sort_keys=True, separators=(",", ":"))
        params = {
            "embed_request": base64.b64encode(bytes(serialized, "utf-8")).decode("utf-8"),
            "hmac": base64.b64encode(
                hmac.new(
                    key=bytes(self._client.api_key, "utf-8"),
                    msg=bytes(serialized, "utf-8"),
                    digestmod=hashlib.sha256,
                ).digest()
            ).decode("utf-8"),
        }

        # Copied nearly directly from httpx.BaseClient._merge_url
        base_url = self._client.base_url
        raw_path = base_url.raw_path + URL("v1/embed/card").raw_path
        return base_url.copy_with(raw_path=raw_path).copy_merge_params(params)

    def provision(
        self,
        card_token: str,
        *,
        certificate: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        client_device_id: str | NotGiven = NOT_GIVEN,
        client_wallet_account_id: str | NotGiven = NOT_GIVEN,
        digital_wallet: Literal["APPLE_PAY", "GOOGLE_PAY", "SAMSUNG_PAY"] | NotGiven = NOT_GIVEN,
        nonce: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        nonce_signature: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardProvisionResponse:
        """
        Allow your cardholders to directly add payment cards to the device's digital
        wallet (e.g. Apple Pay) with one touch from your app.

        This requires some additional setup and configuration. Please
        [Contact Us](https://lithic.com/contact) or your Customer Success representative
        for more information.

        Args:
          certificate: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive only
              `activationData` in the response. Apple's public leaf certificate. Base64
              encoded in PEM format with headers `(-----BEGIN CERTIFICATE-----)` and trailers
              omitted. Provided by the device's wallet.

          client_device_id: Only applicable if `digital_wallet` is `GOOGLE_PAY` or `SAMSUNG_PAY` and the
              card is on the Visa network. Stable device identification set by the wallet
              provider.

          client_wallet_account_id: Only applicable if `digital_wallet` is `GOOGLE_PAY` or `SAMSUNG_PAY` and the
              card is on the Visa network. Consumer ID that identifies the wallet account
              holder entity.

          digital_wallet: Name of digital wallet provider.

          nonce: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive only
              `activationData` in the response. Base64 cryptographic nonce provided by the
              device's wallet.

          nonce_signature: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive only
              `activationData` in the response. Base64 cryptographic nonce provided by the
              device's wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._post(
            f"/v1/cards/{card_token}/provision",
            body=maybe_transform(
                {
                    "certificate": certificate,
                    "client_device_id": client_device_id,
                    "client_wallet_account_id": client_wallet_account_id,
                    "digital_wallet": digital_wallet,
                    "nonce": nonce,
                    "nonce_signature": nonce_signature,
                },
                card_provision_params.CardProvisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardProvisionResponse,
        )

    def reissue(
        self,
        card_token: str,
        *,
        carrier: Carrier | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        shipping_address: ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method: Literal["2-DAY", "EXPEDITED", "EXPRESS", "PRIORITY", "STANDARD", "STANDARD_WITH_TRACKING"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Initiate print and shipment of a duplicate physical card (e.g.

        card is
        physically damaged). The PAN, expiry, and CVC2 will remain the same and the
        original card can continue to be used until the new card is activated. Only
        applies to cards of type `PHYSICAL`. A card can be replaced or renewed a total
        of 8 times.

        Args:
          carrier: If omitted, the previous carrier will be used.

          product_id: Specifies the configuration (e.g. physical card art) that the card should be
              manufactured with, and only applies to cards of type `PHYSICAL`. This must be
              configured with Lithic before use.

          shipping_address: If omitted, the previous shipping address will be used.

          shipping_method: Shipping method for the card. Use of options besides `STANDARD` require
              additional permissions.

              - `STANDARD` - USPS regular mail or similar international option, with no
                tracking
              - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
                with tracking
              - `PRIORITY` - USPS Priority, 1-3 day shipping, with tracking
              - `EXPRESS` - FedEx Express, 3-day shipping, with tracking
              - `2_DAY` - FedEx 2-day shipping, with tracking
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._post(
            f"/v1/cards/{card_token}/reissue",
            body=maybe_transform(
                {
                    "carrier": carrier,
                    "product_id": product_id,
                    "shipping_address": shipping_address,
                    "shipping_method": shipping_method,
                },
                card_reissue_params.CardReissueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def renew(
        self,
        card_token: str,
        *,
        shipping_address: ShippingAddress,
        carrier: Carrier | NotGiven = NOT_GIVEN,
        exp_month: str | NotGiven = NOT_GIVEN,
        exp_year: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        shipping_method: Literal["2-DAY", "EXPEDITED", "EXPRESS", "PRIORITY", "STANDARD", "STANDARD_WITH_TRACKING"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """
        Creates a new card with the same card token and PAN, but updated expiry and CVC2
        code. The original card will keep working for card-present transactions until
        the new card is activated. For card-not-present transactions, the original card
        details (expiry, CVC2) will also keep working until the new card is activated.
        Applies to card types `PHYSICAL` and `VIRTUAL`. A card can be replaced or
        renewed a total of 8 times.

        Args:
          shipping_address: The shipping address this card will be sent to.

          carrier: If omitted, the previous carrier will be used.

          exp_month: Two digit (MM) expiry month. If neither `exp_month` nor `exp_year` is provided,
              an expiration date six years in the future will be generated.

          exp_year: Four digit (yyyy) expiry year. If neither `exp_month` nor `exp_year` is
              provided, an expiration date six years in the future will be generated.

          product_id: Specifies the configuration (e.g. physical card art) that the card should be
              manufactured with, and only applies to cards of type `PHYSICAL`. This must be
              configured with Lithic before use.

          shipping_method: Shipping method for the card. Use of options besides `STANDARD` require
              additional permissions.

              - `STANDARD` - USPS regular mail or similar international option, with no
                tracking
              - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
                with tracking
              - `PRIORITY` - USPS Priority, 1-3 day shipping, with tracking
              - `EXPRESS` - FedEx Express, 3-day shipping, with tracking
              - `2_DAY` - FedEx 2-day shipping, with tracking
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._post(
            f"/v1/cards/{card_token}/renew",
            body=maybe_transform(
                {
                    "shipping_address": shipping_address,
                    "carrier": carrier,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "product_id": product_id,
                    "shipping_method": shipping_method,
                },
                card_renew_params.CardRenewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def retrieve_spend_limits(
        self,
        card_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardSpendLimits:
        """
        Get a Card's available spend limit, which is based on the spend limit configured
        on the Card and the amount already spent over the spend limit's duration. For
        example, if the Card has a monthly spend limit of $1000 configured, and has
        spent $600 in the last month, the available spend limit returned would be $400.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._get(
            f"/v1/cards/{card_token}/spend_limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardSpendLimits,
        )

    def search_by_pan(
        self,
        *,
        pan: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Get card configuration such as spend limit and state.

        Customers must be PCI
        compliant to use this endpoint. Please contact
        [support@lithic.com](mailto:support@lithic.com) for questions. _Note: this is a
        `POST` endpoint because it is more secure to send sensitive data in a request
        body than in a URL._

        Args:
          pan: The PAN for the card being retrieved.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/cards/search_by_pan",
            body=maybe_transform({"pan": pan}, card_search_by_pan_params.CardSearchByPanParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )


class AsyncCards(AsyncAPIResource):
    @cached_property
    def aggregate_balances(self) -> AsyncAggregateBalances:
        return AsyncAggregateBalances(self._client)

    @cached_property
    def balances(self) -> AsyncBalances:
        return AsyncBalances(self._client)

    @cached_property
    def financial_transactions(self) -> AsyncFinancialTransactions:
        return AsyncFinancialTransactions(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCardsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncCardsWithStreamingResponse(self)

    async def create(
        self,
        *,
        type: Literal["MERCHANT_LOCKED", "PHYSICAL", "SINGLE_USE", "VIRTUAL", "UNLOCKED", "DIGITAL_WALLET"],
        account_token: str | NotGiven = NOT_GIVEN,
        card_program_token: str | NotGiven = NOT_GIVEN,
        carrier: Carrier | NotGiven = NOT_GIVEN,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        exp_month: str | NotGiven = NOT_GIVEN,
        exp_year: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        replacement_account_token: str | NotGiven = NOT_GIVEN,
        replacement_for: str | NotGiven = NOT_GIVEN,
        shipping_address: ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method: Literal["2_DAY", "EXPEDITED", "EXPRESS", "PRIORITY", "STANDARD", "STANDARD_WITH_TRACKING"]
        | NotGiven = NOT_GIVEN,
        spend_limit: int | NotGiven = NOT_GIVEN,
        spend_limit_duration: SpendLimitDuration | NotGiven = NOT_GIVEN,
        state: Literal["OPEN", "PAUSED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Create a new virtual or physical card.

        Parameters `shipping_address` and
        `product_id` only apply to physical cards.

        Args:
          type:
              Card types:

              - `VIRTUAL` - Card will authorize at any merchant and can be added to a digital
                wallet like Apple Pay or Google Pay (if the card program is digital
                wallet-enabled).
              - `PHYSICAL` - Manufactured and sent to the cardholder. We offer white label
                branding, credit, ATM, PIN debit, chip/EMV, NFC and magstripe functionality.
                Reach out at [lithic.com/contact](https://lithic.com/contact) for more
                information.
              - `SINGLE_USE` - Card is closed upon first successful authorization.
              - `MERCHANT_LOCKED` - _[Deprecated]_ Card is locked to the first merchant that
                successfully authorizes the card.
              - `UNLOCKED` - _[Deprecated]_ Similar behavior to VIRTUAL cards, please use
                VIRTUAL instead.
              - `DIGITAL_WALLET` - _[Deprecated]_ Similar behavior to VIRTUAL cards, please
                use VIRTUAL instead.

          account_token: Globally unique identifier for the account that the card will be associated
              with. Required for programs enrolling users using the
              [/account_holders endpoint](https://docs.lithic.com/docs/account-holders-kyc).
              See [Managing Your Program](doc:managing-your-program) for more information.

          card_program_token: For card programs with more than one BIN range. This must be configured with
              Lithic before use. Identifies the card program/BIN range under which to create
              the card. If omitted, will utilize the program's default `card_program_token`.
              In Sandbox, use 00000000-0000-0000-1000-000000000000 and
              00000000-0000-0000-2000-000000000000 to test creating cards on specific card
              programs.

          digital_card_art_token: Specifies the digital card art to be displayed in the user’s digital wallet
              after tokenization. This artwork must be approved by Mastercard and configured
              by Lithic to use. See
              [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).

          exp_month: Two digit (MM) expiry month. If neither `exp_month` nor `exp_year` is provided,
              an expiration date will be generated.

          exp_year: Four digit (yyyy) expiry year. If neither `exp_month` nor `exp_year` is
              provided, an expiration date will be generated.

          memo: Friendly name to identify the card.

          pin: Encrypted PIN block (in base64). Applies to cards of type `PHYSICAL` and
              `VIRTUAL`. See
              [Encrypted PIN Block](https://docs.lithic.com/docs/cards#encrypted-pin-block).

          product_id: Only applicable to cards of type `PHYSICAL`. This must be configured with Lithic
              before use. Specifies the configuration (i.e., physical card art) that the card
              should be manufactured with.

          replacement_account_token: Restricted field limited to select use cases. Lithic will reach out directly if
              this field should be used. Globally unique identifier for the replacement card's
              account. If this field is specified, `replacement_for` must also be specified.
              If `replacement_for` is specified and this field is omitted, the replacement
              card's account will be inferred from the card being replaced.

          replacement_for: Globally unique identifier for the card that this card will replace. If the card
              type is `PHYSICAL` it will be replaced by a `PHYSICAL` card. If the card type is
              `VIRTUAL` it will be replaced by a `VIRTUAL` card.

          shipping_method: Shipping method for the card. Only applies to cards of type PHYSICAL. Use of
              options besides `STANDARD` require additional permissions.

              - `STANDARD` - USPS regular mail or similar international option, with no
                tracking
              - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
                with tracking
              - `PRIORITY` - USPS Priority, 1-3 day shipping, with tracking
              - `EXPRESS` - FedEx Express, 3-day shipping, with tracking
              - `2_DAY` - FedEx 2-day shipping, with tracking
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          spend_limit: Amount (in cents) to limit approved authorizations (e.g. 100000 would be a
              $1,000 limit). Transaction requests above the spend limit will be declined. Note
              that a spend limit of 0 is effectively no limit, and should only be used to
              reset or remove a prior limit. Only a limit of 1 or above will result in
              declined transactions due to checks against the card limit.

          spend_limit_duration:
              Spend limit duration values:

              - `ANNUALLY` - Card will authorize transactions up to spend limit for the
                trailing year.
              - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
                of the card.
              - `MONTHLY` - Card will authorize transactions up to spend limit for the
                trailing month. To support recurring monthly payments, which can occur on
                different day every month, the time window we consider for monthly velocity
                starts 6 days after the current calendar date one month prior.
              - `TRANSACTION` - Card will authorize multiple transactions if each individual
                transaction is under the spend limit.

          state:
              Card state values:

              - `OPEN` - Card will approve authorizations (if they match card and account
                parameters).
              - `PAUSED` - Card will decline authorizations, but can be resumed at a later
                time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/cards",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "account_token": account_token,
                    "card_program_token": card_program_token,
                    "carrier": carrier,
                    "digital_card_art_token": digital_card_art_token,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "memo": memo,
                    "pin": pin,
                    "product_id": product_id,
                    "replacement_account_token": replacement_account_token,
                    "replacement_for": replacement_for,
                    "shipping_address": shipping_address,
                    "shipping_method": shipping_method,
                    "spend_limit": spend_limit,
                    "spend_limit_duration": spend_limit_duration,
                    "state": state,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def retrieve(
        self,
        card_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """
        Get card configuration such as spend limit and state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return await self._get(
            f"/v1/cards/{card_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def update(
        self,
        card_token: str,
        *,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        pin_status: Literal["OK"] | NotGiven = NOT_GIVEN,
        spend_limit: int | NotGiven = NOT_GIVEN,
        spend_limit_duration: SpendLimitDuration | NotGiven = NOT_GIVEN,
        state: Literal["CLOSED", "OPEN", "PAUSED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Update the specified properties of the card.

        Unsupplied properties will remain
        unchanged.

        _Note: setting a card to a `CLOSED` state is a final action that cannot be
        undone._

        Args:
          digital_card_art_token: Specifies the digital card art to be displayed in the user’s digital wallet
              after tokenization. This artwork must be approved by Mastercard and configured
              by Lithic to use. See
              [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).

          memo: Friendly name to identify the card.

          pin: Encrypted PIN block (in base64). Only applies to cards of type `PHYSICAL` and
              `VIRTUAL`. Changing PIN also resets PIN status to `OK`. See
              [Encrypted PIN Block](https://docs.lithic.com/docs/cards#encrypted-pin-block).

          pin_status: Indicates if a card is blocked due a PIN status issue (e.g. excessive incorrect
              attempts). Can only be set to `OK` to unblock a card.

          spend_limit: Amount (in cents) to limit approved authorizations (e.g. 100000 would be a
              $1,000 limit). Transaction requests above the spend limit will be declined. Note
              that a spend limit of 0 is effectively no limit, and should only be used to
              reset or remove a prior limit. Only a limit of 1 or above will result in
              declined transactions due to checks against the card limit.

          spend_limit_duration:
              Spend limit duration values:

              - `ANNUALLY` - Card will authorize transactions up to spend limit for the
                trailing year.
              - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
                of the card.
              - `MONTHLY` - Card will authorize transactions up to spend limit for the
                trailing month. To support recurring monthly payments, which can occur on
                different day every month, the time window we consider for monthly velocity
                starts 6 days after the current calendar date one month prior.
              - `TRANSACTION` - Card will authorize multiple transactions if each individual
                transaction is under the spend limit.

          state:
              Card state values:

              - `CLOSED` - Card will no longer approve authorizations. Closing a card cannot
                be undone.
              - `OPEN` - Card will approve authorizations (if they match card and account
                parameters).
              - `PAUSED` - Card will decline authorizations, but can be resumed at a later
                time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return await self._patch(
            f"/v1/cards/{card_token}",
            body=await async_maybe_transform(
                {
                    "digital_card_art_token": digital_card_art_token,
                    "memo": memo,
                    "pin": pin,
                    "pin_status": pin_status,
                    "spend_limit": spend_limit,
                    "spend_limit_duration": spend_limit_duration,
                    "state": state,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        state: Literal["CLOSED", "OPEN", "PAUSED", "PENDING_ACTIVATION", "PENDING_FULFILLMENT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Card, AsyncCursorPage[Card]]:
        """
        List cards.

        Args:
          account_token: Returns cards associated with the specified account.

          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          state: Returns cards with the specified state.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/cards",
            page=AsyncCursorPage[Card],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "state": state,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            model=Card,
        )

    async def convert_physical(
        self,
        card_token: str,
        *,
        shipping_address: ShippingAddress,
        carrier: Carrier | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        shipping_method: Literal["2-DAY", "EXPEDITED", "EXPRESS", "PRIORITY", "STANDARD", "STANDARD_WITH_TRACKING"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Convert a virtual card into a physical card and manufacture it.

        Customer must
        supply relevant fields for physical card creation including `product_id`,
        `carrier`, `shipping_method`, and `shipping_address`. The card token will be
        unchanged. The card's type will be altered to `PHYSICAL`. The card will be set
        to state `PENDING_FULFILLMENT` and fulfilled at next fulfillment cycle. Virtual
        cards created on card programs which do not support physical cards cannot be
        converted. The card program cannot be changed as part of the conversion. Cards
        must be in an `OPEN` state to be converted. Only applies to cards of type
        `VIRTUAL` (or existing cards with deprecated types of `DIGITAL_WALLET` and
        `UNLOCKED`).

        Args:
          shipping_address: The shipping address this card will be sent to.

          carrier: If omitted, the previous carrier will be used.

          product_id: Specifies the configuration (e.g. physical card art) that the card should be
              manufactured with, and only applies to cards of type `PHYSICAL`. This must be
              configured with Lithic before use.

          shipping_method: Shipping method for the card. Use of options besides `STANDARD` require
              additional permissions.

              - `STANDARD` - USPS regular mail or similar international option, with no
                tracking
              - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
                with tracking
              - `PRIORITY` - USPS Priority, 1-3 day shipping, with tracking
              - `EXPRESS` - FedEx Express, 3-day shipping, with tracking
              - `2_DAY` - FedEx 2-day shipping, with tracking
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return await self._post(
            f"/v1/cards/{card_token}/convert_physical",
            body=await async_maybe_transform(
                {
                    "shipping_address": shipping_address,
                    "carrier": carrier,
                    "product_id": product_id,
                    "shipping_method": shipping_method,
                },
                card_convert_physical_params.CardConvertPhysicalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def embed(
        self,
        *,
        embed_request: str,
        hmac: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Handling full card PANs and CVV codes requires that you comply with the Payment
        Card Industry Data Security Standards (PCI DSS). Some clients choose to reduce
        their compliance obligations by leveraging our embedded card UI solution
        documented below.

        In this setup, PANs and CVV codes are presented to the end-user via a card UI
        that we provide, optionally styled in the customer's branding using a specified
        css stylesheet. A user's browser makes the request directly to api.lithic.com,
        so card PANs and CVVs never touch the API customer's servers while full card
        data is displayed to their end-users. The response contains an HTML document
        (see Embedded Card UI or Changelog for upcoming changes in January). This means
        that the url for the request can be inserted straight into the `src` attribute
        of an iframe.

        ```html
        <iframe
          id="card-iframe"
          src="https://sandbox.lithic.com/v1/embed/card?embed_request=eyJjc3MiO...;hmac=r8tx1..."
          allow="clipboard-write"
          class="content"
        ></iframe>
        ```

        You should compute the request payload on the server side. You can render it (or
        the whole iframe) on the server or make an ajax call from your front end code,
        but **do not ever embed your API key into front end code, as doing so introduces
        a serious security vulnerability**.

        Args:
          embed_request: A base64 encoded JSON string of an EmbedRequest to specify which card to load.

          hmac: SHA256 HMAC of the embed_request JSON string with base64 digest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/html", **(extra_headers or {})}
        return await self._get(
            "/v1/embed/card",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "embed_request": embed_request,
                        "hmac": hmac,
                    },
                    card_embed_params.CardEmbedParams,
                ),
            ),
            cast_to=str,
        )

    async def get_embed_html(
        self,
        *,
        token: str,
        css: str | NotGiven = NOT_GIVEN,
        expiration: Union[str, datetime] | NotGiven = NOT_GIVEN,
        target_origin: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
        """
        Generates and executes an embed request, returning html you can serve to the
        user.

        Be aware that this html contains sensitive data whose presence on your server
        could trigger PCI DSS.

        If your company is not certified PCI compliant, we recommend using
        `get_embed_url()` instead. You would then pass that returned URL to the
        frontend, where you can load it via an iframe.
        """
        headers = _merge_mappings({"Accept": "text/html"}, extra_headers or {})
        url = self.get_embed_url(
            css=css,
            token=token,
            expiration=expiration,
            target_origin=target_origin,
        )
        return await self._get(
            str(url),
            cast_to=str,
            options=make_request_options(
                extra_headers=headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
        )

    def get_embed_url(
        self,
        *,
        token: str,
        css: str | NotGiven = NOT_GIVEN,
        expiration: Union[str, datetime] | NotGiven = NOT_GIVEN,
        target_origin: str | NotGiven = NOT_GIVEN,
    ) -> URL:
        """
        Handling full card PANs and CVV codes requires that you comply with the Payment
        Card Industry Data Security Standards (PCI DSS). Some clients choose to reduce
        their compliance obligations by leveraging our embedded card UI solution
        documented below.

        In this setup, PANs and CVV codes are presented to the end-user via a card UI
        that we provide, optionally styled in the customer's branding using a specified
        css stylesheet. A user's browser makes the request directly to api.lithic.com,
        so card PANs and CVVs never touch the API customer's servers while full card
        data is displayed to their end-users. The response contains an HTML document.
        This means that the url for the request can be inserted straight into the `src`
        attribute of an iframe.

        ```html
        <iframe
          id="card-iframe"
          src="https://sandbox.lithic.com/v1/embed/card?embed_request=eyJjc3MiO...;hmac=r8tx1..."
          allow="clipboard-write"
          class="content"
        ></iframe>
        ```

        You should compute the request payload on the server side. You can render it (or
        the whole iframe) on the server or make an ajax call from your front end code,
        but **do not ever embed your API key into front end code, as doing so introduces
        a serious security vulnerability**.
        """
        # Default expiration of 1 minute from now.
        if isinstance(expiration, NotGiven):
            expiration = datetime.now(timezone.utc) + timedelta(minutes=1)

        query = maybe_transform(
            strip_not_given(
                {
                    "css": css,
                    "token": token,
                    "expiration": expiration,
                    "target_origin": target_origin,
                }
            ),
            card_get_embed_url_params.CardGetEmbedURLParams,
        )
        serialized = json.dumps(query, sort_keys=True, separators=(",", ":"))
        params = {
            "embed_request": base64.b64encode(bytes(serialized, "utf-8")).decode("utf-8"),
            "hmac": base64.b64encode(
                hmac.new(
                    key=bytes(self._client.api_key, "utf-8"),
                    msg=bytes(serialized, "utf-8"),
                    digestmod=hashlib.sha256,
                ).digest()
            ).decode("utf-8"),
        }

        # Copied nearly directly from httpx.BaseClient._merge_url
        base_url = self._client.base_url
        raw_path = base_url.raw_path + URL("v1/embed/card").raw_path
        return base_url.copy_with(raw_path=raw_path).copy_merge_params(params)

    async def provision(
        self,
        card_token: str,
        *,
        certificate: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        client_device_id: str | NotGiven = NOT_GIVEN,
        client_wallet_account_id: str | NotGiven = NOT_GIVEN,
        digital_wallet: Literal["APPLE_PAY", "GOOGLE_PAY", "SAMSUNG_PAY"] | NotGiven = NOT_GIVEN,
        nonce: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        nonce_signature: Union[str, Base64FileInput] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardProvisionResponse:
        """
        Allow your cardholders to directly add payment cards to the device's digital
        wallet (e.g. Apple Pay) with one touch from your app.

        This requires some additional setup and configuration. Please
        [Contact Us](https://lithic.com/contact) or your Customer Success representative
        for more information.

        Args:
          certificate: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive only
              `activationData` in the response. Apple's public leaf certificate. Base64
              encoded in PEM format with headers `(-----BEGIN CERTIFICATE-----)` and trailers
              omitted. Provided by the device's wallet.

          client_device_id: Only applicable if `digital_wallet` is `GOOGLE_PAY` or `SAMSUNG_PAY` and the
              card is on the Visa network. Stable device identification set by the wallet
              provider.

          client_wallet_account_id: Only applicable if `digital_wallet` is `GOOGLE_PAY` or `SAMSUNG_PAY` and the
              card is on the Visa network. Consumer ID that identifies the wallet account
              holder entity.

          digital_wallet: Name of digital wallet provider.

          nonce: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive only
              `activationData` in the response. Base64 cryptographic nonce provided by the
              device's wallet.

          nonce_signature: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive only
              `activationData` in the response. Base64 cryptographic nonce provided by the
              device's wallet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return await self._post(
            f"/v1/cards/{card_token}/provision",
            body=await async_maybe_transform(
                {
                    "certificate": certificate,
                    "client_device_id": client_device_id,
                    "client_wallet_account_id": client_wallet_account_id,
                    "digital_wallet": digital_wallet,
                    "nonce": nonce,
                    "nonce_signature": nonce_signature,
                },
                card_provision_params.CardProvisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardProvisionResponse,
        )

    async def reissue(
        self,
        card_token: str,
        *,
        carrier: Carrier | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        shipping_address: ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method: Literal["2-DAY", "EXPEDITED", "EXPRESS", "PRIORITY", "STANDARD", "STANDARD_WITH_TRACKING"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Initiate print and shipment of a duplicate physical card (e.g.

        card is
        physically damaged). The PAN, expiry, and CVC2 will remain the same and the
        original card can continue to be used until the new card is activated. Only
        applies to cards of type `PHYSICAL`. A card can be replaced or renewed a total
        of 8 times.

        Args:
          carrier: If omitted, the previous carrier will be used.

          product_id: Specifies the configuration (e.g. physical card art) that the card should be
              manufactured with, and only applies to cards of type `PHYSICAL`. This must be
              configured with Lithic before use.

          shipping_address: If omitted, the previous shipping address will be used.

          shipping_method: Shipping method for the card. Use of options besides `STANDARD` require
              additional permissions.

              - `STANDARD` - USPS regular mail or similar international option, with no
                tracking
              - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
                with tracking
              - `PRIORITY` - USPS Priority, 1-3 day shipping, with tracking
              - `EXPRESS` - FedEx Express, 3-day shipping, with tracking
              - `2_DAY` - FedEx 2-day shipping, with tracking
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return await self._post(
            f"/v1/cards/{card_token}/reissue",
            body=await async_maybe_transform(
                {
                    "carrier": carrier,
                    "product_id": product_id,
                    "shipping_address": shipping_address,
                    "shipping_method": shipping_method,
                },
                card_reissue_params.CardReissueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def renew(
        self,
        card_token: str,
        *,
        shipping_address: ShippingAddress,
        carrier: Carrier | NotGiven = NOT_GIVEN,
        exp_month: str | NotGiven = NOT_GIVEN,
        exp_year: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        shipping_method: Literal["2-DAY", "EXPEDITED", "EXPRESS", "PRIORITY", "STANDARD", "STANDARD_WITH_TRACKING"]
        | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """
        Creates a new card with the same card token and PAN, but updated expiry and CVC2
        code. The original card will keep working for card-present transactions until
        the new card is activated. For card-not-present transactions, the original card
        details (expiry, CVC2) will also keep working until the new card is activated.
        Applies to card types `PHYSICAL` and `VIRTUAL`. A card can be replaced or
        renewed a total of 8 times.

        Args:
          shipping_address: The shipping address this card will be sent to.

          carrier: If omitted, the previous carrier will be used.

          exp_month: Two digit (MM) expiry month. If neither `exp_month` nor `exp_year` is provided,
              an expiration date six years in the future will be generated.

          exp_year: Four digit (yyyy) expiry year. If neither `exp_month` nor `exp_year` is
              provided, an expiration date six years in the future will be generated.

          product_id: Specifies the configuration (e.g. physical card art) that the card should be
              manufactured with, and only applies to cards of type `PHYSICAL`. This must be
              configured with Lithic before use.

          shipping_method: Shipping method for the card. Use of options besides `STANDARD` require
              additional permissions.

              - `STANDARD` - USPS regular mail or similar international option, with no
                tracking
              - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
                with tracking
              - `PRIORITY` - USPS Priority, 1-3 day shipping, with tracking
              - `EXPRESS` - FedEx Express, 3-day shipping, with tracking
              - `2_DAY` - FedEx 2-day shipping, with tracking
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return await self._post(
            f"/v1/cards/{card_token}/renew",
            body=await async_maybe_transform(
                {
                    "shipping_address": shipping_address,
                    "carrier": carrier,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "product_id": product_id,
                    "shipping_method": shipping_method,
                },
                card_renew_params.CardRenewParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def retrieve_spend_limits(
        self,
        card_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardSpendLimits:
        """
        Get a Card's available spend limit, which is based on the spend limit configured
        on the Card and the amount already spent over the spend limit's duration. For
        example, if the Card has a monthly spend limit of $1000 configured, and has
        spent $600 in the last month, the available spend limit returned would be $400.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return await self._get(
            f"/v1/cards/{card_token}/spend_limits",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardSpendLimits,
        )

    async def search_by_pan(
        self,
        *,
        pan: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """Get card configuration such as spend limit and state.

        Customers must be PCI
        compliant to use this endpoint. Please contact
        [support@lithic.com](mailto:support@lithic.com) for questions. _Note: this is a
        `POST` endpoint because it is more secure to send sensitive data in a request
        body than in a URL._

        Args:
          pan: The PAN for the card being retrieved.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/cards/search_by_pan",
            body=await async_maybe_transform({"pan": pan}, card_search_by_pan_params.CardSearchByPanParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )


class CardsWithRawResponse:
    def __init__(self, cards: Cards) -> None:
        self._cards = cards

        self.create = _legacy_response.to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            cards.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            cards.list,
        )
        self.convert_physical = _legacy_response.to_raw_response_wrapper(
            cards.convert_physical,
        )
        self.embed = _legacy_response.to_raw_response_wrapper(
            cards.embed,
        )
        self.provision = _legacy_response.to_raw_response_wrapper(
            cards.provision,
        )
        self.reissue = _legacy_response.to_raw_response_wrapper(
            cards.reissue,
        )
        self.renew = _legacy_response.to_raw_response_wrapper(
            cards.renew,
        )
        self.retrieve_spend_limits = _legacy_response.to_raw_response_wrapper(
            cards.retrieve_spend_limits,
        )
        self.search_by_pan = _legacy_response.to_raw_response_wrapper(
            cards.search_by_pan,
        )

    @cached_property
    def aggregate_balances(self) -> AggregateBalancesWithRawResponse:
        return AggregateBalancesWithRawResponse(self._cards.aggregate_balances)

    @cached_property
    def balances(self) -> BalancesWithRawResponse:
        return BalancesWithRawResponse(self._cards.balances)

    @cached_property
    def financial_transactions(self) -> FinancialTransactionsWithRawResponse:
        return FinancialTransactionsWithRawResponse(self._cards.financial_transactions)


class AsyncCardsWithRawResponse:
    def __init__(self, cards: AsyncCards) -> None:
        self._cards = cards

        self.create = _legacy_response.async_to_raw_response_wrapper(
            cards.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            cards.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            cards.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            cards.list,
        )
        self.convert_physical = _legacy_response.async_to_raw_response_wrapper(
            cards.convert_physical,
        )
        self.embed = _legacy_response.async_to_raw_response_wrapper(
            cards.embed,
        )
        self.provision = _legacy_response.async_to_raw_response_wrapper(
            cards.provision,
        )
        self.reissue = _legacy_response.async_to_raw_response_wrapper(
            cards.reissue,
        )
        self.renew = _legacy_response.async_to_raw_response_wrapper(
            cards.renew,
        )
        self.retrieve_spend_limits = _legacy_response.async_to_raw_response_wrapper(
            cards.retrieve_spend_limits,
        )
        self.search_by_pan = _legacy_response.async_to_raw_response_wrapper(
            cards.search_by_pan,
        )

    @cached_property
    def aggregate_balances(self) -> AsyncAggregateBalancesWithRawResponse:
        return AsyncAggregateBalancesWithRawResponse(self._cards.aggregate_balances)

    @cached_property
    def balances(self) -> AsyncBalancesWithRawResponse:
        return AsyncBalancesWithRawResponse(self._cards.balances)

    @cached_property
    def financial_transactions(self) -> AsyncFinancialTransactionsWithRawResponse:
        return AsyncFinancialTransactionsWithRawResponse(self._cards.financial_transactions)


class CardsWithStreamingResponse:
    def __init__(self, cards: Cards) -> None:
        self._cards = cards

        self.create = to_streamed_response_wrapper(
            cards.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            cards.update,
        )
        self.list = to_streamed_response_wrapper(
            cards.list,
        )
        self.convert_physical = to_streamed_response_wrapper(
            cards.convert_physical,
        )
        self.embed = to_streamed_response_wrapper(
            cards.embed,
        )
        self.provision = to_streamed_response_wrapper(
            cards.provision,
        )
        self.reissue = to_streamed_response_wrapper(
            cards.reissue,
        )
        self.renew = to_streamed_response_wrapper(
            cards.renew,
        )
        self.retrieve_spend_limits = to_streamed_response_wrapper(
            cards.retrieve_spend_limits,
        )
        self.search_by_pan = to_streamed_response_wrapper(
            cards.search_by_pan,
        )

    @cached_property
    def aggregate_balances(self) -> AggregateBalancesWithStreamingResponse:
        return AggregateBalancesWithStreamingResponse(self._cards.aggregate_balances)

    @cached_property
    def balances(self) -> BalancesWithStreamingResponse:
        return BalancesWithStreamingResponse(self._cards.balances)

    @cached_property
    def financial_transactions(self) -> FinancialTransactionsWithStreamingResponse:
        return FinancialTransactionsWithStreamingResponse(self._cards.financial_transactions)


class AsyncCardsWithStreamingResponse:
    def __init__(self, cards: AsyncCards) -> None:
        self._cards = cards

        self.create = async_to_streamed_response_wrapper(
            cards.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            cards.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            cards.update,
        )
        self.list = async_to_streamed_response_wrapper(
            cards.list,
        )
        self.convert_physical = async_to_streamed_response_wrapper(
            cards.convert_physical,
        )
        self.embed = async_to_streamed_response_wrapper(
            cards.embed,
        )
        self.provision = async_to_streamed_response_wrapper(
            cards.provision,
        )
        self.reissue = async_to_streamed_response_wrapper(
            cards.reissue,
        )
        self.renew = async_to_streamed_response_wrapper(
            cards.renew,
        )
        self.retrieve_spend_limits = async_to_streamed_response_wrapper(
            cards.retrieve_spend_limits,
        )
        self.search_by_pan = async_to_streamed_response_wrapper(
            cards.search_by_pan,
        )

    @cached_property
    def aggregate_balances(self) -> AsyncAggregateBalancesWithStreamingResponse:
        return AsyncAggregateBalancesWithStreamingResponse(self._cards.aggregate_balances)

    @cached_property
    def balances(self) -> AsyncBalancesWithStreamingResponse:
        return AsyncBalancesWithStreamingResponse(self._cards.balances)

    @cached_property
    def financial_transactions(self) -> AsyncFinancialTransactionsWithStreamingResponse:
        return AsyncFinancialTransactionsWithStreamingResponse(self._cards.financial_transactions)
