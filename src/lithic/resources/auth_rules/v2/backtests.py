# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from .... import _legacy_response
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...._base_client import make_request_options
from ....types.auth_rules.v2 import backtest_create_params
from ....types.auth_rules.v2.backtest_results import BacktestResults
from ....types.auth_rules.v2.backtest_create_response import BacktestCreateResponse

__all__ = ["Backtests", "AsyncBacktests"]


class Backtests(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BacktestsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return BacktestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BacktestsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return BacktestsWithStreamingResponse(self)

    def create(
        self,
        auth_rule_token: str,
        *,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BacktestCreateResponse:
        """
        Initiates a request to asynchronously generate a backtest for an authorization
        rule. During backtesting, both the active version (if one exists) and the draft
        version of the Authorization Rule are evaluated by replaying historical
        transaction data against the rule's conditions. This process allows customers to
        simulate and understand the effects of proposed rule changes before deployment.
        The generated backtest report provides detailed results showing whether the
        draft version of the Auth Rule would have approved or declined historical
        transactions which were processed during the backtest period. These reports help
        evaluate how changes to rule configurations might affect overall transaction
        approval rates.

        The generated backtest report will be delivered asynchronously through a webhook
        with `event_type` = `auth_rules.backtest_report.created`. See the docs on
        setting up [webhook subscriptions](https://docs.lithic.com/docs/events-api). It
        is also possible to request backtest reports on-demand through the
        `/v2/auth_rules/{auth_rule_token}/backtests/{auth_rule_backtest_token}`
        endpoint.

        Lithic currently supports backtesting for `CONDITIONAL_BLOCK` rules. Backtesting
        for `VELOCITY_LIMIT` rules is generally not supported. In specific cases (i.e.
        where Lithic has pre-calculated the requested velocity metrics for historical
        transactions), a backtest may be feasible. However, such cases are uncommon and
        customers should not anticipate support for velocity backtests under most
        configurations. If a historical transaction does not feature the required inputs
        to evaluate the rule, then it will not be included in the final backtest report.

        Args:
          end: The end time of the backtest.

          start: The start time of the backtest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return self._post(
            f"/v2/auth_rules/{auth_rule_token}/backtests",
            body=maybe_transform(
                {
                    "end": end,
                    "start": start,
                },
                backtest_create_params.BacktestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BacktestCreateResponse,
        )

    def retrieve(
        self,
        auth_rule_backtest_token: str,
        *,
        auth_rule_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BacktestResults:
        """
        Returns the backtest results of an authorization rule (if available).

        Backtesting is an asynchronous process that requires time to complete. If a
        customer retrieves the backtest results using this endpoint before the report is
        fully generated, the response will return null for `results.current_version` and
        `results.draft_version`. Customers are advised to wait for the backtest creation
        process to complete (as indicated by the webhook event
        auth_rules.backtest_report.created) before retrieving results from this
        endpoint.

        Backtesting is an asynchronous process, while the backtest is being processed,
        results will not be available which will cause `results.current_version` and
        `results.draft_version` objects to contain `null`. The entries in `results` will
        also always represent the configuration of the rule at the time requests are
        made to this endpoint. For example, the results for `current_version` in the
        served backtest report will be consistent with which version of the rule is
        currently activated in the Auth Stream, regardless of which version of the rule
        was active in the Auth Stream at the time a backtest is requested.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        if not auth_rule_backtest_token:
            raise ValueError(
                f"Expected a non-empty value for `auth_rule_backtest_token` but received {auth_rule_backtest_token!r}"
            )
        return self._get(
            f"/v2/auth_rules/{auth_rule_token}/backtests/{auth_rule_backtest_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BacktestResults,
        )


class AsyncBacktests(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBacktestsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBacktestsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBacktestsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncBacktestsWithStreamingResponse(self)

    async def create(
        self,
        auth_rule_token: str,
        *,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BacktestCreateResponse:
        """
        Initiates a request to asynchronously generate a backtest for an authorization
        rule. During backtesting, both the active version (if one exists) and the draft
        version of the Authorization Rule are evaluated by replaying historical
        transaction data against the rule's conditions. This process allows customers to
        simulate and understand the effects of proposed rule changes before deployment.
        The generated backtest report provides detailed results showing whether the
        draft version of the Auth Rule would have approved or declined historical
        transactions which were processed during the backtest period. These reports help
        evaluate how changes to rule configurations might affect overall transaction
        approval rates.

        The generated backtest report will be delivered asynchronously through a webhook
        with `event_type` = `auth_rules.backtest_report.created`. See the docs on
        setting up [webhook subscriptions](https://docs.lithic.com/docs/events-api). It
        is also possible to request backtest reports on-demand through the
        `/v2/auth_rules/{auth_rule_token}/backtests/{auth_rule_backtest_token}`
        endpoint.

        Lithic currently supports backtesting for `CONDITIONAL_BLOCK` rules. Backtesting
        for `VELOCITY_LIMIT` rules is generally not supported. In specific cases (i.e.
        where Lithic has pre-calculated the requested velocity metrics for historical
        transactions), a backtest may be feasible. However, such cases are uncommon and
        customers should not anticipate support for velocity backtests under most
        configurations. If a historical transaction does not feature the required inputs
        to evaluate the rule, then it will not be included in the final backtest report.

        Args:
          end: The end time of the backtest.

          start: The start time of the backtest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        return await self._post(
            f"/v2/auth_rules/{auth_rule_token}/backtests",
            body=await async_maybe_transform(
                {
                    "end": end,
                    "start": start,
                },
                backtest_create_params.BacktestCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BacktestCreateResponse,
        )

    async def retrieve(
        self,
        auth_rule_backtest_token: str,
        *,
        auth_rule_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BacktestResults:
        """
        Returns the backtest results of an authorization rule (if available).

        Backtesting is an asynchronous process that requires time to complete. If a
        customer retrieves the backtest results using this endpoint before the report is
        fully generated, the response will return null for `results.current_version` and
        `results.draft_version`. Customers are advised to wait for the backtest creation
        process to complete (as indicated by the webhook event
        auth_rules.backtest_report.created) before retrieving results from this
        endpoint.

        Backtesting is an asynchronous process, while the backtest is being processed,
        results will not be available which will cause `results.current_version` and
        `results.draft_version` objects to contain `null`. The entries in `results` will
        also always represent the configuration of the rule at the time requests are
        made to this endpoint. For example, the results for `current_version` in the
        served backtest report will be consistent with which version of the rule is
        currently activated in the Auth Stream, regardless of which version of the rule
        was active in the Auth Stream at the time a backtest is requested.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_rule_token:
            raise ValueError(f"Expected a non-empty value for `auth_rule_token` but received {auth_rule_token!r}")
        if not auth_rule_backtest_token:
            raise ValueError(
                f"Expected a non-empty value for `auth_rule_backtest_token` but received {auth_rule_backtest_token!r}"
            )
        return await self._get(
            f"/v2/auth_rules/{auth_rule_token}/backtests/{auth_rule_backtest_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BacktestResults,
        )


class BacktestsWithRawResponse:
    def __init__(self, backtests: Backtests) -> None:
        self._backtests = backtests

        self.create = _legacy_response.to_raw_response_wrapper(
            backtests.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            backtests.retrieve,
        )


class AsyncBacktestsWithRawResponse:
    def __init__(self, backtests: AsyncBacktests) -> None:
        self._backtests = backtests

        self.create = _legacy_response.async_to_raw_response_wrapper(
            backtests.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            backtests.retrieve,
        )


class BacktestsWithStreamingResponse:
    def __init__(self, backtests: Backtests) -> None:
        self._backtests = backtests

        self.create = to_streamed_response_wrapper(
            backtests.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            backtests.retrieve,
        )


class AsyncBacktestsWithStreamingResponse:
    def __init__(self, backtests: AsyncBacktests) -> None:
        self._backtests = backtests

        self.create = async_to_streamed_response_wrapper(
            backtests.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            backtests.retrieve,
        )
