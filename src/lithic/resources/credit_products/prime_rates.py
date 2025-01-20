# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.credit_products import prime_rate_create_params, prime_rate_retrieve_params
from ...types.credit_products.prime_rate_retrieve_response import PrimeRateRetrieveResponse

__all__ = ["PrimeRates", "AsyncPrimeRates"]


class PrimeRates(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrimeRatesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return PrimeRatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrimeRatesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return PrimeRatesWithStreamingResponse(self)

    def create(
        self,
        credit_product_token: str,
        *,
        effective_date: Union[str, date],
        rate: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Post Credit Product Prime Rate

        Args:
          credit_product_token: Globally unique identifier for credit products.

          effective_date: Date the rate goes into effect

          rate: The rate in decimal format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_product_token:
            raise ValueError(
                f"Expected a non-empty value for `credit_product_token` but received {credit_product_token!r}"
            )
        return self._post(
            f"/v1/credit_products/{credit_product_token}/prime_rates",
            body=maybe_transform(
                {
                    "effective_date": effective_date,
                    "rate": rate,
                },
                prime_rate_create_params.PrimeRateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def retrieve(
        self,
        credit_product_token: str,
        *,
        ending_before: Union[str, date] | NotGiven = NOT_GIVEN,
        starting_after: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrimeRateRetrieveResponse:
        """
        Get Credit Product Prime Rates

        Args:
          credit_product_token: Globally unique identifier for credit products.

          ending_before: The effective date that the prime rates ends before

          starting_after: The effective date that the prime rate starts after

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_product_token:
            raise ValueError(
                f"Expected a non-empty value for `credit_product_token` but received {credit_product_token!r}"
            )
        return self._get(
            f"/v1/credit_products/{credit_product_token}/prime_rates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "starting_after": starting_after,
                    },
                    prime_rate_retrieve_params.PrimeRateRetrieveParams,
                ),
            ),
            cast_to=PrimeRateRetrieveResponse,
        )


class AsyncPrimeRates(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrimeRatesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrimeRatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrimeRatesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncPrimeRatesWithStreamingResponse(self)

    async def create(
        self,
        credit_product_token: str,
        *,
        effective_date: Union[str, date],
        rate: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Post Credit Product Prime Rate

        Args:
          credit_product_token: Globally unique identifier for credit products.

          effective_date: Date the rate goes into effect

          rate: The rate in decimal format

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_product_token:
            raise ValueError(
                f"Expected a non-empty value for `credit_product_token` but received {credit_product_token!r}"
            )
        return await self._post(
            f"/v1/credit_products/{credit_product_token}/prime_rates",
            body=await async_maybe_transform(
                {
                    "effective_date": effective_date,
                    "rate": rate,
                },
                prime_rate_create_params.PrimeRateCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def retrieve(
        self,
        credit_product_token: str,
        *,
        ending_before: Union[str, date] | NotGiven = NOT_GIVEN,
        starting_after: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrimeRateRetrieveResponse:
        """
        Get Credit Product Prime Rates

        Args:
          credit_product_token: Globally unique identifier for credit products.

          ending_before: The effective date that the prime rates ends before

          starting_after: The effective date that the prime rate starts after

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_product_token:
            raise ValueError(
                f"Expected a non-empty value for `credit_product_token` but received {credit_product_token!r}"
            )
        return await self._get(
            f"/v1/credit_products/{credit_product_token}/prime_rates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ending_before": ending_before,
                        "starting_after": starting_after,
                    },
                    prime_rate_retrieve_params.PrimeRateRetrieveParams,
                ),
            ),
            cast_to=PrimeRateRetrieveResponse,
        )


class PrimeRatesWithRawResponse:
    def __init__(self, prime_rates: PrimeRates) -> None:
        self._prime_rates = prime_rates

        self.create = _legacy_response.to_raw_response_wrapper(
            prime_rates.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            prime_rates.retrieve,
        )


class AsyncPrimeRatesWithRawResponse:
    def __init__(self, prime_rates: AsyncPrimeRates) -> None:
        self._prime_rates = prime_rates

        self.create = _legacy_response.async_to_raw_response_wrapper(
            prime_rates.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            prime_rates.retrieve,
        )


class PrimeRatesWithStreamingResponse:
    def __init__(self, prime_rates: PrimeRates) -> None:
        self._prime_rates = prime_rates

        self.create = to_streamed_response_wrapper(
            prime_rates.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            prime_rates.retrieve,
        )


class AsyncPrimeRatesWithStreamingResponse:
    def __init__(self, prime_rates: AsyncPrimeRates) -> None:
        self._prime_rates = prime_rates

        self.create = async_to_streamed_response_wrapper(
            prime_rates.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            prime_rates.retrieve,
        )
