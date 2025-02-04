# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import (
    payment_list_params,
    payment_create_params,
    payment_simulate_action_params,
    payment_simulate_return_params,
    payment_simulate_receipt_params,
    payment_simulate_release_params,
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
from ..types.payment import Payment
from ..types.payment_retry_response import PaymentRetryResponse
from ..types.payment_create_response import PaymentCreateResponse
from ..types.payment_simulate_action_response import PaymentSimulateActionResponse
from ..types.payment_simulate_return_response import PaymentSimulateReturnResponse
from ..types.payment_simulate_receipt_response import PaymentSimulateReceiptResponse
from ..types.payment_simulate_release_response import PaymentSimulateReleaseResponse

__all__ = ["Payments", "AsyncPayments"]


class Payments(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return PaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
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
            "/v1/payments",
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
            f"/v1/payments/{payment_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        category: Literal["ACH"] | NotGiven = NOT_GIVEN,
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
            "/v1/payments",
            page=SyncCursorPage[Payment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
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
            f"/v1/payments/{payment_token}/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRetryResponse,
        )

    def simulate_action(
        self,
        payment_token: str,
        *,
        event_type: Literal[
            "ACH_ORIGINATION_REVIEWED",
            "ACH_ORIGINATION_RELEASED",
            "ACH_ORIGINATION_PROCESSED",
            "ACH_ORIGINATION_SETTLED",
            "ACH_RECEIPT_SETTLED",
            "ACH_RETURN_INITIATED",
            "ACH_RETURN_PROCESSED",
            "ACH_RETURN_SETTLED",
        ],
        decline_reason: Literal[
            "PROGRAM_TRANSACTION_LIMIT_EXCEEDED", "PROGRAM_DAILY_LIMIT_EXCEEDED", "PROGRAM_MONTHLY_LIMIT_EXCEEDED"
        ]
        | NotGiven = NOT_GIVEN,
        return_reason_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSimulateActionResponse:
        """
        Simulate payment lifecycle event

        Args:
          event_type: Event Type

          decline_reason: Decline reason

          return_reason_code: Return Reason Code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_token:
            raise ValueError(f"Expected a non-empty value for `payment_token` but received {payment_token!r}")
        return self._post(
            f"/v1/simulate/payments/{payment_token}/action",
            body=maybe_transform(
                {
                    "event_type": event_type,
                    "decline_reason": decline_reason,
                    "return_reason_code": return_reason_code,
                },
                payment_simulate_action_params.PaymentSimulateActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentSimulateActionResponse,
        )

    def simulate_receipt(
        self,
        *,
        token: str,
        amount: int,
        financial_account_token: str,
        receipt_type: Literal["RECEIPT_CREDIT", "RECEIPT_DEBIT"],
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSimulateReceiptResponse:
        """
        Simulates a receipt of a Payment.

        Args:
          token: Payment token

          amount: Amount

          financial_account_token: Financial Account Token

          receipt_type: Receipt Type

          memo: Memo

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulate/payments/receipt",
            body=maybe_transform(
                {
                    "token": token,
                    "amount": amount,
                    "financial_account_token": financial_account_token,
                    "receipt_type": receipt_type,
                    "memo": memo,
                },
                payment_simulate_receipt_params.PaymentSimulateReceiptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentSimulateReceiptResponse,
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
          payment_token: Payment Token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulate/payments/release",
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
          payment_token: Payment Token

          return_reason_code: Return Reason Code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/simulate/payments/return",
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
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
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
            "/v1/payments",
            body=await async_maybe_transform(
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
            f"/v1/payments/{payment_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        begin: Union[str, datetime] | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        category: Literal["ACH"] | NotGiven = NOT_GIVEN,
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
            "/v1/payments",
            page=AsyncCursorPage[Payment],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
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
            f"/v1/payments/{payment_token}/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRetryResponse,
        )

    async def simulate_action(
        self,
        payment_token: str,
        *,
        event_type: Literal[
            "ACH_ORIGINATION_REVIEWED",
            "ACH_ORIGINATION_RELEASED",
            "ACH_ORIGINATION_PROCESSED",
            "ACH_ORIGINATION_SETTLED",
            "ACH_RECEIPT_SETTLED",
            "ACH_RETURN_INITIATED",
            "ACH_RETURN_PROCESSED",
            "ACH_RETURN_SETTLED",
        ],
        decline_reason: Literal[
            "PROGRAM_TRANSACTION_LIMIT_EXCEEDED", "PROGRAM_DAILY_LIMIT_EXCEEDED", "PROGRAM_MONTHLY_LIMIT_EXCEEDED"
        ]
        | NotGiven = NOT_GIVEN,
        return_reason_code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSimulateActionResponse:
        """
        Simulate payment lifecycle event

        Args:
          event_type: Event Type

          decline_reason: Decline reason

          return_reason_code: Return Reason Code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_token:
            raise ValueError(f"Expected a non-empty value for `payment_token` but received {payment_token!r}")
        return await self._post(
            f"/v1/simulate/payments/{payment_token}/action",
            body=await async_maybe_transform(
                {
                    "event_type": event_type,
                    "decline_reason": decline_reason,
                    "return_reason_code": return_reason_code,
                },
                payment_simulate_action_params.PaymentSimulateActionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentSimulateActionResponse,
        )

    async def simulate_receipt(
        self,
        *,
        token: str,
        amount: int,
        financial_account_token: str,
        receipt_type: Literal["RECEIPT_CREDIT", "RECEIPT_DEBIT"],
        memo: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentSimulateReceiptResponse:
        """
        Simulates a receipt of a Payment.

        Args:
          token: Payment token

          amount: Amount

          financial_account_token: Financial Account Token

          receipt_type: Receipt Type

          memo: Memo

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulate/payments/receipt",
            body=await async_maybe_transform(
                {
                    "token": token,
                    "amount": amount,
                    "financial_account_token": financial_account_token,
                    "receipt_type": receipt_type,
                    "memo": memo,
                },
                payment_simulate_receipt_params.PaymentSimulateReceiptParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentSimulateReceiptResponse,
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
          payment_token: Payment Token

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulate/payments/release",
            body=await async_maybe_transform(
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
          payment_token: Payment Token

          return_reason_code: Return Reason Code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/simulate/payments/return",
            body=await async_maybe_transform(
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
        self.simulate_action = _legacy_response.to_raw_response_wrapper(
            payments.simulate_action,
        )
        self.simulate_receipt = _legacy_response.to_raw_response_wrapper(
            payments.simulate_receipt,
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
        self.simulate_action = _legacy_response.async_to_raw_response_wrapper(
            payments.simulate_action,
        )
        self.simulate_receipt = _legacy_response.async_to_raw_response_wrapper(
            payments.simulate_receipt,
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
        self.simulate_action = to_streamed_response_wrapper(
            payments.simulate_action,
        )
        self.simulate_receipt = to_streamed_response_wrapper(
            payments.simulate_receipt,
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
        self.simulate_action = async_to_streamed_response_wrapper(
            payments.simulate_action,
        )
        self.simulate_receipt = async_to_streamed_response_wrapper(
            payments.simulate_receipt,
        )
        self.simulate_release = async_to_streamed_response_wrapper(
            payments.simulate_release,
        )
        self.simulate_return = async_to_streamed_response_wrapper(
            payments.simulate_return,
        )
