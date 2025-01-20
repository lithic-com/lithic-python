# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    external_payment_list_params,
    external_payment_cancel_params,
    external_payment_create_params,
    external_payment_settle_params,
    external_payment_release_params,
    external_payment_reverse_params,
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
from ..types.external_payment import ExternalPayment

__all__ = ["ExternalPayments", "AsyncExternalPayments"]


class ExternalPayments(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExternalPaymentsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return ExternalPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalPaymentsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return ExternalPaymentsWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        category: Literal["EXTERNAL_WIRE", "EXTERNAL_ACH", "EXTERNAL_CHECK", "EXTERNAL_TRANSFER"],
        effective_date: Union[str, date],
        financial_account_token: str,
        payment_type: Literal["DEPOSIT", "WITHDRAWAL"],
        token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        progress_to: Literal["SETTLED", "RELEASED"] | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPayment:
        """
        Create external payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/external_payments",
            body=maybe_transform(
                {
                    "amount": amount,
                    "category": category,
                    "effective_date": effective_date,
                    "financial_account_token": financial_account_token,
                    "payment_type": payment_type,
                    "token": token,
                    "memo": memo,
                    "progress_to": progress_to,
                    "user_defined_id": user_defined_id,
                },
                external_payment_create_params.ExternalPaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPayment,
        )

    def retrieve(
        self,
        external_payment_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPayment:
        """
        Get external payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_payment_token:
            raise ValueError(
                f"Expected a non-empty value for `external_payment_token` but received {external_payment_token!r}"
            )
        return self._get(
            f"/v1/external_payments/{external_payment_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPayment,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        category: Literal["EXTERNAL_WIRE", "EXTERNAL_ACH", "EXTERNAL_CHECK", "EXTERNAL_TRANSFER"]
        | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        result: Literal["APPROVED", "DECLINED"] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[ExternalPayment]:
        """List external payments

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          category: External Payment category to be returned.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          financial_account_token: Globally unique identifier for the financial account or card that will send the
              funds. Accepted type dependent on the program's use case.

          page_size: Page size (for pagination).

          result: External Payment result to be returned.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Book transfer status to be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/external_payments",
            page=SyncCursorPage[ExternalPayment],
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
                        "result": result,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    external_payment_list_params.ExternalPaymentListParams,
                ),
            ),
            model=ExternalPayment,
        )

    def cancel(
        self,
        external_payment_token: str,
        *,
        effective_date: Union[str, date],
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPayment:
        """
        Cancel external payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_payment_token:
            raise ValueError(
                f"Expected a non-empty value for `external_payment_token` but received {external_payment_token!r}"
            )
        return self._post(
            f"/v1/external_payments/{external_payment_token}/cancel",
            body=maybe_transform(
                {
                    "effective_date": effective_date,
                    "memo": memo,
                },
                external_payment_cancel_params.ExternalPaymentCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPayment,
        )

    def release(
        self,
        external_payment_token: str,
        *,
        effective_date: Union[str, date],
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPayment:
        """
        Release external payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_payment_token:
            raise ValueError(
                f"Expected a non-empty value for `external_payment_token` but received {external_payment_token!r}"
            )
        return self._post(
            f"/v1/external_payments/{external_payment_token}/release",
            body=maybe_transform(
                {
                    "effective_date": effective_date,
                    "memo": memo,
                },
                external_payment_release_params.ExternalPaymentReleaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPayment,
        )

    def reverse(
        self,
        external_payment_token: str,
        *,
        effective_date: Union[str, date],
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPayment:
        """
        Reverse external payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_payment_token:
            raise ValueError(
                f"Expected a non-empty value for `external_payment_token` but received {external_payment_token!r}"
            )
        return self._post(
            f"/v1/external_payments/{external_payment_token}/reverse",
            body=maybe_transform(
                {
                    "effective_date": effective_date,
                    "memo": memo,
                },
                external_payment_reverse_params.ExternalPaymentReverseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPayment,
        )

    def settle(
        self,
        external_payment_token: str,
        *,
        effective_date: Union[str, date],
        memo: str | NotGiven = NOT_GIVEN,
        progress_to: Literal["SETTLED", "RELEASED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPayment:
        """
        Settle external payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_payment_token:
            raise ValueError(
                f"Expected a non-empty value for `external_payment_token` but received {external_payment_token!r}"
            )
        return self._post(
            f"/v1/external_payments/{external_payment_token}/settle",
            body=maybe_transform(
                {
                    "effective_date": effective_date,
                    "memo": memo,
                    "progress_to": progress_to,
                },
                external_payment_settle_params.ExternalPaymentSettleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPayment,
        )


class AsyncExternalPayments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExternalPaymentsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalPaymentsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncExternalPaymentsWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        category: Literal["EXTERNAL_WIRE", "EXTERNAL_ACH", "EXTERNAL_CHECK", "EXTERNAL_TRANSFER"],
        effective_date: Union[str, date],
        financial_account_token: str,
        payment_type: Literal["DEPOSIT", "WITHDRAWAL"],
        token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        progress_to: Literal["SETTLED", "RELEASED"] | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPayment:
        """
        Create external payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/external_payments",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "category": category,
                    "effective_date": effective_date,
                    "financial_account_token": financial_account_token,
                    "payment_type": payment_type,
                    "token": token,
                    "memo": memo,
                    "progress_to": progress_to,
                    "user_defined_id": user_defined_id,
                },
                external_payment_create_params.ExternalPaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPayment,
        )

    async def retrieve(
        self,
        external_payment_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPayment:
        """
        Get external payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_payment_token:
            raise ValueError(
                f"Expected a non-empty value for `external_payment_token` but received {external_payment_token!r}"
            )
        return await self._get(
            f"/v1/external_payments/{external_payment_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPayment,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        category: Literal["EXTERNAL_WIRE", "EXTERNAL_ACH", "EXTERNAL_CHECK", "EXTERNAL_TRANSFER"]
        | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        result: Literal["APPROVED", "DECLINED"] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ExternalPayment, AsyncCursorPage[ExternalPayment]]:
        """List external payments

        Args:
          begin: Date string in RFC 3339 format.

        Only entries created after the specified time
              will be included. UTC time zone.

          category: External Payment category to be returned.

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          financial_account_token: Globally unique identifier for the financial account or card that will send the
              funds. Accepted type dependent on the program's use case.

          page_size: Page size (for pagination).

          result: External Payment result to be returned.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Book transfer status to be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/external_payments",
            page=AsyncCursorPage[ExternalPayment],
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
                        "result": result,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    external_payment_list_params.ExternalPaymentListParams,
                ),
            ),
            model=ExternalPayment,
        )

    async def cancel(
        self,
        external_payment_token: str,
        *,
        effective_date: Union[str, date],
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPayment:
        """
        Cancel external payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_payment_token:
            raise ValueError(
                f"Expected a non-empty value for `external_payment_token` but received {external_payment_token!r}"
            )
        return await self._post(
            f"/v1/external_payments/{external_payment_token}/cancel",
            body=await async_maybe_transform(
                {
                    "effective_date": effective_date,
                    "memo": memo,
                },
                external_payment_cancel_params.ExternalPaymentCancelParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPayment,
        )

    async def release(
        self,
        external_payment_token: str,
        *,
        effective_date: Union[str, date],
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPayment:
        """
        Release external payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_payment_token:
            raise ValueError(
                f"Expected a non-empty value for `external_payment_token` but received {external_payment_token!r}"
            )
        return await self._post(
            f"/v1/external_payments/{external_payment_token}/release",
            body=await async_maybe_transform(
                {
                    "effective_date": effective_date,
                    "memo": memo,
                },
                external_payment_release_params.ExternalPaymentReleaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPayment,
        )

    async def reverse(
        self,
        external_payment_token: str,
        *,
        effective_date: Union[str, date],
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPayment:
        """
        Reverse external payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_payment_token:
            raise ValueError(
                f"Expected a non-empty value for `external_payment_token` but received {external_payment_token!r}"
            )
        return await self._post(
            f"/v1/external_payments/{external_payment_token}/reverse",
            body=await async_maybe_transform(
                {
                    "effective_date": effective_date,
                    "memo": memo,
                },
                external_payment_reverse_params.ExternalPaymentReverseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPayment,
        )

    async def settle(
        self,
        external_payment_token: str,
        *,
        effective_date: Union[str, date],
        memo: str | NotGiven = NOT_GIVEN,
        progress_to: Literal["SETTLED", "RELEASED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalPayment:
        """
        Settle external payment

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_payment_token:
            raise ValueError(
                f"Expected a non-empty value for `external_payment_token` but received {external_payment_token!r}"
            )
        return await self._post(
            f"/v1/external_payments/{external_payment_token}/settle",
            body=await async_maybe_transform(
                {
                    "effective_date": effective_date,
                    "memo": memo,
                    "progress_to": progress_to,
                },
                external_payment_settle_params.ExternalPaymentSettleParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalPayment,
        )


class ExternalPaymentsWithRawResponse:
    def __init__(self, external_payments: ExternalPayments) -> None:
        self._external_payments = external_payments

        self.create = _legacy_response.to_raw_response_wrapper(
            external_payments.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            external_payments.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            external_payments.list,
        )
        self.cancel = _legacy_response.to_raw_response_wrapper(
            external_payments.cancel,
        )
        self.release = _legacy_response.to_raw_response_wrapper(
            external_payments.release,
        )
        self.reverse = _legacy_response.to_raw_response_wrapper(
            external_payments.reverse,
        )
        self.settle = _legacy_response.to_raw_response_wrapper(
            external_payments.settle,
        )


class AsyncExternalPaymentsWithRawResponse:
    def __init__(self, external_payments: AsyncExternalPayments) -> None:
        self._external_payments = external_payments

        self.create = _legacy_response.async_to_raw_response_wrapper(
            external_payments.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            external_payments.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            external_payments.list,
        )
        self.cancel = _legacy_response.async_to_raw_response_wrapper(
            external_payments.cancel,
        )
        self.release = _legacy_response.async_to_raw_response_wrapper(
            external_payments.release,
        )
        self.reverse = _legacy_response.async_to_raw_response_wrapper(
            external_payments.reverse,
        )
        self.settle = _legacy_response.async_to_raw_response_wrapper(
            external_payments.settle,
        )


class ExternalPaymentsWithStreamingResponse:
    def __init__(self, external_payments: ExternalPayments) -> None:
        self._external_payments = external_payments

        self.create = to_streamed_response_wrapper(
            external_payments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            external_payments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            external_payments.list,
        )
        self.cancel = to_streamed_response_wrapper(
            external_payments.cancel,
        )
        self.release = to_streamed_response_wrapper(
            external_payments.release,
        )
        self.reverse = to_streamed_response_wrapper(
            external_payments.reverse,
        )
        self.settle = to_streamed_response_wrapper(
            external_payments.settle,
        )


class AsyncExternalPaymentsWithStreamingResponse:
    def __init__(self, external_payments: AsyncExternalPayments) -> None:
        self._external_payments = external_payments

        self.create = async_to_streamed_response_wrapper(
            external_payments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            external_payments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            external_payments.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            external_payments.cancel,
        )
        self.release = async_to_streamed_response_wrapper(
            external_payments.release,
        )
        self.reverse = async_to_streamed_response_wrapper(
            external_payments.reverse,
        )
        self.settle = async_to_streamed_response_wrapper(
            external_payments.settle,
        )
