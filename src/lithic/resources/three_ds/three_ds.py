# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from ..._resource import SyncAPIResource, AsyncAPIResource
from .decisioning import (
    Decisioning,
    AsyncDecisioning,
    DecisioningWithRawResponse,
    AsyncDecisioningWithRawResponse,
)
from .authentication import (
    Authentication,
    AsyncAuthentication,
    AuthenticationWithRawResponse,
    AsyncAuthenticationWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["ThreeDS", "AsyncThreeDS"]


class ThreeDS(SyncAPIResource):
    authentication: Authentication
    decisioning: Decisioning
    with_raw_response: ThreeDSWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.authentication = Authentication(client)
        self.decisioning = Decisioning(client)
        self.with_raw_response = ThreeDSWithRawResponse(self)


class AsyncThreeDS(AsyncAPIResource):
    authentication: AsyncAuthentication
    decisioning: AsyncDecisioning
    with_raw_response: AsyncThreeDSWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.authentication = AsyncAuthentication(client)
        self.decisioning = AsyncDecisioning(client)
        self.with_raw_response = AsyncThreeDSWithRawResponse(self)


class ThreeDSWithRawResponse:
    def __init__(self, three_ds: ThreeDS) -> None:
        self.authentication = AuthenticationWithRawResponse(three_ds.authentication)
        self.decisioning = DecisioningWithRawResponse(three_ds.decisioning)


class AsyncThreeDSWithRawResponse:
    def __init__(self, three_ds: AsyncThreeDS) -> None:
        self.authentication = AsyncAuthenticationWithRawResponse(three_ds.authentication)
        self.decisioning = AsyncDecisioningWithRawResponse(three_ds.decisioning)
