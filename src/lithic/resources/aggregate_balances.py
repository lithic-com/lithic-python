# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import aggregate_balance_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncSinglePage, AsyncSinglePage
from .._base_client import AsyncPaginator, make_request_options
from ..types.aggregate_balance import AggregateBalance

__all__ = ["AggregateBalances", "AsyncAggregateBalances"]


class AggregateBalances(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AggregateBalancesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AggregateBalancesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AggregateBalancesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AggregateBalancesWithStreamingResponse(self)

    def list(
        self,
        *,
        financial_account_type: Literal["ISSUING", "OPERATING", "RESERVE", "SECURITY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[AggregateBalance]:
        """
        Get the aggregated balance across all end-user accounts by financial account
        type

        Args:
          financial_account_type: Get the aggregate balance for a given Financial Account type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/aggregate_balances",
            page=SyncSinglePage[AggregateBalance],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"financial_account_type": financial_account_type},
                    aggregate_balance_list_params.AggregateBalanceListParams,
                ),
            ),
            model=AggregateBalance,
        )


class AsyncAggregateBalances(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAggregateBalancesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAggregateBalancesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAggregateBalancesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncAggregateBalancesWithStreamingResponse(self)

    def list(
        self,
        *,
        financial_account_type: Literal["ISSUING", "OPERATING", "RESERVE", "SECURITY"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AggregateBalance, AsyncSinglePage[AggregateBalance]]:
        """
        Get the aggregated balance across all end-user accounts by financial account
        type

        Args:
          financial_account_type: Get the aggregate balance for a given Financial Account type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/aggregate_balances",
            page=AsyncSinglePage[AggregateBalance],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"financial_account_type": financial_account_type},
                    aggregate_balance_list_params.AggregateBalanceListParams,
                ),
            ),
            model=AggregateBalance,
        )


class AggregateBalancesWithRawResponse:
    def __init__(self, aggregate_balances: AggregateBalances) -> None:
        self._aggregate_balances = aggregate_balances

        self.list = _legacy_response.to_raw_response_wrapper(
            aggregate_balances.list,
        )


class AsyncAggregateBalancesWithRawResponse:
    def __init__(self, aggregate_balances: AsyncAggregateBalances) -> None:
        self._aggregate_balances = aggregate_balances

        self.list = _legacy_response.async_to_raw_response_wrapper(
            aggregate_balances.list,
        )


class AggregateBalancesWithStreamingResponse:
    def __init__(self, aggregate_balances: AggregateBalances) -> None:
        self._aggregate_balances = aggregate_balances

        self.list = to_streamed_response_wrapper(
            aggregate_balances.list,
        )


class AsyncAggregateBalancesWithStreamingResponse:
    def __init__(self, aggregate_balances: AsyncAggregateBalances) -> None:
        self._aggregate_balances = aggregate_balances

        self.list = async_to_streamed_response_wrapper(
            aggregate_balances.list,
        )
