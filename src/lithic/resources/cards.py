# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import hmac
import json
import base64
import hashlib
from typing import Union
from datetime import datetime, timezone, timedelta
from typing_extensions import Literal

from httpx import URL

from ..types import (
    Card,
    SpendLimitDuration,
    CardProvisionResponse,
    shared_params,
    card_list_params,
    card_embed_params,
    card_create_params,
    card_update_params,
    card_reissue_params,
    card_provision_params,
    card_get_embed_url_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, strip_not_given
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, _merge_mappings, make_request_options

__all__ = ["Cards", "AsyncCards"]


class Cards(SyncAPIResource):
    def create(
        self,
        *,
        type: Literal["VIRTUAL", "PHYSICAL", "MERCHANT_LOCKED", "SINGLE_USE"],
        account_token: str | NotGiven = NOT_GIVEN,
        card_program_token: str | NotGiven = NOT_GIVEN,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        exp_month: str | NotGiven = NOT_GIVEN,
        exp_year: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        shipping_address: shared_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method: Literal["STANDARD", "STANDARD_WITH_TRACKING", "EXPEDITED"] | NotGiven = NOT_GIVEN,
        spend_limit: int | NotGiven = NOT_GIVEN,
        spend_limit_duration: SpendLimitDuration | NotGiven = NOT_GIVEN,
        state: Literal["OPEN", "PAUSED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Card:
        """Create a new virtual or physical card.

        Parameters `pin`, `shipping_address`, and
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

          memo: Friendly name to identify the card. We recommend against using this field to
              store JSON data as it can cause unexpected behavior.

          pin: Encrypted PIN block (in base64). Only applies to cards of type `PHYSICAL` and
              `VIRTUAL`. See
              [Encrypted PIN Block](https://docs.lithic.com/docs/cards#encrypted-pin-block-enterprise).

          product_id: Only applicable to cards of type `PHYSICAL`. This must be configured with Lithic
              before use. Specifies the configuration (i.e., physical card art) that the card
              should be manufactured with.

          shipping_method: Shipping method for the card. Only applies to cards of type PHYSICAL. Use of
              options besides `STANDARD` require additional permissions.

              - `STANDARD` - USPS regular mail or similar international option, with no
                tracking
              - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
                with tracking
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          spend_limit: Amount (in cents) to limit approved authorizations. Transaction requests above
              the spend limit will be declined. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the card
              limit.

          spend_limit_duration:
              Spend limit duration values:

              - `ANNUALLY` - Card will authorize transactions up to spend limit in a calendar
                year.
              - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
                of the card.
              - `MONTHLY` - Card will authorize transactions up to spend limit for the
                trailing month. Month is calculated as this calendar date one month prior.
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/cards",
            body=maybe_transform(
                {
                    "type": type,
                    "account_token": account_token,
                    "card_program_token": card_program_token,
                    "digital_card_art_token": digital_card_art_token,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "memo": memo,
                    "pin": pin,
                    "product_id": product_id,
                    "shipping_address": shipping_address,
                    "shipping_method": shipping_method,
                    "spend_limit": spend_limit,
                    "spend_limit_duration": spend_limit_duration,
                    "state": state,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """
        Get card configuration such as spend limit and state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/cards/{card_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    def update(
        self,
        card_token: str,
        *,
        auth_rule_token: str | NotGiven = NOT_GIVEN,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        spend_limit: int | NotGiven = NOT_GIVEN,
        spend_limit_duration: SpendLimitDuration | NotGiven = NOT_GIVEN,
        state: Literal["CLOSED", "OPEN", "PAUSED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Card:
        """Update the specified properties of the card.

        Unsupplied properties will remain
        unchanged. `pin` parameter only applies to physical cards.

        _Note: setting a card to a `CLOSED` state is a final action that cannot be
        undone._

        Args:
          auth_rule_token: Identifier for any Auth Rules that will be applied to transactions taking place
              with the card.

          digital_card_art_token: Specifies the digital card art to be displayed in the user’s digital wallet
              after tokenization. This artwork must be approved by Mastercard and configured
              by Lithic to use. See
              [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).

          memo: Friendly name to identify the card. We recommend against using this field to
              store JSON data as it can cause unexpected behavior.

          pin: Encrypted PIN block (in base64). Only applies to cards of type `PHYSICAL` and
              `VIRTUAL`. See
              [Encrypted PIN Block](https://docs.lithic.com/docs/cards#encrypted-pin-block-enterprise).

          spend_limit: Amount (in cents) to limit approved authorizations. Transaction requests above
              the spend limit will be declined. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the card
              limit.

          spend_limit_duration:
              Spend limit duration values:

              - `ANNUALLY` - Card will authorize transactions up to spend limit in a calendar
                year.
              - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
                of the card.
              - `MONTHLY` - Card will authorize transactions up to spend limit for the
                trailing month. Month is calculated as this calendar date one month prior.
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/cards/{card_token}",
            body=maybe_transform(
                {
                    "auth_rule_token": auth_rule_token,
                    "digital_card_art_token": digital_card_art_token,
                    "memo": memo,
                    "pin": pin,
                    "spend_limit": spend_limit,
                    "spend_limit_duration": spend_limit_duration,
                    "state": state,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Card,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> SyncPage[Card]:
        """
        List cards.

        Args:
          account_token: Returns cards associated with the specified account.

          begin: Date string in RFC 3339 format. Only entries created after the specified date
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included. UTC time zone.

          page: Page (for pagination).

          page_size: Page size (for pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cards",
            page=SyncPage[Card],
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
                        "page": page,
                        "page_size": page_size,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            model=Card,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
            "/embed/card",
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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
        raw_path = base_url.raw_path + URL("embed/card").raw_path
        return base_url.copy_with(raw_path=raw_path).copy_merge_params(params)

    def provision(
        self,
        card_token: str,
        *,
        certificate: str | NotGiven = NOT_GIVEN,
        digital_wallet: Literal["APPLE_PAY", "GOOGLE_PAY", "SAMSUNG_PAY"] | NotGiven = NOT_GIVEN,
        nonce: str | NotGiven = NOT_GIVEN,
        nonce_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/cards/{card_token}/provision",
            body=maybe_transform(
                {
                    "certificate": certificate,
                    "digital_wallet": digital_wallet,
                    "nonce": nonce,
                    "nonce_signature": nonce_signature,
                },
                card_provision_params.CardProvisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardProvisionResponse,
        )

    def reissue(
        self,
        card_token: str,
        *,
        product_id: str | NotGiven = NOT_GIVEN,
        shipping_address: shared_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method: Literal["STANDARD", "STANDARD_WITH_TRACKING", "EXPEDITED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Card:
        """
        Initiate print and shipment of a duplicate physical card.

        Only applies to cards of type `PHYSICAL`.

        Args:
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
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            f"/cards/{card_token}/reissue",
            body=maybe_transform(
                {
                    "product_id": product_id,
                    "shipping_address": shipping_address,
                    "shipping_method": shipping_method,
                },
                card_reissue_params.CardReissueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Card,
        )


class AsyncCards(AsyncAPIResource):
    async def create(
        self,
        *,
        type: Literal["VIRTUAL", "PHYSICAL", "MERCHANT_LOCKED", "SINGLE_USE"],
        account_token: str | NotGiven = NOT_GIVEN,
        card_program_token: str | NotGiven = NOT_GIVEN,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        exp_month: str | NotGiven = NOT_GIVEN,
        exp_year: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        product_id: str | NotGiven = NOT_GIVEN,
        shipping_address: shared_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method: Literal["STANDARD", "STANDARD_WITH_TRACKING", "EXPEDITED"] | NotGiven = NOT_GIVEN,
        spend_limit: int | NotGiven = NOT_GIVEN,
        spend_limit_duration: SpendLimitDuration | NotGiven = NOT_GIVEN,
        state: Literal["OPEN", "PAUSED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Card:
        """Create a new virtual or physical card.

        Parameters `pin`, `shipping_address`, and
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

          memo: Friendly name to identify the card. We recommend against using this field to
              store JSON data as it can cause unexpected behavior.

          pin: Encrypted PIN block (in base64). Only applies to cards of type `PHYSICAL` and
              `VIRTUAL`. See
              [Encrypted PIN Block](https://docs.lithic.com/docs/cards#encrypted-pin-block-enterprise).

          product_id: Only applicable to cards of type `PHYSICAL`. This must be configured with Lithic
              before use. Specifies the configuration (i.e., physical card art) that the card
              should be manufactured with.

          shipping_method: Shipping method for the card. Only applies to cards of type PHYSICAL. Use of
              options besides `STANDARD` require additional permissions.

              - `STANDARD` - USPS regular mail or similar international option, with no
                tracking
              - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
                with tracking
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          spend_limit: Amount (in cents) to limit approved authorizations. Transaction requests above
              the spend limit will be declined. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the card
              limit.

          spend_limit_duration:
              Spend limit duration values:

              - `ANNUALLY` - Card will authorize transactions up to spend limit in a calendar
                year.
              - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
                of the card.
              - `MONTHLY` - Card will authorize transactions up to spend limit for the
                trailing month. Month is calculated as this calendar date one month prior.
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/cards",
            body=maybe_transform(
                {
                    "type": type,
                    "account_token": account_token,
                    "card_program_token": card_program_token,
                    "digital_card_art_token": digital_card_art_token,
                    "exp_month": exp_month,
                    "exp_year": exp_year,
                    "memo": memo,
                    "pin": pin,
                    "product_id": product_id,
                    "shipping_address": shipping_address,
                    "shipping_method": shipping_method,
                    "spend_limit": spend_limit,
                    "spend_limit_duration": spend_limit_duration,
                    "state": state,
                },
                card_create_params.CardCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Card:
        """
        Get card configuration such as spend limit and state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/cards/{card_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Card,
        )

    async def update(
        self,
        card_token: str,
        *,
        auth_rule_token: str | NotGiven = NOT_GIVEN,
        digital_card_art_token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        pin: str | NotGiven = NOT_GIVEN,
        spend_limit: int | NotGiven = NOT_GIVEN,
        spend_limit_duration: SpendLimitDuration | NotGiven = NOT_GIVEN,
        state: Literal["CLOSED", "OPEN", "PAUSED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Card:
        """Update the specified properties of the card.

        Unsupplied properties will remain
        unchanged. `pin` parameter only applies to physical cards.

        _Note: setting a card to a `CLOSED` state is a final action that cannot be
        undone._

        Args:
          auth_rule_token: Identifier for any Auth Rules that will be applied to transactions taking place
              with the card.

          digital_card_art_token: Specifies the digital card art to be displayed in the user’s digital wallet
              after tokenization. This artwork must be approved by Mastercard and configured
              by Lithic to use. See
              [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).

          memo: Friendly name to identify the card. We recommend against using this field to
              store JSON data as it can cause unexpected behavior.

          pin: Encrypted PIN block (in base64). Only applies to cards of type `PHYSICAL` and
              `VIRTUAL`. See
              [Encrypted PIN Block](https://docs.lithic.com/docs/cards#encrypted-pin-block-enterprise).

          spend_limit: Amount (in cents) to limit approved authorizations. Transaction requests above
              the spend limit will be declined. Note that a spend limit of 0 is effectively no
              limit, and should only be used to reset or remove a prior limit. Only a limit of
              1 or above will result in declined transactions due to checks against the card
              limit.

          spend_limit_duration:
              Spend limit duration values:

              - `ANNUALLY` - Card will authorize transactions up to spend limit in a calendar
                year.
              - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
                of the card.
              - `MONTHLY` - Card will authorize transactions up to spend limit for the
                trailing month. Month is calculated as this calendar date one month prior.
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/cards/{card_token}",
            body=maybe_transform(
                {
                    "auth_rule_token": auth_rule_token,
                    "digital_card_art_token": digital_card_art_token,
                    "memo": memo,
                    "pin": pin,
                    "spend_limit": spend_limit,
                    "spend_limit_duration": spend_limit_duration,
                    "state": state,
                },
                card_update_params.CardUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Card,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Card, AsyncPage[Card]]:
        """
        List cards.

        Args:
          account_token: Returns cards associated with the specified account.

          begin: Date string in RFC 3339 format. Only entries created after the specified date
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included. UTC time zone.

          page: Page (for pagination).

          page_size: Page size (for pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cards",
            page=AsyncPage[Card],
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
                        "page": page,
                        "page_size": page_size,
                    },
                    card_list_params.CardListParams,
                ),
            ),
            model=Card,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
            "/embed/card",
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
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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
        raw_path = base_url.raw_path + URL("embed/card").raw_path
        return base_url.copy_with(raw_path=raw_path).copy_merge_params(params)

    async def provision(
        self,
        card_token: str,
        *,
        certificate: str | NotGiven = NOT_GIVEN,
        digital_wallet: Literal["APPLE_PAY", "GOOGLE_PAY", "SAMSUNG_PAY"] | NotGiven = NOT_GIVEN,
        nonce: str | NotGiven = NOT_GIVEN,
        nonce_signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/cards/{card_token}/provision",
            body=maybe_transform(
                {
                    "certificate": certificate,
                    "digital_wallet": digital_wallet,
                    "nonce": nonce,
                    "nonce_signature": nonce_signature,
                },
                card_provision_params.CardProvisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=CardProvisionResponse,
        )

    async def reissue(
        self,
        card_token: str,
        *,
        product_id: str | NotGiven = NOT_GIVEN,
        shipping_address: shared_params.ShippingAddress | NotGiven = NOT_GIVEN,
        shipping_method: Literal["STANDARD", "STANDARD_WITH_TRACKING", "EXPEDITED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> Card:
        """
        Initiate print and shipment of a duplicate physical card.

        Only applies to cards of type `PHYSICAL`.

        Args:
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
              - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
                tracking

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            f"/cards/{card_token}/reissue",
            body=maybe_transform(
                {
                    "product_id": product_id,
                    "shipping_address": shipping_address,
                    "shipping_method": shipping_method,
                },
                card_reissue_params.CardReissueParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=Card,
        )
