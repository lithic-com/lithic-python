# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..types import CardProductCreditDetailResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Lithic, AsyncLithic

__all__ = ["CardProduct", "AsyncCardProduct"]


class CardProduct(SyncAPIResource):
    with_raw_response: CardProductWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = CardProductWithRawResponse(self)

    def credit_detail(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardProductCreditDetailResponse:
        """Get the Credit Detail for the card product"""
        return self._get(
            "/card_product/credit_detail",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardProductCreditDetailResponse,
        )


class AsyncCardProduct(AsyncAPIResource):
    with_raw_response: AsyncCardProductWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncCardProductWithRawResponse(self)

    async def credit_detail(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardProductCreditDetailResponse:
        """Get the Credit Detail for the card product"""
        return await self._get(
            "/card_product/credit_detail",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardProductCreditDetailResponse,
        )


class CardProductWithRawResponse:
    def __init__(self, card_product: CardProduct) -> None:
        self.credit_detail = to_raw_response_wrapper(
            card_product.credit_detail,
        )


class AsyncCardProductWithRawResponse:
    def __init__(self, card_product: AsyncCardProduct) -> None:
        self.credit_detail = async_to_raw_response_wrapper(
            card_product.credit_detail,
        )
