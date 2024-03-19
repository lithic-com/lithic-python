# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .settlement import (
    Settlement,
    AsyncSettlement,
    SettlementWithRawResponse,
    AsyncSettlementWithRawResponse,
    SettlementWithStreamingResponse,
    AsyncSettlementWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Reports", "AsyncReports"]


class Reports(SyncAPIResource):
    @cached_property
    def settlement(self) -> Settlement:
        return Settlement(self._client)

    @cached_property
    def with_raw_response(self) -> ReportsWithRawResponse:
        return ReportsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsWithStreamingResponse:
        return ReportsWithStreamingResponse(self)


class AsyncReports(AsyncAPIResource):
    @cached_property
    def settlement(self) -> AsyncSettlement:
        return AsyncSettlement(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportsWithRawResponse:
        return AsyncReportsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsWithStreamingResponse:
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
