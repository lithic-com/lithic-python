# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import FinancialAccount, financial_account_list_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from .balances import Balances, AsyncBalances, BalancesWithRawResponse, AsyncBalancesWithRawResponse
from ..._compat import cached_property
from .statements import Statements, AsyncStatements, StatementsWithRawResponse, AsyncStatementsWithRawResponse
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
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
        self.balances = BalancesWithRawResponse(financial_accounts.balances)
        self.financial_transactions = FinancialTransactionsWithRawResponse(financial_accounts.financial_transactions)
        self.statements = StatementsWithRawResponse(financial_accounts.statements)

        self.list = to_raw_response_wrapper(
            financial_accounts.list,
        )


class AsyncFinancialAccountsWithRawResponse:
    def __init__(self, financial_accounts: AsyncFinancialAccounts) -> None:
        self.balances = AsyncBalancesWithRawResponse(financial_accounts.balances)
        self.financial_transactions = AsyncFinancialTransactionsWithRawResponse(
            financial_accounts.financial_transactions
        )
        self.statements = AsyncStatementsWithRawResponse(financial_accounts.statements)

        self.list = async_to_raw_response_wrapper(
            financial_accounts.list,
        )
