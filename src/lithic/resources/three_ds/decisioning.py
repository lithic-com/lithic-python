# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.three_ds import DecisioningRetrieveSecretResponse

__all__ = ["Decisioning", "AsyncDecisioning"]


class Decisioning(SyncAPIResource):
    def retrieve_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
    async def retrieve_secret(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
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
        timeout: float | None | NotGiven = NOT_GIVEN,
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
