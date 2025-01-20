# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import card_program_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ..pagination import SyncCursorPage, AsyncCursorPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.card_program import CardProgram

__all__ = ["CardPrograms", "AsyncCardPrograms"]


class CardPrograms(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardProgramsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return CardProgramsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardProgramsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return CardProgramsWithStreamingResponse(self)

    def retrieve(
        self,
        card_program_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardProgram:
        """
        Get card program.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_program_token:
            raise ValueError(f"Expected a non-empty value for `card_program_token` but received {card_program_token!r}")
        return self._get(
            f"/v1/card_programs/{card_program_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardProgram,
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
    ) -> SyncCursorPage[CardProgram]:
        """
        List card programs.

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
            "/v1/card_programs",
            page=SyncCursorPage[CardProgram],
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
                    card_program_list_params.CardProgramListParams,
                ),
            ),
            model=CardProgram,
        )


class AsyncCardPrograms(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardProgramsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardProgramsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardProgramsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncCardProgramsWithStreamingResponse(self)

    async def retrieve(
        self,
        card_program_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CardProgram:
        """
        Get card program.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_program_token:
            raise ValueError(f"Expected a non-empty value for `card_program_token` but received {card_program_token!r}")
        return await self._get(
            f"/v1/card_programs/{card_program_token}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardProgram,
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
    ) -> AsyncPaginator[CardProgram, AsyncCursorPage[CardProgram]]:
        """
        List card programs.

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
            "/v1/card_programs",
            page=AsyncCursorPage[CardProgram],
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
                    card_program_list_params.CardProgramListParams,
                ),
            ),
            model=CardProgram,
        )


class CardProgramsWithRawResponse:
    def __init__(self, card_programs: CardPrograms) -> None:
        self._card_programs = card_programs

        self.retrieve = _legacy_response.to_raw_response_wrapper(
            card_programs.retrieve,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            card_programs.list,
        )


class AsyncCardProgramsWithRawResponse:
    def __init__(self, card_programs: AsyncCardPrograms) -> None:
        self._card_programs = card_programs

        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            card_programs.retrieve,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            card_programs.list,
        )


class CardProgramsWithStreamingResponse:
    def __init__(self, card_programs: CardPrograms) -> None:
        self._card_programs = card_programs

        self.retrieve = to_streamed_response_wrapper(
            card_programs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            card_programs.list,
        )


class AsyncCardProgramsWithStreamingResponse:
    def __init__(self, card_programs: AsyncCardPrograms) -> None:
        self._card_programs = card_programs

        self.retrieve = async_to_streamed_response_wrapper(
            card_programs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            card_programs.list,
        )
