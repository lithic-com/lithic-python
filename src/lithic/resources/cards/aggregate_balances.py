# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ...types.cards import AggregateBalanceListResponse, aggregate_balance_list_params
from ..._base_client import AsyncPaginator, make_request_options

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["AggregateBalances", "AsyncAggregateBalances"]


class AggregateBalances(SyncAPIResource):
    with_raw_response: AggregateBalancesWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = AggregateBalancesWithRawResponse(self)

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
    with_raw_response: AsyncAggregateBalancesWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncAggregateBalancesWithRawResponse(self)

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
        self.list = to_raw_response_wrapper(
            aggregate_balances.list,
        )


class AsyncAggregateBalancesWithRawResponse:
    def __init__(self, aggregate_balances: AsyncAggregateBalances) -> None:
        self.list = async_to_raw_response_wrapper(
            aggregate_balances.list,
        )
