# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import hold_list_params, hold_void_params, hold_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from ..types.hold import Hold
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["Holds", "AsyncHolds"]


class Holds(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HoldsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return HoldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HoldsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return HoldsWithStreamingResponse(self)

    def create(
        self,
        financial_account_token: str,
        *,
        amount: int,
        token: str | Omit = omit,
        expiration_datetime: Union[str, datetime] | Omit = omit,
        memo: Optional[str] | Omit = omit,
        user_defined_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Hold:
        """Create a hold on a financial account.

        Holds reserve funds by moving them from
        available to pending balance. They can be resolved via settlement (linked to a
        payment or book transfer), voiding, or expiration.

        Args:
          amount: Amount to hold in cents

          token: Customer-provided token for idempotency. Becomes the hold token.

          expiration_datetime: When the hold should auto-expire

          memo: Reason for the hold

          user_defined_id: User-provided identifier for the hold

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
            path_template(
                "/v1/financial_accounts/{financial_account_token}/holds",
                financial_account_token=financial_account_token,
            ),
            body=maybe_transform(
                {
                    "amount": amount,
                    "token": token,
                    "expiration_datetime": expiration_datetime,
                    "memo": memo,
                    "user_defined_id": user_defined_id,
                },
                hold_create_params.HoldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Hold,
        )

    def retrieve(
        self,
        hold_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Hold:
        """
        Get hold by token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hold_token:
            raise ValueError(f"Expected a non-empty value for `hold_token` but received {hold_token!r}")
        return self._get(
            path_template("/v1/holds/{hold_token}", hold_token=hold_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Hold,
        )

    def list(
        self,
        financial_account_token: str,
        *,
        begin: Union[str, datetime] | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        status: Literal["PENDING", "SETTLED", "EXPIRED", "VOIDED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Hold]:
        """
        List holds for a financial account.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Hold status to filter by.

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
                "/v1/financial_accounts/{financial_account_token}/holds",
                financial_account_token=financial_account_token,
            ),
            page=SyncCursorPage[Hold],
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
                        "status": status,
                    },
                    hold_list_params.HoldListParams,
                ),
            ),
            model=Hold,
        )

    def void(
        self,
        hold_token: str,
        *,
        memo: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Hold:
        """Void an active hold.

        This returns the held funds from pending back to available
        balance. Only holds in PENDING status can be voided.

        Args:
          memo: Reason for voiding the hold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hold_token:
            raise ValueError(f"Expected a non-empty value for `hold_token` but received {hold_token!r}")
        return self._post(
            path_template("/v1/holds/{hold_token}/void", hold_token=hold_token),
            body=maybe_transform({"memo": memo}, hold_void_params.HoldVoidParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Hold,
        )


class AsyncHolds(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHoldsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHoldsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHoldsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncHoldsWithStreamingResponse(self)

    async def create(
        self,
        financial_account_token: str,
        *,
        amount: int,
        token: str | Omit = omit,
        expiration_datetime: Union[str, datetime] | Omit = omit,
        memo: Optional[str] | Omit = omit,
        user_defined_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Hold:
        """Create a hold on a financial account.

        Holds reserve funds by moving them from
        available to pending balance. They can be resolved via settlement (linked to a
        payment or book transfer), voiding, or expiration.

        Args:
          amount: Amount to hold in cents

          token: Customer-provided token for idempotency. Becomes the hold token.

          expiration_datetime: When the hold should auto-expire

          memo: Reason for the hold

          user_defined_id: User-provided identifier for the hold

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
            path_template(
                "/v1/financial_accounts/{financial_account_token}/holds",
                financial_account_token=financial_account_token,
            ),
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "token": token,
                    "expiration_datetime": expiration_datetime,
                    "memo": memo,
                    "user_defined_id": user_defined_id,
                },
                hold_create_params.HoldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Hold,
        )

    async def retrieve(
        self,
        hold_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Hold:
        """
        Get hold by token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hold_token:
            raise ValueError(f"Expected a non-empty value for `hold_token` but received {hold_token!r}")
        return await self._get(
            path_template("/v1/holds/{hold_token}", hold_token=hold_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Hold,
        )

    def list(
        self,
        financial_account_token: str,
        *,
        begin: Union[str, datetime] | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        status: Literal["PENDING", "SETTLED", "EXPIRED", "VOIDED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Hold, AsyncCursorPage[Hold]]:
        """
        List holds for a financial account.

        Args:
          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Page size (for pagination).

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Hold status to filter by.

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
                "/v1/financial_accounts/{financial_account_token}/holds",
                financial_account_token=financial_account_token,
            ),
            page=AsyncCursorPage[Hold],
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
                        "status": status,
                    },
                    hold_list_params.HoldListParams,
                ),
            ),
            model=Hold,
        )

    async def void(
        self,
        hold_token: str,
        *,
        memo: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Hold:
        """Void an active hold.

        This returns the held funds from pending back to available
        balance. Only holds in PENDING status can be voided.

        Args:
          memo: Reason for voiding the hold

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hold_token:
            raise ValueError(f"Expected a non-empty value for `hold_token` but received {hold_token!r}")
        return await self._post(
            path_template("/v1/holds/{hold_token}/void", hold_token=hold_token),
            body=await async_maybe_transform({"memo": memo}, hold_void_params.HoldVoidParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Hold,
        )


class HoldsWithRawResponse:
    def __init__(self, holds: Holds) -> None:
        self._holds = holds

        self.create = _legacy_response.to_raw_response_wrapper(
            holds.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            holds.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            holds.list,
        )
        self.void = _legacy_response.to_raw_response_wrapper(
            holds.void,
        )


class AsyncHoldsWithRawResponse:
    def __init__(self, holds: AsyncHolds) -> None:
        self._holds = holds

        self.create = _legacy_response.async_to_raw_response_wrapper(
            holds.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            holds.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            holds.list,
        )
        self.void = _legacy_response.async_to_raw_response_wrapper(
            holds.void,
        )


class HoldsWithStreamingResponse:
    def __init__(self, holds: Holds) -> None:
        self._holds = holds

        self.create = to_streamed_response_wrapper(
            holds.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            holds.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            holds.list,
        )
        self.void = to_streamed_response_wrapper(
            holds.void,
        )


class AsyncHoldsWithStreamingResponse:
    def __init__(self, holds: AsyncHolds) -> None:
        self._holds = holds

        self.create = async_to_streamed_response_wrapper(
            holds.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            holds.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            holds.list,
        )
        self.void = async_to_streamed_response_wrapper(
            holds.void,
        )
