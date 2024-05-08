# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ...types import (
    financial_account_list_params,
    financial_account_create_params,
    financial_account_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .balances import (
    BalancesResource,
    AsyncBalancesResource,
    BalancesResourceWithRawResponse,
    AsyncBalancesResourceWithRawResponse,
    BalancesResourceWithStreamingResponse,
    AsyncBalancesResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .statements import (
    StatementsResource,
    AsyncStatementsResource,
    StatementsResourceWithRawResponse,
    AsyncStatementsResourceWithRawResponse,
    StatementsResourceWithStreamingResponse,
    AsyncStatementsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .statements.statements import StatementsResource, AsyncStatementsResource
from .financial_transactions import (
    FinancialTransactionsResource,
    AsyncFinancialTransactionsResource,
    FinancialTransactionsResourceWithRawResponse,
    AsyncFinancialTransactionsResourceWithRawResponse,
    FinancialTransactionsResourceWithStreamingResponse,
    AsyncFinancialTransactionsResourceWithStreamingResponse,
)
from ...types.financial_account import FinancialAccount

__all__ = ["FinancialAccountsResource", "AsyncFinancialAccountsResource"]


class FinancialAccountsResource(SyncAPIResource):
    @cached_property
    def balances(self) -> BalancesResource:
        return BalancesResource(self._client)

    @cached_property
    def financial_transactions(self) -> FinancialTransactionsResource:
        return FinancialTransactionsResource(self._client)

    @cached_property
    def statements(self) -> StatementsResource:
        return StatementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> FinancialAccountsResourceWithRawResponse:
        return FinancialAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FinancialAccountsResourceWithStreamingResponse:
        return FinancialAccountsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        nickname: str,
        type: Literal["OPERATING"],
        account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialAccount:
        """
        Create a new financial account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/financial_accounts",
            body=maybe_transform(
                {
                    "nickname": nickname,
                    "type": type,
                    "account_token": account_token,
                },
                financial_account_create_params.FinancialAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialAccount,
        )

    def retrieve(
        self,
        financial_account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialAccount:
        """
        Get a financial account

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
        return self._get(
            f"/financial_accounts/{financial_account_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialAccount,
        )

    def update(
        self,
        financial_account_token: str,
        *,
        nickname: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialAccount:
        """
        Update a financial account

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
        return self._patch(
            f"/financial_accounts/{financial_account_token}",
            body=maybe_transform({"nickname": nickname}, financial_account_update_params.FinancialAccountUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialAccount,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        type: Literal["ISSUING", "OPERATING", "RESERVE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[FinancialAccount]:
        """
        Retrieve information on your financial accounts including routing and account
        number.

        Args:
          account_token: List financial accounts for a given account_token or business_account_token

          business_account_token: List financial accounts for a given business_account_token

          type: List financial accounts of a given type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/financial_accounts",
            page=SyncSinglePage[FinancialAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "business_account_token": business_account_token,
                        "type": type,
                    },
                    financial_account_list_params.FinancialAccountListParams,
                ),
            ),
            model=FinancialAccount,
        )


class AsyncFinancialAccountsResource(AsyncAPIResource):
    @cached_property
    def balances(self) -> AsyncBalancesResource:
        return AsyncBalancesResource(self._client)

    @cached_property
    def financial_transactions(self) -> AsyncFinancialTransactionsResource:
        return AsyncFinancialTransactionsResource(self._client)

    @cached_property
    def statements(self) -> AsyncStatementsResource:
        return AsyncStatementsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFinancialAccountsResourceWithRawResponse:
        return AsyncFinancialAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFinancialAccountsResourceWithStreamingResponse:
        return AsyncFinancialAccountsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        nickname: str,
        type: Literal["OPERATING"],
        account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialAccount:
        """
        Create a new financial account

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/financial_accounts",
            body=await async_maybe_transform(
                {
                    "nickname": nickname,
                    "type": type,
                    "account_token": account_token,
                },
                financial_account_create_params.FinancialAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialAccount,
        )

    async def retrieve(
        self,
        financial_account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialAccount:
        """
        Get a financial account

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
        return await self._get(
            f"/financial_accounts/{financial_account_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialAccount,
        )

    async def update(
        self,
        financial_account_token: str,
        *,
        nickname: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FinancialAccount:
        """
        Update a financial account

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
        return await self._patch(
            f"/financial_accounts/{financial_account_token}",
            body=await async_maybe_transform(
                {"nickname": nickname}, financial_account_update_params.FinancialAccountUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialAccount,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        business_account_token: str | NotGiven = NOT_GIVEN,
        type: Literal["ISSUING", "OPERATING", "RESERVE"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[FinancialAccount, AsyncSinglePage[FinancialAccount]]:
        """
        Retrieve information on your financial accounts including routing and account
        number.

        Args:
          account_token: List financial accounts for a given account_token or business_account_token

          business_account_token: List financial accounts for a given business_account_token

          type: List financial accounts of a given type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/financial_accounts",
            page=AsyncSinglePage[FinancialAccount],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "business_account_token": business_account_token,
                        "type": type,
                    },
                    financial_account_list_params.FinancialAccountListParams,
                ),
            ),
            model=FinancialAccount,
        )


