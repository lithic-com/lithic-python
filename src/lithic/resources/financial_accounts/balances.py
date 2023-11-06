# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from datetime import datetime

import httpx

from ...types import Balance
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.financial_accounts import balance_list_params

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["Balances", "AsyncBalances"]


class Balances(SyncAPIResource):
    with_raw_response: BalancesWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = BalancesWithRawResponse(self)

    def list(
        self,
        financial_account_token: str,
        *,
        balance_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_transaction_event_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[Balance]:
        """
        Get the balances for a given financial account.

        Args:
          balance_date: UTC date of the balance to retrieve. Defaults to latest available balance

          last_transaction_event_token: Balance after a given financial event occured. For example, passing the
              event_token of a $5 CARD_CLEARING financial event will return a balance
              decreased by $5

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/financial_accounts/{financial_account_token}/balances",
            page=SyncSinglePage[Balance],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "balance_date": balance_date,
                        "last_transaction_event_token": last_transaction_event_token,
                    },
                    balance_list_params.BalanceListParams,
                ),
            ),
            model=Balance,
        )


class AsyncBalances(AsyncAPIResource):
    with_raw_response: AsyncBalancesWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncBalancesWithRawResponse(self)

    def list(
        self,
        financial_account_token: str,
        *,
        balance_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_transaction_event_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Balance, AsyncSinglePage[Balance]]:
        """
        Get the balances for a given financial account.

        Args:
          balance_date: UTC date of the balance to retrieve. Defaults to latest available balance

          last_transaction_event_token: Balance after a given financial event occured. For example, passing the
              event_token of a $5 CARD_CLEARING financial event will return a balance
              decreased by $5

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            f"/financial_accounts/{financial_account_token}/balances",
            page=AsyncSinglePage[Balance],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "balance_date": balance_date,
                        "last_transaction_event_token": last_transaction_event_token,
                    },
                    balance_list_params.BalanceListParams,
                ),
            ),
            model=Balance,
        )


class BalancesWithRawResponse:
    def __init__(self, balances: Balances) -> None:
        self.list = to_raw_response_wrapper(
            balances.list,
        )


class AsyncBalancesWithRawResponse:
    def __init__(self, balances: AsyncBalances) -> None:
        self.list = async_to_raw_response_wrapper(
            balances.list,
        )
