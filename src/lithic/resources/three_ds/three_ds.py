# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return ThreeDSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ThreeDSWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncThreeDSWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncThreeDSWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncThreeDSWithStreamingResponse(self)


class ThreeDSWithRawResponse:
    def __init__(self, three_ds: ThreeDS) -> None:
        self._three_ds = three_ds

    @cached_property
    def authentication(self) -> AuthenticationWithRawResponse:
        return AuthenticationWithRawResponse(self._three_ds.authentication)

    @cached_property
    def decisioning(self) -> DecisioningWithRawResponse:
        return DecisioningWithRawResponse(self._three_ds.decisioning)


class AsyncThreeDSWithRawResponse:
    def __init__(self, three_ds: AsyncThreeDS) -> None:
        self._three_ds = three_ds

    @cached_property
    def authentication(self) -> AsyncAuthenticationWithRawResponse:
        return AsyncAuthenticationWithRawResponse(self._three_ds.authentication)

    @cached_property
    def decisioning(self) -> AsyncDecisioningWithRawResponse:
        return AsyncDecisioningWithRawResponse(self._three_ds.decisioning)


class ThreeDSWithStreamingResponse:
    def __init__(self, three_ds: ThreeDS) -> None:
        self._three_ds = three_ds

    @cached_property
    def authentication(self) -> AuthenticationWithStreamingResponse:
        return AuthenticationWithStreamingResponse(self._three_ds.authentication)

    @cached_property
    def decisioning(self) -> DecisioningWithStreamingResponse:
        return DecisioningWithStreamingResponse(self._three_ds.decisioning)


class AsyncThreeDSWithStreamingResponse:
    def __init__(self, three_ds: AsyncThreeDS) -> None:
        self._three_ds = three_ds

    @cached_property
    def authentication(self) -> AsyncAuthenticationWithStreamingResponse:
        return AsyncAuthenticationWithStreamingResponse(self._three_ds.authentication)

    @cached_property
    def decisioning(self) -> AsyncDecisioningWithStreamingResponse:
        return AsyncDecisioningWithStreamingResponse(self._three_ds.decisioning)
