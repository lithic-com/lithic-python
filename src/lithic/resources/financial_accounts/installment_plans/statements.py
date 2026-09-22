# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from .... import _legacy_response
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.financial_accounts.installment_plans import statement_list_params
from ....types.financial_accounts.installment_plans.installment_plan_statement import InstallmentPlanStatement

__all__ = ["Statements", "AsyncStatements"]


class Statements(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatementsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return StatementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatementsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return StatementsWithStreamingResponse(self)

    def retrieve(
        self,
        statement_token: str,
        *,
        financial_account_token: str,
        installment_plan_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallmentPlanStatement:
        """
        Get a specific statement snapshot for a given installment plan.

        Args:
          financial_account_token: Globally unique identifier for financial account.

          installment_plan_token: Globally unique identifier for installment plan.

          statement_token: Globally unique identifier for statement.

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
        if not statement_token:
            raise ValueError(f"Expected a non-empty value for `statement_token` but received {statement_token!r}")
        return self._get(
            path_template(
                "/v1/financial_accounts/{financial_account_token}/installment_plans/{installment_plan_token}/statements/{statement_token}",
                financial_account_token=financial_account_token,
                installment_plan_token=installment_plan_token,
                statement_token=statement_token,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstallmentPlanStatement,
        )

    def list(
        self,
        installment_plan_token: str,
        *,
        financial_account_token: str,
        begin: Union[str, date] | Omit = omit,
        end: Union[str, date] | Omit = omit,
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
    ) -> SyncCursorPage[InstallmentPlanStatement]:
        """
        List the statement snapshots for a given installment plan.

        Args:
          financial_account_token: Globally unique identifier for financial account.

          installment_plan_token: Globally unique identifier for installment plan.

          begin: Date string in RFC 3339 format. Only entries created after the specified date
              will be included.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          state: Only snapshots in which the plan was in this state will be included.

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
        return self._get_api_list(
            path_template(
                "/v1/financial_accounts/{financial_account_token}/installment_plans/{installment_plan_token}/statements",
                financial_account_token=financial_account_token,
                installment_plan_token=installment_plan_token,
            ),
            page=SyncCursorPage[InstallmentPlanStatement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "state": state,
                    },
                    statement_list_params.StatementListParams,
                ),
            ),
            model=InstallmentPlanStatement,
        )


class AsyncStatements(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatementsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatementsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatementsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncStatementsWithStreamingResponse(self)

    async def retrieve(
        self,
        statement_token: str,
        *,
        financial_account_token: str,
        installment_plan_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InstallmentPlanStatement:
        """
        Get a specific statement snapshot for a given installment plan.

        Args:
          financial_account_token: Globally unique identifier for financial account.

          installment_plan_token: Globally unique identifier for installment plan.

          statement_token: Globally unique identifier for statement.

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
        if not statement_token:
            raise ValueError(f"Expected a non-empty value for `statement_token` but received {statement_token!r}")
        return await self._get(
            path_template(
                "/v1/financial_accounts/{financial_account_token}/installment_plans/{installment_plan_token}/statements/{statement_token}",
                financial_account_token=financial_account_token,
                installment_plan_token=installment_plan_token,
                statement_token=statement_token,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InstallmentPlanStatement,
        )

    def list(
        self,
        installment_plan_token: str,
        *,
        financial_account_token: str,
        begin: Union[str, date] | Omit = omit,
        end: Union[str, date] | Omit = omit,
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
    ) -> AsyncPaginator[InstallmentPlanStatement, AsyncCursorPage[InstallmentPlanStatement]]:
        """
        List the statement snapshots for a given installment plan.

        Args:
          financial_account_token: Globally unique identifier for financial account.

          installment_plan_token: Globally unique identifier for installment plan.

          begin: Date string in RFC 3339 format. Only entries created after the specified date
              will be included.

          end: Date string in RFC 3339 format. Only entries created before the specified date
              will be included.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          state: Only snapshots in which the plan was in this state will be included.

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
        return self._get_api_list(
            path_template(
                "/v1/financial_accounts/{financial_account_token}/installment_plans/{installment_plan_token}/statements",
                financial_account_token=financial_account_token,
                installment_plan_token=installment_plan_token,
            ),
            page=AsyncCursorPage[InstallmentPlanStatement],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "state": state,
                    },
                    statement_list_params.StatementListParams,
                ),
            ),
            model=InstallmentPlanStatement,
        )


class StatementsWithRawResponse:
    def __init__(self, statements: Statements) -> None:
        self._statements = statements

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            statements.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            statements.list,
        )


class AsyncStatementsWithRawResponse:
    def __init__(self, statements: AsyncStatements) -> None:
        self._statements = statements

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            statements.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            statements.list,
        )


class StatementsWithStreamingResponse:
    def __init__(self, statements: Statements) -> None:
        self._statements = statements

        self.retrieve = to_streamed_response_wrapper(
            statements.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            statements.list,
        )


class AsyncStatementsWithStreamingResponse:
    def __init__(self, statements: AsyncStatements) -> None:
        self._statements = statements

        self.retrieve = async_to_streamed_response_wrapper(
            statements.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            statements.list,
        )
