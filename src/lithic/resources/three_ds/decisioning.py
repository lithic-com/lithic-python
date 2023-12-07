# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper
from ..._base_client import make_request_options
from ...types.three_ds import DecisioningRetrieveSecretResponse

if TYPE_CHECKING:
    from ..._client import Lithic, AsyncLithic

__all__ = ["Decisioning", "AsyncDecisioning"]


class Decisioning(SyncAPIResource):
    with_raw_response: DecisioningWithRawResponse

    def __init__(self, client: Lithic) -> None:
        super().__init__(client)
        self.with_raw_response = DecisioningWithRawResponse(self)

    def retrieve_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DecisioningRetrieveSecretResponse:
        """Retrieve the 3DS Decisioning HMAC secret key.

        If one does not exist for your
        program yet, calling this endpoint will create one for you. The headers (which
        you can use to verify 3DS Decisioning requests) will begin appearing shortly
        after calling this endpoint for the first time. See
        [this page](https://docs.lithic.com/docs/3ds-decisioning#3ds-decisioning-hmac-secrets)
        for more detail about verifying 3DS Decisioning requests.
        """
        return self._get(
            "/three_ds_decisioning/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DecisioningRetrieveSecretResponse,
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
        """Generate a new 3DS Decisioning HMAC secret key.

        The old secret key will be
        deactivated 24 hours after a successful request to this endpoint. Make a
        [`GET /three_ds_decisioning/secret`](https://docs.lithic.com/reference/getthreedsdecisioningsecret)
        request to retrieve the new secret key.
        """
        return self._post(
            "/three_ds_decisioning/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class AsyncDecisioning(AsyncAPIResource):
    with_raw_response: AsyncDecisioningWithRawResponse

    def __init__(self, client: AsyncLithic) -> None:
        super().__init__(client)
        self.with_raw_response = AsyncDecisioningWithRawResponse(self)

    async def retrieve_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DecisioningRetrieveSecretResponse:
        """Retrieve the 3DS Decisioning HMAC secret key.

        If one does not exist for your
        program yet, calling this endpoint will create one for you. The headers (which
        you can use to verify 3DS Decisioning requests) will begin appearing shortly
        after calling this endpoint for the first time. See
        [this page](https://docs.lithic.com/docs/3ds-decisioning#3ds-decisioning-hmac-secrets)
        for more detail about verifying 3DS Decisioning requests.
        """
        return await self._get(
            "/three_ds_decisioning/secret",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DecisioningRetrieveSecretResponse,
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
        """Generate a new 3DS Decisioning HMAC secret key.

        The old secret key will be
        deactivated 24 hours after a successful request to this endpoint. Make a
        [`GET /three_ds_decisioning/secret`](https://docs.lithic.com/reference/getthreedsdecisioningsecret)
        request to retrieve the new secret key.
        """
        return await self._post(
            "/three_ds_decisioning/secret/rotate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                idempotency_key=idempotency_key,
            ),
            cast_to=NoneType,
        )


class DecisioningWithRawResponse:
    def __init__(self, decisioning: Decisioning) -> None:
        self.retrieve_secret = to_raw_response_wrapper(
            decisioning.retrieve_secret,
        )
        self.rotate_secret = to_raw_response_wrapper(
            decisioning.rotate_secret,
        )


class AsyncDecisioningWithRawResponse:
    def __init__(self, decisioning: AsyncDecisioning) -> None:
        self.retrieve_secret = async_to_raw_response_wrapper(
            decisioning.retrieve_secret,
        )
        self.rotate_secret = async_to_raw_response_wrapper(
            decisioning.rotate_secret,
        )
