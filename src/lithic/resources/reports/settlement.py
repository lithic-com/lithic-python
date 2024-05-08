# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ...types.reports import settlement_list_details_params
from ...types.settlement_detail import SettlementDetail
from ...types.settlement_report import SettlementReport

__all__ = ["SettlementResource", "AsyncSettlementResource"]


class SettlementResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SettlementResourceWithRawResponse:
        return SettlementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettlementResourceWithStreamingResponse:
        return SettlementResourceWithStreamingResponse(self)

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
            f"/reports/settlement/details/{report_date}",
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
        """
        Get the settlement report for a specified report date.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_date:
            raise ValueError(f"Expected a non-empty value for `report_date` but received {report_date!r}")
        return self._get(
            f"/reports/settlement/summary/{report_date}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettlementReport,
        )


class AsyncSettlementResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSettlementResourceWithRawResponse:
        return AsyncSettlementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettlementResourceWithStreamingResponse:
        return AsyncSettlementResourceWithStreamingResponse(self)

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
            f"/reports/settlement/details/{report_date}",
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
        """
        Get the settlement report for a specified report date.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_date:
            raise ValueError(f"Expected a non-empty value for `report_date` but received {report_date!r}")
        return await self._get(
            f"/reports/settlement/summary/{report_date}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SettlementReport,
        )


class SettlementResourceWithRawResponse:
    def __init__(self, settlement: SettlementResource) -> None:
        self._settlement = settlement

        self.list_details = _legacy_response.to_raw_response_wrapper(
            settlement.list_details,
        )
        self.summary = _legacy_response.to_raw_response_wrapper(
            settlement.summary,
        )


class AsyncSettlementResourceWithRawResponse:
    def __init__(self, settlement: AsyncSettlementResource) -> None:
        self._settlement = settlement

        self.list_details = _legacy_response.async_to_raw_response_wrapper(
            settlement.list_details,
        )
        self.summary = _legacy_response.async_to_raw_response_wrapper(
            settlement.summary,
        )


class SettlementResourceWithStreamingResponse:
    def __init__(self, settlement: SettlementResource) -> None:
        self._settlement = settlement

        self.list_details = to_streamed_response_wrapper(
            settlement.list_details,
        )
        self.summary = to_streamed_response_wrapper(
            settlement.summary,
        )


class AsyncSettlementResourceWithStreamingResponse:
    def __init__(self, settlement: AsyncSettlementResource) -> None:
        self._settlement = settlement

        self.list_details = async_to_streamed_response_wrapper(
            settlement.list_details,
        )
        self.summary = async_to_streamed_response_wrapper(
            settlement.summary,
        )
