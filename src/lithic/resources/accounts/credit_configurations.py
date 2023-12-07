# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ...types import BusinessAccount
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.accounts import credit_configuration_update_params

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["CreditConfigurations", "AsyncCreditConfigurations"]


class CreditConfigurations(SyncAPIResource):
    with_raw_response: CreditConfigurationsWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = CreditConfigurationsWithRawResponse(self)

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
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BusinessAccount,
        )


class AsyncCreditConfigurations(AsyncAPIResource):
    with_raw_response: AsyncCreditConfigurationsWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncCreditConfigurationsWithRawResponse(self)

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
        idempotency_key: str | None = None,
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

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=BusinessAccount,
        )


class CreditConfigurationsWithRawResponse:
    def __init__(self, credit_configurations: CreditConfigurations) -> None:
        self.retrieve = to_raw_response_wrapper(
            credit_configurations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            credit_configurations.update,
        )


class AsyncCreditConfigurationsWithRawResponse:
    def __init__(self, credit_configurations: AsyncCreditConfigurations) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            credit_configurations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            credit_configurations.update,
        )
