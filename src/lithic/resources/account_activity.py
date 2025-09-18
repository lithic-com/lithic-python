# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from .. import _legacy_response
from ..types import account_activity_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.account_activity_list_response import AccountActivityListResponse
from ..types.account_activity_retrieve_transaction_response import AccountActivityRetrieveTransactionResponse

__all__ = ["AccountActivity", "AsyncAccountActivity"]


class AccountActivity(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountActivityWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AccountActivityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountActivityWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AccountActivityWithStreamingResponse(self)

    def list(
        self,
        *,
        account_token: str | Omit = omit,
        begin: Union[str, datetime] | Omit = omit,
        business_account_token: str | Omit = omit,
        category: Literal[
            "ACH",
            "BALANCE_OR_FUNDING",
            "CARD",
            "EXTERNAL_ACH",
            "EXTERNAL_CHECK",
            "EXTERNAL_TRANSFER",
            "EXTERNAL_WIRE",
            "MANAGEMENT_ADJUSTMENT",
            "MANAGEMENT_DISPUTE",
            "MANAGEMENT_FEE",
            "MANAGEMENT_REWARD",
            "MANAGEMENT_DISBURSEMENT",
            "PROGRAM_FUNDING",
        ]
        | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        ending_before: str | Omit = omit,
        financial_account_token: str | Omit = omit,
        page_size: int | Omit = omit,
        result: Literal["APPROVED", "DECLINED"] | Omit = omit,
        starting_after: str | Omit = omit,
        status: Literal["DECLINED", "EXPIRED", "PENDING", "RETURNED", "REVERSED", "SETTLED", "VOIDED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[AccountActivityListResponse]:
        """
        Retrieve a list of transactions across all public accounts.

        Args:
          account_token: Filter by account token

          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          business_account_token: Filter by business account token

          category: Filter by transaction category

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          financial_account_token: Filter by financial account token

          page_size: Page size (for pagination).

          result: Filter by transaction result

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Filter by transaction status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/account_activity",
            page=SyncCursorPage[AccountActivityListResponse],
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
                    account_activity_list_params.AccountActivityListParams,
                ),
            ),
            model=cast(
                Any, AccountActivityListResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )

    def retrieve_transaction(
        self,
        transaction_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountActivityRetrieveTransactionResponse:
        """
        Retrieve a single transaction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_token:
            raise ValueError(f"Expected a non-empty value for `transaction_token` but received {transaction_token!r}")
        return cast(
            AccountActivityRetrieveTransactionResponse,
            self._get(
                f"/v1/account_activity/{transaction_token}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AccountActivityRetrieveTransactionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncAccountActivity(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountActivityWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountActivityWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountActivityWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncAccountActivityWithStreamingResponse(self)

    def list(
        self,
        *,
        account_token: str | Omit = omit,
        begin: Union[str, datetime] | Omit = omit,
        business_account_token: str | Omit = omit,
        category: Literal[
            "ACH",
            "BALANCE_OR_FUNDING",
            "CARD",
            "EXTERNAL_ACH",
            "EXTERNAL_CHECK",
            "EXTERNAL_TRANSFER",
            "EXTERNAL_WIRE",
            "MANAGEMENT_ADJUSTMENT",
            "MANAGEMENT_DISPUTE",
            "MANAGEMENT_FEE",
            "MANAGEMENT_REWARD",
            "MANAGEMENT_DISBURSEMENT",
            "PROGRAM_FUNDING",
        ]
        | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        ending_before: str | Omit = omit,
        financial_account_token: str | Omit = omit,
        page_size: int | Omit = omit,
        result: Literal["APPROVED", "DECLINED"] | Omit = omit,
        starting_after: str | Omit = omit,
        status: Literal["DECLINED", "EXPIRED", "PENDING", "RETURNED", "REVERSED", "SETTLED", "VOIDED"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AccountActivityListResponse, AsyncCursorPage[AccountActivityListResponse]]:
        """
        Retrieve a list of transactions across all public accounts.

        Args:
          account_token: Filter by account token

          begin: Date string in RFC 3339 format. Only entries created after the specified time
              will be included. UTC time zone.

          business_account_token: Filter by business account token

          category: Filter by transaction category

          end: Date string in RFC 3339 format. Only entries created before the specified time
              will be included. UTC time zone.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          financial_account_token: Filter by financial account token

          page_size: Page size (for pagination).

          result: Filter by transaction result

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          status: Filter by transaction status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/account_activity",
            page=AsyncCursorPage[AccountActivityListResponse],
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
                    account_activity_list_params.AccountActivityListParams,
                ),
            ),
            model=cast(
                Any, AccountActivityListResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )

    async def retrieve_transaction(
        self,
        transaction_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountActivityRetrieveTransactionResponse:
        """
        Retrieve a single transaction

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not transaction_token:
            raise ValueError(f"Expected a non-empty value for `transaction_token` but received {transaction_token!r}")
        return cast(
            AccountActivityRetrieveTransactionResponse,
            await self._get(
                f"/v1/account_activity/{transaction_token}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, AccountActivityRetrieveTransactionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AccountActivityWithRawResponse:
    def __init__(self, account_activity: AccountActivity) -> None:
        self._account_activity = account_activity

        self.list = _legacy_response.to_raw_response_wrapper(
            account_activity.list,
        )
        self.retrieve_transaction = _legacy_response.to_raw_response_wrapper(
            account_activity.retrieve_transaction,
        )


class AsyncAccountActivityWithRawResponse:
    def __init__(self, account_activity: AsyncAccountActivity) -> None:
        self._account_activity = account_activity

        self.list = _legacy_response.async_to_raw_response_wrapper(
            account_activity.list,
        )
        self.retrieve_transaction = _legacy_response.async_to_raw_response_wrapper(
            account_activity.retrieve_transaction,
        )


class AccountActivityWithStreamingResponse:
    def __init__(self, account_activity: AccountActivity) -> None:
        self._account_activity = account_activity

        self.list = to_streamed_response_wrapper(
            account_activity.list,
        )
        self.retrieve_transaction = to_streamed_response_wrapper(
            account_activity.retrieve_transaction,
        )


class AsyncAccountActivityWithStreamingResponse:
    def __init__(self, account_activity: AsyncAccountActivity) -> None:
        self._account_activity = account_activity

        self.list = async_to_streamed_response_wrapper(
            account_activity.list,
        )
        self.retrieve_transaction = async_to_streamed_response_wrapper(
            account_activity.retrieve_transaction,
        )
