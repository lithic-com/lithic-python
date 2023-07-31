# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ..._resource import SyncAPIResource, AsyncAPIResource
from .decisioning import Decisioning, AsyncDecisioning
from .authentication import Authentication, AsyncAuthentication

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["ThreeDS", "AsyncThreeDS"]


class ThreeDS(SyncAPIResource):
    authentication: Authentication
    decisioning: Decisioning

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.authentication = Authentication(client)
        self.decisioning = Decisioning(client)


class AsyncThreeDS(AsyncAPIResource):
    authentication: AsyncAuthentication
    decisioning: AsyncDecisioning

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.authentication = AsyncAuthentication(client)
        self.decisioning = AsyncDecisioning(client)
