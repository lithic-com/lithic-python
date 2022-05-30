# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union, Optional

from .._types import Timeout, NotGiven
from .._models import NoneModel, StringModel
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import AsyncPaginator, make_request_options
from ..types.auth_stream_enrollment import *
from ..types.auth_stream_enrollment_enroll_params import *

__all__ = ["AuthStreamEnrollmentResource", "AsyncAuthStreamEnrollmentResource"]


class AuthStreamEnrollmentResource(SyncAPIResource):
    def retrieve(
        self,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthStreamEnrollment:
        """
        Check status for whether you have enrolled in Authorization Stream Access (ASA)
        for your program in Sandbox.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._get("/auth_stream", model=AuthStreamEnrollment, options=options)

    def disenroll(
        self,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> None:
        """Disenroll Authorization Stream Access (ASA) in Sandbox."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        self._delete("/auth_stream", model=NoneModel, options=options)

    def enroll(
        self,
        body: Optional[AuthStreamEnrollmentEnrollParams] = None,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
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
        self._post("/auth_stream", model=NoneModel, body=body, options=options)


class AsyncAuthStreamEnrollmentResource(AsyncAPIResource):
    async def retrieve(
        self,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AuthStreamEnrollment:
        """
        Check status for whether you have enrolled in Authorization Stream Access (ASA)
        for your program in Sandbox.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._get("/auth_stream", model=AuthStreamEnrollment, options=options)

    async def disenroll(
        self,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> None:
        """Disenroll Authorization Stream Access (ASA) in Sandbox."""
        headers = {"Accept": "*/*", **(headers or {})}
        options = make_request_options(headers, max_retries, timeout)
        await self._delete("/auth_stream", model=NoneModel, options=options)

    async def enroll(
        self,
        body: Optional[AuthStreamEnrollmentEnrollParams] = None,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
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
        await self._post("/auth_stream", model=NoneModel, body=body, options=options)
