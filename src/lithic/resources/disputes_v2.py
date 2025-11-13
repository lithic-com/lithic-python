# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from .. import _legacy_response
from ..types import disputes_v2_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.dispute_v2 import DisputeV2

__all__ = ["DisputesV2", "AsyncDisputesV2"]


class DisputesV2(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DisputesV2WithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return DisputesV2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DisputesV2WithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return DisputesV2WithStreamingResponse(self)

    def retrieve(
        self,
        dispute_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DisputeV2:
        """
        Retrieves a specific dispute by its token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        return self._get(
            f"/v2/disputes/{dispute_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeV2,
        )

    def list(
        self,
        *,
        account_token: str | Omit = omit,
        begin: Union[str, datetime] | Omit = omit,
        card_token: str | Omit = omit,
        disputed_transaction_token: str | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[DisputeV2]:
        """
        Returns a paginated list of disputes.

        Args:
          account_token: Filter by account token.

          begin: RFC 3339 timestamp for filtering by created date, inclusive.

          card_token: Filter by card token.

          disputed_transaction_token: Filter by the token of the transaction being disputed. Corresponds with
              transaction_series.related_transaction_token in the Dispute.

          end: RFC 3339 timestamp for filtering by created date, inclusive.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Number of items to return.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/disputes",
            page=SyncCursorPage[DisputeV2],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "begin": begin,
                        "card_token": card_token,
                        "disputed_transaction_token": disputed_transaction_token,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    disputes_v2_list_params.DisputesV2ListParams,
                ),
            ),
            model=DisputeV2,
        )


class AsyncDisputesV2(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDisputesV2WithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDisputesV2WithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDisputesV2WithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncDisputesV2WithStreamingResponse(self)

    async def retrieve(
        self,
        dispute_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DisputeV2:
        """
        Retrieves a specific dispute by its token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dispute_token:
            raise ValueError(f"Expected a non-empty value for `dispute_token` but received {dispute_token!r}")
        return await self._get(
            f"/v2/disputes/{dispute_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DisputeV2,
        )

    def list(
        self,
        *,
        account_token: str | Omit = omit,
        begin: Union[str, datetime] | Omit = omit,
        card_token: str | Omit = omit,
        disputed_transaction_token: str | Omit = omit,
        end: Union[str, datetime] | Omit = omit,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DisputeV2, AsyncCursorPage[DisputeV2]]:
        """
        Returns a paginated list of disputes.

        Args:
          account_token: Filter by account token.

          begin: RFC 3339 timestamp for filtering by created date, inclusive.

          card_token: Filter by card token.

          disputed_transaction_token: Filter by the token of the transaction being disputed. Corresponds with
              transaction_series.related_transaction_token in the Dispute.

          end: RFC 3339 timestamp for filtering by created date, inclusive.

          ending_before: A cursor representing an item's token before which a page of results should end.
              Used to retrieve the previous page of results before this item.

          page_size: Number of items to return.

          starting_after: A cursor representing an item's token after which a page of results should
              begin. Used to retrieve the next page of results after this item.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v2/disputes",
            page=AsyncCursorPage[DisputeV2],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_token": account_token,
                        "begin": begin,
                        "card_token": card_token,
                        "disputed_transaction_token": disputed_transaction_token,
                        "end": end,
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    disputes_v2_list_params.DisputesV2ListParams,
                ),
            ),
            model=DisputeV2,
        )


class DisputesV2WithRawResponse:
    def __init__(self, disputes_v2: DisputesV2) -> None:
        self._disputes_v2 = disputes_v2

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            disputes_v2.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            disputes_v2.list,
        )


class AsyncDisputesV2WithRawResponse:
    def __init__(self, disputes_v2: AsyncDisputesV2) -> None:
        self._disputes_v2 = disputes_v2

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            disputes_v2.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            disputes_v2.list,
        )


class DisputesV2WithStreamingResponse:
    def __init__(self, disputes_v2: DisputesV2) -> None:
        self._disputes_v2 = disputes_v2

        self.retrieve = to_streamed_response_wrapper(
            disputes_v2.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            disputes_v2.list,
        )


class AsyncDisputesV2WithStreamingResponse:
    def __init__(self, disputes_v2: AsyncDisputesV2) -> None:
        self._disputes_v2 = disputes_v2

        self.retrieve = async_to_streamed_response_wrapper(
            disputes_v2.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            disputes_v2.list,
        )
