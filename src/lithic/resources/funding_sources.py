# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, overload
from typing_extensions import Literal

from ..types import FundingSource
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import required_args
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["FundingSources", "AsyncFundingSources"]


class FundingSources(SyncAPIResource):
    @overload
    def create(
        self,
        *,
        validation_method: Literal["BANK"],
        account_name: str | NotGiven = NOT_GIVEN,
        account_number: str,
        account_token: str | NotGiven = NOT_GIVEN,
        routing_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> FundingSource:
        """
        Add a funding source using bank routing and account numbers or via Plaid.

        In the production environment, funding accounts will be set to `PENDING` state
        until micro-deposit validation completes while funding accounts in sandbox will
        be set to `ENABLED` state automatically.

        Args:
          account_name: The name associated with the bank account. This property is only for
              identification purposes, and has no bearing on the external properties of the
              bank.

          account_number: The account number of the bank account.

          account_token: Only required for multi-account users. Token identifying the account that the
              bank account will be associated with. Only applicable if using account holder
              enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          routing_number: The routing number of the bank account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    def create(
        self,
        *,
        validation_method: Literal["PLAID"],
        account_token: str | NotGiven = NOT_GIVEN,
        processor_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> FundingSource:
        """
        Add a funding source using bank routing and account numbers or via Plaid.

        In the production environment, funding accounts will be set to `PENDING` state
        until micro-deposit validation completes while funding accounts in sandbox will
        be set to `ENABLED` state automatically.

        Args:
          account_token: Only required for multi-account users. Token identifying the account associated
              with the bank account. Only applicable if using account holder enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          processor_token: The processor token associated with the bank account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @required_args(["validation_method", "account_number", "routing_number"], ["validation_method", "processor_token"])
    def create(
        self,
        *,
        validation_method: Literal["BANK"] | Literal["PLAID"] | NotGiven = NOT_GIVEN,
        account_name: str | NotGiven = NOT_GIVEN,
        account_number: str | NotGiven = NOT_GIVEN,
        account_token: str | str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        processor_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> FundingSource:
        """
        Add a funding source using bank routing and account numbers or via Plaid.

        In the production environment, funding accounts will be set to `PENDING` state
        until micro-deposit validation completes while funding accounts in sandbox will
        be set to `ENABLED` state automatically.

        Args:
          account_name: The name associated with the bank account. This property is only for
              identification purposes, and has no bearing on the external properties of the
              bank.

          account_number: The account number of the bank account.

          account_token: Only required for multi-account users. Token identifying the account that the
              bank account will be associated with. Only applicable if using account holder
              enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          routing_number: The routing number of the bank account.

          processor_token: The processor token associated with the bank account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/funding_sources",
            body={
                "validation_method": validation_method,
                "account_name": account_name,
                "account_number": account_number,
                "account_token": account_token,
                "routing_number": routing_number,
                "processor_token": processor_token,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=FundingSource,
        )

    def update(
        self,
        funding_source_token: str,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        state: Literal["DELETED", "ENABLED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> FundingSource:
        """
        Update a funding source.

        Args:
          account_token: Only required for multi-account users. Token identifying the account that the
              bank account will be associated with. Only applicable if using account holder
              enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          state: The desired state of the bank account.

              If a bank account is set to `DELETED`, all cards linked to this account will no
              longer be associated with it. If there are no other bank accounts in state
              `ENABLED` on the account, authorizations will not be accepted on the card until
              a new funding account is added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._patch(
            f"/funding_sources/{funding_source_token}",
            body={
                "account_token": account_token,
                "state": state,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=FundingSource,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SyncPage[FundingSource]:
        """
        List all the funding sources associated with the Lithic account.

        Args:
          page: Page (for pagination).

          page_size: Page size (for pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/funding_sources",
            page=SyncPage[FundingSource],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "account_token": account_token,
                    "page": page,
                    "page_size": page_size,
                },
            ),
            model=FundingSource,
        )

    def verify(
        self,
        funding_source_token: str,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        micro_deposits: List[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> FundingSource:
        """
        Verify a bank account as a funding source by providing received micro-deposit
        amounts.

        Args:
          account_token: Only required for multi-account users. Token identifying the account that the
              bank account will be associated with. Only applicable if using account holder
              enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          micro_deposits: An array of dollar amounts (in cents) received in two credit transactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            f"/funding_sources/{funding_source_token}/verify",
            body={
                "account_token": account_token,
                "micro_deposits": micro_deposits,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=FundingSource,
        )


class AsyncFundingSources(AsyncAPIResource):
    @overload
    async def create(
        self,
        *,
        validation_method: Literal["BANK"],
        account_name: str | NotGiven = NOT_GIVEN,
        account_number: str,
        account_token: str | NotGiven = NOT_GIVEN,
        routing_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> FundingSource:
        """
        Add a funding source using bank routing and account numbers or via Plaid.

        In the production environment, funding accounts will be set to `PENDING` state
        until micro-deposit validation completes while funding accounts in sandbox will
        be set to `ENABLED` state automatically.

        Args:
          account_name: The name associated with the bank account. This property is only for
              identification purposes, and has no bearing on the external properties of the
              bank.

          account_number: The account number of the bank account.

          account_token: Only required for multi-account users. Token identifying the account that the
              bank account will be associated with. Only applicable if using account holder
              enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          routing_number: The routing number of the bank account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @overload
    async def create(
        self,
        *,
        validation_method: Literal["PLAID"],
        account_token: str | NotGiven = NOT_GIVEN,
        processor_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> FundingSource:
        """
        Add a funding source using bank routing and account numbers or via Plaid.

        In the production environment, funding accounts will be set to `PENDING` state
        until micro-deposit validation completes while funding accounts in sandbox will
        be set to `ENABLED` state automatically.

        Args:
          account_token: Only required for multi-account users. Token identifying the account associated
              with the bank account. Only applicable if using account holder enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          processor_token: The processor token associated with the bank account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        ...

    @required_args(["validation_method", "account_number", "routing_number"], ["validation_method", "processor_token"])
    async def create(
        self,
        *,
        validation_method: Literal["BANK"] | Literal["PLAID"] | NotGiven = NOT_GIVEN,
        account_name: str | NotGiven = NOT_GIVEN,
        account_number: str | NotGiven = NOT_GIVEN,
        account_token: str | str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        processor_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> FundingSource:
        """
        Add a funding source using bank routing and account numbers or via Plaid.

        In the production environment, funding accounts will be set to `PENDING` state
        until micro-deposit validation completes while funding accounts in sandbox will
        be set to `ENABLED` state automatically.

        Args:
          account_name: The name associated with the bank account. This property is only for
              identification purposes, and has no bearing on the external properties of the
              bank.

          account_number: The account number of the bank account.

          account_token: Only required for multi-account users. Token identifying the account that the
              bank account will be associated with. Only applicable if using account holder
              enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          routing_number: The routing number of the bank account.

          processor_token: The processor token associated with the bank account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/funding_sources",
            body={
                "validation_method": validation_method,
                "account_name": account_name,
                "account_number": account_number,
                "account_token": account_token,
                "routing_number": routing_number,
                "processor_token": processor_token,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=FundingSource,
        )

    async def update(
        self,
        funding_source_token: str,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        state: Literal["DELETED", "ENABLED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> FundingSource:
        """
        Update a funding source.

        Args:
          account_token: Only required for multi-account users. Token identifying the account that the
              bank account will be associated with. Only applicable if using account holder
              enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          state: The desired state of the bank account.

              If a bank account is set to `DELETED`, all cards linked to this account will no
              longer be associated with it. If there are no other bank accounts in state
              `ENABLED` on the account, authorizations will not be accepted on the card until
              a new funding account is added.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._patch(
            f"/funding_sources/{funding_source_token}",
            body={
                "account_token": account_token,
                "state": state,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=FundingSource,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AsyncPaginator[FundingSource, AsyncPage[FundingSource]]:
        """
        List all the funding sources associated with the Lithic account.

        Args:
          page: Page (for pagination).

          page_size: Page size (for pagination).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._get_api_list(
            "/funding_sources",
            page=AsyncPage[FundingSource],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                query={
                    "account_token": account_token,
                    "page": page,
                    "page_size": page_size,
                },
            ),
            model=FundingSource,
        )

    async def verify(
        self,
        funding_source_token: str,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        micro_deposits: List[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> FundingSource:
        """
        Verify a bank account as a funding source by providing received micro-deposit
        amounts.

        Args:
          account_token: Only required for multi-account users. Token identifying the account that the
              bank account will be associated with. Only applicable if using account holder
              enrollment. See
              [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
              more information.

          micro_deposits: An array of dollar amounts (in cents) received in two credit transactions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            f"/funding_sources/{funding_source_token}/verify",
            body={
                "account_token": account_token,
                "micro_deposits": micro_deposits,
            },
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=FundingSource,
        )
