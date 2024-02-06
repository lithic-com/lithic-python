# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable

import httpx

from ... import _legacy_response
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import (
    make_request_options,
)
from ...types.external_bank_accounts import MicroDepositCreateResponse, micro_deposit_create_params

__all__ = ["MicroDeposits", "AsyncMicroDeposits"]


class MicroDeposits(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MicroDepositsWithRawResponse:
        return MicroDepositsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MicroDepositsWithStreamingResponse:
        return MicroDepositsWithStreamingResponse(self)

    def create(
        self,
        external_bank_account_token: str,
        *,
        micro_deposits: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MicroDepositCreateResponse:
        """
        Verify the external bank account by providing the micro deposit amounts.

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
            f"/external_bank_accounts/{external_bank_account_token}/micro_deposits",
            body=maybe_transform(
                {"micro_deposits": micro_deposits}, micro_deposit_create_params.MicroDepositCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MicroDepositCreateResponse,
        )


class AsyncMicroDeposits(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMicroDepositsWithRawResponse:
        return AsyncMicroDepositsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMicroDepositsWithStreamingResponse:
        return AsyncMicroDepositsWithStreamingResponse(self)

    async def create(
        self,
        external_bank_account_token: str,
        *,
        micro_deposits: Iterable[int],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MicroDepositCreateResponse:
        """
        Verify the external bank account by providing the micro deposit amounts.

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
            f"/external_bank_accounts/{external_bank_account_token}/micro_deposits",
            body=maybe_transform(
                {"micro_deposits": micro_deposits}, micro_deposit_create_params.MicroDepositCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MicroDepositCreateResponse,
        )


class MicroDepositsWithRawResponse:
    def __init__(self, micro_deposits: MicroDeposits) -> None:
        self._micro_deposits = micro_deposits

        self.create = _legacy_response.to_raw_response_wrapper(
            micro_deposits.create,
        )


class AsyncMicroDepositsWithRawResponse:
    def __init__(self, micro_deposits: AsyncMicroDeposits) -> None:
        self._micro_deposits = micro_deposits

        self.create = _legacy_response.async_to_raw_response_wrapper(
            micro_deposits.create,
        )


class MicroDepositsWithStreamingResponse:
    def __init__(self, micro_deposits: MicroDeposits) -> None:
        self._micro_deposits = micro_deposits

        self.create = to_streamed_response_wrapper(
            micro_deposits.create,
        )


class AsyncMicroDepositsWithStreamingResponse:
    def __init__(self, micro_deposits: AsyncMicroDeposits) -> None:
        self._micro_deposits = micro_deposits

        self.create = async_to_streamed_response_wrapper(
            micro_deposits.create,
        )
