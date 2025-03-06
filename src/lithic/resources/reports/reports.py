# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .settlement.settlement import (
    Settlement,
    AsyncSettlement,
    SettlementWithRawResponse,
    AsyncSettlementWithRawResponse,
    SettlementWithStreamingResponse,
    AsyncSettlementWithStreamingResponse,
)

__all__ = ["Reports", "AsyncReports"]


class Reports(SyncAPIResource):
    @cached_property
    def settlement(self) -> Settlement:
        return Settlement(self._client)

    @cached_property
    def with_raw_response(self) -> ReportsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return ReportsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return ReportsWithStreamingResponse(self)


class AsyncReports(AsyncAPIResource):
    @cached_property
    def settlement(self) -> AsyncSettlement:
        return AsyncSettlement(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReportsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncReportsWithStreamingResponse(self)


class ReportsWithRawResponse:
    def __init__(self, reports: Reports) -> None:
        self._reports = reports

    @cached_property
    def settlement(self) -> SettlementWithRawResponse:
        return SettlementWithRawResponse(self._reports.settlement)


class AsyncReportsWithRawResponse:
    def __init__(self, reports: AsyncReports) -> None:
        self._reports = reports

    @cached_property
    def settlement(self) -> AsyncSettlementWithRawResponse:
        return AsyncSettlementWithRawResponse(self._reports.settlement)


class ReportsWithStreamingResponse:
    def __init__(self, reports: Reports) -> None:
        self._reports = reports

    @cached_property
    def settlement(self) -> SettlementWithStreamingResponse:
        return SettlementWithStreamingResponse(self._reports.settlement)


class AsyncReportsWithStreamingResponse:
    def __init__(self, reports: AsyncReports) -> None:
        self._reports = reports

    @cached_property
    def settlement(self) -> AsyncSettlementWithStreamingResponse:
        return AsyncSettlementWithStreamingResponse(self._reports.settlement)
