# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._compat import cached_property
from .settlement import Settlement, AsyncSettlement, SettlementWithRawResponse, AsyncSettlementWithRawResponse
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["Reports", "AsyncReports"]


class Reports(SyncAPIResource):
    @cached_property
    def settlement(self) -> Settlement:
        return Settlement(self._client)

    @cached_property
    def with_raw_response(self) -> ReportsWithRawResponse:
        return ReportsWithRawResponse(self)


class AsyncReports(AsyncAPIResource):
    @cached_property
    def settlement(self) -> AsyncSettlement:
        return AsyncSettlement(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReportsWithRawResponse:
        return AsyncReportsWithRawResponse(self)


class ReportsWithRawResponse:
    def __init__(self, reports: Reports) -> None:
        self.settlement = SettlementWithRawResponse(reports.settlement)


class AsyncReportsWithRawResponse:
    def __init__(self, reports: AsyncReports) -> None:
        self.settlement = AsyncSettlementWithRawResponse(reports.settlement)
