# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING
from typing_extensions import Literal

from ...types import FinancialAccount, financial_account_list_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from .balances import Balances, AsyncBalances
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from .financial_transactions import FinancialTransactions, AsyncFinancialTransactions

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["FinancialAccounts", "AsyncFinancialAccounts"]


class FinancialAccounts(SyncAPIResource):
    balances: Balances
    financial_transactions: FinancialTransactions

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.balances = Balances(client)
        self.financial_transactions = FinancialTransactions(client)

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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
    balances: AsyncBalances
    financial_transactions: AsyncFinancialTransactions

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.balances = AsyncBalances(client)
        self.financial_transactions = AsyncFinancialTransactions(client)

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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
