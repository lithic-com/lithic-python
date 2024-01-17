# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ...types.cards import AggregateBalanceListResponse, aggregate_balance_list_params
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["AggregateBalances", "AsyncAggregateBalances"]


class AggregateBalances(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AggregateBalancesWithRawResponse:
        return AggregateBalancesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AggregateBalancesWithStreamingResponse:
        return AggregateBalancesWithStreamingResponse(self)

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[AggregateBalanceListResponse]:
        """
        Get the aggregated card balance across all end-user accounts.

        Args:
          account_token: Cardholder to retrieve aggregate balances for.

          business_account_token: Business to retrieve aggregate balances for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cards/aggregate_balances",
            page=SyncSinglePage[AggregateBalanceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "business_account_token": business_account_token,
                    },
                    aggregate_balance_list_params.AggregateBalanceListParams,
                ),
            ),
            model=AggregateBalanceListResponse,
        )


class AsyncAggregateBalances(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAggregateBalancesWithRawResponse:
        return AsyncAggregateBalancesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAggregateBalancesWithStreamingResponse:
        return AsyncAggregateBalancesWithStreamingResponse(self)

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[AggregateBalanceListResponse, AsyncSinglePage[AggregateBalanceListResponse]]:
        """
        Get the aggregated card balance across all end-user accounts.

        Args:
          account_token: Cardholder to retrieve aggregate balances for.

          business_account_token: Business to retrieve aggregate balances for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/cards/aggregate_balances",
            page=AsyncSinglePage[AggregateBalanceListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "business_account_token": business_account_token,
                    },
                    aggregate_balance_list_params.AggregateBalanceListParams,
                ),
            ),
            model=AggregateBalanceListResponse,
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
