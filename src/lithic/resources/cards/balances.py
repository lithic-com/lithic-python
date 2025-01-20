# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ...types.cards import balance_list_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.cards.balance_list_response import BalanceListResponse

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
        card_token: str,
        *,
        balance_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_transaction_event_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[BalanceListResponse]:
        """
        Get the balances for a given card.

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
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._get_api_list(
            f"/v1/cards/{card_token}/balances",
            page=SyncSinglePage[BalanceListResponse],
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
            model=BalanceListResponse,
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
        card_token: str,
        *,
        balance_date: Union[str, datetime] | NotGiven = NOT_GIVEN,
        last_transaction_event_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[BalanceListResponse, AsyncSinglePage[BalanceListResponse]]:
        """
        Get the balances for a given card.

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
        if not card_token:
            raise ValueError(f"Expected a non-empty value for `card_token` but received {card_token!r}")
        return self._get_api_list(
            f"/v1/cards/{card_token}/balances",
            page=AsyncSinglePage[BalanceListResponse],
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
            model=BalanceListResponse,
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
