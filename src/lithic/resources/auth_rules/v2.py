# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, overload

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.auth_rules import v2_list_params, v2_apply_params, v2_draft_params, v2_create_params, v2_update_params
from ...types.auth_rules.v2_list_response import V2ListResponse
from ...types.auth_rules.v2_apply_response import V2ApplyResponse
from ...types.auth_rules.v2_draft_response import V2DraftResponse
from ...types.auth_rules.v2_create_response import V2CreateResponse
from ...types.auth_rules.v2_report_response import V2ReportResponse
from ...types.auth_rules.v2_update_response import V2UpdateResponse
from ...types.auth_rules.v2_promote_response import V2PromoteResponse
from ...types.auth_rules.v2_retrieve_response import V2RetrieveResponse

__all__ = ["V2", "AsyncV2"]


class V2(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2WithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return V2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2WithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return V2WithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_tokens: List[str],
        parameters: v2_create_params.CreateAuthRuleRequestAccountTokensParameters | NotGiven = NOT_GIVEN,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2CreateResponse:
        """
        Creates a new V2 authorization rule in draft mode

        Args:
          account_tokens: Account tokens to which the Auth Rule applies.

          parameters: Parameters for the current version of the Auth Rule

          type: The type of Auth Rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        card_tokens: List[str],
        parameters: v2_create_params.CreateAuthRuleRequestCardTokensParameters | NotGiven = NOT_GIVEN,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2CreateResponse:
        """
        Creates a new V2 authorization rule in draft mode

        Args:
          card_tokens: Card tokens to which the Auth Rule applies.

          parameters: Parameters for the current version of the Auth Rule

          type: The type of Auth Rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        program_level: bool,
        parameters: v2_create_params.CreateAuthRuleRequestProgramLevelParameters | NotGiven = NOT_GIVEN,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2CreateResponse:
        """
        Creates a new V2 authorization rule in draft mode

        Args:
          program_level: Whether the Auth Rule applies to all authorizations on the card program.

          parameters: Parameters for the current version of the Auth Rule

          type: The type of Auth Rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_tokens"], ["card_tokens"], ["program_level"])
    def create(
        self,
        *,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        parameters: v2_create_params.CreateAuthRuleRequestAccountTokensParameters | NotGiven = NOT_GIVEN,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"] | NotGiven = NOT_GIVEN,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2CreateResponse:
        return self._post(
            "/v2/auth_rules",
            body=maybe_transform(
                {
                    "account_tokens": account_tokens,
                    "parameters": parameters,
                    "type": type,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                },
                v2_create_params.V2CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2CreateResponse,
        )

    def retrieve(
        self,
        auth_rule_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2RetrieveResponse:
        """
        Fetches an authorization rule by its token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._get(
            f"/v2/auth_rules/{auth_rule_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2RetrieveResponse,
        )

    def update(
        self,
        auth_rule_token: str,
        *,
        state: Literal["INACTIVE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2UpdateResponse:
        """
        Updates an authorization rule's properties

        Args:
          state: The desired state of the Auth Rule.

              Note that only deactivating an Auth Rule through this endpoint is supported at
              this time. If you need to (re-)activate an Auth Rule the /promote endpoint
              should be used to promote a draft to the currently active version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._patch(
            f"/v2/auth_rules/{auth_rule_token}",
            body=maybe_transform({"state": state}, v2_update_params.V2UpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2UpdateResponse,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        card_token: str | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[V2ListResponse]:
        """
        Lists V2 authorization rules

        Args:
          account_token: Only return Authorization Rules that are bound to the provided account token.

          card_token: Only return Authorization Rules that are bound to the provided card token.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/auth_rules",
            page=SyncCursorPage[V2ListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "card_token": card_token,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    v2_list_params.V2ListParams,
                ),
            ),
            model=V2ListResponse,
        )

    @overload
    def apply(
        self,
        auth_rule_token: str,
        *,
        account_tokens: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ApplyResponse:
        """
        Associates an authorization rules with a card program, the provided account(s)
        or card(s).

        This endpoint will replace any existing associations with the provided list of
        entities.

        Args:
          account_tokens: Account tokens to which the Auth Rule applies.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def apply(
        self,
        auth_rule_token: str,
        *,
        card_tokens: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ApplyResponse:
        """
        Associates an authorization rules with a card program, the provided account(s)
        or card(s).

        This endpoint will replace any existing associations with the provided list of
        entities.

        Args:
          card_tokens: Card tokens to which the Auth Rule applies.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def apply(
        self,
        auth_rule_token: str,
        *,
        program_level: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ApplyResponse:
        """
        Associates an authorization rules with a card program, the provided account(s)
        or card(s).

        This endpoint will replace any existing associations with the provided list of
        entities.

        Args:
          program_level: Whether the Auth Rule applies to all authorizations on the card program.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_tokens"], ["card_tokens"], ["program_level"])
    def apply(
        self,
        auth_rule_token: str,
        *,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ApplyResponse:
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._post(
            f"/v2/auth_rules/{auth_rule_token}/apply",
            body=maybe_transform(
                {
                    "account_tokens": account_tokens,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                },
                v2_apply_params.V2ApplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2ApplyResponse,
        )

    def draft(
        self,
        auth_rule_token: str,
        *,
        parameters: Optional[v2_draft_params.Parameters] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2DraftResponse:
        """
        Creates a new draft version of an authorization rules that will be ran in shadow
        mode.

        This can also be utilized to reset the draft parameters, causing a draft version
        to no longer be ran in shadow mode.

        Args:
          parameters: Parameters for the current version of the Auth Rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._post(
            f"/v2/auth_rules/{auth_rule_token}/draft",
            body=maybe_transform({"parameters": parameters}, v2_draft_params.V2DraftParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2DraftResponse,
        )

    def promote(
        self,
        auth_rule_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PromoteResponse:
        """
        Promotes a draft version of an authorization rule to the currently active
        version such that it is enforced in the authorization stream.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._post(
            f"/v2/auth_rules/{auth_rule_token}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2PromoteResponse,
        )

    def report(
        self,
        auth_rule_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ReportResponse:
        """
        Requests a performance report of an authorization rule to be asynchronously
        generated. Reports can only be run on rules in draft or active mode and will
        included approved and declined statistics as well as examples. The generated
        report will be delivered asynchronously through a webhook with `event_type` =
        `auth_rules.performance_report.created`. See the docs on setting up
        [webhook subscriptions](https://docs.lithic.com/docs/events-api).

        Note that generating a report may take up to 15 minutes and that delivery is not
        guaranteed. Customers are required to have created an event subscription to
        receive the webhook. Additionally, there is a delay of approximately 15 minutes
        between when Lithic's transaction processing systems have processed the
        transaction, and when a transaction will be included in the report.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._post(
            f"/v2/auth_rules/{auth_rule_token}/report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2ReportResponse,
        )


class AsyncV2(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2WithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2WithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncV2WithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_tokens: List[str],
        parameters: v2_create_params.CreateAuthRuleRequestAccountTokensParameters | NotGiven = NOT_GIVEN,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2CreateResponse:
        """
        Creates a new V2 authorization rule in draft mode

        Args:
          account_tokens: Account tokens to which the Auth Rule applies.

          parameters: Parameters for the current version of the Auth Rule

          type: The type of Auth Rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        card_tokens: List[str],
        parameters: v2_create_params.CreateAuthRuleRequestCardTokensParameters | NotGiven = NOT_GIVEN,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2CreateResponse:
        """
        Creates a new V2 authorization rule in draft mode

        Args:
          card_tokens: Card tokens to which the Auth Rule applies.

          parameters: Parameters for the current version of the Auth Rule

          type: The type of Auth Rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        program_level: bool,
        parameters: v2_create_params.CreateAuthRuleRequestProgramLevelParameters | NotGiven = NOT_GIVEN,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2CreateResponse:
        """
        Creates a new V2 authorization rule in draft mode

        Args:
          program_level: Whether the Auth Rule applies to all authorizations on the card program.

          parameters: Parameters for the current version of the Auth Rule

          type: The type of Auth Rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_tokens"], ["card_tokens"], ["program_level"])
    async def create(
        self,
        *,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        parameters: v2_create_params.CreateAuthRuleRequestAccountTokensParameters | NotGiven = NOT_GIVEN,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"] | NotGiven = NOT_GIVEN,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2CreateResponse:
        return await self._post(
            "/v2/auth_rules",
            body=await async_maybe_transform(
                {
                    "account_tokens": account_tokens,
                    "parameters": parameters,
                    "type": type,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                },
                v2_create_params.V2CreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2CreateResponse,
        )

    async def retrieve(
        self,
        auth_rule_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2RetrieveResponse:
        """
        Fetches an authorization rule by its token

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._get(
            f"/v2/auth_rules/{auth_rule_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2RetrieveResponse,
        )

    async def update(
        self,
        auth_rule_token: str,
        *,
        state: Literal["INACTIVE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2UpdateResponse:
        """
        Updates an authorization rule's properties

        Args:
          state: The desired state of the Auth Rule.

              Note that only deactivating an Auth Rule through this endpoint is supported at
              this time. If you need to (re-)activate an Auth Rule the /promote endpoint
              should be used to promote a draft to the currently active version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._patch(
            f"/v2/auth_rules/{auth_rule_token}",
            body=await async_maybe_transform({"state": state}, v2_update_params.V2UpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2UpdateResponse,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        card_token: str | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[V2ListResponse, AsyncCursorPage[V2ListResponse]]:
        """
        Lists V2 authorization rules

        Args:
          account_token: Only return Authorization Rules that are bound to the provided account token.

          card_token: Only return Authorization Rules that are bound to the provided card token.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/auth_rules",
            page=AsyncCursorPage[V2ListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "card_token": card_token,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    v2_list_params.V2ListParams,
                ),
            ),
            model=V2ListResponse,
        )

    @overload
    async def apply(
        self,
        auth_rule_token: str,
        *,
        account_tokens: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ApplyResponse:
        """
        Associates an authorization rules with a card program, the provided account(s)
        or card(s).

        This endpoint will replace any existing associations with the provided list of
        entities.

        Args:
          account_tokens: Account tokens to which the Auth Rule applies.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def apply(
        self,
        auth_rule_token: str,
        *,
        card_tokens: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ApplyResponse:
        """
        Associates an authorization rules with a card program, the provided account(s)
        or card(s).

        This endpoint will replace any existing associations with the provided list of
        entities.

        Args:
          card_tokens: Card tokens to which the Auth Rule applies.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def apply(
        self,
        auth_rule_token: str,
        *,
        program_level: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ApplyResponse:
        """
        Associates an authorization rules with a card program, the provided account(s)
        or card(s).

        This endpoint will replace any existing associations with the provided list of
        entities.

        Args:
          program_level: Whether the Auth Rule applies to all authorizations on the card program.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_tokens"], ["card_tokens"], ["program_level"])
    async def apply(
        self,
        auth_rule_token: str,
        *,
        account_tokens: List[str] | NotGiven = NOT_GIVEN,
        card_tokens: List[str] | NotGiven = NOT_GIVEN,
        program_level: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ApplyResponse:
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._post(
            f"/v2/auth_rules/{auth_rule_token}/apply",
            body=await async_maybe_transform(
                {
                    "account_tokens": account_tokens,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                },
                v2_apply_params.V2ApplyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2ApplyResponse,
        )

    async def draft(
        self,
        auth_rule_token: str,
        *,
        parameters: Optional[v2_draft_params.Parameters] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2DraftResponse:
        """
        Creates a new draft version of an authorization rules that will be ran in shadow
        mode.

        This can also be utilized to reset the draft parameters, causing a draft version
        to no longer be ran in shadow mode.

        Args:
          parameters: Parameters for the current version of the Auth Rule

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._post(
            f"/v2/auth_rules/{auth_rule_token}/draft",
            body=await async_maybe_transform({"parameters": parameters}, v2_draft_params.V2DraftParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2DraftResponse,
        )

    async def promote(
        self,
        auth_rule_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2PromoteResponse:
        """
        Promotes a draft version of an authorization rule to the currently active
        version such that it is enforced in the authorization stream.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._post(
            f"/v2/auth_rules/{auth_rule_token}/promote",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2PromoteResponse,
        )

    async def report(
        self,
        auth_rule_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ReportResponse:
        """
        Requests a performance report of an authorization rule to be asynchronously
        generated. Reports can only be run on rules in draft or active mode and will
        included approved and declined statistics as well as examples. The generated
        report will be delivered asynchronously through a webhook with `event_type` =
        `auth_rules.performance_report.created`. See the docs on setting up
        [webhook subscriptions](https://docs.lithic.com/docs/events-api).

        Note that generating a report may take up to 15 minutes and that delivery is not
        guaranteed. Customers are required to have created an event subscription to
        receive the webhook. Additionally, there is a delay of approximately 15 minutes
        between when Lithic's transaction processing systems have processed the
        transaction, and when a transaction will be included in the report.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._post(
            f"/v2/auth_rules/{auth_rule_token}/report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2ReportResponse,
        )


class V2WithRawResponse:
    def __init__(self, v2: V2) -> None:
        self._v2 = v2

        self.create = _legacy_response.to_raw_response_wrapper(
            v2.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            v2.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            v2.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            v2.list,
        )
        self.apply = _legacy_response.to_raw_response_wrapper(
            v2.apply,
        )
        self.draft = _legacy_response.to_raw_response_wrapper(
            v2.draft,
        )
        self.promote = _legacy_response.to_raw_response_wrapper(
            v2.promote,
        )
        self.report = _legacy_response.to_raw_response_wrapper(
            v2.report,
        )


class AsyncV2WithRawResponse:
    def __init__(self, v2: AsyncV2) -> None:
        self._v2 = v2

        self.create = _legacy_response.async_to_raw_response_wrapper(
            v2.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            v2.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            v2.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            v2.list,
        )
        self.apply = _legacy_response.async_to_raw_response_wrapper(
            v2.apply,
        )
        self.draft = _legacy_response.async_to_raw_response_wrapper(
            v2.draft,
        )
        self.promote = _legacy_response.async_to_raw_response_wrapper(
            v2.promote,
        )
        self.report = _legacy_response.async_to_raw_response_wrapper(
            v2.report,
        )


class V2WithStreamingResponse:
    def __init__(self, v2: V2) -> None:
        self._v2 = v2

        self.create = to_streamed_response_wrapper(
            v2.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            v2.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            v2.update,
        )
        self.list = to_streamed_response_wrapper(
            v2.list,
        )
        self.apply = to_streamed_response_wrapper(
            v2.apply,
        )
        self.draft = to_streamed_response_wrapper(
            v2.draft,
        )
        self.promote = to_streamed_response_wrapper(
            v2.promote,
        )
        self.report = to_streamed_response_wrapper(
            v2.report,
        )


class AsyncV2WithStreamingResponse:
    def __init__(self, v2: AsyncV2) -> None:
        self._v2 = v2

        self.create = async_to_streamed_response_wrapper(
            v2.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            v2.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            v2.update,
        )
        self.list = async_to_streamed_response_wrapper(
            v2.list,
        )
        self.apply = async_to_streamed_response_wrapper(
            v2.apply,
        )
        self.draft = async_to_streamed_response_wrapper(
            v2.draft,
        )
        self.promote = async_to_streamed_response_wrapper(
            v2.promote,
        )
        self.report = async_to_streamed_response_wrapper(
            v2.report,
        )
