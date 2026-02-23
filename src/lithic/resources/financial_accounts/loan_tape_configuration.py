# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.financial_accounts.loan_tape_configuration import LoanTapeConfiguration

__all__ = ["LoanTapeConfigurationResource", "AsyncLoanTapeConfigurationResource"]


class LoanTapeConfigurationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LoanTapeConfigurationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return LoanTapeConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoanTapeConfigurationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return LoanTapeConfigurationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        financial_account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoanTapeConfiguration:
        """
        Get the loan tape configuration for a given financial account.

        Args:
          financial_account_token: Globally unique identifier for financial account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        return self._get(
            f"/v1/financial_accounts/{financial_account_token}/loan_tape_configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoanTapeConfiguration,
        )


class AsyncLoanTapeConfigurationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLoanTapeConfigurationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLoanTapeConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoanTapeConfigurationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncLoanTapeConfigurationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        financial_account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoanTapeConfiguration:
        """
        Get the loan tape configuration for a given financial account.

        Args:
          financial_account_token: Globally unique identifier for financial account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        return await self._get(
            f"/v1/financial_accounts/{financial_account_token}/loan_tape_configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoanTapeConfiguration,
        )


class LoanTapeConfigurationResourceWithRawResponse:
    def __init__(self, loan_tape_configuration: LoanTapeConfigurationResource) -> None:
        self._loan_tape_configuration = loan_tape_configuration

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            loan_tape_configuration.retrieve,
        )


class AsyncLoanTapeConfigurationResourceWithRawResponse:
    def __init__(self, loan_tape_configuration: AsyncLoanTapeConfigurationResource) -> None:
        self._loan_tape_configuration = loan_tape_configuration

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            loan_tape_configuration.retrieve,
        )


class LoanTapeConfigurationResourceWithStreamingResponse:
    def __init__(self, loan_tape_configuration: LoanTapeConfigurationResource) -> None:
        self._loan_tape_configuration = loan_tape_configuration

        self.retrieve = to_streamed_response_wrapper(
            loan_tape_configuration.retrieve,
        )


class AsyncLoanTapeConfigurationResourceWithStreamingResponse:
    def __init__(self, loan_tape_configuration: AsyncLoanTapeConfigurationResource) -> None:
        self._loan_tape_configuration = loan_tape_configuration

        self.retrieve = async_to_streamed_response_wrapper(
            loan_tape_configuration.retrieve,
        )
