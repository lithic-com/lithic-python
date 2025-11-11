# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, overload

import httpx

from .... import _legacy_response
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
from .backtests import (
    Backtests,
    AsyncBacktests,
    BacktestsWithRawResponse,
    AsyncBacktestsWithRawResponse,
    BacktestsWithStreamingResponse,
    AsyncBacktestsWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.auth_rules import (
    v2_list_params,
    v2_draft_params,
    v2_create_params,
    v2_update_params,
    v2_retrieve_report_params,
    v2_retrieve_features_params,
)
from ....types.auth_rules.v2_list_response import V2ListResponse
from ....types.auth_rules.v2_draft_response import V2DraftResponse
from ....types.auth_rules.v2_create_response import V2CreateResponse
from ....types.auth_rules.v2_update_response import V2UpdateResponse
from ....types.auth_rules.v2_promote_response import V2PromoteResponse
from ....types.auth_rules.v2_retrieve_response import V2RetrieveResponse
from ....types.auth_rules.v2_retrieve_report_response import V2RetrieveReportResponse
from ....types.auth_rules.v2_retrieve_features_response import V2RetrieveFeaturesResponse

__all__ = ["V2", "AsyncV2"]


class V2(SyncAPIResource):
    @cached_property
    def backtests(self) -> Backtests:
        return Backtests(self._client)

    @cached_property
    def with_raw_response(self) -> V2WithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        parameters: v2_create_params.AccountLevelRuleParameters,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION"],
        account_tokens: SequenceNotStr[str] | Omit = omit,
        business_account_tokens: SequenceNotStr[str] | Omit = omit,
        event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2CreateResponse:
        """
        Creates a new V2 Auth rule in draft mode

        Args:
          parameters: Parameters for the Auth Rule

          type: The type of Auth Rule. For certain rule types, this determines the event stream
              during which it will be evaluated. For rules that can be applied to one of
              several event streams, the effective one is defined by the separate
              `event_stream` field.

              - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
              - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
              - `MERCHANT_LOCK`: AUTHORIZATION event stream.
              - `CONDITIONAL_ACTION`: AUTHORIZATION or THREE_DS_AUTHENTICATION event stream.

          account_tokens: Account tokens to which the Auth Rule applies.

          business_account_tokens: Business Account tokens to which the Auth Rule applies.

          event_stream: The event stream during which the rule will be evaluated.

          name: Auth Rule Name

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
        card_tokens: SequenceNotStr[str],
        parameters: v2_create_params.CardLevelRuleParameters,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION"],
        event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2CreateResponse:
        """
        Creates a new V2 Auth rule in draft mode

        Args:
          card_tokens: Card tokens to which the Auth Rule applies.

          parameters: Parameters for the Auth Rule

          type: The type of Auth Rule. For certain rule types, this determines the event stream
              during which it will be evaluated. For rules that can be applied to one of
              several event streams, the effective one is defined by the separate
              `event_stream` field.

              - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
              - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
              - `MERCHANT_LOCK`: AUTHORIZATION event stream.
              - `CONDITIONAL_ACTION`: AUTHORIZATION or THREE_DS_AUTHENTICATION event stream.

          event_stream: The event stream during which the rule will be evaluated.

          name: Auth Rule Name

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
        parameters: v2_create_params.ProgramLevelRuleParameters,
        program_level: bool,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION"],
        event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"] | Omit = omit,
        excluded_card_tokens: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2CreateResponse:
        """
        Creates a new V2 Auth rule in draft mode

        Args:
          parameters: Parameters for the Auth Rule

          program_level: Whether the Auth Rule applies to all authorizations on the card program.

          type: The type of Auth Rule. For certain rule types, this determines the event stream
              during which it will be evaluated. For rules that can be applied to one of
              several event streams, the effective one is defined by the separate
              `event_stream` field.

              - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
              - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
              - `MERCHANT_LOCK`: AUTHORIZATION event stream.
              - `CONDITIONAL_ACTION`: AUTHORIZATION or THREE_DS_AUTHENTICATION event stream.

          event_stream: The event stream during which the rule will be evaluated.

          excluded_card_tokens: Card tokens to which the Auth Rule does not apply.

          name: Auth Rule Name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["parameters", "type"], ["card_tokens", "parameters", "type"], ["parameters", "program_level", "type"]
    )
    def create(
        self,
        *,
        parameters: v2_create_params.AccountLevelRuleParameters
        | v2_create_params.CardLevelRuleParameters
        | v2_create_params.ProgramLevelRuleParameters,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION"],
        account_tokens: SequenceNotStr[str] | Omit = omit,
        business_account_tokens: SequenceNotStr[str] | Omit = omit,
        event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"] | Omit = omit,
        name: Optional[str] | Omit = omit,
        card_tokens: SequenceNotStr[str] | Omit = omit,
        program_level: bool | Omit = omit,
        excluded_card_tokens: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2CreateResponse:
        return self._post(
            "/v2/auth_rules",
            body=maybe_transform(
                {
                    "parameters": parameters,
                    "type": type,
                    "account_tokens": account_tokens,
                    "business_account_tokens": business_account_tokens,
                    "event_stream": event_stream,
                    "name": name,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                    "excluded_card_tokens": excluded_card_tokens,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveResponse:
        """
        Fetches a V2 Auth rule by its token

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

    @overload
    def update(
        self,
        auth_rule_token: str,
        *,
        account_tokens: SequenceNotStr[str] | Omit = omit,
        business_account_tokens: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        state: Literal["INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2UpdateResponse:
        """
        Updates a V2 Auth rule's properties

        If `account_tokens`, `card_tokens`, `program_level`, or `excluded_card_tokens`
        is provided, this will replace existing associations with the provided list of
        entities.

        Args:
          account_tokens: Account tokens to which the Auth Rule applies.

          business_account_tokens: Business Account tokens to which the Auth Rule applies.

          name: Auth Rule Name

          state: The desired state of the Auth Rule.

              Note that only deactivating an Auth Rule through this endpoint is supported at
              this time. If you need to (re-)activate an Auth Rule the /promote endpoint
              should be used to promote a draft to the currently active version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        auth_rule_token: str,
        *,
        card_tokens: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        state: Literal["INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2UpdateResponse:
        """
        Updates a V2 Auth rule's properties

        If `account_tokens`, `card_tokens`, `program_level`, or `excluded_card_tokens`
        is provided, this will replace existing associations with the provided list of
        entities.

        Args:
          card_tokens: Card tokens to which the Auth Rule applies.

          name: Auth Rule Name

          state: The desired state of the Auth Rule.

              Note that only deactivating an Auth Rule through this endpoint is supported at
              this time. If you need to (re-)activate an Auth Rule the /promote endpoint
              should be used to promote a draft to the currently active version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        auth_rule_token: str,
        *,
        excluded_card_tokens: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        program_level: bool | Omit = omit,
        state: Literal["INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2UpdateResponse:
        """
        Updates a V2 Auth rule's properties

        If `account_tokens`, `card_tokens`, `program_level`, or `excluded_card_tokens`
        is provided, this will replace existing associations with the provided list of
        entities.

        Args:
          excluded_card_tokens: Card tokens to which the Auth Rule does not apply.

          name: Auth Rule Name

          program_level: Whether the Auth Rule applies to all authorizations on the card program.

          state: The desired state of the Auth Rule.

              Note that only deactivating an Auth Rule through this endpoint is supported at
              this time. If you need to (re-)activate an Auth Rule the /promote endpoint
              should be used to promote a draft to the currently active version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def update(
        self,
        auth_rule_token: str,
        *,
        account_tokens: SequenceNotStr[str] | Omit = omit,
        business_account_tokens: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        state: Literal["INACTIVE"] | Omit = omit,
        card_tokens: SequenceNotStr[str] | Omit = omit,
        excluded_card_tokens: SequenceNotStr[str] | Omit = omit,
        program_level: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2UpdateResponse:
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._patch(
            f"/v2/auth_rules/{auth_rule_token}",
            body=maybe_transform(
                {
                    "account_tokens": account_tokens,
                    "business_account_tokens": business_account_tokens,
                    "name": name,
                    "state": state,
                    "card_tokens": card_tokens,
                    "excluded_card_tokens": excluded_card_tokens,
                    "program_level": program_level,
                },
                v2_update_params.V2UpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2UpdateResponse,
        )

    def list(
        self,
        *,
        account_token: str | Omit = omit,
        business_account_token: str | Omit = omit,
        card_token: str | Omit = omit,
        ending_before: str | Omit = omit,
        event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"] | Omit = omit,
        page_size: int | Omit = omit,
        scope: Literal["PROGRAM", "ACCOUNT", "BUSINESS_ACCOUNT", "CARD", "ANY"] | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[V2ListResponse]:
        """
        Lists V2 Auth rules

        Args:
          account_token: Only return Auth Rules that are bound to the provided account token.

          business_account_token: Only return Auth Rules that are bound to the provided business account token.

          card_token: Only return Auth Rules that are bound to the provided card token.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          event_stream: Only return Auth rules that are executed during the provided event stream.

          page_size: Page size (for pagination).

          scope: Only return Auth Rules that are bound to the provided scope.

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
                        "business_account_token": business_account_token,
                        "card_token": card_token,
                        "ending_before": ending_before,
                        "event_stream": event_stream,
                        "page_size": page_size,
                        "scope": scope,
                        "starting_after": starting_after,
                    },
                    v2_list_params.V2ListParams,
                ),
            ),
            model=V2ListResponse,
        )

    def delete(
        self,
        auth_rule_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a V2 Auth rule

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._delete(
            f"/v2/auth_rules/{auth_rule_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def draft(
        self,
        auth_rule_token: str,
        *,
        parameters: Optional[v2_draft_params.Parameters] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2DraftResponse:
        """
        Creates a new draft version of a rule that will be ran in shadow mode.

        This can also be utilized to reset the draft parameters, causing a draft version
        to no longer be ran in shadow mode.

        Args:
          parameters: Parameters for the Auth Rule

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2PromoteResponse:
        """
        Promotes the draft version of an Auth rule to the currently active version such
        that it is enforced in the respective stream.

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

    def retrieve_features(
        self,
        auth_rule_token: str,
        *,
        account_token: str | Omit = omit,
        card_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveFeaturesResponse:
        """
        Fetches the current calculated Feature values for the given Auth Rule

        This only calculates the features for the active version.

        - VelocityLimit Rules calculates the current Velocity Feature data. This
          requires a `card_token` or `account_token` matching what the rule is Scoped
          to.
        - ConditionalBlock Rules calculates the CARD*TRANSACTION_COUNT*\\** attributes on
          the rule. This requires a `card_token`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._get(
            f"/v2/auth_rules/{auth_rule_token}/features",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "card_token": card_token,
                    },
                    v2_retrieve_features_params.V2RetrieveFeaturesParams,
                ),
            ),
            cast_to=V2RetrieveFeaturesResponse,
        )

    def retrieve_report(
        self,
        auth_rule_token: str,
        *,
        begin: Union[str, date],
        end: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveReportResponse:
        """
        Retrieves a performance report for an Auth rule containing daily statistics and
        evaluation outcomes.

        **Time Range Limitations:**

        - Reports are supported for the past 3 months only
        - Maximum interval length is 1 month
        - Report data is available only through the previous day in UTC (current day
          data is not available)

        The report provides daily statistics for both current and draft versions of the
        Auth rule, including approval, decline, and challenge counts along with sample
        events.

        Args:
          begin: Start date for the report

          end: End date for the report

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._get(
            f"/v2/auth_rules/{auth_rule_token}/report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                    },
                    v2_retrieve_report_params.V2RetrieveReportParams,
                ),
            ),
            cast_to=V2RetrieveReportResponse,
        )


class AsyncV2(AsyncAPIResource):
    @cached_property
    def backtests(self) -> AsyncBacktests:
        return AsyncBacktests(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2WithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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
        parameters: v2_create_params.AccountLevelRuleParameters,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION"],
        account_tokens: SequenceNotStr[str] | Omit = omit,
        business_account_tokens: SequenceNotStr[str] | Omit = omit,
        event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2CreateResponse:
        """
        Creates a new V2 Auth rule in draft mode

        Args:
          parameters: Parameters for the Auth Rule

          type: The type of Auth Rule. For certain rule types, this determines the event stream
              during which it will be evaluated. For rules that can be applied to one of
              several event streams, the effective one is defined by the separate
              `event_stream` field.

              - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
              - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
              - `MERCHANT_LOCK`: AUTHORIZATION event stream.
              - `CONDITIONAL_ACTION`: AUTHORIZATION or THREE_DS_AUTHENTICATION event stream.

          account_tokens: Account tokens to which the Auth Rule applies.

          business_account_tokens: Business Account tokens to which the Auth Rule applies.

          event_stream: The event stream during which the rule will be evaluated.

          name: Auth Rule Name

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
        card_tokens: SequenceNotStr[str],
        parameters: v2_create_params.CardLevelRuleParameters,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION"],
        event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2CreateResponse:
        """
        Creates a new V2 Auth rule in draft mode

        Args:
          card_tokens: Card tokens to which the Auth Rule applies.

          parameters: Parameters for the Auth Rule

          type: The type of Auth Rule. For certain rule types, this determines the event stream
              during which it will be evaluated. For rules that can be applied to one of
              several event streams, the effective one is defined by the separate
              `event_stream` field.

              - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
              - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
              - `MERCHANT_LOCK`: AUTHORIZATION event stream.
              - `CONDITIONAL_ACTION`: AUTHORIZATION or THREE_DS_AUTHENTICATION event stream.

          event_stream: The event stream during which the rule will be evaluated.

          name: Auth Rule Name

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
        parameters: v2_create_params.ProgramLevelRuleParameters,
        program_level: bool,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION"],
        event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"] | Omit = omit,
        excluded_card_tokens: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2CreateResponse:
        """
        Creates a new V2 Auth rule in draft mode

        Args:
          parameters: Parameters for the Auth Rule

          program_level: Whether the Auth Rule applies to all authorizations on the card program.

          type: The type of Auth Rule. For certain rule types, this determines the event stream
              during which it will be evaluated. For rules that can be applied to one of
              several event streams, the effective one is defined by the separate
              `event_stream` field.

              - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
              - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
              - `MERCHANT_LOCK`: AUTHORIZATION event stream.
              - `CONDITIONAL_ACTION`: AUTHORIZATION or THREE_DS_AUTHENTICATION event stream.

          event_stream: The event stream during which the rule will be evaluated.

          excluded_card_tokens: Card tokens to which the Auth Rule does not apply.

          name: Auth Rule Name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["parameters", "type"], ["card_tokens", "parameters", "type"], ["parameters", "program_level", "type"]
    )
    async def create(
        self,
        *,
        parameters: v2_create_params.AccountLevelRuleParameters
        | v2_create_params.CardLevelRuleParameters
        | v2_create_params.ProgramLevelRuleParameters,
        type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION"],
        account_tokens: SequenceNotStr[str] | Omit = omit,
        business_account_tokens: SequenceNotStr[str] | Omit = omit,
        event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"] | Omit = omit,
        name: Optional[str] | Omit = omit,
        card_tokens: SequenceNotStr[str] | Omit = omit,
        program_level: bool | Omit = omit,
        excluded_card_tokens: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2CreateResponse:
        return await self._post(
            "/v2/auth_rules",
            body=await async_maybe_transform(
                {
                    "parameters": parameters,
                    "type": type,
                    "account_tokens": account_tokens,
                    "business_account_tokens": business_account_tokens,
                    "event_stream": event_stream,
                    "name": name,
                    "card_tokens": card_tokens,
                    "program_level": program_level,
                    "excluded_card_tokens": excluded_card_tokens,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveResponse:
        """
        Fetches a V2 Auth rule by its token

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

    @overload
    async def update(
        self,
        auth_rule_token: str,
        *,
        account_tokens: SequenceNotStr[str] | Omit = omit,
        business_account_tokens: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        state: Literal["INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2UpdateResponse:
        """
        Updates a V2 Auth rule's properties

        If `account_tokens`, `card_tokens`, `program_level`, or `excluded_card_tokens`
        is provided, this will replace existing associations with the provided list of
        entities.

        Args:
          account_tokens: Account tokens to which the Auth Rule applies.

          business_account_tokens: Business Account tokens to which the Auth Rule applies.

          name: Auth Rule Name

          state: The desired state of the Auth Rule.

              Note that only deactivating an Auth Rule through this endpoint is supported at
              this time. If you need to (re-)activate an Auth Rule the /promote endpoint
              should be used to promote a draft to the currently active version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        auth_rule_token: str,
        *,
        card_tokens: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        state: Literal["INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2UpdateResponse:
        """
        Updates a V2 Auth rule's properties

        If `account_tokens`, `card_tokens`, `program_level`, or `excluded_card_tokens`
        is provided, this will replace existing associations with the provided list of
        entities.

        Args:
          card_tokens: Card tokens to which the Auth Rule applies.

          name: Auth Rule Name

          state: The desired state of the Auth Rule.

              Note that only deactivating an Auth Rule through this endpoint is supported at
              this time. If you need to (re-)activate an Auth Rule the /promote endpoint
              should be used to promote a draft to the currently active version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        auth_rule_token: str,
        *,
        excluded_card_tokens: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        program_level: bool | Omit = omit,
        state: Literal["INACTIVE"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2UpdateResponse:
        """
        Updates a V2 Auth rule's properties

        If `account_tokens`, `card_tokens`, `program_level`, or `excluded_card_tokens`
        is provided, this will replace existing associations with the provided list of
        entities.

        Args:
          excluded_card_tokens: Card tokens to which the Auth Rule does not apply.

          name: Auth Rule Name

          program_level: Whether the Auth Rule applies to all authorizations on the card program.

          state: The desired state of the Auth Rule.

              Note that only deactivating an Auth Rule through this endpoint is supported at
              this time. If you need to (re-)activate an Auth Rule the /promote endpoint
              should be used to promote a draft to the currently active version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def update(
        self,
        auth_rule_token: str,
        *,
        account_tokens: SequenceNotStr[str] | Omit = omit,
        business_account_tokens: SequenceNotStr[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        state: Literal["INACTIVE"] | Omit = omit,
        card_tokens: SequenceNotStr[str] | Omit = omit,
        excluded_card_tokens: SequenceNotStr[str] | Omit = omit,
        program_level: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2UpdateResponse:
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._patch(
            f"/v2/auth_rules/{auth_rule_token}",
            body=await async_maybe_transform(
                {
                    "account_tokens": account_tokens,
                    "business_account_tokens": business_account_tokens,
                    "name": name,
                    "state": state,
                    "card_tokens": card_tokens,
                    "excluded_card_tokens": excluded_card_tokens,
                    "program_level": program_level,
                },
                v2_update_params.V2UpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=V2UpdateResponse,
        )

    def list(
        self,
        *,
        account_token: str | Omit = omit,
        business_account_token: str | Omit = omit,
        card_token: str | Omit = omit,
        ending_before: str | Omit = omit,
        event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"] | Omit = omit,
        page_size: int | Omit = omit,
        scope: Literal["PROGRAM", "ACCOUNT", "BUSINESS_ACCOUNT", "CARD", "ANY"] | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[V2ListResponse, AsyncCursorPage[V2ListResponse]]:
        """
        Lists V2 Auth rules

        Args:
          account_token: Only return Auth Rules that are bound to the provided account token.

          business_account_token: Only return Auth Rules that are bound to the provided business account token.

          card_token: Only return Auth Rules that are bound to the provided card token.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          event_stream: Only return Auth rules that are executed during the provided event stream.

          page_size: Page size (for pagination).

          scope: Only return Auth Rules that are bound to the provided scope.

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
                        "business_account_token": business_account_token,
                        "card_token": card_token,
                        "ending_before": ending_before,
                        "event_stream": event_stream,
                        "page_size": page_size,
                        "scope": scope,
                        "starting_after": starting_after,
                    },
                    v2_list_params.V2ListParams,
                ),
            ),
            model=V2ListResponse,
        )

    async def delete(
        self,
        auth_rule_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a V2 Auth rule

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._delete(
            f"/v2/auth_rules/{auth_rule_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def draft(
        self,
        auth_rule_token: str,
        *,
        parameters: Optional[v2_draft_params.Parameters] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2DraftResponse:
        """
        Creates a new draft version of a rule that will be ran in shadow mode.

        This can also be utilized to reset the draft parameters, causing a draft version
        to no longer be ran in shadow mode.

        Args:
          parameters: Parameters for the Auth Rule

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2PromoteResponse:
        """
        Promotes the draft version of an Auth rule to the currently active version such
        that it is enforced in the respective stream.

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

    async def retrieve_features(
        self,
        auth_rule_token: str,
        *,
        account_token: str | Omit = omit,
        card_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveFeaturesResponse:
        """
        Fetches the current calculated Feature values for the given Auth Rule

        This only calculates the features for the active version.

        - VelocityLimit Rules calculates the current Velocity Feature data. This
          requires a `card_token` or `account_token` matching what the rule is Scoped
          to.
        - ConditionalBlock Rules calculates the CARD*TRANSACTION_COUNT*\\** attributes on
          the rule. This requires a `card_token`

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._get(
            f"/v2/auth_rules/{auth_rule_token}/features",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "account_token": account_token,
                        "card_token": card_token,
                    },
                    v2_retrieve_features_params.V2RetrieveFeaturesParams,
                ),
            ),
            cast_to=V2RetrieveFeaturesResponse,
        )

    async def retrieve_report(
        self,
        auth_rule_token: str,
        *,
        begin: Union[str, date],
        end: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2RetrieveReportResponse:
        """
        Retrieves a performance report for an Auth rule containing daily statistics and
        evaluation outcomes.

        **Time Range Limitations:**

        - Reports are supported for the past 3 months only
        - Maximum interval length is 1 month
        - Report data is available only through the previous day in UTC (current day
          data is not available)

        The report provides daily statistics for both current and draft versions of the
        Auth rule, including approval, decline, and challenge counts along with sample
        events.

        Args:
          begin: Start date for the report

          end: End date for the report

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._get(
            f"/v2/auth_rules/{auth_rule_token}/report",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                    },
                    v2_retrieve_report_params.V2RetrieveReportParams,
                ),
            ),
            cast_to=V2RetrieveReportResponse,
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
        self.delete = _legacy_response.to_raw_response_wrapper(
            v2.delete,
        )
        self.draft = _legacy_response.to_raw_response_wrapper(
            v2.draft,
        )
        self.promote = _legacy_response.to_raw_response_wrapper(
            v2.promote,
        )
        self.retrieve_features = _legacy_response.to_raw_response_wrapper(
            v2.retrieve_features,
        )
        self.retrieve_report = _legacy_response.to_raw_response_wrapper(
            v2.retrieve_report,
        )

    @cached_property
    def backtests(self) -> BacktestsWithRawResponse:
        return BacktestsWithRawResponse(self._v2.backtests)


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
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            v2.delete,
        )
        self.draft = _legacy_response.async_to_raw_response_wrapper(
            v2.draft,
        )
        self.promote = _legacy_response.async_to_raw_response_wrapper(
            v2.promote,
        )
        self.retrieve_features = _legacy_response.async_to_raw_response_wrapper(
            v2.retrieve_features,
        )
        self.retrieve_report = _legacy_response.async_to_raw_response_wrapper(
            v2.retrieve_report,
        )

    @cached_property
    def backtests(self) -> AsyncBacktestsWithRawResponse:
        return AsyncBacktestsWithRawResponse(self._v2.backtests)


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
        self.delete = to_streamed_response_wrapper(
            v2.delete,
        )
        self.draft = to_streamed_response_wrapper(
            v2.draft,
        )
        self.promote = to_streamed_response_wrapper(
            v2.promote,
        )
        self.retrieve_features = to_streamed_response_wrapper(
            v2.retrieve_features,
        )
        self.retrieve_report = to_streamed_response_wrapper(
            v2.retrieve_report,
        )

    @cached_property
    def backtests(self) -> BacktestsWithStreamingResponse:
        return BacktestsWithStreamingResponse(self._v2.backtests)


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
        self.delete = async_to_streamed_response_wrapper(
            v2.delete,
        )
        self.draft = async_to_streamed_response_wrapper(
            v2.draft,
        )
        self.promote = async_to_streamed_response_wrapper(
            v2.promote,
        )
        self.retrieve_features = async_to_streamed_response_wrapper(
            v2.retrieve_features,
        )
        self.retrieve_report = async_to_streamed_response_wrapper(
            v2.retrieve_report,
        )

    @cached_property
    def backtests(self) -> AsyncBacktestsWithStreamingResponse:
        return AsyncBacktestsWithStreamingResponse(self._v2.backtests)
