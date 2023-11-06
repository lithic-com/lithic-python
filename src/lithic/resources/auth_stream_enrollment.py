# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..types import (
    AuthStreamSecret,
    AuthStreamEnrollment,
    auth_stream_enrollment_enroll_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Lithic, AsyncLithic

__all__ = ["AuthStreamEnrollmentResource", "AsyncAuthStreamEnrollmentResource"]


class AuthStreamEnrollmentResource(SyncAPIResource):
    with_raw_response: AuthStreamEnrollmentResourceWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = AuthStreamEnrollmentResourceWithRawResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthStreamEnrollment:
        """
        Check status for whether you have enrolled in Authorization Stream Access (ASA)
        for your program in Sandbox.
        """
        return self._get(
            "/auth_stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """Disenroll Authorization Stream Access (ASA) in Sandbox."""
        return self._delete(
            "/auth_stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return self._post(
            "/auth_stream",
            body=maybe_transform(
                {"webhook_url": webhook_url}, auth_stream_enrollment_enroll_params.AuthStreamEnrollmentEnrollParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    def retrieve_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthStreamSecret:
        """Retrieve the ASA HMAC secret key.

        If one does not exist for your program yet,
        calling this endpoint will create one for you. The headers (which you can use to
        verify webhooks) will begin appearing shortly after calling this endpoint for
        the first time. See
        [this page](https://docs.lithic.com/docs/auth-stream-access-asa#asa-webhook-verification)
        for more detail about verifying ASA webhooks.
        """
        return self._get(
            "/auth_stream/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthStreamSecret,
        )

    def rotate_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """Generate a new ASA HMAC secret key.

        The old ASA HMAC secret key will be
        deactivated 24 hours after a successful request to this endpoint. Make a
        [`GET /auth_stream/secret`](https://docs.lithic.com/reference/getauthstreamsecret)
        request to retrieve the new secret key.
        """
        return self._post(
            "/auth_stream/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncAuthStreamEnrollmentResource(AsyncAPIResource):
    with_raw_response: AsyncAuthStreamEnrollmentResourceWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncAuthStreamEnrollmentResourceWithRawResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthStreamEnrollment:
        """
        Check status for whether you have enrolled in Authorization Stream Access (ASA)
        for your program in Sandbox.
        """
        return await self._get(
            "/auth_stream",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """Disenroll Authorization Stream Access (ASA) in Sandbox."""
        return await self._delete(
            "/auth_stream",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
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

          timeout: Override the client-level default timeout for this request, in seconds

          idempotency_key: Specify a custom idempotency key for this request
        """
        return await self._post(
            "/auth_stream",
            body=maybe_transform(
                {"webhook_url": webhook_url}, auth_stream_enrollment_enroll_params.AuthStreamEnrollmentEnrollParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )

    async def retrieve_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthStreamSecret:
        """Retrieve the ASA HMAC secret key.

        If one does not exist for your program yet,
        calling this endpoint will create one for you. The headers (which you can use to
        verify webhooks) will begin appearing shortly after calling this endpoint for
        the first time. See
        [this page](https://docs.lithic.com/docs/auth-stream-access-asa#asa-webhook-verification)
        for more detail about verifying ASA webhooks.
        """
        return await self._get(
            "/auth_stream/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthStreamSecret,
        )

    async def rotate_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
    ) -> None:
        """Generate a new ASA HMAC secret key.

        The old ASA HMAC secret key will be
        deactivated 24 hours after a successful request to this endpoint. Make a
        [`GET /auth_stream/secret`](https://docs.lithic.com/reference/getauthstreamsecret)
        request to retrieve the new secret key.
        """
        return await self._post(
            "/auth_stream/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AuthStreamEnrollmentResourceWithRawResponse:
    def __init__(self, auth_stream_enrollment: AuthStreamEnrollmentResource) -> None:
        self.retrieve = to_raw_response_wrapper(
            auth_stream_enrollment.retrieve,
        )
        self.disenroll = to_raw_response_wrapper(
            auth_stream_enrollment.disenroll,
        )
        self.enroll = to_raw_response_wrapper(
            auth_stream_enrollment.enroll,
        )
        self.retrieve_secret = to_raw_response_wrapper(
            auth_stream_enrollment.retrieve_secret,
        )
        self.rotate_secret = to_raw_response_wrapper(
            auth_stream_enrollment.rotate_secret,
        )


class AsyncAuthStreamEnrollmentResourceWithRawResponse:
    def __init__(self, auth_stream_enrollment: AsyncAuthStreamEnrollmentResource) -> None:
        self.retrieve = async_to_raw_response_wrapper(
            auth_stream_enrollment.retrieve,
        )
        self.disenroll = async_to_raw_response_wrapper(
            auth_stream_enrollment.disenroll,
        )
        self.enroll = async_to_raw_response_wrapper(
            auth_stream_enrollment.enroll,
        )
        self.retrieve_secret = async_to_raw_response_wrapper(
            auth_stream_enrollment.retrieve_secret,
        )
        self.rotate_secret = async_to_raw_response_wrapper(
            auth_stream_enrollment.rotate_secret,
        )
