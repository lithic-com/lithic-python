# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .extended_credit import (
    ExtendedCreditResource,
    AsyncExtendedCreditResource,
    ExtendedCreditResourceWithRawResponse,
    AsyncExtendedCreditResourceWithRawResponse,
    ExtendedCreditResourceWithStreamingResponse,
    AsyncExtendedCreditResourceWithStreamingResponse,
)

__all__ = ["CreditProducts", "AsyncCreditProducts"]


class CreditProducts(SyncAPIResource):
    @cached_property
    def extended_credit(self) -> ExtendedCreditResource:
        return ExtendedCreditResource(self._client)

    @cached_property
    def with_raw_response(self) -> CreditProductsWithRawResponse:
        return CreditProductsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditProductsWithStreamingResponse:
        return CreditProductsWithStreamingResponse(self)


class AsyncCreditProducts(AsyncAPIResource):
    @cached_property
    def extended_credit(self) -> AsyncExtendedCreditResource:
        return AsyncExtendedCreditResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCreditProductsWithRawResponse:
        return AsyncCreditProductsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditProductsWithStreamingResponse:
        return AsyncCreditProductsWithStreamingResponse(self)


class CreditProductsWithRawResponse:
    def __init__(self, credit_products: CreditProducts) -> None:
        self._credit_products = credit_products

    @cached_property
    def extended_credit(self) -> ExtendedCreditResourceWithRawResponse:
        return ExtendedCreditResourceWithRawResponse(self._credit_products.extended_credit)


class AsyncCreditProductsWithRawResponse:
    def __init__(self, credit_products: AsyncCreditProducts) -> None:
        self._credit_products = credit_products

    @cached_property
    def extended_credit(self) -> AsyncExtendedCreditResourceWithRawResponse:
        return AsyncExtendedCreditResourceWithRawResponse(self._credit_products.extended_credit)


class CreditProductsWithStreamingResponse:
    def __init__(self, credit_products: CreditProducts) -> None:
        self._credit_products = credit_products

    @cached_property
    def extended_credit(self) -> ExtendedCreditResourceWithStreamingResponse:
        return ExtendedCreditResourceWithStreamingResponse(self._credit_products.extended_credit)


class AsyncCreditProductsWithStreamingResponse:
    def __init__(self, credit_products: AsyncCreditProducts) -> None:
        self._credit_products = credit_products

    @cached_property
    def extended_credit(self) -> AsyncExtendedCreditResourceWithStreamingResponse:
        return AsyncExtendedCreditResourceWithStreamingResponse(self._credit_products.extended_credit)
