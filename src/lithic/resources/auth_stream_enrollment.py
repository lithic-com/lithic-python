# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..types import AuthStreamSecret
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import Lithic, AsyncLithic

__all__ = ["AuthStreamEnrollment", "AsyncAuthStreamEnrollment"]


class AuthStreamEnrollment(SyncAPIResource):
    with_raw_response: AuthStreamEnrollmentWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = AuthStreamEnrollmentWithRawResponse(self)

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


class AsyncAuthStreamEnrollment(AsyncAPIResource):
    with_raw_response: AsyncAuthStreamEnrollmentWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncAuthStreamEnrollmentWithRawResponse(self)

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


class AuthStreamEnrollmentWithRawResponse:
    def __init__(self, auth_stream_enrollment: AuthStreamEnrollment) -> None:
        self.retrieve_secret = to_raw_response_wrapper(
            auth_stream_enrollment.retrieve_secret,
        )
        self.rotate_secret = to_raw_response_wrapper(
            auth_stream_enrollment.rotate_secret,
        )


class AsyncAuthStreamEnrollmentWithRawResponse:
    def __init__(self, auth_stream_enrollment: AsyncAuthStreamEnrollment) -> None:
        self.retrieve_secret = async_to_raw_response_wrapper(
            auth_stream_enrollment.retrieve_secret,
        )
        self.rotate_secret = async_to_raw_response_wrapper(
            auth_stream_enrollment.rotate_secret,
        )
