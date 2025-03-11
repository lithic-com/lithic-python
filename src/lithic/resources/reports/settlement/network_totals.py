# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from .... import _legacy_response
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.reports.settlement import network_total_list_params
from ....types.reports.settlement.network_total_list_response import NetworkTotalListResponse
from ....types.reports.settlement.network_total_retrieve_response import NetworkTotalRetrieveResponse

__all__ = ["NetworkTotals", "AsyncNetworkTotals"]


class NetworkTotals(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NetworkTotalsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return NetworkTotalsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NetworkTotalsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return NetworkTotalsWithStreamingResponse(self)

    def retrieve(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkTotalRetrieveResponse:
        """Retrieve a specific network total record by token.

        Not available in sandbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return self._get(
            f"/v1/reports/settlement/network_totals/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkTotalRetrieveResponse,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        institution_id: str | NotGiven = NOT_GIVEN,
        network: Literal["VISA", "MASTERCARD", "MAESTRO", "INTERLINK"] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        report_date: Union[str, date] | NotGiven = NOT_GIVEN,
        report_date_begin: Union[str, date] | NotGiven = NOT_GIVEN,
        report_date_end: Union[str, date] | NotGiven = NOT_GIVEN,
        settlement_institution_id: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[NetworkTotalListResponse]:
        """List network total records with optional filters.

        Not available in sandbox.

        Args:
          begin: Datetime in RFC 3339 format. Only entries created after the specified time will
              be included. UTC time zone.

          end: Datetime in RFC 3339 format. Only entries created before the specified time will
              be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          institution_id: Institution ID to filter on.

          network: Network to filter on.

          page_size: Number of records per page.

          report_date: Singular report date to filter on (YYYY-MM-DD). Cannot be populated in
              conjunction with report_date_begin or report_date_end.

          report_date_begin: Earliest report date to filter on, inclusive (YYYY-MM-DD).

          report_date_end: Latest report date to filter on, inclusive (YYYY-MM-DD).

          settlement_institution_id: Settlement institution ID to filter on.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/reports/settlement/network_totals",
            page=SyncCursorPage[NetworkTotalListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "institution_id": institution_id,
                        "network": network,
                        "page_size": page_size,
                        "report_date": report_date,
                        "report_date_begin": report_date_begin,
                        "report_date_end": report_date_end,
                        "settlement_institution_id": settlement_institution_id,
                        "starting_after": starting_after,
                    },
                    network_total_list_params.NetworkTotalListParams,
                ),
            ),
            model=NetworkTotalListResponse,
        )


class AsyncNetworkTotals(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNetworkTotalsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNetworkTotalsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNetworkTotalsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncNetworkTotalsWithStreamingResponse(self)

    async def retrieve(
        self,
        token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NetworkTotalRetrieveResponse:
        """Retrieve a specific network total record by token.

        Not available in sandbox.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not token:
            raise ValueError(f"Expected a non-empty value for `token` but received {token!r}")
        return await self._get(
            f"/v1/reports/settlement/network_totals/{token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NetworkTotalRetrieveResponse,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        institution_id: str | NotGiven = NOT_GIVEN,
        network: Literal["VISA", "MASTERCARD", "MAESTRO", "INTERLINK"] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        report_date: Union[str, date] | NotGiven = NOT_GIVEN,
        report_date_begin: Union[str, date] | NotGiven = NOT_GIVEN,
        report_date_end: Union[str, date] | NotGiven = NOT_GIVEN,
        settlement_institution_id: str | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[NetworkTotalListResponse, AsyncCursorPage[NetworkTotalListResponse]]:
        """List network total records with optional filters.

        Not available in sandbox.

        Args:
          begin: Datetime in RFC 3339 format. Only entries created after the specified time will
              be included. UTC time zone.

          end: Datetime in RFC 3339 format. Only entries created before the specified time will
              be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          institution_id: Institution ID to filter on.

          network: Network to filter on.

          page_size: Number of records per page.

          report_date: Singular report date to filter on (YYYY-MM-DD). Cannot be populated in
              conjunction with report_date_begin or report_date_end.

          report_date_begin: Earliest report date to filter on, inclusive (YYYY-MM-DD).

          report_date_end: Latest report date to filter on, inclusive (YYYY-MM-DD).

          settlement_institution_id: Settlement institution ID to filter on.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/reports/settlement/network_totals",
            page=AsyncCursorPage[NetworkTotalListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "institution_id": institution_id,
                        "network": network,
                        "page_size": page_size,
                        "report_date": report_date,
                        "report_date_begin": report_date_begin,
                        "report_date_end": report_date_end,
                        "settlement_institution_id": settlement_institution_id,
                        "starting_after": starting_after,
                    },
                    network_total_list_params.NetworkTotalListParams,
                ),
            ),
            model=NetworkTotalListResponse,
        )


class NetworkTotalsWithRawResponse:
    def __init__(self, network_totals: NetworkTotals) -> None:
        self._network_totals = network_totals

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            network_totals.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            network_totals.list,
        )


class AsyncNetworkTotalsWithRawResponse:
    def __init__(self, network_totals: AsyncNetworkTotals) -> None:
        self._network_totals = network_totals

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            network_totals.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            network_totals.list,
        )


class NetworkTotalsWithStreamingResponse:
    def __init__(self, network_totals: NetworkTotals) -> None:
        self._network_totals = network_totals

        self.retrieve = to_streamed_response_wrapper(
            network_totals.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            network_totals.list,
        )


class AsyncNetworkTotalsWithStreamingResponse:
    def __init__(self, network_totals: AsyncNetworkTotals) -> None:
        self._network_totals = network_totals

        self.retrieve = async_to_streamed_response_wrapper(
            network_totals.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            network_totals.list,
        )
