# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from .... import _legacy_response
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncCursorPage, AsyncCursorPage
from .network_totals import (
    NetworkTotals,
    AsyncNetworkTotals,
    NetworkTotalsWithRawResponse,
    AsyncNetworkTotalsWithRawResponse,
    NetworkTotalsWithStreamingResponse,
    AsyncNetworkTotalsWithStreamingResponse,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.reports import settlement_list_details_params
from ....types.settlement_detail import SettlementDetail
from ....types.settlement_report import SettlementReport

__all__ = ["Settlement", "AsyncSettlement"]


class Settlement(SyncAPIResource):
    @cached_property
    def network_totals(self) -> NetworkTotals:
        return NetworkTotals(self._client)

    @cached_property
    def with_raw_response(self) -> SettlementWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return SettlementWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettlementWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return SettlementWithStreamingResponse(self)

    def list_details(
        self,
        report_date: Union[str, date],
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[SettlementDetail]:
        """
        List details.

        Args:
          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_date:
            raise ValueError(f"Expected a non-empty value for `report_date` but received {report_date!r}")
        return self._get_api_list(
            f"/v1/reports/settlement/details/{report_date}",
            page=SyncCursorPage[SettlementDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    settlement_list_details_params.SettlementListDetailsParams,
                ),
            ),
            model=SettlementDetail,
        )

    def summary(
        self,
        report_date: Union[str, date],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettlementReport:
        """Get the settlement report for a specified report date.

        Not available in sandbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_date:
            raise ValueError(f"Expected a non-empty value for `report_date` but received {report_date!r}")
        return self._get(
            f"/v1/reports/settlement/summary/{report_date}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettlementReport,
        )


class AsyncSettlement(AsyncAPIResource):
    @cached_property
    def network_totals(self) -> AsyncNetworkTotals:
        return AsyncNetworkTotals(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettlementWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSettlementWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettlementWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncSettlementWithStreamingResponse(self)

    def list_details(
        self,
        report_date: Union[str, date],
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[SettlementDetail, AsyncCursorPage[SettlementDetail]]:
        """
        List details.

        Args:
          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_date:
            raise ValueError(f"Expected a non-empty value for `report_date` but received {report_date!r}")
        return self._get_api_list(
            f"/v1/reports/settlement/details/{report_date}",
            page=AsyncCursorPage[SettlementDetail],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    settlement_list_details_params.SettlementListDetailsParams,
                ),
            ),
            model=SettlementDetail,
        )

    async def summary(
        self,
        report_date: Union[str, date],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SettlementReport:
        """Get the settlement report for a specified report date.

        Not available in sandbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_date:
            raise ValueError(f"Expected a non-empty value for `report_date` but received {report_date!r}")
        return await self._get(
            f"/v1/reports/settlement/summary/{report_date}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettlementReport,
        )


class SettlementWithRawResponse:
    def __init__(self, settlement: Settlement) -> None:
        self._settlement = settlement

        self.list_details = _legacy_response.to_raw_response_wrapper(
            settlement.list_details,
        )
        self.summary = _legacy_response.to_raw_response_wrapper(
            settlement.summary,
        )

    @cached_property
    def network_totals(self) -> NetworkTotalsWithRawResponse:
        return NetworkTotalsWithRawResponse(self._settlement.network_totals)


class AsyncSettlementWithRawResponse:
    def __init__(self, settlement: AsyncSettlement) -> None:
        self._settlement = settlement

        self.list_details = _legacy_response.async_to_raw_response_wrapper(
            settlement.list_details,
        )
        self.summary = _legacy_response.async_to_raw_response_wrapper(
            settlement.summary,
        )

    @cached_property
    def network_totals(self) -> AsyncNetworkTotalsWithRawResponse:
        return AsyncNetworkTotalsWithRawResponse(self._settlement.network_totals)


class SettlementWithStreamingResponse:
    def __init__(self, settlement: Settlement) -> None:
        self._settlement = settlement

        self.list_details = to_streamed_response_wrapper(
            settlement.list_details,
        )
        self.summary = to_streamed_response_wrapper(
            settlement.summary,
        )

    @cached_property
    def network_totals(self) -> NetworkTotalsWithStreamingResponse:
        return NetworkTotalsWithStreamingResponse(self._settlement.network_totals)


class AsyncSettlementWithStreamingResponse:
    def __init__(self, settlement: AsyncSettlement) -> None:
        self._settlement = settlement

        self.list_details = async_to_streamed_response_wrapper(
            settlement.list_details,
        )
        self.summary = async_to_streamed_response_wrapper(
            settlement.summary,
        )

    @cached_property
    def network_totals(self) -> AsyncNetworkTotalsWithStreamingResponse:
        return AsyncNetworkTotalsWithStreamingResponse(self._settlement.network_totals)
