# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, overload
from datetime import date
from typing_extensions import Literal

import httpx

from ...types import (
    OwnerType,
    VerificationMethod,
    ExternalBankAccountAddressParam,
    ExternalBankAccountListResponse,
    ExternalBankAccountCreateResponse,
    ExternalBankAccountUpdateResponse,
    ExternalBankAccountRetrieveResponse,
    external_bank_account_list_params,
    external_bank_account_create_params,
    external_bank_account_update_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import required_args, maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from .micro_deposits import (
    MicroDeposits,
    AsyncMicroDeposits,
    MicroDepositsWithRawResponse,
    AsyncMicroDepositsWithRawResponse,
)

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["ExternalBankAccounts", "AsyncExternalBankAccounts"]


class ExternalBankAccounts(SyncAPIResource):
    micro_deposits: MicroDeposits
    with_raw_response: ExternalBankAccountsWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.micro_deposits = MicroDeposits(client)
        self.with_raw_response = ExternalBankAccountsWithRawResponse(self)

    @overload
    def create(
        self,
        *,
        owner: str,
        owner_type: OwnerType,
        processor_token: str,
        verification_method: VerificationMethod,
        account_token: str | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        doing_business_as: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalBankAccountCreateResponse:
        """
        Creates an external bank account within a program or Lithic account.

        Args:
          dob: Date of Birth of the Individual that owns the external bank account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    def create(
        self,
        *,
        account_number: str,
        country: str,
        currency: str,
        owner: str,
        owner_type: OwnerType,
        routing_number: str,
        type: Literal["CHECKING", "SAVINGS"],
        verification_method: VerificationMethod,
        account_token: str | NotGiven = NOT_GIVEN,
        address: ExternalBankAccountAddressParam | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        doing_business_as: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        verification_enforcement: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalBankAccountCreateResponse:
        """
        Creates an external bank account within a program or Lithic account.

        Args:
          address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules.

          dob: Date of Birth of the Individual that owns the external bank account

          verification_enforcement: Indicates whether verification was enforced for a given association record. For
              MICRO_DEPOSIT, option to disable verification if the external bank account has
              already been verified before. By default, verification will be required unless
              users pass in a value of false

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(
        ["owner", "owner_type", "processor_token", "verification_method"],
        [
            "account_number",
            "country",
            "currency",
            "owner",
            "owner_type",
            "routing_number",
            "type",
            "verification_method",
        ],
    )
    def create(
        self,
        *,
        owner: str,
        owner_type: OwnerType,
        processor_token: str | NotGiven = NOT_GIVEN,
        verification_method: VerificationMethod,
        account_token: str | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        doing_business_as: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        account_number: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        type: Literal["CHECKING", "SAVINGS"] | NotGiven = NOT_GIVEN,
        address: ExternalBankAccountAddressParam | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        verification_enforcement: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalBankAccountCreateResponse:
        return self._post(
            "/external_bank_accounts",
            body=maybe_transform(
                {
                    "owner": owner,
                    "owner_type": owner_type,
                    "processor_token": processor_token,
                    "verification_method": verification_method,
                    "account_token": account_token,
                    "company_id": company_id,
                    "dob": dob,
                    "doing_business_as": doing_business_as,
                    "user_defined_id": user_defined_id,
                    "account_number": account_number,
                    "country": country,
                    "currency": currency,
                    "routing_number": routing_number,
                    "type": type,
                    "address": address,
                    "name": name,
                    "verification_enforcement": verification_enforcement,
                },
                external_bank_account_create_params.ExternalBankAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExternalBankAccountCreateResponse,
        )

    def retrieve(
        self,
        external_bank_account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalBankAccountRetrieveResponse:
        """
        Get the external bank account by token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/external_bank_accounts/{external_bank_account_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBankAccountRetrieveResponse,
        )

    def update(
        self,
        external_bank_account_token: str,
        *,
        address: ExternalBankAccountAddressParam | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        doing_business_as: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        owner_type: OwnerType | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalBankAccountUpdateResponse:
        """
        Update the external bank account by token.

        Args:
          address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules.

          dob: Date of Birth of the Individual that owns the external bank account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._patch(
            f"/external_bank_accounts/{external_bank_account_token}",
            body=maybe_transform(
                {
                    "address": address,
                    "company_id": company_id,
                    "dob": dob,
                    "doing_business_as": doing_business_as,
                    "name": name,
                    "owner": owner,
                    "owner_type": owner_type,
                    "user_defined_id": user_defined_id,
                },
                external_bank_account_update_params.ExternalBankAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExternalBankAccountUpdateResponse,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        account_types: List[Literal["CHECKING", "SAVINGS"]] | NotGiven = NOT_GIVEN,
        countries: List[str] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        owner_types: List[OwnerType] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        states: List[Literal["ENABLED", "CLOSED", "PAUSED"]] | NotGiven = NOT_GIVEN,
        verification_states: List[Literal["PENDING", "ENABLED", "FAILED_VERIFICATION"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[ExternalBankAccountListResponse]:
        """
        List all the external bank accounts for the provided search criteria.

        Args:
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
            "/external_bank_accounts",
            page=SyncCursorPage[ExternalBankAccountListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "account_types": account_types,
                        "countries": countries,
                        "ending_before": ending_before,
                        "owner_types": owner_types,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "states": states,
                        "verification_states": verification_states,
                    },
                    external_bank_account_list_params.ExternalBankAccountListParams,
                ),
            ),
            model=ExternalBankAccountListResponse,
        )


class AsyncExternalBankAccounts(AsyncAPIResource):
    micro_deposits: AsyncMicroDeposits
    with_raw_response: AsyncExternalBankAccountsWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.micro_deposits = AsyncMicroDeposits(client)
        self.with_raw_response = AsyncExternalBankAccountsWithRawResponse(self)

    @overload
    async def create(
        self,
        *,
        owner: str,
        owner_type: OwnerType,
        processor_token: str,
        verification_method: VerificationMethod,
        account_token: str | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        doing_business_as: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalBankAccountCreateResponse:
        """
        Creates an external bank account within a program or Lithic account.

        Args:
          dob: Date of Birth of the Individual that owns the external bank account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_number: str,
        country: str,
        currency: str,
        owner: str,
        owner_type: OwnerType,
        routing_number: str,
        type: Literal["CHECKING", "SAVINGS"],
        verification_method: VerificationMethod,
        account_token: str | NotGiven = NOT_GIVEN,
        address: ExternalBankAccountAddressParam | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        doing_business_as: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        verification_enforcement: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalBankAccountCreateResponse:
        """
        Creates an external bank account within a program or Lithic account.

        Args:
          address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules.

          dob: Date of Birth of the Individual that owns the external bank account

          verification_enforcement: Indicates whether verification was enforced for a given association record. For
              MICRO_DEPOSIT, option to disable verification if the external bank account has
              already been verified before. By default, verification will be required unless
              users pass in a value of false

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        ...

    @required_args(
        ["owner", "owner_type", "processor_token", "verification_method"],
        [
            "account_number",
            "country",
            "currency",
            "owner",
            "owner_type",
            "routing_number",
            "type",
            "verification_method",
        ],
    )
    async def create(
        self,
        *,
        owner: str,
        owner_type: OwnerType,
        processor_token: str | NotGiven = NOT_GIVEN,
        verification_method: VerificationMethod,
        account_token: str | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        doing_business_as: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        account_number: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        routing_number: str | NotGiven = NOT_GIVEN,
        type: Literal["CHECKING", "SAVINGS"] | NotGiven = NOT_GIVEN,
        address: ExternalBankAccountAddressParam | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        verification_enforcement: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalBankAccountCreateResponse:
        return await self._post(
            "/external_bank_accounts",
            body=maybe_transform(
                {
                    "owner": owner,
                    "owner_type": owner_type,
                    "processor_token": processor_token,
                    "verification_method": verification_method,
                    "account_token": account_token,
                    "company_id": company_id,
                    "dob": dob,
                    "doing_business_as": doing_business_as,
                    "user_defined_id": user_defined_id,
                    "account_number": account_number,
                    "country": country,
                    "currency": currency,
                    "routing_number": routing_number,
                    "type": type,
                    "address": address,
                    "name": name,
                    "verification_enforcement": verification_enforcement,
                },
                external_bank_account_create_params.ExternalBankAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExternalBankAccountCreateResponse,
        )

    async def retrieve(
        self,
        external_bank_account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalBankAccountRetrieveResponse:
        """
        Get the external bank account by token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/external_bank_accounts/{external_bank_account_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBankAccountRetrieveResponse,
        )

    async def update(
        self,
        external_bank_account_token: str,
        *,
        address: ExternalBankAccountAddressParam | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        doing_business_as: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        owner: str | NotGiven = NOT_GIVEN,
        owner_type: OwnerType | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> ExternalBankAccountUpdateResponse:
        """
        Update the external bank account by token.

        Args:
          address: Address used during Address Verification Service (AVS) checks during
              transactions if enabled via Auth Rules.

          dob: Date of Birth of the Individual that owns the external bank account

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._patch(
            f"/external_bank_accounts/{external_bank_account_token}",
            body=maybe_transform(
                {
                    "address": address,
                    "company_id": company_id,
                    "dob": dob,
                    "doing_business_as": doing_business_as,
                    "name": name,
                    "owner": owner,
                    "owner_type": owner_type,
                    "user_defined_id": user_defined_id,
                },
                external_bank_account_update_params.ExternalBankAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=ExternalBankAccountUpdateResponse,
        )

    def list(
        self,
        *,
        account_token: str | NotGiven = NOT_GIVEN,
        account_types: List[Literal["CHECKING", "SAVINGS"]] | NotGiven = NOT_GIVEN,
        countries: List[str] | NotGiven = NOT_GIVEN,
        ending_before: str | NotGiven = NOT_GIVEN,
        owner_types: List[OwnerType] | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        states: List[Literal["ENABLED", "CLOSED", "PAUSED"]] | NotGiven = NOT_GIVEN,
        verification_states: List[Literal["PENDING", "ENABLED", "FAILED_VERIFICATION"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ExternalBankAccountListResponse, AsyncCursorPage[ExternalBankAccountListResponse]]:
        """
        List all the external bank accounts for the provided search criteria.

        Args:
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
            "/external_bank_accounts",
            page=AsyncCursorPage[ExternalBankAccountListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "account_types": account_types,
                        "countries": countries,
                        "ending_before": ending_before,
                        "owner_types": owner_types,
                        "page_size": page_size,
                        "starting_after": starting_after,
                        "states": states,
                        "verification_states": verification_states,
                    },
                    external_bank_account_list_params.ExternalBankAccountListParams,
                ),
            ),
            model=ExternalBankAccountListResponse,
        )


class ExternalBankAccountsWithRawResponse:
    def __init__(self, external_bank_accounts: ExternalBankAccounts) -> None:
        self.micro_deposits = MicroDepositsWithRawResponse(external_bank_accounts.micro_deposits)

        self.create = to_raw_response_wrapper(
            external_bank_accounts.create,
        )
        self.retrieve = to_raw_response_wrapper(
            external_bank_accounts.retrieve,
        )
        self.update = to_raw_response_wrapper(
            external_bank_accounts.update,
        )
        self.list = to_raw_response_wrapper(
            external_bank_accounts.list,
        )


class AsyncExternalBankAccountsWithRawResponse:
    def __init__(self, external_bank_accounts: AsyncExternalBankAccounts) -> None:
        self.micro_deposits = AsyncMicroDepositsWithRawResponse(external_bank_accounts.micro_deposits)

        self.create = async_to_raw_response_wrapper(
            external_bank_accounts.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            external_bank_accounts.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            external_bank_accounts.update,
        )
        self.list = async_to_raw_response_wrapper(
            external_bank_accounts.list,
        )
