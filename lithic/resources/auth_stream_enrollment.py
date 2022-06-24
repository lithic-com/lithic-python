# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NoneType, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options
from ..types.auth_stream_enrollment import *
from ..types.auth_stream_enrollment_enroll_params import (
    AuthStreamEnrollmentEnrollParams,
)

__all__ = ["AuthStreamEnrollmentResource", "AsyncAuthStreamEnrollmentResource"]


class AuthStreamEnrollmentResource(SyncAPIResource):
    def retrieve(
        self,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AuthStreamEnrollment:
        """
        Check status for whether you have enrolled in Authorization Stream Access (ASA)
        for your program in Sandbox.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._get(
            "/auth_stream",
            options=options,
            cast_to=AuthStreamEnrollment,
        )

    def disenroll(
        self,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> None:
        """Disenroll Authorization Stream Access (ASA) in Sandbox."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self._delete(
            "/auth_stream",
            options=options,
            cast_to=NoneType,
        )

    def enroll(
        self,
        body: AuthStreamEnrollmentEnrollParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/auth_stream",
            body=body,
            options=options,
            cast_to=NoneType,
        )


class AsyncAuthStreamEnrollmentResource(AsyncAPIResource):
    async def retrieve(
        self,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AuthStreamEnrollment:
        """
        Check status for whether you have enrolled in Authorization Stream Access (ASA)
        for your program in Sandbox.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._get(
            "/auth_stream",
            options=options,
            cast_to=AuthStreamEnrollment,
        )

    async def disenroll(
        self,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> None:
        """Disenroll Authorization Stream Access (ASA) in Sandbox."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self._delete(
            "/auth_stream",
            options=options,
            cast_to=NoneType,
        )

    async def enroll(
        self,
        body: AuthStreamEnrollmentEnrollParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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
        """
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/auth_stream",
            body=body,
            options=options,
            cast_to=NoneType,
        )
