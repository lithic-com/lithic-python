# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .v2.v2 import (
    V2,
    AsyncV2,
    V2WithRawResponse,
    AsyncV2WithRawResponse,
    V2WithStreamingResponse,
    AsyncV2WithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["AuthRules", "AsyncAuthRules"]


class AuthRules(SyncAPIResource):
    @cached_property
    def v2(self) -> V2:
        return V2(self._client)

    @cached_property
    def with_raw_response(self) -> AuthRulesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AuthRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthRulesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AuthRulesWithStreamingResponse(self)


class AsyncAuthRules(AsyncAPIResource):
    @cached_property
    def v2(self) -> AsyncV2:
        return AsyncV2(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthRulesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthRulesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncAuthRulesWithStreamingResponse(self)


class AuthRulesWithRawResponse:
    def __init__(self, auth_rules: AuthRules) -> None:
        self._auth_rules = auth_rules

    @cached_property
    def v2(self) -> V2WithRawResponse:
        return V2WithRawResponse(self._auth_rules.v2)


class AsyncAuthRulesWithRawResponse:
    def __init__(self, auth_rules: AsyncAuthRules) -> None:
        self._auth_rules = auth_rules

    @cached_property
    def v2(self) -> AsyncV2WithRawResponse:
        return AsyncV2WithRawResponse(self._auth_rules.v2)


class AuthRulesWithStreamingResponse:
    def __init__(self, auth_rules: AuthRules) -> None:
        self._auth_rules = auth_rules

    @cached_property
    def v2(self) -> V2WithStreamingResponse:
        return V2WithStreamingResponse(self._auth_rules.v2)


class AsyncAuthRulesWithStreamingResponse:
    def __init__(self, auth_rules: AsyncAuthRules) -> None:
        self._auth_rules = auth_rules

    @cached_property
    def v2(self) -> AsyncV2WithStreamingResponse:
        return AsyncV2WithStreamingResponse(self._auth_rules.v2)
