# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .decisioning import Decisioning, AsyncDecisioning, DecisioningWithRawResponse, AsyncDecisioningWithRawResponse
from .authentication import (
    Authentication,
    AsyncAuthentication,
    AuthenticationWithRawResponse,
    AsyncAuthenticationWithRawResponse,
)

__all__ = ["ThreeDS", "AsyncThreeDS"]


class ThreeDS(SyncAPIResource):
    @cached_property
    def authentication(self) -> Authentication:
        return Authentication(self._client)

    @cached_property
    def decisioning(self) -> Decisioning:
        return Decisioning(self._client)

    @cached_property
    def with_raw_response(self) -> ThreeDSWithRawResponse:
        return ThreeDSWithRawResponse(self)


class AsyncThreeDS(AsyncAPIResource):
    @cached_property
    def authentication(self) -> AsyncAuthentication:
        return AsyncAuthentication(self._client)

    @cached_property
    def decisioning(self) -> AsyncDecisioning:
        return AsyncDecisioning(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncThreeDSWithRawResponse:
        return AsyncThreeDSWithRawResponse(self)


class ThreeDSWithRawResponse:
    def __init__(self, three_ds: ThreeDS) -> None:
        self.authentication = AuthenticationWithRawResponse(three_ds.authentication)
        self.decisioning = DecisioningWithRawResponse(three_ds.decisioning)


class AsyncThreeDSWithRawResponse:
    def __init__(self, three_ds: AsyncThreeDS) -> None:
        self.authentication = AsyncAuthenticationWithRawResponse(three_ds.authentication)
        self.decisioning = AsyncDecisioningWithRawResponse(three_ds.decisioning)
