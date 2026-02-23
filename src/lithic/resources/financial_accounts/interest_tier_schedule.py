# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.financial_accounts import (
    interest_tier_schedule_list_params,
    interest_tier_schedule_create_params,
    interest_tier_schedule_update_params,
)
from ...types.financial_accounts.interest_tier_schedule import InterestTierSchedule

__all__ = ["InterestTierScheduleResource", "AsyncInterestTierScheduleResource"]


class InterestTierScheduleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InterestTierScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return InterestTierScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InterestTierScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return InterestTierScheduleResourceWithStreamingResponse(self)

    def create(
        self,
        financial_account_token: str,
        *,
        credit_product_token: str,
        effective_date: Union[str, date],
        tier_name: str | Omit = omit,
        tier_rates: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InterestTierSchedule:
        """
        Create a new interest tier schedule entry for a supported financial account

        Args:
          credit_product_token: Globally unique identifier for a credit product

          effective_date: Date the tier should be effective in YYYY-MM-DD format

          tier_name: Name of a tier contained in the credit product. Mutually exclusive with
              tier_rates

          tier_rates: Custom rates per category. Mutually exclusive with tier_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        return self._post(
            f"/v1/financial_accounts/{financial_account_token}/interest_tier_schedule",
            body=maybe_transform(
                {
                    "credit_product_token": credit_product_token,
                    "effective_date": effective_date,
                    "tier_name": tier_name,
                    "tier_rates": tier_rates,
                },
                interest_tier_schedule_create_params.InterestTierScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InterestTierSchedule,
        )

    def retrieve(
        self,
        effective_date: Union[str, date],
        *,
        financial_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InterestTierSchedule:
        """
        Get a specific interest tier schedule by effective date

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        if not effective_date:
            raise ValueError(f"Expected a non-empty value for `effective_date` but received {effective_date!r}")
        return self._get(
            f"/v1/financial_accounts/{financial_account_token}/interest_tier_schedule/{effective_date}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InterestTierSchedule,
        )

    def update(
        self,
        effective_date: Union[str, date],
        *,
        financial_account_token: str,
        tier_name: str | Omit = omit,
        tier_rates: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InterestTierSchedule:
        """
        Update an existing interest tier schedule

        Args:
          tier_name: Name of a tier contained in the credit product. Mutually exclusive with
              tier_rates

          tier_rates: Custom rates per category. Mutually exclusive with tier_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        if not effective_date:
            raise ValueError(f"Expected a non-empty value for `effective_date` but received {effective_date!r}")
        return self._put(
            f"/v1/financial_accounts/{financial_account_token}/interest_tier_schedule/{effective_date}",
            body=maybe_transform(
                {
                    "tier_name": tier_name,
                    "tier_rates": tier_rates,
                },
                interest_tier_schedule_update_params.InterestTierScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InterestTierSchedule,
        )

    def list(
        self,
        financial_account_token: str,
        *,
        after_date: Union[str, date] | Omit = omit,
        before_date: Union[str, date] | Omit = omit,
        for_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[InterestTierSchedule]:
        """
        List interest tier schedules for a financial account with optional date
        filtering.

        If no date parameters are provided, returns all tier schedules. If date
        parameters are provided, uses filtering to return matching schedules (max 100).

        - for_date: Returns exact match (takes precedence over other dates)
        - before_date: Returns schedules with effective_date <= before_date
        - after_date: Returns schedules with effective_date >= after_date
        - Both before_date and after_date: Returns schedules in range

        Args:
          after_date: Return schedules with effective_date >= after_date (ISO format YYYY-MM-DD)

          before_date: Return schedules with effective_date <= before_date (ISO format YYYY-MM-DD)

          for_date: Return schedule with effective_date == for_date (ISO format YYYY-MM-DD)

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
            f"/v1/financial_accounts/{financial_account_token}/interest_tier_schedule",
            page=SyncSinglePage[InterestTierSchedule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_date": after_date,
                        "before_date": before_date,
                        "for_date": for_date,
                    },
                    interest_tier_schedule_list_params.InterestTierScheduleListParams,
                ),
            ),
            model=InterestTierSchedule,
        )

    def delete(
        self,
        effective_date: Union[str, date],
        *,
        financial_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an interest tier schedule entry.

        Returns:

        - 400 Bad Request: Invalid effective_date format OR attempting to delete the
          earliest tier schedule entry for a non-PENDING account
        - 404 Not Found: Tier schedule entry not found for the given effective_date OR
          ledger account not found

        Note: PENDING accounts can delete the earliest tier schedule entry (account
        hasn't opened yet). Active/non-PENDING accounts cannot delete the earliest entry
        to prevent orphaning the account.

        If the deleted tier schedule has a past effective_date and the account is
        ACTIVE, the loan tape rebuild configuration will be updated to trigger rebuilds
        from that date.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        if not effective_date:
            raise ValueError(f"Expected a non-empty value for `effective_date` but received {effective_date!r}")
        return self._delete(
            f"/v1/financial_accounts/{financial_account_token}/interest_tier_schedule/{effective_date}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncInterestTierScheduleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInterestTierScheduleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInterestTierScheduleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInterestTierScheduleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncInterestTierScheduleResourceWithStreamingResponse(self)

    async def create(
        self,
        financial_account_token: str,
        *,
        credit_product_token: str,
        effective_date: Union[str, date],
        tier_name: str | Omit = omit,
        tier_rates: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InterestTierSchedule:
        """
        Create a new interest tier schedule entry for a supported financial account

        Args:
          credit_product_token: Globally unique identifier for a credit product

          effective_date: Date the tier should be effective in YYYY-MM-DD format

          tier_name: Name of a tier contained in the credit product. Mutually exclusive with
              tier_rates

          tier_rates: Custom rates per category. Mutually exclusive with tier_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        return await self._post(
            f"/v1/financial_accounts/{financial_account_token}/interest_tier_schedule",
            body=await async_maybe_transform(
                {
                    "credit_product_token": credit_product_token,
                    "effective_date": effective_date,
                    "tier_name": tier_name,
                    "tier_rates": tier_rates,
                },
                interest_tier_schedule_create_params.InterestTierScheduleCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InterestTierSchedule,
        )

    async def retrieve(
        self,
        effective_date: Union[str, date],
        *,
        financial_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InterestTierSchedule:
        """
        Get a specific interest tier schedule by effective date

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        if not effective_date:
            raise ValueError(f"Expected a non-empty value for `effective_date` but received {effective_date!r}")
        return await self._get(
            f"/v1/financial_accounts/{financial_account_token}/interest_tier_schedule/{effective_date}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InterestTierSchedule,
        )

    async def update(
        self,
        effective_date: Union[str, date],
        *,
        financial_account_token: str,
        tier_name: str | Omit = omit,
        tier_rates: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InterestTierSchedule:
        """
        Update an existing interest tier schedule

        Args:
          tier_name: Name of a tier contained in the credit product. Mutually exclusive with
              tier_rates

          tier_rates: Custom rates per category. Mutually exclusive with tier_name

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        if not effective_date:
            raise ValueError(f"Expected a non-empty value for `effective_date` but received {effective_date!r}")
        return await self._put(
            f"/v1/financial_accounts/{financial_account_token}/interest_tier_schedule/{effective_date}",
            body=await async_maybe_transform(
                {
                    "tier_name": tier_name,
                    "tier_rates": tier_rates,
                },
                interest_tier_schedule_update_params.InterestTierScheduleUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InterestTierSchedule,
        )

    def list(
        self,
        financial_account_token: str,
        *,
        after_date: Union[str, date] | Omit = omit,
        before_date: Union[str, date] | Omit = omit,
        for_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[InterestTierSchedule, AsyncSinglePage[InterestTierSchedule]]:
        """
        List interest tier schedules for a financial account with optional date
        filtering.

        If no date parameters are provided, returns all tier schedules. If date
        parameters are provided, uses filtering to return matching schedules (max 100).

        - for_date: Returns exact match (takes precedence over other dates)
        - before_date: Returns schedules with effective_date <= before_date
        - after_date: Returns schedules with effective_date >= after_date
        - Both before_date and after_date: Returns schedules in range

        Args:
          after_date: Return schedules with effective_date >= after_date (ISO format YYYY-MM-DD)

          before_date: Return schedules with effective_date <= before_date (ISO format YYYY-MM-DD)

          for_date: Return schedule with effective_date == for_date (ISO format YYYY-MM-DD)

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
            f"/v1/financial_accounts/{financial_account_token}/interest_tier_schedule",
            page=AsyncSinglePage[InterestTierSchedule],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after_date": after_date,
                        "before_date": before_date,
                        "for_date": for_date,
                    },
                    interest_tier_schedule_list_params.InterestTierScheduleListParams,
                ),
            ),
            model=InterestTierSchedule,
        )

    async def delete(
        self,
        effective_date: Union[str, date],
        *,
        financial_account_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an interest tier schedule entry.

        Returns:

        - 400 Bad Request: Invalid effective_date format OR attempting to delete the
          earliest tier schedule entry for a non-PENDING account
        - 404 Not Found: Tier schedule entry not found for the given effective_date OR
          ledger account not found

        Note: PENDING accounts can delete the earliest tier schedule entry (account
        hasn't opened yet). Active/non-PENDING accounts cannot delete the earliest entry
        to prevent orphaning the account.

        If the deleted tier schedule has a past effective_date and the account is
        ACTIVE, the loan tape rebuild configuration will be updated to trigger rebuilds
        from that date.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not financial_account_token:
            raise ValueError(
                f"Expected a non-empty value for `financial_account_token` but received {financial_account_token!r}"
            )
        if not effective_date:
            raise ValueError(f"Expected a non-empty value for `effective_date` but received {effective_date!r}")
        return await self._delete(
            f"/v1/financial_accounts/{financial_account_token}/interest_tier_schedule/{effective_date}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class InterestTierScheduleResourceWithRawResponse:
    def __init__(self, interest_tier_schedule: InterestTierScheduleResource) -> None:
        self._interest_tier_schedule = interest_tier_schedule

        self.create = _legacy_response.to_raw_response_wrapper(
            interest_tier_schedule.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            interest_tier_schedule.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            interest_tier_schedule.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            interest_tier_schedule.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            interest_tier_schedule.delete,
        )


class AsyncInterestTierScheduleResourceWithRawResponse:
    def __init__(self, interest_tier_schedule: AsyncInterestTierScheduleResource) -> None:
        self._interest_tier_schedule = interest_tier_schedule

        self.create = _legacy_response.async_to_raw_response_wrapper(
            interest_tier_schedule.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            interest_tier_schedule.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            interest_tier_schedule.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            interest_tier_schedule.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            interest_tier_schedule.delete,
        )


class InterestTierScheduleResourceWithStreamingResponse:
    def __init__(self, interest_tier_schedule: InterestTierScheduleResource) -> None:
        self._interest_tier_schedule = interest_tier_schedule

        self.create = to_streamed_response_wrapper(
            interest_tier_schedule.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            interest_tier_schedule.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            interest_tier_schedule.update,
        )
        self.list = to_streamed_response_wrapper(
            interest_tier_schedule.list,
        )
        self.delete = to_streamed_response_wrapper(
            interest_tier_schedule.delete,
        )


class AsyncInterestTierScheduleResourceWithStreamingResponse:
    def __init__(self, interest_tier_schedule: AsyncInterestTierScheduleResource) -> None:
        self._interest_tier_schedule = interest_tier_schedule

        self.create = async_to_streamed_response_wrapper(
            interest_tier_schedule.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            interest_tier_schedule.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            interest_tier_schedule.update,
        )
        self.list = async_to_streamed_response_wrapper(
            interest_tier_schedule.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            interest_tier_schedule.delete,
        )
