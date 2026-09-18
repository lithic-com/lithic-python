# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.financial_accounts import installment_plan_list_params
from ...types.financial_accounts.installment_plan import InstallmentPlan

__all__ = ["InstallmentPlans", "AsyncInstallmentPlans"]


class InstallmentPlans(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InstallmentPlansWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return InstallmentPlansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InstallmentPlansWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return InstallmentPlansWithStreamingResponse(self)

    def retrieve(
        self,
        installment_plan_token: str,
        *,
        financial_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallmentPlan:
        """
        Get a specific installment plan for a given financial account.

        Args:
          financial_account_token: Globally unique identifier for financial account.

          installment_plan_token: Globally unique identifier for installment plan.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        if not installment_plan_token:
            raise ValueError(
                f"Expected a non-empty value for `installment_plan_token` but received {installment_plan_token!r}"
            )
        return self._get(
            path_template(
                "/v1/financial_accounts/{financial_account_token}/installment_plans/{installment_plan_token}",
                financial_account_token=financial_account_token,
                installment_plan_token=installment_plan_token,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstallmentPlan,
        )

    def list(
        self,
        financial_account_token: str,
        *,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        state: Optional[Literal["PENDING", "ACTIVE", "REBUILD_IN_PROGRESS", "FULLY_PAID", "CANCELLED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[InstallmentPlan]:
        """
        List the installment plans for a given financial account.

        Args:
          financial_account_token: Globally unique identifier for financial account.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          state: Only installment plans in this state will be included.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        return self._get_api_list(
            path_template(
                "/v1/financial_accounts/{financial_account_token}/installment_plans",
                financial_account_token=financial_account_token,
            ),
            page=SyncCursorPage[InstallmentPlan],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "state": state,
                    },
                    installment_plan_list_params.InstallmentPlanListParams,
                ),
            ),
            model=InstallmentPlan,
        )


class AsyncInstallmentPlans(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInstallmentPlansWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInstallmentPlansWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInstallmentPlansWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncInstallmentPlansWithStreamingResponse(self)

    async def retrieve(
        self,
        installment_plan_token: str,
        *,
        financial_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallmentPlan:
        """
        Get a specific installment plan for a given financial account.

        Args:
          financial_account_token: Globally unique identifier for financial account.

          installment_plan_token: Globally unique identifier for installment plan.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        if not installment_plan_token:
            raise ValueError(
                f"Expected a non-empty value for `installment_plan_token` but received {installment_plan_token!r}"
            )
        return await self._get(
            path_template(
                "/v1/financial_accounts/{financial_account_token}/installment_plans/{installment_plan_token}",
                financial_account_token=financial_account_token,
                installment_plan_token=installment_plan_token,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstallmentPlan,
        )

    def list(
        self,
        financial_account_token: str,
        *,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        state: Optional[Literal["PENDING", "ACTIVE", "REBUILD_IN_PROGRESS", "FULLY_PAID", "CANCELLED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InstallmentPlan, AsyncCursorPage[InstallmentPlan]]:
        """
        List the installment plans for a given financial account.

        Args:
          financial_account_token: Globally unique identifier for financial account.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          state: Only installment plans in this state will be included.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        return self._get_api_list(
            path_template(
                "/v1/financial_accounts/{financial_account_token}/installment_plans",
                financial_account_token=financial_account_token,
            ),
            page=AsyncCursorPage[InstallmentPlan],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "state": state,
                    },
                    installment_plan_list_params.InstallmentPlanListParams,
                ),
            ),
            model=InstallmentPlan,
        )


class InstallmentPlansWithRawResponse:
    def __init__(self, installment_plans: InstallmentPlans) -> None:
        self._installment_plans = installment_plans

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            installment_plans.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            installment_plans.list,
        )


class AsyncInstallmentPlansWithRawResponse:
    def __init__(self, installment_plans: AsyncInstallmentPlans) -> None:
        self._installment_plans = installment_plans

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            installment_plans.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            installment_plans.list,
        )


class InstallmentPlansWithStreamingResponse:
    def __init__(self, installment_plans: InstallmentPlans) -> None:
        self._installment_plans = installment_plans

        self.retrieve = to_streamed_response_wrapper(
            installment_plans.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            installment_plans.list,
        )


class AsyncInstallmentPlansWithStreamingResponse:
    def __init__(self, installment_plans: AsyncInstallmentPlans) -> None:
        self._installment_plans = installment_plans

        self.retrieve = async_to_streamed_response_wrapper(
            installment_plans.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            installment_plans.list,
        )
