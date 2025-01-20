# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.financial_accounts import credit_configuration_update_params
from ...types.financial_accounts.financial_account_credit_config import FinancialAccountCreditConfig

__all__ = ["CreditConfiguration", "AsyncCreditConfiguration"]


class CreditConfiguration(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditConfigurationWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return CreditConfigurationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditConfigurationWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return CreditConfigurationWithStreamingResponse(self)

    def retrieve(
        self,
        financial_account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialAccountCreditConfig:
        """
        Get an Account's credit configuration

        Args:
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
            f"/v1/financial_accounts/{financial_account_token}/credit_configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialAccountCreditConfig,
        )

    def update(
        self,
        financial_account_token: str,
        *,
        credit_limit: int | NotGiven = NOT_GIVEN,
        credit_product_token: str | NotGiven = NOT_GIVEN,
        external_bank_account_token: str | NotGiven = NOT_GIVEN,
        tier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialAccountCreditConfig:
        """
        Update an account's credit configuration

        Args:
          credit_product_token: Globally unique identifier for the credit product

          tier: Tier to assign to a financial account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        return self._patch(
            f"/v1/financial_accounts/{financial_account_token}/credit_configuration",
            body=maybe_transform(
                {
                    "credit_limit": credit_limit,
                    "credit_product_token": credit_product_token,
                    "external_bank_account_token": external_bank_account_token,
                    "tier": tier,
                },
                credit_configuration_update_params.CreditConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialAccountCreditConfig,
        )


class AsyncCreditConfiguration(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditConfigurationWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditConfigurationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditConfigurationWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncCreditConfigurationWithStreamingResponse(self)

    async def retrieve(
        self,
        financial_account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialAccountCreditConfig:
        """
        Get an Account's credit configuration

        Args:
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
            f"/v1/financial_accounts/{financial_account_token}/credit_configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialAccountCreditConfig,
        )

    async def update(
        self,
        financial_account_token: str,
        *,
        credit_limit: int | NotGiven = NOT_GIVEN,
        credit_product_token: str | NotGiven = NOT_GIVEN,
        external_bank_account_token: str | NotGiven = NOT_GIVEN,
        tier: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialAccountCreditConfig:
        """
        Update an account's credit configuration

        Args:
          credit_product_token: Globally unique identifier for the credit product

          tier: Tier to assign to a financial account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        return await self._patch(
            f"/v1/financial_accounts/{financial_account_token}/credit_configuration",
            body=await async_maybe_transform(
                {
                    "credit_limit": credit_limit,
                    "credit_product_token": credit_product_token,
                    "external_bank_account_token": external_bank_account_token,
                    "tier": tier,
                },
                credit_configuration_update_params.CreditConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialAccountCreditConfig,
        )


class CreditConfigurationWithRawResponse:
    def __init__(self, credit_configuration: CreditConfiguration) -> None:
        self._credit_configuration = credit_configuration

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            credit_configuration.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            credit_configuration.update,
        )


class AsyncCreditConfigurationWithRawResponse:
    def __init__(self, credit_configuration: AsyncCreditConfiguration) -> None:
        self._credit_configuration = credit_configuration

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            credit_configuration.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            credit_configuration.update,
        )


class CreditConfigurationWithStreamingResponse:
    def __init__(self, credit_configuration: CreditConfiguration) -> None:
        self._credit_configuration = credit_configuration

        self.retrieve = to_streamed_response_wrapper(
            credit_configuration.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            credit_configuration.update,
        )


class AsyncCreditConfigurationWithStreamingResponse:
    def __init__(self, credit_configuration: AsyncCreditConfiguration) -> None:
        self._credit_configuration = credit_configuration

        self.retrieve = async_to_streamed_response_wrapper(
            credit_configuration.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            credit_configuration.update,
        )
