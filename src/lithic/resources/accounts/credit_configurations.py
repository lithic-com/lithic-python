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
from ..._base_client import (
    make_request_options,
)
from ...types.accounts import credit_configuration_update_params
from ...types.business_account import BusinessAccount

__all__ = ["CreditConfigurationsResource", "AsyncCreditConfigurationsResource"]


class CreditConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditConfigurationsResourceWithRawResponse:
        return CreditConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditConfigurationsResourceWithStreamingResponse:
        return CreditConfigurationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BusinessAccount:
        """
        Get an Account's credit configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return self._get(
            f"/accounts/{account_token}/credit_configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusinessAccount,
        )

    def update(
        self,
        account_token: str,
        *,
        billing_period: int | NotGiven = NOT_GIVEN,
        credit_limit: int | NotGiven = NOT_GIVEN,
        external_bank_account_token: str | NotGiven = NOT_GIVEN,
        payment_period: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BusinessAccount:
        """
        Update a Business Accounts credit configuration

        Args:
          billing_period: Number of days within the billing period

          credit_limit: Credit limit extended to the Business Account

          external_bank_account_token: The external bank account token to use for auto-collections

          payment_period: Number of days after the billing period ends that a payment is required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return self._patch(
            f"/accounts/{account_token}/credit_configuration",
            body=maybe_transform(
                {
                    "billing_period": billing_period,
                    "credit_limit": credit_limit,
                    "external_bank_account_token": external_bank_account_token,
                    "payment_period": payment_period,
                },
                credit_configuration_update_params.CreditConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusinessAccount,
        )


class AsyncCreditConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditConfigurationsResourceWithRawResponse:
        return AsyncCreditConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditConfigurationsResourceWithStreamingResponse:
        return AsyncCreditConfigurationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BusinessAccount:
        """
        Get an Account's credit configuration

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return await self._get(
            f"/accounts/{account_token}/credit_configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusinessAccount,
        )

    async def update(
        self,
        account_token: str,
        *,
        billing_period: int | NotGiven = NOT_GIVEN,
        credit_limit: int | NotGiven = NOT_GIVEN,
        external_bank_account_token: str | NotGiven = NOT_GIVEN,
        payment_period: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BusinessAccount:
        """
        Update a Business Accounts credit configuration

        Args:
          billing_period: Number of days within the billing period

          credit_limit: Credit limit extended to the Business Account

          external_bank_account_token: The external bank account token to use for auto-collections

          payment_period: Number of days after the billing period ends that a payment is required

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_token:
            raise ValueError(f"Expected a non-empty value for `account_token` but received {account_token!r}")
        return await self._patch(
            f"/accounts/{account_token}/credit_configuration",
            body=await async_maybe_transform(
                {
                    "billing_period": billing_period,
                    "credit_limit": credit_limit,
                    "external_bank_account_token": external_bank_account_token,
                    "payment_period": payment_period,
                },
                credit_configuration_update_params.CreditConfigurationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BusinessAccount,
        )


class CreditConfigurationsResourceWithRawResponse:
    def __init__(self, credit_configurations: CreditConfigurationsResource) -> None:
        self._credit_configurations = credit_configurations

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            credit_configurations.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            credit_configurations.update,
        )


class AsyncCreditConfigurationsResourceWithRawResponse:
    def __init__(self, credit_configurations: AsyncCreditConfigurationsResource) -> None:
        self._credit_configurations = credit_configurations

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            credit_configurations.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            credit_configurations.update,
        )


class CreditConfigurationsResourceWithStreamingResponse:
    def __init__(self, credit_configurations: CreditConfigurationsResource) -> None:
        self._credit_configurations = credit_configurations

        self.retrieve = to_streamed_response_wrapper(
            credit_configurations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            credit_configurations.update,
        )


class AsyncCreditConfigurationsResourceWithStreamingResponse:
    def __init__(self, credit_configurations: AsyncCreditConfigurationsResource) -> None:
        self._credit_configurations = credit_configurations

        self.retrieve = async_to_streamed_response_wrapper(
            credit_configurations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            credit_configurations.update,
        )
