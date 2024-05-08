# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .decisioning import (
    DecisioningResource,
    AsyncDecisioningResource,
    DecisioningResourceWithRawResponse,
    AsyncDecisioningResourceWithRawResponse,
    DecisioningResourceWithStreamingResponse,
    AsyncDecisioningResourceWithStreamingResponse,
)
from .authentication import (
    AuthenticationResource,
    AsyncAuthenticationResource,
    AuthenticationResourceWithRawResponse,
    AsyncAuthenticationResourceWithRawResponse,
    AuthenticationResourceWithStreamingResponse,
    AsyncAuthenticationResourceWithStreamingResponse,
)

__all__ = ["ThreeDSResource", "AsyncThreeDSResource"]


class ThreeDSResource(SyncAPIResource):
    @cached_property
    def authentication(self) -> AuthenticationResource:
        return AuthenticationResource(self._client)

    @cached_property
    def decisioning(self) -> DecisioningResource:
        return DecisioningResource(self._client)

    @cached_property
    def with_raw_response(self) -> ThreeDSResourceWithRawResponse:
        return ThreeDSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ThreeDSResourceWithStreamingResponse:
        return ThreeDSResourceWithStreamingResponse(self)


class AsyncThreeDSResource(AsyncAPIResource):
    @cached_property
    def authentication(self) -> AsyncAuthenticationResource:
        return AsyncAuthenticationResource(self._client)

    @cached_property
    def decisioning(self) -> AsyncDecisioningResource:
        return AsyncDecisioningResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncThreeDSResourceWithRawResponse:
        return AsyncThreeDSResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncThreeDSResourceWithStreamingResponse:
        return AsyncThreeDSResourceWithStreamingResponse(self)


class ThreeDSResourceWithRawResponse:
    def __init__(self, three_ds: ThreeDSResource) -> None:
        self._three_ds = three_ds

    @cached_property
    def authentication(self) -> AuthenticationResourceWithRawResponse:
        return AuthenticationResourceWithRawResponse(self._three_ds.authentication)

    @cached_property
    def decisioning(self) -> DecisioningResourceWithRawResponse:
        return DecisioningResourceWithRawResponse(self._three_ds.decisioning)


class AsyncThreeDSResourceWithRawResponse:
    def __init__(self, three_ds: AsyncThreeDSResource) -> None:
        self._three_ds = three_ds

    @cached_property
    def authentication(self) -> AsyncAuthenticationResourceWithRawResponse:
        return AsyncAuthenticationResourceWithRawResponse(self._three_ds.authentication)

    @cached_property
    def decisioning(self) -> AsyncDecisioningResourceWithRawResponse:
        return AsyncDecisioningResourceWithRawResponse(self._three_ds.decisioning)


class ThreeDSResourceWithStreamingResponse:
    def __init__(self, three_ds: ThreeDSResource) -> None:
        self._three_ds = three_ds

    @cached_property
    def authentication(self) -> AuthenticationResourceWithStreamingResponse:
        return AuthenticationResourceWithStreamingResponse(self._three_ds.authentication)

    @cached_property
    def decisioning(self) -> DecisioningResourceWithStreamingResponse:
        return DecisioningResourceWithStreamingResponse(self._three_ds.decisioning)


class AsyncThreeDSResourceWithStreamingResponse:
    def __init__(self, three_ds: AsyncThreeDSResource) -> None:
        self._three_ds = three_ds

    @cached_property
    def authentication(self) -> AsyncAuthenticationResourceWithStreamingResponse:
        return AsyncAuthenticationResourceWithStreamingResponse(self._three_ds.authentication)

    @cached_property
    def decisioning(self) -> AsyncDecisioningResourceWithStreamingResponse:
        return AsyncDecisioningResourceWithStreamingResponse(self._three_ds.decisioning)
