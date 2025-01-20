# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import digital_card_art_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.digital_card_art import DigitalCardArt

__all__ = ["DigitalCardArtResource", "AsyncDigitalCardArtResource"]


class DigitalCardArtResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DigitalCardArtResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return DigitalCardArtResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DigitalCardArtResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return DigitalCardArtResourceWithStreamingResponse(self)

    def retrieve(
        self,
        digital_card_art_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DigitalCardArt:
        """
        Get digital card art by token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not digital_card_art_token:
            raise ValueError(
                f"Expected a non-empty value for `digital_card_art_token` but received {digital_card_art_token!r}"
            )
        return self._get(
            f"/v1/digital_card_art/{digital_card_art_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DigitalCardArt,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPage[DigitalCardArt]:
        """
        List digital card art.

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
            "/v1/digital_card_art",
            page=SyncCursorPage[DigitalCardArt],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    digital_card_art_list_params.DigitalCardArtListParams,
                ),
            ),
            model=DigitalCardArt,
        )


class AsyncDigitalCardArtResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDigitalCardArtResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDigitalCardArtResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDigitalCardArtResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncDigitalCardArtResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        digital_card_art_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DigitalCardArt:
        """
        Get digital card art by token.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not digital_card_art_token:
            raise ValueError(
                f"Expected a non-empty value for `digital_card_art_token` but received {digital_card_art_token!r}"
            )
        return await self._get(
            f"/v1/digital_card_art/{digital_card_art_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DigitalCardArt,
        )

    def list(
        self,
        *,
        ending_before: str | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        starting_after: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[DigitalCardArt, AsyncCursorPage[DigitalCardArt]]:
        """
        List digital card art.

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
            "/v1/digital_card_art",
            page=AsyncCursorPage[DigitalCardArt],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_before": ending_before,
                        "page_size": page_size,
                        "starting_after": starting_after,
                    },
                    digital_card_art_list_params.DigitalCardArtListParams,
                ),
            ),
            model=DigitalCardArt,
        )


class DigitalCardArtResourceWithRawResponse:
    def __init__(self, digital_card_art: DigitalCardArtResource) -> None:
        self._digital_card_art = digital_card_art

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            digital_card_art.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            digital_card_art.list,
        )


class AsyncDigitalCardArtResourceWithRawResponse:
    def __init__(self, digital_card_art: AsyncDigitalCardArtResource) -> None:
        self._digital_card_art = digital_card_art

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            digital_card_art.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            digital_card_art.list,
        )


class DigitalCardArtResourceWithStreamingResponse:
    def __init__(self, digital_card_art: DigitalCardArtResource) -> None:
        self._digital_card_art = digital_card_art

        self.retrieve = to_streamed_response_wrapper(
            digital_card_art.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            digital_card_art.list,
        )


class AsyncDigitalCardArtResourceWithStreamingResponse:
    def __init__(self, digital_card_art: AsyncDigitalCardArtResource) -> None:
        self._digital_card_art = digital_card_art

        self.retrieve = async_to_streamed_response_wrapper(
            digital_card_art.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            digital_card_art.list,
        )
