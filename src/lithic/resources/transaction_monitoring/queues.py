# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ... import _legacy_response
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...pagination import SyncCursorPage, AsyncCursorPage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.transaction_monitoring import queue_list_params, queue_create_params, queue_update_params
from ...types.transaction_monitoring.queue import Queue

__all__ = ["Queues", "AsyncQueues"]


class Queues(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueuesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return QueuesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueuesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return QueuesWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Queue:
        """
        Creates a new queue for grouping transaction monitoring cases.

        Args:
          name: Human-readable name of the queue

          description: Optional description of the queue

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/transaction_monitoring/queues",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                queue_create_params.QueueCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Queue,
        )

    def retrieve(
        self,
        queue_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Queue:
        """
        Retrieves a single transaction monitoring queue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_token:
            raise ValueError(f"Expected a non-empty value for `queue_token` but received {queue_token!r}")
        return self._get(
            path_template("/v1/transaction_monitoring/queues/{queue_token}", queue_token=queue_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Queue,
        )

    def update(
        self,
        queue_token: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Queue:
        """
        Updates a transaction monitoring queue.

        Args:
          description: New description for the queue, or `null` to clear it

          name: New name for the queue

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_token:
            raise ValueError(f"Expected a non-empty value for `queue_token` but received {queue_token!r}")
        return self._patch(
            path_template("/v1/transaction_monitoring/queues/{queue_token}", queue_token=queue_token),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                queue_update_params.QueueUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Queue,
        )

    def list(
        self,
        *,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPage[Queue]:
        """
        Lists transaction monitoring queues.

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
            "/v1/transaction_monitoring/queues",
            page=SyncCursorPage[Queue],
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
                    queue_list_params.QueueListParams,
                ),
            ),
            model=Queue,
        )

    def delete(
        self,
        queue_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a transaction monitoring queue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_token:
            raise ValueError(f"Expected a non-empty value for `queue_token` but received {queue_token!r}")
        return self._delete(
            path_template("/v1/transaction_monitoring/queues/{queue_token}", queue_token=queue_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncQueues(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueuesWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueuesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueuesWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncQueuesWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Queue:
        """
        Creates a new queue for grouping transaction monitoring cases.

        Args:
          name: Human-readable name of the queue

          description: Optional description of the queue

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/transaction_monitoring/queues",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                queue_create_params.QueueCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Queue,
        )

    async def retrieve(
        self,
        queue_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Queue:
        """
        Retrieves a single transaction monitoring queue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_token:
            raise ValueError(f"Expected a non-empty value for `queue_token` but received {queue_token!r}")
        return await self._get(
            path_template("/v1/transaction_monitoring/queues/{queue_token}", queue_token=queue_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Queue,
        )

    async def update(
        self,
        queue_token: str,
        *,
        description: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Queue:
        """
        Updates a transaction monitoring queue.

        Args:
          description: New description for the queue, or `null` to clear it

          name: New name for the queue

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_token:
            raise ValueError(f"Expected a non-empty value for `queue_token` but received {queue_token!r}")
        return await self._patch(
            path_template("/v1/transaction_monitoring/queues/{queue_token}", queue_token=queue_token),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                queue_update_params.QueueUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Queue,
        )

    def list(
        self,
        *,
        ending_before: str | Omit = omit,
        page_size: int | Omit = omit,
        starting_after: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Queue, AsyncCursorPage[Queue]]:
        """
        Lists transaction monitoring queues.

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
            "/v1/transaction_monitoring/queues",
            page=AsyncCursorPage[Queue],
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
                    queue_list_params.QueueListParams,
                ),
            ),
            model=Queue,
        )

    async def delete(
        self,
        queue_token: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a transaction monitoring queue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not queue_token:
            raise ValueError(f"Expected a non-empty value for `queue_token` but received {queue_token!r}")
        return await self._delete(
            path_template("/v1/transaction_monitoring/queues/{queue_token}", queue_token=queue_token),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class QueuesWithRawResponse:
    def __init__(self, queues: Queues) -> None:
        self._queues = queues

        self.create = _legacy_response.to_raw_response_wrapper(
            queues.create,
        )
        self.retrieve = _legacy_response.to_raw_response_wrapper(
            queues.retrieve,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            queues.update,
        )
        self.list = _legacy_response.to_raw_response_wrapper(
            queues.list,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            queues.delete,
        )


class AsyncQueuesWithRawResponse:
    def __init__(self, queues: AsyncQueues) -> None:
        self._queues = queues

        self.create = _legacy_response.async_to_raw_response_wrapper(
            queues.create,
        )
        self.retrieve = _legacy_response.async_to_raw_response_wrapper(
            queues.retrieve,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            queues.update,
        )
        self.list = _legacy_response.async_to_raw_response_wrapper(
            queues.list,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            queues.delete,
        )


class QueuesWithStreamingResponse:
    def __init__(self, queues: Queues) -> None:
        self._queues = queues

        self.create = to_streamed_response_wrapper(
            queues.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            queues.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            queues.update,
        )
        self.list = to_streamed_response_wrapper(
            queues.list,
        )
        self.delete = to_streamed_response_wrapper(
            queues.delete,
        )


class AsyncQueuesWithStreamingResponse:
    def __init__(self, queues: AsyncQueues) -> None:
        self._queues = queues

        self.create = async_to_streamed_response_wrapper(
            queues.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            queues.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            queues.update,
        )
        self.list = async_to_streamed_response_wrapper(
            queues.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            queues.delete,
        )
