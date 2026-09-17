# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ... import _legacy_response
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..._base_client import make_request_options
from ...types.financial_accounts.open_to_buy import OpenToBuy

__all__ = ["OpenToBuyResource", "AsyncOpenToBuyResource"]


class OpenToBuyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OpenToBuyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return OpenToBuyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpenToBuyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return OpenToBuyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        financial_account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenToBuy:
        """
        Get the funds available for card spend backed by a given Security Account, along
        with the balances that amount is derived from.

        Open to buy is the amount Lithic authorizes card spend against. It is not a
        stored balance, so it is recalculated on every request from the Security
        Account, the funds held against spend Lithic has already paid out to the
        networks on your behalf, and the spend that has not yet been collected. The
        accounts that feed the calculation depend on your program setup, so
        `summary.settled_funds` is `null` outside Commercial Charge.

        Supported for Commercial Charge, Dynamic Reserve, and Secured Charge programs.
        Returns `404` if `financial_account_token` is not a Security Account you own, or
        if your program setup does not use an open to buy calculation.

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
            path_template(
                "/v1/financial_accounts/{financial_account_token}/open_to_buy",
                financial_account_token=financial_account_token,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenToBuy,
        )


class AsyncOpenToBuyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOpenToBuyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOpenToBuyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpenToBuyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncOpenToBuyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        financial_account_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OpenToBuy:
        """
        Get the funds available for card spend backed by a given Security Account, along
        with the balances that amount is derived from.

        Open to buy is the amount Lithic authorizes card spend against. It is not a
        stored balance, so it is recalculated on every request from the Security
        Account, the funds held against spend Lithic has already paid out to the
        networks on your behalf, and the spend that has not yet been collected. The
        accounts that feed the calculation depend on your program setup, so
        `summary.settled_funds` is `null` outside Commercial Charge.

        Supported for Commercial Charge, Dynamic Reserve, and Secured Charge programs.
        Returns `404` if `financial_account_token` is not a Security Account you own, or
        if your program setup does not use an open to buy calculation.

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
            path_template(
                "/v1/financial_accounts/{financial_account_token}/open_to_buy",
                financial_account_token=financial_account_token,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OpenToBuy,
        )


class OpenToBuyResourceWithRawResponse:
    def __init__(self, open_to_buy: OpenToBuyResource) -> None:
        self._open_to_buy = open_to_buy

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            open_to_buy.retrieve,
        )


class AsyncOpenToBuyResourceWithRawResponse:
    def __init__(self, open_to_buy: AsyncOpenToBuyResource) -> None:
        self._open_to_buy = open_to_buy

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            open_to_buy.retrieve,
        )


class OpenToBuyResourceWithStreamingResponse:
    def __init__(self, open_to_buy: OpenToBuyResource) -> None:
        self._open_to_buy = open_to_buy

        self.retrieve = to_streamed_response_wrapper(
            open_to_buy.retrieve,
        )


class AsyncOpenToBuyResourceWithStreamingResponse:
    def __init__(self, open_to_buy: AsyncOpenToBuyResource) -> None:
        self._open_to_buy = open_to_buy

        self.retrieve = async_to_streamed_response_wrapper(
            open_to_buy.retrieve,
        )
