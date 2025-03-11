# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import date
from typing_extensions import Literal, overload

import httpx

from ... import _legacy_response
from ...types import (
    OwnerType,
    VerificationMethod,
    external_bank_account_list_params,
    external_bank_account_create_params,
    external_bank_account_update_params,
    external_bank_account_retry_prenote_params,
    external_bank_account_retry_micro_deposits_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from .micro_deposits import (
    MicroDeposits,
    AsyncMicroDeposits,
    MicroDepositsWithRawResponse,
    AsyncMicroDepositsWithRawResponse,
    MicroDepositsWithStreamingResponse,
    AsyncMicroDepositsWithStreamingResponse,
)
from ...types.owner_type import OwnerType
from ...types.verification_method import VerificationMethod
from ...types.external_bank_account_address_param import ExternalBankAccountAddressParam
from ...types.external_bank_account_list_response import ExternalBankAccountListResponse
from ...types.external_bank_account_create_response import ExternalBankAccountCreateResponse
from ...types.external_bank_account_update_response import ExternalBankAccountUpdateResponse
from ...types.external_bank_account_retrieve_response import ExternalBankAccountRetrieveResponse
from ...types.external_bank_account_retry_prenote_response import ExternalBankAccountRetryPrenoteResponse
from ...types.external_bank_account_retry_micro_deposits_response import ExternalBankAccountRetryMicroDepositsResponse

__all__ = ["ExternalBankAccounts", "AsyncExternalBankAccounts"]


class ExternalBankAccounts(SyncAPIResource):
    @cached_property
    def micro_deposits(self) -> MicroDeposits:
        return MicroDeposits(self._client)

    @cached_property
    def with_raw_response(self) -> ExternalBankAccountsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return ExternalBankAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalBankAccountsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return ExternalBankAccountsWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_number: str,
        country: str,
        currency: str,
        financial_account_token: str,
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
    ) -> ExternalBankAccountCreateResponse:
        """
        Creates an external bank account within a program or Lithic account.

        Args:
          account_number: Account Number

          country: The country that the bank account is located in using ISO 3166-1. We will only
              accept USA bank accounts e.g., USA

          currency: currency of the external account 3-character alphabetic ISO 4217 code

          financial_account_token: The financial account token of the operating account to fund the micro deposits

          owner: Legal Name of the business or individual who owns the external account. This
              will appear in statements

          owner_type: Owner Type

          routing_number: Routing Number

          type: Account Type

          verification_method: Verification Method

          account_token: Indicates which Lithic account the external account is associated with. For
              external accounts that are associated with the program, account_token field
              returned will be null

          address: Address

          company_id: Optional field that helps identify bank accounts in receipts

          dob: Date of Birth of the Individual that owns the external bank account

          doing_business_as: Doing Business As

          name: The nickname for this External Bank Account

          user_defined_id: User Defined ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

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
    ) -> ExternalBankAccountCreateResponse:
        """
        Creates an external bank account within a program or Lithic account.

        Args:
          owner: Legal Name of the business or individual who owns the external account. This
              will appear in statements

          owner_type: Owner Type

          verification_method: Verification Method

          account_token: Indicates which Lithic account the external account is associated with. For
              external accounts that are associated with the program, account_token field
              returned will be null

          company_id: Optional field that helps identify bank accounts in receipts

          dob: Date of Birth of the Individual that owns the external bank account

          doing_business_as: Doing Business As

          user_defined_id: User Defined ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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
        verification_method: Literal["EXTERNALLY_VERIFIED"],
        account_token: str | NotGiven = NOT_GIVEN,
        address: ExternalBankAccountAddressParam | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        doing_business_as: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalBankAccountCreateResponse:
        """
        Creates an external bank account within a program or Lithic account.

        Args:
          account_number: Account Number

          country: The country that the bank account is located in using ISO 3166-1. We will only
              accept USA bank accounts e.g., USA

          currency: currency of the external account 3-character alphabetic ISO 4217 code

          owner: Legal Name of the business or individual who owns the external account. This
              will appear in statements

          owner_type: Owner Type

          routing_number: Routing Number

          type: Account Type

          verification_method: Verification Method

          account_token: Indicates which Lithic account the external account is associated with. For
              external accounts that are associated with the program, account_token field
              returned will be null

          address: Address

          company_id: Optional field that helps identify bank accounts in receipts

          dob: Date of Birth of the Individual that owns the external bank account

          doing_business_as: Doing Business As

          name: The nickname for this External Bank Account

          user_defined_id: User Defined ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        [
            "account_number",
            "country",
            "currency",
            "financial_account_token",
            "owner",
            "owner_type",
            "routing_number",
            "type",
            "verification_method",
        ],
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
        account_number: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        owner: str,
        owner_type: OwnerType,
        routing_number: str | NotGiven = NOT_GIVEN,
        type: Literal["CHECKING", "SAVINGS"] | NotGiven = NOT_GIVEN,
        verification_method: VerificationMethod | Literal["EXTERNALLY_VERIFIED"],
        account_token: str | NotGiven = NOT_GIVEN,
        address: ExternalBankAccountAddressParam | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        doing_business_as: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        verification_enforcement: bool | NotGiven = NOT_GIVEN,
        processor_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalBankAccountCreateResponse:
        return self._post(
            "/v1/external_bank_accounts",
            body=maybe_transform(
                {
                    "account_number": account_number,
                    "country": country,
                    "currency": currency,
                    "financial_account_token": financial_account_token,
                    "owner": owner,
                    "owner_type": owner_type,
                    "routing_number": routing_number,
                    "type": type,
                    "verification_method": verification_method,
                    "account_token": account_token,
                    "address": address,
                    "company_id": company_id,
                    "dob": dob,
                    "doing_business_as": doing_business_as,
                    "name": name,
                    "user_defined_id": user_defined_id,
                    "verification_enforcement": verification_enforcement,
                    "processor_token": processor_token,
                },
                external_bank_account_create_params.ExternalBankAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        if not external_bank_account_token:
            raise ValueError(
                f"Expected a non-empty value for `external_bank_account_token` but received {external_bank_account_token!r}"
            )
        return self._get(
            f"/v1/external_bank_accounts/{external_bank_account_token}",
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
        type: Literal["CHECKING", "SAVINGS"] | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalBankAccountUpdateResponse:
        """
        Update the external bank account by token.

        Args:
          address: Address

          company_id: Optional field that helps identify bank accounts in receipts

          dob: Date of Birth of the Individual that owns the external bank account

          doing_business_as: Doing Business As

          name: The nickname for this External Bank Account

          owner: Legal Name of the business or individual who owns the external account. This
              will appear in statements

          owner_type: Owner Type

          user_defined_id: User Defined ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_bank_account_token:
            raise ValueError(
                f"Expected a non-empty value for `external_bank_account_token` but received {external_bank_account_token!r}"
            )
        return self._patch(
            f"/v1/external_bank_accounts/{external_bank_account_token}",
            body=maybe_transform(
                {
                    "address": address,
                    "company_id": company_id,
                    "dob": dob,
                    "doing_business_as": doing_business_as,
                    "name": name,
                    "owner": owner,
                    "owner_type": owner_type,
                    "type": type,
                    "user_defined_id": user_defined_id,
                },
                external_bank_account_update_params.ExternalBankAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        verification_states: List[Literal["PENDING", "ENABLED", "FAILED_VERIFICATION", "INSUFFICIENT_FUNDS"]]
        | NotGiven = NOT_GIVEN,
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
            "/v1/external_bank_accounts",
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

    def retry_micro_deposits(
        self,
        external_bank_account_token: str,
        *,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalBankAccountRetryMicroDepositsResponse:
        """
        Retry external bank account micro deposit verification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_bank_account_token:
            raise ValueError(
                f"Expected a non-empty value for `external_bank_account_token` but received {external_bank_account_token!r}"
            )
        return self._post(
            f"/v1/external_bank_accounts/{external_bank_account_token}/retry_micro_deposits",
            body=maybe_transform(
                {"financial_account_token": financial_account_token},
                external_bank_account_retry_micro_deposits_params.ExternalBankAccountRetryMicroDepositsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBankAccountRetryMicroDepositsResponse,
        )

    def retry_prenote(
        self,
        external_bank_account_token: str,
        *,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalBankAccountRetryPrenoteResponse:
        """
        Retry external bank account prenote verification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_bank_account_token:
            raise ValueError(
                f"Expected a non-empty value for `external_bank_account_token` but received {external_bank_account_token!r}"
            )
        return self._post(
            f"/v1/external_bank_accounts/{external_bank_account_token}/retry_prenote",
            body=maybe_transform(
                {"financial_account_token": financial_account_token},
                external_bank_account_retry_prenote_params.ExternalBankAccountRetryPrenoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBankAccountRetryPrenoteResponse,
        )


class AsyncExternalBankAccounts(AsyncAPIResource):
    @cached_property
    def micro_deposits(self) -> AsyncMicroDeposits:
        return AsyncMicroDeposits(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExternalBankAccountsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalBankAccountsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalBankAccountsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncExternalBankAccountsWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_number: str,
        country: str,
        currency: str,
        financial_account_token: str,
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
    ) -> ExternalBankAccountCreateResponse:
        """
        Creates an external bank account within a program or Lithic account.

        Args:
          account_number: Account Number

          country: The country that the bank account is located in using ISO 3166-1. We will only
              accept USA bank accounts e.g., USA

          currency: currency of the external account 3-character alphabetic ISO 4217 code

          financial_account_token: The financial account token of the operating account to fund the micro deposits

          owner: Legal Name of the business or individual who owns the external account. This
              will appear in statements

          owner_type: Owner Type

          routing_number: Routing Number

          type: Account Type

          verification_method: Verification Method

          account_token: Indicates which Lithic account the external account is associated with. For
              external accounts that are associated with the program, account_token field
              returned will be null

          address: Address

          company_id: Optional field that helps identify bank accounts in receipts

          dob: Date of Birth of the Individual that owns the external bank account

          doing_business_as: Doing Business As

          name: The nickname for this External Bank Account

          user_defined_id: User Defined ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

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
    ) -> ExternalBankAccountCreateResponse:
        """
        Creates an external bank account within a program or Lithic account.

        Args:
          owner: Legal Name of the business or individual who owns the external account. This
              will appear in statements

          owner_type: Owner Type

          verification_method: Verification Method

          account_token: Indicates which Lithic account the external account is associated with. For
              external accounts that are associated with the program, account_token field
              returned will be null

          company_id: Optional field that helps identify bank accounts in receipts

          dob: Date of Birth of the Individual that owns the external bank account

          doing_business_as: Doing Business As

          user_defined_id: User Defined ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
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
        verification_method: Literal["EXTERNALLY_VERIFIED"],
        account_token: str | NotGiven = NOT_GIVEN,
        address: ExternalBankAccountAddressParam | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        doing_business_as: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalBankAccountCreateResponse:
        """
        Creates an external bank account within a program or Lithic account.

        Args:
          account_number: Account Number

          country: The country that the bank account is located in using ISO 3166-1. We will only
              accept USA bank accounts e.g., USA

          currency: currency of the external account 3-character alphabetic ISO 4217 code

          owner: Legal Name of the business or individual who owns the external account. This
              will appear in statements

          owner_type: Owner Type

          routing_number: Routing Number

          type: Account Type

          verification_method: Verification Method

          account_token: Indicates which Lithic account the external account is associated with. For
              external accounts that are associated with the program, account_token field
              returned will be null

          address: Address

          company_id: Optional field that helps identify bank accounts in receipts

          dob: Date of Birth of the Individual that owns the external bank account

          doing_business_as: Doing Business As

          name: The nickname for this External Bank Account

          user_defined_id: User Defined ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        [
            "account_number",
            "country",
            "currency",
            "financial_account_token",
            "owner",
            "owner_type",
            "routing_number",
            "type",
            "verification_method",
        ],
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
        account_number: str | NotGiven = NOT_GIVEN,
        country: str | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        owner: str,
        owner_type: OwnerType,
        routing_number: str | NotGiven = NOT_GIVEN,
        type: Literal["CHECKING", "SAVINGS"] | NotGiven = NOT_GIVEN,
        verification_method: VerificationMethod | Literal["EXTERNALLY_VERIFIED"],
        account_token: str | NotGiven = NOT_GIVEN,
        address: ExternalBankAccountAddressParam | NotGiven = NOT_GIVEN,
        company_id: str | NotGiven = NOT_GIVEN,
        dob: Union[str, date] | NotGiven = NOT_GIVEN,
        doing_business_as: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        verification_enforcement: bool | NotGiven = NOT_GIVEN,
        processor_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalBankAccountCreateResponse:
        return await self._post(
            "/v1/external_bank_accounts",
            body=await async_maybe_transform(
                {
                    "account_number": account_number,
                    "country": country,
                    "currency": currency,
                    "financial_account_token": financial_account_token,
                    "owner": owner,
                    "owner_type": owner_type,
                    "routing_number": routing_number,
                    "type": type,
                    "verification_method": verification_method,
                    "account_token": account_token,
                    "address": address,
                    "company_id": company_id,
                    "dob": dob,
                    "doing_business_as": doing_business_as,
                    "name": name,
                    "user_defined_id": user_defined_id,
                    "verification_enforcement": verification_enforcement,
                    "processor_token": processor_token,
                },
                external_bank_account_create_params.ExternalBankAccountCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        if not external_bank_account_token:
            raise ValueError(
                f"Expected a non-empty value for `external_bank_account_token` but received {external_bank_account_token!r}"
            )
        return await self._get(
            f"/v1/external_bank_accounts/{external_bank_account_token}",
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
        type: Literal["CHECKING", "SAVINGS"] | NotGiven = NOT_GIVEN,
        user_defined_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalBankAccountUpdateResponse:
        """
        Update the external bank account by token.

        Args:
          address: Address

          company_id: Optional field that helps identify bank accounts in receipts

          dob: Date of Birth of the Individual that owns the external bank account

          doing_business_as: Doing Business As

          name: The nickname for this External Bank Account

          owner: Legal Name of the business or individual who owns the external account. This
              will appear in statements

          owner_type: Owner Type

          user_defined_id: User Defined ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_bank_account_token:
            raise ValueError(
                f"Expected a non-empty value for `external_bank_account_token` but received {external_bank_account_token!r}"
            )
        return await self._patch(
            f"/v1/external_bank_accounts/{external_bank_account_token}",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "company_id": company_id,
                    "dob": dob,
                    "doing_business_as": doing_business_as,
                    "name": name,
                    "owner": owner,
                    "owner_type": owner_type,
                    "type": type,
                    "user_defined_id": user_defined_id,
                },
                external_bank_account_update_params.ExternalBankAccountUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
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
        verification_states: List[Literal["PENDING", "ENABLED", "FAILED_VERIFICATION", "INSUFFICIENT_FUNDS"]]
        | NotGiven = NOT_GIVEN,
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
            "/v1/external_bank_accounts",
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

    async def retry_micro_deposits(
        self,
        external_bank_account_token: str,
        *,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalBankAccountRetryMicroDepositsResponse:
        """
        Retry external bank account micro deposit verification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_bank_account_token:
            raise ValueError(
                f"Expected a non-empty value for `external_bank_account_token` but received {external_bank_account_token!r}"
            )
        return await self._post(
            f"/v1/external_bank_accounts/{external_bank_account_token}/retry_micro_deposits",
            body=await async_maybe_transform(
                {"financial_account_token": financial_account_token},
                external_bank_account_retry_micro_deposits_params.ExternalBankAccountRetryMicroDepositsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBankAccountRetryMicroDepositsResponse,
        )

    async def retry_prenote(
        self,
        external_bank_account_token: str,
        *,
        financial_account_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExternalBankAccountRetryPrenoteResponse:
        """
        Retry external bank account prenote verification.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_bank_account_token:
            raise ValueError(
                f"Expected a non-empty value for `external_bank_account_token` but received {external_bank_account_token!r}"
            )
        return await self._post(
            f"/v1/external_bank_accounts/{external_bank_account_token}/retry_prenote",
            body=await async_maybe_transform(
                {"financial_account_token": financial_account_token},
                external_bank_account_retry_prenote_params.ExternalBankAccountRetryPrenoteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalBankAccountRetryPrenoteResponse,
        )


class ExternalBankAccountsWithRawResponse:
    def __init__(self, external_bank_accounts: ExternalBankAccounts) -> None:
        self._external_bank_accounts = external_bank_accounts

        self.create = _legacy_response.to_raw_response_wrapper(
            external_bank_accounts.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            external_bank_accounts.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            external_bank_accounts.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            external_bank_accounts.list,
        )
        self.retry_micro_deposits = _legacy_response.to_raw_response_wrapper(
            external_bank_accounts.retry_micro_deposits,
        )
        self.retry_prenote = _legacy_response.to_raw_response_wrapper(
            external_bank_accounts.retry_prenote,
        )

    @cached_property
    def micro_deposits(self) -> MicroDepositsWithRawResponse:
        return MicroDepositsWithRawResponse(self._external_bank_accounts.micro_deposits)


class AsyncExternalBankAccountsWithRawResponse:
    def __init__(self, external_bank_accounts: AsyncExternalBankAccounts) -> None:
        self._external_bank_accounts = external_bank_accounts

        self.create = _legacy_response.async_to_raw_response_wrapper(
            external_bank_accounts.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            external_bank_accounts.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            external_bank_accounts.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            external_bank_accounts.list,
        )
        self.retry_micro_deposits = _legacy_response.async_to_raw_response_wrapper(
            external_bank_accounts.retry_micro_deposits,
        )
        self.retry_prenote = _legacy_response.async_to_raw_response_wrapper(
            external_bank_accounts.retry_prenote,
        )

    @cached_property
    def micro_deposits(self) -> AsyncMicroDepositsWithRawResponse:
        return AsyncMicroDepositsWithRawResponse(self._external_bank_accounts.micro_deposits)


class ExternalBankAccountsWithStreamingResponse:
    def __init__(self, external_bank_accounts: ExternalBankAccounts) -> None:
        self._external_bank_accounts = external_bank_accounts

        self.create = to_streamed_response_wrapper(
            external_bank_accounts.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            external_bank_accounts.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            external_bank_accounts.update,
        )
        self.list = to_streamed_response_wrapper(
            external_bank_accounts.list,
        )
        self.retry_micro_deposits = to_streamed_response_wrapper(
            external_bank_accounts.retry_micro_deposits,
        )
        self.retry_prenote = to_streamed_response_wrapper(
            external_bank_accounts.retry_prenote,
        )

    @cached_property
    def micro_deposits(self) -> MicroDepositsWithStreamingResponse:
        return MicroDepositsWithStreamingResponse(self._external_bank_accounts.micro_deposits)


class AsyncExternalBankAccountsWithStreamingResponse:
    def __init__(self, external_bank_accounts: AsyncExternalBankAccounts) -> None:
        self._external_bank_accounts = external_bank_accounts

        self.create = async_to_streamed_response_wrapper(
            external_bank_accounts.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            external_bank_accounts.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            external_bank_accounts.update,
        )
        self.list = async_to_streamed_response_wrapper(
            external_bank_accounts.list,
        )
        self.retry_micro_deposits = async_to_streamed_response_wrapper(
            external_bank_accounts.retry_micro_deposits,
        )
        self.retry_prenote = async_to_streamed_response_wrapper(
            external_bank_accounts.retry_prenote,
        )

    @cached_property
    def micro_deposits(self) -> AsyncMicroDepositsWithStreamingResponse:
        return AsyncMicroDepositsWithStreamingResponse(self._external_bank_accounts.micro_deposits)
