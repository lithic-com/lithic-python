# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .settlement import Settlement, AsyncSettlement
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["Reports", "AsyncReports"]


class Reports(SyncAPIResource):
    settlement: Settlement

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.settlement = Settlement(client)


class AsyncReports(AsyncAPIResource):
    settlement: AsyncSettlement

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.settlement = AsyncSettlement(client)
