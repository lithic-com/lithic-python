# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import CardProductCreditDetailResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import (
    make_request_options,
)

__all__ = ["CardProduct", "AsyncCardProduct"]


class CardProduct(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardProductWithRawResponse:
        return CardProductWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardProductWithStreamingResponse:
        return CardProductWithStreamingResponse(self)

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
    @cached_property
    def with_raw_response(self) -> AsyncCardProductWithRawResponse:
        return AsyncCardProductWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardProductWithStreamingResponse:
        return AsyncCardProductWithStreamingResponse(self)

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
        self._card_product = card_product

        self.credit_detail = _legacy_response.to_raw_response_wrapper(
            card_product.credit_detail,
        )


class AsyncCardProductWithRawResponse:
    def __init__(self, card_product: AsyncCardProduct) -> None:
        self._card_product = card_product

        self.credit_detail = _legacy_response.async_to_raw_response_wrapper(
            card_product.credit_detail,
        )


class CardProductWithStreamingResponse:
    def __init__(self, card_product: CardProduct) -> None:
        self._card_product = card_product

        self.credit_detail = to_streamed_response_wrapper(
            card_product.credit_detail,
        )


class AsyncCardProductWithStreamingResponse:
    def __init__(self, card_product: AsyncCardProduct) -> None:
        self._card_product = card_product

        self.credit_detail = async_to_streamed_response_wrapper(
            card_product.credit_detail,
        )
