# File generated from our OpenAPI spec by Stainless.

import hmac
import json
import base64
import hashlib
from typing import Union
from datetime import datetime, timezone, timedelta

from httpx import URL

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from ..types.card import *
from .._base_client import AsyncPaginator, make_request_options
from ..types.card_list_params import CardListParams
from ..types.card_embed_params import CardEmbedParams
from ..types.card_create_params import CardCreateParams
from ..types.card_update_params import CardUpdateParams
from ..types.card_reissue_params import CardReissueParams
from ..types.embed_request_param import *
from ..types.card_provision_params import CardProvisionParams
from ..types.card_provision_response import *
from ..types.card_get_embed_url_params import CardGetEmbedURLParams
from ..types.card_get_embed_html_params import CardGetEmbedHTMLParams

__all__ = ["Cards", "AsyncCards"]


class Cards(SyncAPIResource):
    def create(
        self,
        body: CardCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        """Create a new virtual or physical card.

        Parameters `pin`, `shipping_address`, and `product_id` only apply to physical
        cards.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/cards",
            body=body,
            options=options,
            cast_to=Card,
        )

    def retrieve(
        self,
        card_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        """Get card configuration such as spend limit and state."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            f"/cards/{card_token}",
            options=options,
            cast_to=Card,
        )

    def update(
        self,
        card_token: str,
        body: CardUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        """Update the specified properties of the card.

        Unsupplied properties will remain unchanged. `pin` parameter only applies to
        physical cards.

        _Note: setting a card to a `CLOSED` state is a final action that cannot be
        undone._
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._patch(
            f"/cards/{card_token}",
            body=body,
            options=options,
            cast_to=Card,
        )

    def list(
        self,
        query: CardListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[Card]:
        """List cards."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/cards",
            page=SyncPage[Card],
            query=query,
            options=options,
            model=Card,
        )

    def embed(
        self,
        query: CardEmbedParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """
        headers = {"Accept": "text/html", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            "/embed/card",
            query=query,
            options=options,
            cast_to=str,
        )

    def get_embed_html(
        self,
        query: CardGetEmbedHTMLParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        headers = {"Accept": "text/html", **(headers or {})}
        return self._get(
            str(self.get_embed_url(query)),
            cast_to=str,
            options=make_request_options(headers, max_retries, timeout),
        )

    def get_embed_url(self, query: CardGetEmbedURLParams) -> URL:
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
        query.setdefault("expiration", (datetime.now(timezone.utc) + timedelta(minutes=1)).isoformat())
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
        body: CardProvisionParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CardProvisionResponse:
        """
        Allow your cardholders to directly add payment cards to the device's digital
        wallet (e.g. Apple Pay) with one touch from your app.

        This requires some additional setup and configuration. Please
        [Contact Us](https://lithic.com/contact) or your Customer Success representative
        for more information.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            f"/cards/{card_token}/provision",
            body=body,
            options=options,
            cast_to=CardProvisionResponse,
        )

    def reissue(
        self,
        card_token: str,
        body: CardReissueParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        """Initiate print and shipment of a duplicate card.

        Only applies to cards of type `PHYSICAL` [beta].
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            f"/cards/{card_token}/reissue",
            body=body,
            options=options,
            cast_to=Card,
        )


class AsyncCards(AsyncAPIResource):
    async def create(
        self,
        body: CardCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        """Create a new virtual or physical card.

        Parameters `pin`, `shipping_address`, and `product_id` only apply to physical
        cards.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/cards",
            body=body,
            options=options,
            cast_to=Card,
        )

    async def retrieve(
        self,
        card_token: str,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        """Get card configuration such as spend limit and state."""
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            f"/cards/{card_token}",
            options=options,
            cast_to=Card,
        )

    async def update(
        self,
        card_token: str,
        body: CardUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        """Update the specified properties of the card.

        Unsupplied properties will remain unchanged. `pin` parameter only applies to
        physical cards.

        _Note: setting a card to a `CLOSED` state is a final action that cannot be
        undone._
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._patch(
            f"/cards/{card_token}",
            body=body,
            options=options,
            cast_to=Card,
        )

    def list(
        self,
        query: CardListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[Card, AsyncPage[Card]]:
        """List cards."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/cards",
            page=AsyncPage[Card],
            query=query,
            options=options,
            model=Card,
        )

    async def embed(
        self,
        query: CardEmbedParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """
        headers = {"Accept": "text/html", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            "/embed/card",
            query=query,
            options=options,
            cast_to=str,
        )

    async def get_embed_html(
        self,
        query: CardGetEmbedHTMLParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        headers = {"Accept": "text/html", **(headers or {})}
        return await self._get(
            str(self.get_embed_url(query)),
            cast_to=str,
            options=make_request_options(headers, max_retries, timeout),
        )

    def get_embed_url(self, query: CardGetEmbedURLParams) -> URL:
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
        query.setdefault("expiration", (datetime.now(timezone.utc) + timedelta(minutes=1)).isoformat())
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
        body: CardProvisionParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> CardProvisionResponse:
        """
        Allow your cardholders to directly add payment cards to the device's digital
        wallet (e.g. Apple Pay) with one touch from your app.

        This requires some additional setup and configuration. Please
        [Contact Us](https://lithic.com/contact) or your Customer Success representative
        for more information.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            f"/cards/{card_token}/provision",
            body=body,
            options=options,
            cast_to=CardProvisionResponse,
        )

    async def reissue(
        self,
        card_token: str,
        body: CardReissueParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Card:
        """Initiate print and shipment of a duplicate card.

        Only applies to cards of type `PHYSICAL` [beta].
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            f"/cards/{card_token}/reissue",
            body=body,
            options=options,
            cast_to=Card,
        )
