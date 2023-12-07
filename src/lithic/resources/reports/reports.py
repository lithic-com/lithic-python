# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .settlement import (
    Settlement,
    AsyncSettlement,
    SettlementWithRawResponse,
    AsyncSettlementWithRawResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["Reports", "AsyncReports"]


class Reports(SyncAPIResource):
    settlement: Settlement
    with_raw_response: ReportsWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.settlement = Settlement(client)
        self.with_raw_response = ReportsWithRawResponse(self)


class AsyncReports(AsyncAPIResource):
    settlement: AsyncSettlement
    with_raw_response: AsyncReportsWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.settlement = AsyncSettlement(client)
        self.with_raw_response = AsyncReportsWithRawResponse(self)


class ReportsWithRawResponse:
    def __init__(self, reports: Reports) -> None:
        self.settlement = SettlementWithRawResponse(reports.settlement)


class AsyncReportsWithRawResponse:
    def __init__(self, reports: AsyncReports) -> None:
        self.settlement = AsyncSettlementWithRawResponse(reports.settlement)
