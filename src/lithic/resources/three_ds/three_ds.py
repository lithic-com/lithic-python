# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ..._resource import SyncAPIResource, AsyncAPIResource
from .descisioning import Descisioning, AsyncDescisioning
from .authentication import Authentication, AsyncAuthentication

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["ThreeDS", "AsyncThreeDS"]


class ThreeDS(SyncAPIResource):
    authentication: Authentication
    descisioning: Descisioning

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.authentication = Authentication(client)
        self.descisioning = Descisioning(client)


class AsyncThreeDS(AsyncAPIResource):
    authentication: AsyncAuthentication
    descisioning: AsyncDescisioning

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.authentication = AsyncAuthentication(client)
        self.descisioning = AsyncDescisioning(client)
