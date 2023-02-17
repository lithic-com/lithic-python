# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..types import AuthStreamEnrollment
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["AuthStreamEnrollmentResource", "AsyncAuthStreamEnrollmentResource"]


class AuthStreamEnrollmentResource(SyncAPIResource):
    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AuthStreamEnrollment:
        """
        Check status for whether you have enrolled in Authorization Stream Access (ASA)
        for your program in Sandbox.
        """
        return self._get(
            "/auth_stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AuthStreamEnrollment,
        )

    def disenroll(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """Disenroll Authorization Stream Access (ASA) in Sandbox."""
        return self._delete(
            "/auth_stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )

    def enroll(
        self,
        *,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Authorization Stream Access (ASA) provides the ability to make custom
        transaction approval decisions through an HTTP interface to the ISO 8583 message
        stream.

        ASA requests are delivered as an HTTP POST during authorization. The ASA request
        body adheres to the Lithic transaction schema, with some additional fields added
        for use in decisioning. A response should be sent with HTTP response code 200
        and the approval decision in the response body. This response is converted by
        Lithic back into ISO 8583 format and forwarded to the network.

        In Sandbox, users can self-enroll and disenroll in ASA. In production,
        onboarding requires manual approval and setup.

        Args:
          webhook_url: A user-specified url to receive and respond to ASA request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return self._post(
            "/auth_stream",
            body={"webhook_url": webhook_url},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )


class AsyncAuthStreamEnrollmentResource(AsyncAPIResource):
    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> AuthStreamEnrollment:
        """
        Check status for whether you have enrolled in Authorization Stream Access (ASA)
        for your program in Sandbox.
        """
        return await self._get(
            "/auth_stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=AuthStreamEnrollment,
        )

    async def disenroll(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """Disenroll Authorization Stream Access (ASA) in Sandbox."""
        return await self._delete(
            "/auth_stream",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )

    async def enroll(
        self,
        *,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> None:
        """
        Authorization Stream Access (ASA) provides the ability to make custom
        transaction approval decisions through an HTTP interface to the ISO 8583 message
        stream.

        ASA requests are delivered as an HTTP POST during authorization. The ASA request
        body adheres to the Lithic transaction schema, with some additional fields added
        for use in decisioning. A response should be sent with HTTP response code 200
        and the approval decision in the response body. This response is converted by
        Lithic back into ISO 8583 format and forwarded to the network.

        In Sandbox, users can self-enroll and disenroll in ASA. In production,
        onboarding requires manual approval and setup.

        Args:
          webhook_url: A user-specified url to receive and respond to ASA request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request
        """
        return await self._post(
            "/auth_stream",
            body={"webhook_url": webhook_url},
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body),
            cast_to=NoneType,
        )
