# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .decisioning import (
    Decisioning,
    AsyncDecisioning,
    DecisioningWithRawResponse,
    AsyncDecisioningWithRawResponse,
    DecisioningWithStreamingResponse,
    AsyncDecisioningWithStreamingResponse,
)
from .authentication import (
    Authentication,
    AsyncAuthentication,
    AuthenticationWithRawResponse,
    AsyncAuthenticationWithRawResponse,
    AuthenticationWithStreamingResponse,
    AsyncAuthenticationWithStreamingResponse,
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

    @cached_property
    def with_streaming_response(self) -> ThreeDSWithStreamingResponse:
        return ThreeDSWithStreamingResponse(self)


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

    @cached_property
    def with_streaming_response(self) -> AsyncThreeDSWithStreamingResponse:
        return AsyncThreeDSWithStreamingResponse(self)


class ThreeDSWithRawResponse:
    def __init__(self, three_ds: ThreeDS) -> None:
        self.authentication = AuthenticationWithRawResponse(three_ds.authentication)
        self.decisioning = DecisioningWithRawResponse(three_ds.decisioning)


class AsyncThreeDSWithRawResponse:
    def __init__(self, three_ds: AsyncThreeDS) -> None:
        self.authentication = AsyncAuthenticationWithRawResponse(three_ds.authentication)
        self.decisioning = AsyncDecisioningWithRawResponse(three_ds.decisioning)


class ThreeDSWithStreamingResponse:
    def __init__(self, three_ds: ThreeDS) -> None:
        self.authentication = AuthenticationWithStreamingResponse(three_ds.authentication)
        self.decisioning = DecisioningWithStreamingResponse(three_ds.decisioning)


class AsyncThreeDSWithStreamingResponse:
    def __init__(self, three_ds: AsyncThreeDS) -> None:
        self.authentication = AsyncAuthenticationWithStreamingResponse(three_ds.authentication)
        self.decisioning = AsyncDecisioningWithStreamingResponse(three_ds.decisioning)
