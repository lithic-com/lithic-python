# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import CardProductCreditDetailResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["CardProduct", "AsyncCardProduct"]


class CardProduct(SyncAPIResource):
    def credit_detail(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
    async def credit_detail(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CardProductCreditDetailResponse:
        """Get the Credit Detail for the card product"""
        return await self._get(
            "/card_product/credit_detail",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardProductCreditDetailResponse,
        )
