# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    management_operation_list_params,
    management_operation_create_params,
    management_operation_reverse_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.management_operation_transaction import ManagementOperationTransaction

__all__ = ["ManagementOperations", "AsyncManagementOperations"]


class ManagementOperations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ManagementOperationsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return ManagementOperationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ManagementOperationsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return ManagementOperationsWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        category: Literal["MANAGEMENT_FEE", "MANAGEMENT_DISPUTE", "MANAGEMENT_REWARD", "MANAGEMENT_ADJUSTMENT"],
        direction: Literal["CREDIT", "DEBIT"],
        effective_date: Union[str, date],
        event_type: Literal[
            "CASH_BACK",
            "CURRENCY_CONVERSION",
            "INTEREST",
            "LATE_PAYMENT",
            "BILLING_ERROR",
            "PROVISIONAL_CREDIT",
            "CASH_BACK_REVERSAL",
            "CURRENCY_CONVERSION_REVERSAL",
            "INTEREST_REVERSAL",
            "LATE_PAYMENT_REVERSAL",
            "BILLING_ERROR_REVERSAL",
            "PROVISIONAL_CREDIT_REVERSAL",
            "RETURNED_PAYMENT",
            "RETURNED_PAYMENT_REVERSAL",
        ],
        financial_account_token: str,
        token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        subtype: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagementOperationTransaction:
        """
        Create management operation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/management_operations",
            body=maybe_transform(
                {
                    "amount": amount,
                    "category": category,
                    "direction": direction,
                    "effective_date": effective_date,
                    "event_type": event_type,
                    "financial_account_token": financial_account_token,
                    "token": token,
                    "memo": memo,
                    "subtype": subtype,
                    "user_defined_id": user_defined_id,
                },
                management_operation_create_params.ManagementOperationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagementOperationTransaction,
        )

    def retrieve(
        self,
        management_operation_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagementOperationTransaction:
        """
        Get management operation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not management_operation_token:
            raise ValueError(
                f"Expected a non-empty value for `management_operation_token` but received {management_operation_token!r}"
            )
        return self._get(
            f"/v1/management_operations/{management_operation_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagementOperationTransaction,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        category: Literal["MANAGEMENT_FEE", "MANAGEMENT_DISPUTE", "MANAGEMENT_REWARD", "MANAGEMENT_ADJUSTMENT"]
        | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[ManagementOperationTransaction]:
        """List management operations

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          category: Management operation category to be returned.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          financial_account_token: Globally unique identifier for the financial account. Accepted type dependent on
              the program's use case.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Management operation status to be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/management_operations",
            page=SyncCursorPage[ManagementOperationTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "business_account_token": business_account_token,
                        "category": category,
                        "end": end,
                        "ending_before": ending_before,
                        "financial_account_token": financial_account_token,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    management_operation_list_params.ManagementOperationListParams,
                ),
            ),
            model=ManagementOperationTransaction,
        )

    def reverse(
        self,
        management_operation_token: str,
        *,
        effective_date: Union[str, date],
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagementOperationTransaction:
        """
        Reverse a management operation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not management_operation_token:
            raise ValueError(
                f"Expected a non-empty value for `management_operation_token` but received {management_operation_token!r}"
            )
        return self._post(
            f"/v1/management_operations/{management_operation_token}/reverse",
            body=maybe_transform(
                {
                    "effective_date": effective_date,
                    "memo": memo,
                },
                management_operation_reverse_params.ManagementOperationReverseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagementOperationTransaction,
        )


class AsyncManagementOperations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncManagementOperationsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncManagementOperationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncManagementOperationsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncManagementOperationsWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        category: Literal["MANAGEMENT_FEE", "MANAGEMENT_DISPUTE", "MANAGEMENT_REWARD", "MANAGEMENT_ADJUSTMENT"],
        direction: Literal["CREDIT", "DEBIT"],
        effective_date: Union[str, date],
        event_type: Literal[
            "CASH_BACK",
            "CURRENCY_CONVERSION",
            "INTEREST",
            "LATE_PAYMENT",
            "BILLING_ERROR",
            "PROVISIONAL_CREDIT",
            "CASH_BACK_REVERSAL",
            "CURRENCY_CONVERSION_REVERSAL",
            "INTEREST_REVERSAL",
            "LATE_PAYMENT_REVERSAL",
            "BILLING_ERROR_REVERSAL",
            "PROVISIONAL_CREDIT_REVERSAL",
            "RETURNED_PAYMENT",
            "RETURNED_PAYMENT_REVERSAL",
        ],
        financial_account_token: str,
        token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        subtype: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagementOperationTransaction:
        """
        Create management operation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/management_operations",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "category": category,
                    "direction": direction,
                    "effective_date": effective_date,
                    "event_type": event_type,
                    "financial_account_token": financial_account_token,
                    "token": token,
                    "memo": memo,
                    "subtype": subtype,
                    "user_defined_id": user_defined_id,
                },
                management_operation_create_params.ManagementOperationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagementOperationTransaction,
        )

    async def retrieve(
        self,
        management_operation_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagementOperationTransaction:
        """
        Get management operation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not management_operation_token:
            raise ValueError(
                f"Expected a non-empty value for `management_operation_token` but received {management_operation_token!r}"
            )
        return await self._get(
            f"/v1/management_operations/{management_operation_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagementOperationTransaction,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        category: Literal["MANAGEMENT_FEE", "MANAGEMENT_DISPUTE", "MANAGEMENT_REWARD", "MANAGEMENT_ADJUSTMENT"]
        | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ManagementOperationTransaction, AsyncCursorPage[ManagementOperationTransaction]]:
        """List management operations

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          category: Management operation category to be returned.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          financial_account_token: Globally unique identifier for the financial account. Accepted type dependent on
              the program's use case.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Management operation status to be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/management_operations",
            page=AsyncCursorPage[ManagementOperationTransaction],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "begin": begin,
                        "business_account_token": business_account_token,
                        "category": category,
                        "end": end,
                        "ending_before": ending_before,
                        "financial_account_token": financial_account_token,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    management_operation_list_params.ManagementOperationListParams,
                ),
            ),
            model=ManagementOperationTransaction,
        )

    async def reverse(
        self,
        management_operation_token: str,
        *,
        effective_date: Union[str, date],
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ManagementOperationTransaction:
        """
        Reverse a management operation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not management_operation_token:
            raise ValueError(
                f"Expected a non-empty value for `management_operation_token` but received {management_operation_token!r}"
            )
        return await self._post(
            f"/v1/management_operations/{management_operation_token}/reverse",
            body=await async_maybe_transform(
                {
                    "effective_date": effective_date,
                    "memo": memo,
                },
                management_operation_reverse_params.ManagementOperationReverseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagementOperationTransaction,
        )


class ManagementOperationsWithRawResponse:
    def __init__(self, management_operations: ManagementOperations) -> None:
        self._management_operations = management_operations

        self.create = _legacy_response.to_raw_response_wrapper(
            management_operations.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            management_operations.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            management_operations.list,
        )
        self.reverse = _legacy_response.to_raw_response_wrapper(
            management_operations.reverse,
        )


class AsyncManagementOperationsWithRawResponse:
    def __init__(self, management_operations: AsyncManagementOperations) -> None:
        self._management_operations = management_operations

        self.create = _legacy_response.async_to_raw_response_wrapper(
            management_operations.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            management_operations.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            management_operations.list,
        )
        self.reverse = _legacy_response.async_to_raw_response_wrapper(
            management_operations.reverse,
        )


class ManagementOperationsWithStreamingResponse:
    def __init__(self, management_operations: ManagementOperations) -> None:
        self._management_operations = management_operations

        self.create = to_streamed_response_wrapper(
            management_operations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            management_operations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            management_operations.list,
        )
        self.reverse = to_streamed_response_wrapper(
            management_operations.reverse,
        )


class AsyncManagementOperationsWithStreamingResponse:
    def __init__(self, management_operations: AsyncManagementOperations) -> None:
        self._management_operations = management_operations

        self.create = async_to_streamed_response_wrapper(
            management_operations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            management_operations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            management_operations.list,
        )
        self.reverse = async_to_streamed_response_wrapper(
            management_operations.reverse,
        )
