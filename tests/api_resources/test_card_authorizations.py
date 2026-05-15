# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCardAuthorizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_challenge_response(self, client: Lithic) -> None:
        card_authorization = client.card_authorizations.challenge_response(
            event_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            response="APPROVE",
        )
        assert card_authorization is None

    @parametrize
    def test_raw_response_challenge_response(self, client: Lithic) -> None:
        response = client.card_authorizations.with_raw_response.challenge_response(
            event_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            response="APPROVE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_authorization = response.parse()
        assert card_authorization is None

    @parametrize
    def test_streaming_response_challenge_response(self, client: Lithic) -> None:
        with client.card_authorizations.with_streaming_response.challenge_response(
            event_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            response="APPROVE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_authorization = response.parse()
            assert card_authorization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_challenge_response(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_token` but received ''"):
            client.card_authorizations.with_raw_response.challenge_response(
                event_token="",
                response="APPROVE",
            )


class TestAsyncCardAuthorizations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_challenge_response(self, async_client: AsyncLithic) -> None:
        card_authorization = await async_client.card_authorizations.challenge_response(
            event_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            response="APPROVE",
        )
        assert card_authorization is None

    @parametrize
    async def test_raw_response_challenge_response(self, async_client: AsyncLithic) -> None:
        response = await async_client.card_authorizations.with_raw_response.challenge_response(
            event_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            response="APPROVE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card_authorization = response.parse()
        assert card_authorization is None

    @parametrize
    async def test_streaming_response_challenge_response(self, async_client: AsyncLithic) -> None:
        async with async_client.card_authorizations.with_streaming_response.challenge_response(
            event_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            response="APPROVE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card_authorization = await response.parse()
            assert card_authorization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_challenge_response(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_token` but received ''"):
            await async_client.card_authorizations.with_raw_response.challenge_response(
                event_token="",
                response="APPROVE",
            )
