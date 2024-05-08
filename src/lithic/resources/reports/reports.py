# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .settlement import (
    SettlementResource,
    AsyncSettlementResource,
    SettlementResourceWithRawResponse,
    AsyncSettlementResourceWithRawResponse,
    SettlementResourceWithStreamingResponse,
    AsyncSettlementResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ReportsResource", "AsyncReportsResource"]


class ReportsResource(SyncAPIResource):
    @cached_property
    def settlement(self) -> SettlementResource:
        return SettlementResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReportsResourceWithRawResponse:
        return ReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportsResourceWithStreamingResponse:
        return ReportsResourceWithStreamingResponse(self)


class AsyncReportsResource(AsyncAPIResource):
    @cached_property
    def settlement(self) -> AsyncSettlementResource:
        return AsyncSettlementResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportsResourceWithRawResponse:
        return AsyncReportsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportsResourceWithStreamingResponse:
        return AsyncReportsResourceWithStreamingResponse(self)


class ReportsResourceWithRawResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

    @cached_property
    def settlement(self) -> SettlementResourceWithRawResponse:
        return SettlementResourceWithRawResponse(self._reports.settlement)


class AsyncReportsResourceWithRawResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

    @cached_property
    def settlement(self) -> AsyncSettlementResourceWithRawResponse:
        return AsyncSettlementResourceWithRawResponse(self._reports.settlement)


class ReportsResourceWithStreamingResponse:
    def __init__(self, reports: ReportsResource) -> None:
        self._reports = reports

    @cached_property
    def settlement(self) -> SettlementResourceWithStreamingResponse:
        return SettlementResourceWithStreamingResponse(self._reports.settlement)


class AsyncReportsResourceWithStreamingResponse:
    def __init__(self, reports: AsyncReportsResource) -> None:
        self._reports = reports

    @cached_property
    def settlement(self) -> AsyncSettlementResourceWithStreamingResponse:
        return AsyncSettlementResourceWithStreamingResponse(self._reports.settlement)
