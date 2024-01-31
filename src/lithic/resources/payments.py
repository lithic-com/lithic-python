# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    Payment,
    PaymentRetryResponse,
    PaymentCreateResponse,
    PaymentSimulateReturnResponse,
    PaymentSimulateReleaseResponse,
    payment_list_params,
    payment_create_params,
    payment_simulate_return_params,
    payment_simulate_release_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import (
    AsyncPaginator,
    make_request_options,
)

__all__ = ["Payments", "AsyncPayments"]


class Payments(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsWithRawResponse:
        return PaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsWithStreamingResponse:
        return PaymentsWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: int,
        external_bank_account_token: str,
        financial_account_token: str,
        method: Literal["ACH_NEXT_DAY", "ACH_SAME_DAY"],
        method_attributes: payment_create_params.MethodAttributes,
        type: Literal["COLLECTION", "PAYMENT"],
        token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreateResponse:
        """
        Initiates a payment between a financial account and an external bank account.

        Args:
          token: Customer-provided token that will serve as an idempotency token. This token will
              become the transaction token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/payments",
            body=maybe_transform(
                {
                    "amount": amount,
                    "external_bank_account_token": external_bank_account_token,
                    "financial_account_token": financial_account_token,
                    "method": method,
                    "method_attributes": method_attributes,
                    "type": type,
                    "token": token,
                    "memo": memo,
                    "user_defined_id": user_defined_id,
                },
                payment_create_params.PaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentCreateResponse,
        )

    def retrieve(
        self,
        payment_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Payment:
        """
        Get the payment by token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_token:
            raise ValueError(f"Expected a non-empty value for `payment_token` but received {payment_token!r}")
        return self._get(
            f"/payments/{payment_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        result: Literal["APPROVED", "DECLINED"] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["DECLINED", "PENDING", "RETURNED", "SETTLED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[Payment]:
        """
        List all the payments for the provided search criteria.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payments",
            page=SyncCursorPage[Payment],
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
                        "financial_account_token": financial_account_token,
                        "page_size": page_size,
                        "result": result,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=Payment,
        )

    def retry(
        self,
        payment_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentRetryResponse:
        """
        Retry an origination which has been returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_token:
            raise ValueError(f"Expected a non-empty value for `payment_token` but received {payment_token!r}")
        return self._post(
            f"/payments/{payment_token}/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRetryResponse,
        )

    def simulate_release(
        self,
        *,
        payment_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSimulateReleaseResponse:
        """
        Simulates a release of a Payment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/simulate/payments/release",
            body=maybe_transform(
                {"payment_token": payment_token}, payment_simulate_release_params.PaymentSimulateReleaseParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentSimulateReleaseResponse,
        )

    def simulate_return(
        self,
        *,
        payment_token: str,
        return_reason_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSimulateReturnResponse:
        """
        Simulates a return of a Payment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/simulate/payments/return",
            body=maybe_transform(
                {
                    "payment_token": payment_token,
                    "return_reason_code": return_reason_code,
                },
                payment_simulate_return_params.PaymentSimulateReturnParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentSimulateReturnResponse,
        )


class AsyncPayments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsWithRawResponse:
        return AsyncPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsWithStreamingResponse:
        return AsyncPaymentsWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: int,
        external_bank_account_token: str,
        financial_account_token: str,
        method: Literal["ACH_NEXT_DAY", "ACH_SAME_DAY"],
        method_attributes: payment_create_params.MethodAttributes,
        type: Literal["COLLECTION", "PAYMENT"],
        token: str | NotGiven = NOT_GIVEN,
        memo: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentCreateResponse:
        """
        Initiates a payment between a financial account and an external bank account.

        Args:
          token: Customer-provided token that will serve as an idempotency token. This token will
              become the transaction token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/payments",
            body=maybe_transform(
                {
                    "amount": amount,
                    "external_bank_account_token": external_bank_account_token,
                    "financial_account_token": financial_account_token,
                    "method": method,
                    "method_attributes": method_attributes,
                    "type": type,
                    "token": token,
                    "memo": memo,
                    "user_defined_id": user_defined_id,
                },
                payment_create_params.PaymentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentCreateResponse,
        )

    async def retrieve(
        self,
        payment_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Payment:
        """
        Get the payment by token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_token:
            raise ValueError(f"Expected a non-empty value for `payment_token` but received {payment_token!r}")
        return await self._get(
            f"/payments/{payment_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    def list(
        self,
        *,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        result: Literal["APPROVED", "DECLINED"] | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        status: Literal["DECLINED", "PENDING", "RETURNED", "SETTLED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Payment, AsyncCursorPage[Payment]]:
        """
        List all the payments for the provided search criteria.

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

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/payments",
            page=AsyncCursorPage[Payment],
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
                        "financial_account_token": financial_account_token,
                        "page_size": page_size,
                        "result": result,
                        "starting_after": starting_after,
                        "status": status,
                    },
                    payment_list_params.PaymentListParams,
                ),
            ),
            model=Payment,
        )

    async def retry(
        self,
        payment_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentRetryResponse:
        """
        Retry an origination which has been returned.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_token:
            raise ValueError(f"Expected a non-empty value for `payment_token` but received {payment_token!r}")
        return await self._post(
            f"/payments/{payment_token}/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRetryResponse,
        )

    async def simulate_release(
        self,
        *,
        payment_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSimulateReleaseResponse:
        """
        Simulates a release of a Payment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/simulate/payments/release",
            body=maybe_transform(
                {"payment_token": payment_token}, payment_simulate_release_params.PaymentSimulateReleaseParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentSimulateReleaseResponse,
        )

    async def simulate_return(
        self,
        *,
        payment_token: str,
        return_reason_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSimulateReturnResponse:
        """
        Simulates a return of a Payment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/simulate/payments/return",
            body=maybe_transform(
                {
                    "payment_token": payment_token,
                    "return_reason_code": return_reason_code,
                },
                payment_simulate_return_params.PaymentSimulateReturnParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentSimulateReturnResponse,
        )


class PaymentsWithRawResponse:
    def __init__(self, payments: Payments) -> None:
        self._payments = payments

        self.create = _legacy_response.to_raw_response_wrapper(
            payments.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            payments.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            payments.list,
        )
        self.retry = _legacy_response.to_raw_response_wrapper(
            payments.retry,
        )
        self.simulate_release = _legacy_response.to_raw_response_wrapper(
            payments.simulate_release,
        )
        self.simulate_return = _legacy_response.to_raw_response_wrapper(
            payments.simulate_return,
        )


class AsyncPaymentsWithRawResponse:
    def __init__(self, payments: AsyncPayments) -> None:
        self._payments = payments

        self.create = _legacy_response.async_to_raw_response_wrapper(
            payments.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            payments.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            payments.list,
        )
        self.retry = _legacy_response.async_to_raw_response_wrapper(
            payments.retry,
        )
        self.simulate_release = _legacy_response.async_to_raw_response_wrapper(
            payments.simulate_release,
        )
        self.simulate_return = _legacy_response.async_to_raw_response_wrapper(
            payments.simulate_return,
        )


class PaymentsWithStreamingResponse:
    def __init__(self, payments: Payments) -> None:
        self._payments = payments

        self.create = to_streamed_response_wrapper(
            payments.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            payments.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            payments.list,
        )
        self.retry = to_streamed_response_wrapper(
            payments.retry,
        )
        self.simulate_release = to_streamed_response_wrapper(
            payments.simulate_release,
        )
        self.simulate_return = to_streamed_response_wrapper(
            payments.simulate_return,
        )


class AsyncPaymentsWithStreamingResponse:
    def __init__(self, payments: AsyncPayments) -> None:
        self._payments = payments

        self.create = async_to_streamed_response_wrapper(
            payments.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            payments.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            payments.list,
        )
        self.retry = async_to_streamed_response_wrapper(
            payments.retry,
        )
        self.simulate_release = async_to_streamed_response_wrapper(
            payments.simulate_release,
        )
        self.simulate_return = async_to_streamed_response_wrapper(
            payments.simulate_return,
        )
