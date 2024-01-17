# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ...types import FinancialAccount, financial_account_list_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from .balances import (
    Balances,
    AsyncBalances,
    BalancesWithRawResponse,
    AsyncBalancesWithRawResponse,
    BalancesWithStreamingResponse,
    AsyncBalancesWithStreamingResponse,
)
from ..._compat import cached_property
from .statements import (
    Statements,
    AsyncStatements,
    StatementsWithRawResponse,
    AsyncStatementsWithRawResponse,
    StatementsWithStreamingResponse,
    AsyncStatementsWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .statements.statements import Statements, AsyncStatements
from .financial_transactions import (
    FinancialTransactions,
    AsyncFinancialTransactions,
    FinancialTransactionsWithRawResponse,
    AsyncFinancialTransactionsWithRawResponse,
    FinancialTransactionsWithStreamingResponse,
    AsyncFinancialTransactionsWithStreamingResponse,
)

__all__ = ["FinancialAccounts", "AsyncFinancialAccounts"]


class FinancialAccounts(SyncAPIResource):
    @cached_property
    def balances(self) -> Balances:
        return Balances(self._client)

    @cached_property
    def financial_transactions(self) -> FinancialTransactions:
        return FinancialTransactions(self._client)

    @cached_property
    def statements(self) -> Statements:
        return Statements(self._client)

    @cached_property
    def with_raw_response(self) -> FinancialAccountsWithRawResponse:
        return FinancialAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FinancialAccountsWithStreamingResponse:
        return FinancialAccountsWithStreamingResponse(self)

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        type: Literal["ISSUING", "RESERVE"] | NotGiven = NOT_GIVEN,
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
          account_token: List financial accounts for a given account_token

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
                        "type": type,
                    },
                    financial_account_list_params.FinancialAccountListParams,
                ),
            ),
            model=FinancialAccount,
        )


class AsyncFinancialAccounts(AsyncAPIResource):
    @cached_property
    def balances(self) -> AsyncBalances:
        return AsyncBalances(self._client)

    @cached_property
    def financial_transactions(self) -> AsyncFinancialTransactions:
        return AsyncFinancialTransactions(self._client)

    @cached_property
    def statements(self) -> AsyncStatements:
        return AsyncStatements(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFinancialAccountsWithRawResponse:
        return AsyncFinancialAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFinancialAccountsWithStreamingResponse:
        return AsyncFinancialAccountsWithStreamingResponse(self)

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        type: Literal["ISSUING", "RESERVE"] | NotGiven = NOT_GIVEN,
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
          account_token: List financial accounts for a given account_token

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
                        "type": type,
                    },
                    financial_account_list_params.FinancialAccountListParams,
                ),
            ),
            model=FinancialAccount,
        )


class FinancialAccountsWithRawResponse:
    def __init__(self, financial_accounts: FinancialAccounts) -> None:
        self._financial_accounts = financial_accounts

        self.list = _legacy_response.to_raw_response_wrapper(
            financial_accounts.list,
        )

    @cached_property
    def balances(self) -> BalancesWithRawResponse:
        return BalancesWithRawResponse(self._financial_accounts.balances)

    @cached_property
    def financial_transactions(self) -> FinancialTransactionsWithRawResponse:
        return FinancialTransactionsWithRawResponse(self._financial_accounts.financial_transactions)

    @cached_property
    def statements(self) -> StatementsWithRawResponse:
        return StatementsWithRawResponse(self._financial_accounts.statements)


class AsyncFinancialAccountsWithRawResponse:
    def __init__(self, financial_accounts: AsyncFinancialAccounts) -> None:
        self._financial_accounts = financial_accounts

        self.list = _legacy_response.async_to_raw_response_wrapper(
            financial_accounts.list,
        )

    @cached_property
    def balances(self) -> AsyncBalancesWithRawResponse:
        return AsyncBalancesWithRawResponse(self._financial_accounts.balances)

    @cached_property
    def financial_transactions(self) -> AsyncFinancialTransactionsWithRawResponse:
        return AsyncFinancialTransactionsWithRawResponse(self._financial_accounts.financial_transactions)

    @cached_property
    def statements(self) -> AsyncStatementsWithRawResponse:
        return AsyncStatementsWithRawResponse(self._financial_accounts.statements)


class FinancialAccountsWithStreamingResponse:
    def __init__(self, financial_accounts: FinancialAccounts) -> None:
        self._financial_accounts = financial_accounts

        self.list = to_streamed_response_wrapper(
            financial_accounts.list,
        )

    @cached_property
    def balances(self) -> BalancesWithStreamingResponse:
        return BalancesWithStreamingResponse(self._financial_accounts.balances)

    @cached_property
    def financial_transactions(self) -> FinancialTransactionsWithStreamingResponse:
        return FinancialTransactionsWithStreamingResponse(self._financial_accounts.financial_transactions)

    @cached_property
    def statements(self) -> StatementsWithStreamingResponse:
        return StatementsWithStreamingResponse(self._financial_accounts.statements)


class AsyncFinancialAccountsWithStreamingResponse:
    def __init__(self, financial_accounts: AsyncFinancialAccounts) -> None:
        self._financial_accounts = financial_accounts

        self.list = async_to_streamed_response_wrapper(
            financial_accounts.list,
        )

    @cached_property
    def balances(self) -> AsyncBalancesWithStreamingResponse:
        return AsyncBalancesWithStreamingResponse(self._financial_accounts.balances)

    @cached_property
    def financial_transactions(self) -> AsyncFinancialTransactionsWithStreamingResponse:
        return AsyncFinancialTransactionsWithStreamingResponse(self._financial_accounts.financial_transactions)

    @cached_property
    def statements(self) -> AsyncStatementsWithStreamingResponse:
        return AsyncStatementsWithStreamingResponse(self._financial_accounts.statements)
