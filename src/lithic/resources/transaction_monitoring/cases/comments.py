# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .... import _legacy_response
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from ...._base_client import make_request_options
from ....types.transaction_monitoring.cases import comment_create_params, comment_update_params
from ....types.transaction_monitoring.case_activity_entry import CaseActivityEntry

__all__ = ["Comments", "AsyncComments"]


class Comments(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CommentsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return CommentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommentsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return CommentsWithStreamingResponse(self)

    def create(
        self,
        case_token: str,
        *,
        comment: str,
        actor_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaseActivityEntry:
        """
        Adds a comment to a case.

        Args:
          comment: Text of the comment

          actor_token: Optional client-provided identifier for the actor performing this action,
              recorded on the resulting activity entry. This value is supplied by the client
              (for example, your own internal user ID) and is not authenticated by Lithic

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        return self._post(
            path_template("/v1/transaction_monitoring/cases/{case_token}/comments", case_token=case_token),
            body=maybe_transform(
                {
                    "comment": comment,
                    "actor_token": actor_token,
                },
                comment_create_params.CommentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaseActivityEntry,
        )

    def update(
        self,
        comment_token: str,
        *,
        case_token: str,
        comment: str,
        actor_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaseActivityEntry:
        """
        Edits an existing comment on a case.

        Args:
          comment: New text of the comment

          actor_token: Optional client-provided identifier for the actor performing this action,
              recorded on the resulting activity entry. This value is supplied by the client
              (for example, your own internal user ID) and is not authenticated by Lithic

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        if not comment_token:
            raise ValueError(f"Expected a non-empty value for `comment_token` but received {comment_token!r}")
        return self._patch(
            path_template(
                "/v1/transaction_monitoring/cases/{case_token}/comments/{comment_token}",
                case_token=case_token,
                comment_token=comment_token,
            ),
            body=maybe_transform(
                {
                    "comment": comment,
                    "actor_token": actor_token,
                },
                comment_update_params.CommentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaseActivityEntry,
        )

    def delete(
        self,
        comment_token: str,
        *,
        case_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a comment from a case.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        if not comment_token:
            raise ValueError(f"Expected a non-empty value for `comment_token` but received {comment_token!r}")
        return self._delete(
            path_template(
                "/v1/transaction_monitoring/cases/{case_token}/comments/{comment_token}",
                case_token=case_token,
                comment_token=comment_token,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncComments(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCommentsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommentsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncCommentsWithStreamingResponse(self)

    async def create(
        self,
        case_token: str,
        *,
        comment: str,
        actor_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaseActivityEntry:
        """
        Adds a comment to a case.

        Args:
          comment: Text of the comment

          actor_token: Optional client-provided identifier for the actor performing this action,
              recorded on the resulting activity entry. This value is supplied by the client
              (for example, your own internal user ID) and is not authenticated by Lithic

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        return await self._post(
            path_template("/v1/transaction_monitoring/cases/{case_token}/comments", case_token=case_token),
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "actor_token": actor_token,
                },
                comment_create_params.CommentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaseActivityEntry,
        )

    async def update(
        self,
        comment_token: str,
        *,
        case_token: str,
        comment: str,
        actor_token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CaseActivityEntry:
        """
        Edits an existing comment on a case.

        Args:
          comment: New text of the comment

          actor_token: Optional client-provided identifier for the actor performing this action,
              recorded on the resulting activity entry. This value is supplied by the client
              (for example, your own internal user ID) and is not authenticated by Lithic

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        if not comment_token:
            raise ValueError(f"Expected a non-empty value for `comment_token` but received {comment_token!r}")
        return await self._patch(
            path_template(
                "/v1/transaction_monitoring/cases/{case_token}/comments/{comment_token}",
                case_token=case_token,
                comment_token=comment_token,
            ),
            body=await async_maybe_transform(
                {
                    "comment": comment,
                    "actor_token": actor_token,
                },
                comment_update_params.CommentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CaseActivityEntry,
        )

    async def delete(
        self,
        comment_token: str,
        *,
        case_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a comment from a case.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not case_token:
            raise ValueError(f"Expected a non-empty value for `case_token` but received {case_token!r}")
        if not comment_token:
            raise ValueError(f"Expected a non-empty value for `comment_token` but received {comment_token!r}")
        return await self._delete(
            path_template(
                "/v1/transaction_monitoring/cases/{case_token}/comments/{comment_token}",
                case_token=case_token,
                comment_token=comment_token,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CommentsWithRawResponse:
    def __init__(self, comments: Comments) -> None:
        self._comments = comments

        self.create = _legacy_response.to_raw_response_wrapper(
            comments.create,
        )
        self.update = _legacy_response.to_raw_response_wrapper(
            comments.update,
        )
        self.delete = _legacy_response.to_raw_response_wrapper(
            comments.delete,
        )


class AsyncCommentsWithRawResponse:
    def __init__(self, comments: AsyncComments) -> None:
        self._comments = comments

        self.create = _legacy_response.async_to_raw_response_wrapper(
            comments.create,
        )
        self.update = _legacy_response.async_to_raw_response_wrapper(
            comments.update,
        )
        self.delete = _legacy_response.async_to_raw_response_wrapper(
            comments.delete,
        )


class CommentsWithStreamingResponse:
    def __init__(self, comments: Comments) -> None:
        self._comments = comments

        self.create = to_streamed_response_wrapper(
            comments.create,
        )
        self.update = to_streamed_response_wrapper(
            comments.update,
        )
        self.delete = to_streamed_response_wrapper(
            comments.delete,
        )


class AsyncCommentsWithStreamingResponse:
    def __init__(self, comments: AsyncComments) -> None:
        self._comments = comments

        self.create = async_to_streamed_response_wrapper(
            comments.create,
        )
        self.update = async_to_streamed_response_wrapper(
            comments.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            comments.delete,
        )