class FinancialAccountsResourceWithRawResponse:
    def __init__(self, financial_accounts: FinancialAccountsResource) -> None:
        self._financial_accounts = financial_accounts

        self.create = _legacy_response.to_raw_response_wrapper(
            financial_accounts.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            financial_accounts.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            financial_accounts.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            financial_accounts.list,
        )

    @cached_property
    def balances(self) -> BalancesResourceWithRawResponse:
        return BalancesResourceWithRawResponse(self._financial_accounts.balances)

    @cached_property
    def financial_transactions(self) -> FinancialTransactionsResourceWithRawResponse:
        return FinancialTransactionsResourceWithRawResponse(self._financial_accounts.financial_transactions)

    @cached_property
    def statements(self) -> StatementsResourceWithRawResponse:
        return StatementsResourceWithRawResponse(self._financial_accounts.statements)


class AsyncFinancialAccountsResourceWithRawResponse:
    def __init__(self, financial_accounts: AsyncFinancialAccountsResource) -> None:
        self._financial_accounts = financial_accounts

        self.create = _legacy_response.async_to_raw_response_wrapper(
            financial_accounts.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            financial_accounts.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            financial_accounts.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            financial_accounts.list,
        )

    @cached_property
    def balances(self) -> AsyncBalancesResourceWithRawResponse:
        return AsyncBalancesResourceWithRawResponse(self._financial_accounts.balances)

    @cached_property
    def financial_transactions(self) -> AsyncFinancialTransactionsResourceWithRawResponse:
        return AsyncFinancialTransactionsResourceWithRawResponse(self._financial_accounts.financial_transactions)

    @cached_property
    def statements(self) -> AsyncStatementsResourceWithRawResponse:
        return AsyncStatementsResourceWithRawResponse(self._financial_accounts.statements)


class FinancialAccountsResourceWithStreamingResponse:
    def __init__(self, financial_accounts: FinancialAccountsResource) -> None:
        self._financial_accounts = financial_accounts

        self.create = to_streamed_response_wrapper(
            financial_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            financial_accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            financial_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            financial_accounts.list,
        )

    @cached_property
    def balances(self) -> BalancesResourceWithStreamingResponse:
        return BalancesResourceWithStreamingResponse(self._financial_accounts.balances)

    @cached_property
    def financial_transactions(self) -> FinancialTransactionsResourceWithStreamingResponse:
        return FinancialTransactionsResourceWithStreamingResponse(self._financial_accounts.financial_transactions)

    @cached_property
    def statements(self) -> StatementsResourceWithStreamingResponse:
        return StatementsResourceWithStreamingResponse(self._financial_accounts.statements)


class AsyncFinancialAccountsResourceWithStreamingResponse:
    def __init__(self, financial_accounts: AsyncFinancialAccountsResource) -> None:
        self._financial_accounts = financial_accounts

        self.create = async_to_streamed_response_wrapper(
            financial_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            financial_accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            financial_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            financial_accounts.list,
        )

    @cached_property
    def balances(self) -> AsyncBalancesResourceWithStreamingResponse:
        return AsyncBalancesResourceWithStreamingResponse(self._financial_accounts.balances)

    @cached_property
    def financial_transactions(self) -> AsyncFinancialTransactionsResourceWithStreamingResponse:
        return AsyncFinancialTransactionsResourceWithStreamingResponse(self._financial_accounts.financial_transactions)

    @cached_property
    def statements(self) -> AsyncStatementsResourceWithStreamingResponse:
        return AsyncStatementsResourceWithStreamingResponse(self._financial_accounts.statements)
