# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Dict
from .._core import Timeout, make_request_options
from .._resource import SyncAPIResource, AsyncAPIResource
from .._models import StringModel, NoneModel
from ..pagination import SyncPage, AsyncPage
from ..types.card import *
from ..types.card_provision_response import *
from ..types.card_create_params import *
from ..types.card_update_params import *
from ..types.card_list_params import *
from ..types.card_embed_params import *
from ..types.card_provision_params import *
from ..types.card_reissue_params import *

__all__ = ["Cards", "AsyncCards"]


class Cards(SyncAPIResource):
    def create(
        self,
        body: CardCreateParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> Card:
        """Create a new virtual or physical card.

        Parameters `pin`, `shipping_address`, and `product_id` only
        apply to physical cards.
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.post("/cards", model=Card, body=body, options=options)

    def retrieve(
        self,
        id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> Card:
        """Get card configuration such as spend limit and state."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.get(f"/cards/{id}", model=Card, options=options)

    def update(
        self,
        id: str,
        body: CardUpdateParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> Card:
        """Update the specified properties of the card.

        Unsupplied properties will remain unchanged. `pin` parameter
        only applies to physical cards. *Note: setting a card to a
        `CLOSED` state is a final action that cannot be undone.*
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.patch(f"/cards/{id}", model=Card, body=body, options=options)

    def list(
        self,
        query: Optional[CardListParams] = None,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> SyncPage[Card]:
        """List cards."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.get_api_list("/cards", model=Card, page=SyncPage[Card], query=query, options=options)

    def embed(
        self,
        query: Optional[CardEmbedParams] = None,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> str:
        """Handling full card PANs and CVV codes requires that you comply with
        the Payment Card Industry Data Security Standards (PCI DSS).

        Some clients choose to reduce their compliance obligations by
        leveraging our embedded card UI solution documented below. In
        this setup, PANs and CVV codes are presented to the end-user via
        a card UI that we provide, optionally styled in the customer's
        branding using a specified css stylesheet. A user's browser
        makes the request directly to api.lithic.com, so card PANs and
        CVVs never touch the API customer's servers while full card data
        is displayed to their end-users. The response contains an HTML
        document. This means that the url for the request can be
        inserted straight into the `src` attribute of an iframe. ```html
        ``` You should compute the request payload on the server side.
        You can render it (or the whole iframe) on the server or make an
        ajax call from your front end code, but **do not ever embed your
        API key into front end code, as doing so introduces a serious
        security vulnerability**.
        """
        headers = {"Accept": "text/html", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        result = self.get("/embed/card", model=StringModel, query=query, options=options)
        return result.content

    def provision(
        self,
        id: str,
        body: CardProvisionParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> CardProvisionResponse:
        """Allow your cardholders to directly add payment cards to the device's
        digital wallet (e.g. Apple Pay) with one touch from your app.

        This requires some additional setup and configuration. Please
        reach out to [api@lithic.com](mailto:api@lithic.com) or your
        account rep for more information.
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.post(f"/cards/{id}/provision", model=CardProvisionResponse, body=body, options=options)

    def reissue(
        self,
        id: str,
        body: CardReissueParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> Card:
        """Initiate print and shipment of a duplicate card.

        Only applies to cards of type `PHYSICAL` [beta].
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.post(f"/cards/{id}/reissue", model=Card, body=body, options=options)


class AsyncCards(AsyncAPIResource):
    async def create(
        self,
        body: CardCreateParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> Card:
        """Create a new virtual or physical card.

        Parameters `pin`, `shipping_address`, and `product_id` only
        apply to physical cards.
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.post("/cards", model=Card, body=body, options=options)

    async def retrieve(
        self,
        id: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> Card:
        """Get card configuration such as spend limit and state."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.get(f"/cards/{id}", model=Card, options=options)

    async def update(
        self,
        id: str,
        body: CardUpdateParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> Card:
        """Update the specified properties of the card.

        Unsupplied properties will remain unchanged. `pin` parameter
        only applies to physical cards. *Note: setting a card to a
        `CLOSED` state is a final action that cannot be undone.*
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.patch(f"/cards/{id}", model=Card, body=body, options=options)

    def list(
        self,
        query: Optional[CardListParams] = None,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> AsyncPage[Card]:
        """List cards."""
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self.get_api_list("/cards", model=Card, page=AsyncPage[Card], query=query, options=options)

    async def embed(
        self,
        query: Optional[CardEmbedParams] = None,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> str:
        """Handling full card PANs and CVV codes requires that you comply with
        the Payment Card Industry Data Security Standards (PCI DSS).

        Some clients choose to reduce their compliance obligations by
        leveraging our embedded card UI solution documented below. In
        this setup, PANs and CVV codes are presented to the end-user via
        a card UI that we provide, optionally styled in the customer's
        branding using a specified css stylesheet. A user's browser
        makes the request directly to api.lithic.com, so card PANs and
        CVVs never touch the API customer's servers while full card data
        is displayed to their end-users. The response contains an HTML
        document. This means that the url for the request can be
        inserted straight into the `src` attribute of an iframe. ```html
        ``` You should compute the request payload on the server side.
        You can render it (or the whole iframe) on the server or make an
        ajax call from your front end code, but **do not ever embed your
        API key into front end code, as doing so introduces a serious
        security vulnerability**.
        """
        headers = {"Accept": "text/html", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        result = await self.get("/embed/card", model=StringModel, query=query, options=options)
        return result.content

    async def provision(
        self,
        id: str,
        body: CardProvisionParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> CardProvisionResponse:
        """Allow your cardholders to directly add payment cards to the device's
        digital wallet (e.g. Apple Pay) with one touch from your app.

        This requires some additional setup and configuration. Please
        reach out to [api@lithic.com](mailto:api@lithic.com) or your
        account rep for more information.
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.post(f"/cards/{id}/provision", model=CardProvisionResponse, body=body, options=options)

    async def reissue(
        self,
        id: str,
        body: CardReissueParams,
        *,
        headers: Optional[Dict[str, str]] = None,
        max_retries: Optional[int] = None,
        timeout: Optional[Union[float, Timeout]] = None,
    ) -> Card:
        """Initiate print and shipment of a duplicate card.

        Only applies to cards of type `PHYSICAL` [beta].
        """
        headers = {"Accept": "application/json", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self.post(f"/cards/{id}/reissue", model=Card, body=body, options=options)
