# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import balance_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncSinglePage, AsyncSinglePage
from .._base_client import AsyncPaginator, make_request_options
from ..types.balance import Balance

__all__ = ["Balances", "AsyncBalances"]


class Balances(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BalancesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return BalancesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BalancesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return BalancesWithStreamingResponse(self)

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        balance_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        financial_account_type: Literal["ISSUING", "OPERATING", "RESERVE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Balance]:
        """
        Get the balances for a program, business, or a given end-user account

        Args:
          account_token: List balances for all financial accounts of a given account_token.

          balance_date: UTC date and time of the balances to retrieve. Defaults to latest available
              balances

          business_account_token: List balances for all financial accounts of a given business_account_token.

          financial_account_type: List balances for a given Financial Account type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/balances",
            page=SyncSinglePage[Balance],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "balance_date": balance_date,
                        "business_account_token": business_account_token,
                        "financial_account_type": financial_account_type,
                    },
                    balance_list_params.BalanceListParams,
                ),
            ),
            model=Balance,
        )


class AsyncBalances(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBalancesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBalancesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBalancesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncBalancesWithStreamingResponse(self)

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        balance_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        financial_account_type: Literal["ISSUING", "OPERATING", "RESERVE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Balance, AsyncSinglePage[Balance]]:
        """
        Get the balances for a program, business, or a given end-user account

        Args:
          account_token: List balances for all financial accounts of a given account_token.

          balance_date: UTC date and time of the balances to retrieve. Defaults to latest available
              balances

          business_account_token: List balances for all financial accounts of a given business_account_token.

          financial_account_type: List balances for a given Financial Account type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/balances",
            page=AsyncSinglePage[Balance],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "balance_date": balance_date,
                        "business_account_token": business_account_token,
                        "financial_account_type": financial_account_type,
                    },
                    balance_list_params.BalanceListParams,
                ),
            ),
            model=Balance,
        )


class BalancesWithRawResponse:
    def __init__(self, balances: Balances) -> None:
        self._balances = balances

        self.list = _legacy_response.to_raw_response_wrapper(
            balances.list,
        )


class AsyncBalancesWithRawResponse:
    def __init__(self, balances: AsyncBalances) -> None:
        self._balances = balances

        self.list = _legacy_response.async_to_raw_response_wrapper(
            balances.list,
        )


class BalancesWithStreamingResponse:
    def __init__(self, balances: Balances) -> None:
        self._balances = balances

        self.list = to_streamed_response_wrapper(
            balances.list,
        )


class AsyncBalancesWithStreamingResponse:
    def __init__(self, balances: AsyncBalances) -> None:
        self._balances = balances

        self.list = async_to_streamed_response_wrapper(
            balances.list,
        )
