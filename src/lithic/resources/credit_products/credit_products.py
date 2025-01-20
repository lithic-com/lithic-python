# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .prime_rates import (
    PrimeRates,
    AsyncPrimeRates,
    PrimeRatesWithRawResponse,
    AsyncPrimeRatesWithRawResponse,
    PrimeRatesWithStreamingResponse,
    AsyncPrimeRatesWithStreamingResponse,
)
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
    def prime_rates(self) -> PrimeRates:
        return PrimeRates(self._client)

    @cached_property
    def with_raw_response(self) -> CreditProductsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return CreditProductsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditProductsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return CreditProductsWithStreamingResponse(self)


class AsyncCreditProducts(AsyncAPIResource):
    @cached_property
    def extended_credit(self) -> AsyncExtendedCreditResource:
        return AsyncExtendedCreditResource(self._client)

    @cached_property
    def prime_rates(self) -> AsyncPrimeRates:
        return AsyncPrimeRates(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCreditProductsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditProductsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditProductsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncCreditProductsWithStreamingResponse(self)


class CreditProductsWithRawResponse:
    def __init__(self, credit_products: CreditProducts) -> None:
        self._credit_products = credit_products

    @cached_property
    def extended_credit(self) -> ExtendedCreditResourceWithRawResponse:
        return ExtendedCreditResourceWithRawResponse(self._credit_products.extended_credit)

    @cached_property
    def prime_rates(self) -> PrimeRatesWithRawResponse:
        return PrimeRatesWithRawResponse(self._credit_products.prime_rates)


class AsyncCreditProductsWithRawResponse:
    def __init__(self, credit_products: AsyncCreditProducts) -> None:
        self._credit_products = credit_products

    @cached_property
    def extended_credit(self) -> AsyncExtendedCreditResourceWithRawResponse:
        return AsyncExtendedCreditResourceWithRawResponse(self._credit_products.extended_credit)

    @cached_property
    def prime_rates(self) -> AsyncPrimeRatesWithRawResponse:
        return AsyncPrimeRatesWithRawResponse(self._credit_products.prime_rates)


class CreditProductsWithStreamingResponse:
    def __init__(self, credit_products: CreditProducts) -> None:
        self._credit_products = credit_products

    @cached_property
    def extended_credit(self) -> ExtendedCreditResourceWithStreamingResponse:
        return ExtendedCreditResourceWithStreamingResponse(self._credit_products.extended_credit)

    @cached_property
    def prime_rates(self) -> PrimeRatesWithStreamingResponse:
        return PrimeRatesWithStreamingResponse(self._credit_products.prime_rates)


class AsyncCreditProductsWithStreamingResponse:
    def __init__(self, credit_products: AsyncCreditProducts) -> None:
        self._credit_products = credit_products

    @cached_property
    def extended_credit(self) -> AsyncExtendedCreditResourceWithStreamingResponse:
        return AsyncExtendedCreditResourceWithStreamingResponse(self._credit_products.extended_credit)

    @cached_property
    def prime_rates(self) -> AsyncPrimeRatesWithStreamingResponse:
        return AsyncPrimeRatesWithStreamingResponse(self._credit_products.prime_rates)
