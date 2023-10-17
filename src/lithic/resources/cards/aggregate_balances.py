# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncSinglePage, AsyncSinglePage
from ...types.cards import AggregateBalanceListResponse, aggregate_balance_list_params
from ..._base_client import AsyncPaginator, make_request_options

__all__ = ["AggregateBalances", "AsyncAggregateBalances"]


class AggregateBalances(SyncAPIResource):
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
