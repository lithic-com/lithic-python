# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime

import httpx

from .... import _legacy_response
from .files import (
    Files,
    AsyncFiles,
    FilesWithRawResponse,
    AsyncFilesWithRawResponse,
    FilesWithStreamingResponse,
    AsyncFilesWithStreamingResponse,
)
from .comments import (
    Comments,
    AsyncComments,
    CommentsWithRawResponse,
    AsyncCommentsWithRawResponse,
    CommentsWithStreamingResponse,
    AsyncCommentsWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ....pagination import SyncCursorPage, AsyncCursorPage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.transaction_monitoring import (
    CaseStatus,
    CasePriority,
    CaseSortOrder,
    ResolutionOutcome,
    case_list_params,
    case_update_params,
    case_list_activity_params,
    case_list_transactions_params,
)
from ....types.transaction_monitoring.case_status import CaseStatus
from ....types.transaction_monitoring.case_priority import CasePriority
from ....types.transaction_monitoring.case_sort_order import CaseSortOrder
from ....types.transaction_monitoring.monitoring_case import MonitoringCase
from ....types.transaction_monitoring.case_transaction import CaseTransaction
from ....types.transaction_monitoring.resolution_outcome import ResolutionOutcome
from ....types.transaction_monitoring.case_activity_entry import CaseActivityEntry
from ....types.transaction_monitoring.case_retrieve_cards_response import CaseRetrieveCardsResponse

__all__ = ["Cases", "AsyncCases"]


class Cases(SyncAPIResource):
    @cached_property
    def comments(self) -> Comments:
        return Comments(self._client)

    @cached_property
    def files(self) -> Files:
        return Files(self._client)

    @cached_property
    def with_raw_response(self) -> CasesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return CasesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CasesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return CasesWithStreamingResponse(self)

    def retrieve(
        self,
        case_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitoringCase:
        """
        Retrieves a single transaction monitoring case.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        return self._get(
            path_template("/v1/transaction_monitoring/cases/{case_token}", case_token=case_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitoringCase,
        )

    def update(
        self,
        case_token: str,
        *,
        actor_token: str | Omit = omit,
        assignee: Optional[str] | Omit = omit,
        priority: CasePriority | Omit = omit,
        resolution: ResolutionOutcome | Omit = omit,
        resolution_notes: str | Omit = omit,
        sla_deadline: Union[str, datetime, None] | Omit = omit,
        status: CaseStatus | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitoringCase:
        """
        Updates a transaction monitoring case.

        Args:
          actor_token: Optional client-provided identifier for the actor performing this action,
              recorded on the resulting activity entry. This value is supplied by the client
              (for example, your own internal user ID) and is not authenticated by Lithic

          assignee: New assignee for the case, or `null` to unassign

          priority: Priority level of a case, controlling queue ordering and SLA urgency

          resolution:
              Outcome recorded when a case is resolved:

              - `CONFIRMED_FRAUD` - The reviewed activity was confirmed to be fraudulent
              - `SUSPICIOUS_ACTIVITY` - The activity is suspicious but not confirmed fraud
              - `FALSE_POSITIVE` - The activity was legitimate and the alert was a false
                positive
              - `NO_ACTION_REQUIRED` - No further action is required
              - `ESCALATED_EXTERNAL` - The case was escalated to an external party

          resolution_notes: Notes describing the resolution

          sla_deadline: New SLA deadline for the case, or `null` to clear it

          status:
              Status of a case as it progresses through the review workflow:

              - `OPEN` - The case has been created and is still collecting matching
                transactions
              - `ASSIGNED` - An analyst has been assigned and transaction collection has
                stopped
              - `IN_REVIEW` - The case is actively being investigated
              - `ESCALATED` - The case has been reviewed and requires additional oversight
              - `RESOLVED` - A determination has been made and a resolution recorded
              - `CLOSED` - The case is finalized

          tags: Arbitrary key-value metadata to set on the case

          title: New title for the case, or `null` to clear it

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        return self._patch(
            path_template("/v1/transaction_monitoring/cases/{case_token}", case_token=case_token),
            body=maybe_transform(
                {
                    "actor_token": actor_token,
                    "assignee": assignee,
                    "priority": priority,
                    "resolution": resolution,
                    "resolution_notes": resolution_notes,
                    "sla_deadline": sla_deadline,
                    "status": status,
                    "tags": tags,
                    "title": title,
                },
                case_update_params.CaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitoringCase,
        )

    def list(
        self,
        *,
        account_token: str | Omit = omit,
        assignee: str | Omit = omit,
        begin: Union[str, datetime] | Omit = omit,
        card_token: str | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        ending_before: str | Omit = omit,
        entity_token: str | Omit = omit,
        page_size: int | Omit = omit,
        queue_token: str | Omit = omit,
        rule_token: str | Omit = omit,
        sort_by: CaseSortOrder | Omit = omit,
        starting_after: str | Omit = omit,
        status: CaseStatus | Omit = omit,
        transaction_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[MonitoringCase]:
        """
        Lists transaction monitoring cases, optionally filtered.

        Args:
          account_token: Only return cases that include transactions on the provided account.

          assignee: Only return cases assigned to the provided value. Pass an empty string to return
              only unassigned cases.

          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          card_token: Only return cases that include transactions on the provided card.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          entity_token: Only return cases associated with the provided entity.

          page_size: Page size (for pagination).

          queue_token: Only return cases belonging to the provided queue.

          rule_token: Only return cases triggered by the provided transaction monitoring rule.

          sort_by: Sort order for the returned cases.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Only return cases with the provided status.

          transaction_token: Only return cases that include the provided transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/transaction_monitoring/cases",
            page=SyncCursorPage[MonitoringCase],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "assignee": assignee,
                        "begin": begin,
                        "card_token": card_token,
                        "end": end,
                        "ending_before": ending_before,
                        "entity_token": entity_token,
                        "page_size": page_size,
                        "queue_token": queue_token,
                        "rule_token": rule_token,
                        "sort_by": sort_by,
                        "starting_after": starting_after,
                        "status": status,
                        "transaction_token": transaction_token,
                    },
                    case_list_params.CaseListParams,
                ),
            ),
            model=MonitoringCase,
        )

    def list_activity(
        self,
        case_token: str,
        *,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CaseActivityEntry]:
        """
        Lists the activity feed for a case.

        Args:
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
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        return self._get_api_list(
            path_template("/v1/transaction_monitoring/cases/{case_token}/activity", case_token=case_token),
            page=SyncCursorPage[CaseActivityEntry],
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
                    },
                    case_list_activity_params.CaseListActivityParams,
                ),
            ),
            model=CaseActivityEntry,
        )

    def list_transactions(
        self,
        case_token: str,
        *,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[CaseTransaction]:
        """
        Lists the transactions associated with a case.

        Args:
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
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        return self._get_api_list(
            path_template("/v1/transaction_monitoring/cases/{case_token}/transactions", case_token=case_token),
            page=SyncCursorPage[CaseTransaction],
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
                    },
                    case_list_transactions_params.CaseListTransactionsParams,
                ),
            ),
            model=CaseTransaction,
        )

    def retrieve_cards(
        self,
        case_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaseRetrieveCardsResponse:
        """
        Lists the cards involved in a case, with per-card transaction counts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        return self._get(
            path_template("/v1/transaction_monitoring/cases/{case_token}/cards", case_token=case_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaseRetrieveCardsResponse,
        )


class AsyncCases(AsyncAPIResource):
    @cached_property
    def comments(self) -> AsyncComments:
        return AsyncComments(self._client)

    @cached_property
    def files(self) -> AsyncFiles:
        return AsyncFiles(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCasesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCasesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCasesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncCasesWithStreamingResponse(self)

    async def retrieve(
        self,
        case_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitoringCase:
        """
        Retrieves a single transaction monitoring case.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        return await self._get(
            path_template("/v1/transaction_monitoring/cases/{case_token}", case_token=case_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitoringCase,
        )

    async def update(
        self,
        case_token: str,
        *,
        actor_token: str | Omit = omit,
        assignee: Optional[str] | Omit = omit,
        priority: CasePriority | Omit = omit,
        resolution: ResolutionOutcome | Omit = omit,
        resolution_notes: str | Omit = omit,
        sla_deadline: Union[str, datetime, None] | Omit = omit,
        status: CaseStatus | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MonitoringCase:
        """
        Updates a transaction monitoring case.

        Args:
          actor_token: Optional client-provided identifier for the actor performing this action,
              recorded on the resulting activity entry. This value is supplied by the client
              (for example, your own internal user ID) and is not authenticated by Lithic

          assignee: New assignee for the case, or `null` to unassign

          priority: Priority level of a case, controlling queue ordering and SLA urgency

          resolution:
              Outcome recorded when a case is resolved:

              - `CONFIRMED_FRAUD` - The reviewed activity was confirmed to be fraudulent
              - `SUSPICIOUS_ACTIVITY` - The activity is suspicious but not confirmed fraud
              - `FALSE_POSITIVE` - The activity was legitimate and the alert was a false
                positive
              - `NO_ACTION_REQUIRED` - No further action is required
              - `ESCALATED_EXTERNAL` - The case was escalated to an external party

          resolution_notes: Notes describing the resolution

          sla_deadline: New SLA deadline for the case, or `null` to clear it

          status:
              Status of a case as it progresses through the review workflow:

              - `OPEN` - The case has been created and is still collecting matching
                transactions
              - `ASSIGNED` - An analyst has been assigned and transaction collection has
                stopped
              - `IN_REVIEW` - The case is actively being investigated
              - `ESCALATED` - The case has been reviewed and requires additional oversight
              - `RESOLVED` - A determination has been made and a resolution recorded
              - `CLOSED` - The case is finalized

          tags: Arbitrary key-value metadata to set on the case

          title: New title for the case, or `null` to clear it

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        return await self._patch(
            path_template("/v1/transaction_monitoring/cases/{case_token}", case_token=case_token),
            body=await async_maybe_transform(
                {
                    "actor_token": actor_token,
                    "assignee": assignee,
                    "priority": priority,
                    "resolution": resolution,
                    "resolution_notes": resolution_notes,
                    "sla_deadline": sla_deadline,
                    "status": status,
                    "tags": tags,
                    "title": title,
                },
                case_update_params.CaseUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MonitoringCase,
        )

    def list(
        self,
        *,
        account_token: str | Omit = omit,
        assignee: str | Omit = omit,
        begin: Union[str, datetime] | Omit = omit,
        card_token: str | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        ending_before: str | Omit = omit,
        entity_token: str | Omit = omit,
        page_size: int | Omit = omit,
        queue_token: str | Omit = omit,
        rule_token: str | Omit = omit,
        sort_by: CaseSortOrder | Omit = omit,
        starting_after: str | Omit = omit,
        status: CaseStatus | Omit = omit,
        transaction_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[MonitoringCase, AsyncCursorPage[MonitoringCase]]:
        """
        Lists transaction monitoring cases, optionally filtered.

        Args:
          account_token: Only return cases that include transactions on the provided account.

          assignee: Only return cases assigned to the provided value. Pass an empty string to return
              only unassigned cases.

          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          card_token: Only return cases that include transactions on the provided card.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          entity_token: Only return cases associated with the provided entity.

          page_size: Page size (for pagination).

          queue_token: Only return cases belonging to the provided queue.

          rule_token: Only return cases triggered by the provided transaction monitoring rule.

          sort_by: Sort order for the returned cases.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Only return cases with the provided status.

          transaction_token: Only return cases that include the provided transaction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/transaction_monitoring/cases",
            page=AsyncCursorPage[MonitoringCase],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "assignee": assignee,
                        "begin": begin,
                        "card_token": card_token,
                        "end": end,
                        "ending_before": ending_before,
                        "entity_token": entity_token,
                        "page_size": page_size,
                        "queue_token": queue_token,
                        "rule_token": rule_token,
                        "sort_by": sort_by,
                        "starting_after": starting_after,
                        "status": status,
                        "transaction_token": transaction_token,
                    },
                    case_list_params.CaseListParams,
                ),
            ),
            model=MonitoringCase,
        )

    def list_activity(
        self,
        case_token: str,
        *,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CaseActivityEntry, AsyncCursorPage[CaseActivityEntry]]:
        """
        Lists the activity feed for a case.

        Args:
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
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        return self._get_api_list(
            path_template("/v1/transaction_monitoring/cases/{case_token}/activity", case_token=case_token),
            page=AsyncCursorPage[CaseActivityEntry],
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
                    },
                    case_list_activity_params.CaseListActivityParams,
                ),
            ),
            model=CaseActivityEntry,
        )

    def list_transactions(
        self,
        case_token: str,
        *,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CaseTransaction, AsyncCursorPage[CaseTransaction]]:
        """
        Lists the transactions associated with a case.

        Args:
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
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        return self._get_api_list(
            path_template("/v1/transaction_monitoring/cases/{case_token}/transactions", case_token=case_token),
            page=AsyncCursorPage[CaseTransaction],
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
                    },
                    case_list_transactions_params.CaseListTransactionsParams,
                ),
            ),
            model=CaseTransaction,
        )

    async def retrieve_cards(
        self,
        case_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaseRetrieveCardsResponse:
        """
        Lists the cards involved in a case, with per-card transaction counts.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        return await self._get(
            path_template("/v1/transaction_monitoring/cases/{case_token}/cards", case_token=case_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaseRetrieveCardsResponse,
        )


class CasesWithRawResponse:
    def __init__(self, cases: Cases) -> None:
        self._cases = cases

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            cases.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            cases.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            cases.list,
        )
        self.list_activity = _legacy_response.to_raw_response_wrapper(
            cases.list_activity,
        )
        self.list_transactions = _legacy_response.to_raw_response_wrapper(
            cases.list_transactions,
        )
        self.retrieve_cards = _legacy_response.to_raw_response_wrapper(
            cases.retrieve_cards,
        )

    @cached_property
    def comments(self) -> CommentsWithRawResponse:
        return CommentsWithRawResponse(self._cases.comments)

    @cached_property
    def files(self) -> FilesWithRawResponse:
        return FilesWithRawResponse(self._cases.files)


class AsyncCasesWithRawResponse:
    def __init__(self, cases: AsyncCases) -> None:
        self._cases = cases

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            cases.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            cases.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            cases.list,
        )
        self.list_activity = _legacy_response.async_to_raw_response_wrapper(
            cases.list_activity,
        )
        self.list_transactions = _legacy_response.async_to_raw_response_wrapper(
            cases.list_transactions,
        )
        self.retrieve_cards = _legacy_response.async_to_raw_response_wrapper(
            cases.retrieve_cards,
        )

    @cached_property
    def comments(self) -> AsyncCommentsWithRawResponse:
        return AsyncCommentsWithRawResponse(self._cases.comments)

    @cached_property
    def files(self) -> AsyncFilesWithRawResponse:
        return AsyncFilesWithRawResponse(self._cases.files)


class CasesWithStreamingResponse:
    def __init__(self, cases: Cases) -> None:
        self._cases = cases

        self.retrieve = to_streamed_response_wrapper(
            cases.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            cases.update,
        )
        self.list = to_streamed_response_wrapper(
            cases.list,
        )
        self.list_activity = to_streamed_response_wrapper(
            cases.list_activity,
        )
        self.list_transactions = to_streamed_response_wrapper(
            cases.list_transactions,
        )
        self.retrieve_cards = to_streamed_response_wrapper(
            cases.retrieve_cards,
        )

    @cached_property
    def comments(self) -> CommentsWithStreamingResponse:
        return CommentsWithStreamingResponse(self._cases.comments)

    @cached_property
    def files(self) -> FilesWithStreamingResponse:
        return FilesWithStreamingResponse(self._cases.files)


class AsyncCasesWithStreamingResponse:
    def __init__(self, cases: AsyncCases) -> None:
        self._cases = cases

        self.retrieve = async_to_streamed_response_wrapper(
            cases.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            cases.update,
        )
        self.list = async_to_streamed_response_wrapper(
            cases.list,
        )
        self.list_activity = async_to_streamed_response_wrapper(
            cases.list_activity,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            cases.list_transactions,
        )
        self.retrieve_cards = async_to_streamed_response_wrapper(
            cases.retrieve_cards,
        )

    @cached_property
    def comments(self) -> AsyncCommentsWithStreamingResponse:
        return AsyncCommentsWithStreamingResponse(self._cases.comments)

    @cached_property
    def files(self) -> AsyncFilesWithStreamingResponse:
        return AsyncFilesWithStreamingResponse(self._cases.files)
