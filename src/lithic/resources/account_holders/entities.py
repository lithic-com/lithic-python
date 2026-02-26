# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ... import _legacy_response
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.account_holders import entity_create_params
from ...types.account_holders.account_holder_entity import AccountHolderEntity
from ...types.account_holders.entity_create_response import EntityCreateResponse

__all__ = ["Entities", "AsyncEntities"]


class Entities(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EntitiesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return EntitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return EntitiesWithStreamingResponse(self)

    def create(
        self,
        account_holder_token: str,
        *,
        address: entity_create_params.Address,
        dob: str,
        email: str,
        first_name: str,
        government_id: str,
        last_name: str,
        phone_number: str,
        type: Literal["BENEFICIAL_OWNER_INDIVIDUAL", "CONTROL_PERSON"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityCreateResponse:
        """
        Create a new beneficial owner or replace the control person entity on an
        existing KYB account holder. This endpoint is only applicable for account
        holders enrolled through a KYB workflow with the Persona KYB provider. A new
        control person can only replace the existing one. A maximum of 4 beneficial
        owners can be associated with an account holder.

        Args:
          address: Individual's current address - PO boxes, UPS drops, and FedEx drops are not
              acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.

          dob: Individual's date of birth, as an RFC 3339 date.

          email: Individual's email address. If utilizing Lithic for chargeback processing, this
              customer email address may be used to communicate dispute status and resolution.

          first_name: Individual's first name, as it appears on government-issued identity documents.

          government_id: Government-issued identification number (required for identity verification and
              compliance with banking regulations). Social Security Numbers (SSN) and
              Individual Taxpayer Identification Numbers (ITIN) are currently supported,
              entered as full nine-digits, with or without hyphens

          last_name: Individual's last name, as it appears on government-issued identity documents.

          phone_number: Individual's phone number, entered in E.164 format.

          type: The type of entity to create on the account holder

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        return self._post(
            f"/v1/account_holders/{account_holder_token}/entities",
            body=maybe_transform(
                {
                    "address": address,
                    "dob": dob,
                    "email": email,
                    "first_name": first_name,
                    "government_id": government_id,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "type": type,
                },
                entity_create_params.EntityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityCreateResponse,
        )

    def delete(
        self,
        entity_token: str,
        *,
        account_holder_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountHolderEntity:
        """Deactivate a beneficial owner entity on an existing KYB account holder.

        Only
        beneficial owner entities can be deactivated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        if not entity_token:
            raise ValueError(f"Expected a non-empty value for `entity_token` but received {entity_token!r}")
        return self._delete(
            f"/v1/account_holders/{account_holder_token}/entities/{entity_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderEntity,
        )


class AsyncEntities(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEntitiesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEntitiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncEntitiesWithStreamingResponse(self)

    async def create(
        self,
        account_holder_token: str,
        *,
        address: entity_create_params.Address,
        dob: str,
        email: str,
        first_name: str,
        government_id: str,
        last_name: str,
        phone_number: str,
        type: Literal["BENEFICIAL_OWNER_INDIVIDUAL", "CONTROL_PERSON"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> EntityCreateResponse:
        """
        Create a new beneficial owner or replace the control person entity on an
        existing KYB account holder. This endpoint is only applicable for account
        holders enrolled through a KYB workflow with the Persona KYB provider. A new
        control person can only replace the existing one. A maximum of 4 beneficial
        owners can be associated with an account holder.

        Args:
          address: Individual's current address - PO boxes, UPS drops, and FedEx drops are not
              acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.

          dob: Individual's date of birth, as an RFC 3339 date.

          email: Individual's email address. If utilizing Lithic for chargeback processing, this
              customer email address may be used to communicate dispute status and resolution.

          first_name: Individual's first name, as it appears on government-issued identity documents.

          government_id: Government-issued identification number (required for identity verification and
              compliance with banking regulations). Social Security Numbers (SSN) and
              Individual Taxpayer Identification Numbers (ITIN) are currently supported,
              entered as full nine-digits, with or without hyphens

          last_name: Individual's last name, as it appears on government-issued identity documents.

          phone_number: Individual's phone number, entered in E.164 format.

          type: The type of entity to create on the account holder

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        return await self._post(
            f"/v1/account_holders/{account_holder_token}/entities",
            body=await async_maybe_transform(
                {
                    "address": address,
                    "dob": dob,
                    "email": email,
                    "first_name": first_name,
                    "government_id": government_id,
                    "last_name": last_name,
                    "phone_number": phone_number,
                    "type": type,
                },
                entity_create_params.EntityCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityCreateResponse,
        )

    async def delete(
        self,
        entity_token: str,
        *,
        account_holder_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountHolderEntity:
        """Deactivate a beneficial owner entity on an existing KYB account holder.

        Only
        beneficial owner entities can be deactivated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_holder_token:
            raise ValueError(
                f"Expected a non-empty value for `account_holder_token` but received {account_holder_token!r}"
            )
        if not entity_token:
            raise ValueError(f"Expected a non-empty value for `entity_token` but received {entity_token!r}")
        return await self._delete(
            f"/v1/account_holders/{account_holder_token}/entities/{entity_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountHolderEntity,
        )


class EntitiesWithRawResponse:
    def __init__(self, entities: Entities) -> None:
        self._entities = entities

        self.create = _legacy_response.to_raw_response_wrapper(
            entities.create,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            entities.delete,
        )


class AsyncEntitiesWithRawResponse:
    def __init__(self, entities: AsyncEntities) -> None:
        self._entities = entities

        self.create = _legacy_response.async_to_raw_response_wrapper(
            entities.create,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            entities.delete,
        )


class EntitiesWithStreamingResponse:
    def __init__(self, entities: Entities) -> None:
        self._entities = entities

        self.create = to_streamed_response_wrapper(
            entities.create,
        )
        self.delete = to_streamed_response_wrapper(
            entities.delete,
        )


class AsyncEntitiesWithStreamingResponse:
    def __init__(self, entities: AsyncEntities) -> None:
        self._entities = entities

        self.create = async_to_streamed_response_wrapper(
            entities.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            entities.delete,
        )
