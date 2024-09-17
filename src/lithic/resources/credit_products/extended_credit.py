# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.credit_products.extended_credit import ExtendedCredit

__all__ = ["ExtendedCreditResource", "AsyncExtendedCreditResource"]


class ExtendedCreditResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtendedCreditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return ExtendedCreditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtendedCreditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return ExtendedCreditResourceWithStreamingResponse(self)

    def retrieve(
        self,
        credit_product_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtendedCredit:
        """
        Get the extended credit for a given credit product under a program

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_product_id:
            raise ValueError(f"Expected a non-empty value for `credit_product_id` but received {credit_product_id!r}")
        return self._get(
            f"/v1/credit_products/{credit_product_id}/extended_credit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtendedCredit,
        )


class AsyncExtendedCreditResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtendedCreditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExtendedCreditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtendedCreditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncExtendedCreditResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        credit_product_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExtendedCredit:
        """
        Get the extended credit for a given credit product under a program

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_product_id:
            raise ValueError(f"Expected a non-empty value for `credit_product_id` but received {credit_product_id!r}")
        return await self._get(
            f"/v1/credit_products/{credit_product_id}/extended_credit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtendedCredit,
        )


class ExtendedCreditResourceWithRawResponse:
    def __init__(self, extended_credit: ExtendedCreditResource) -> None:
        self._extended_credit = extended_credit

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            extended_credit.retrieve,
        )


class AsyncExtendedCreditResourceWithRawResponse:
    def __init__(self, extended_credit: AsyncExtendedCreditResource) -> None:
        self._extended_credit = extended_credit

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            extended_credit.retrieve,
        )


class ExtendedCreditResourceWithStreamingResponse:
    def __init__(self, extended_credit: ExtendedCreditResource) -> None:
        self._extended_credit = extended_credit

        self.retrieve = to_streamed_response_wrapper(
            extended_credit.retrieve,
        )


class AsyncExtendedCreditResourceWithStreamingResponse:
    def __init__(self, extended_credit: AsyncExtendedCreditResource) -> None:
        self._extended_credit = extended_credit

        self.retrieve = async_to_streamed_response_wrapper(
            extended_credit.retrieve,
        )
