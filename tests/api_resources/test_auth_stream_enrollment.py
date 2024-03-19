# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import AuthStreamSecret

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthStreamEnrollment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_secret(self, client: Lithic) -> None:
        auth_stream_enrollment = client.auth_stream_enrollment.retrieve_secret()
        assert_matches_type(AuthStreamSecret, auth_stream_enrollment, path=["response"])

    @parametrize
    def test_raw_response_retrieve_secret(self, client: Lithic) -> None:
        response = client.auth_stream_enrollment.with_raw_response.retrieve_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert_matches_type(AuthStreamSecret, auth_stream_enrollment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_secret(self, client: Lithic) -> None:
        with client.auth_stream_enrollment.with_streaming_response.retrieve_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_stream_enrollment = response.parse()
            assert_matches_type(AuthStreamSecret, auth_stream_enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_rotate_secret(self, client: Lithic) -> None:
        auth_stream_enrollment = client.auth_stream_enrollment.rotate_secret()
        assert auth_stream_enrollment is None

    @parametrize
    def test_raw_response_rotate_secret(self, client: Lithic) -> None:
        response = client.auth_stream_enrollment.with_raw_response.rotate_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert auth_stream_enrollment is None

    @parametrize
    def test_streaming_response_rotate_secret(self, client: Lithic) -> None:
        with client.auth_stream_enrollment.with_streaming_response.rotate_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_stream_enrollment = response.parse()
            assert auth_stream_enrollment is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAuthStreamEnrollment:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve_secret(self, async_client: AsyncLithic) -> None:
        auth_stream_enrollment = await async_client.auth_stream_enrollment.retrieve_secret()
        assert_matches_type(AuthStreamSecret, auth_stream_enrollment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_secret(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_stream_enrollment.with_raw_response.retrieve_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert_matches_type(AuthStreamSecret, auth_stream_enrollment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_secret(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_stream_enrollment.with_streaming_response.retrieve_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_stream_enrollment = await response.parse()
            assert_matches_type(AuthStreamSecret, auth_stream_enrollment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_rotate_secret(self, async_client: AsyncLithic) -> None:
        auth_stream_enrollment = await async_client.auth_stream_enrollment.rotate_secret()
        assert auth_stream_enrollment is None

    @parametrize
    async def test_raw_response_rotate_secret(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_stream_enrollment.with_raw_response.rotate_secret()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert auth_stream_enrollment is None

    @parametrize
    async def test_streaming_response_rotate_secret(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_stream_enrollment.with_streaming_response.rotate_secret() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth_stream_enrollment = await response.parse()
            assert auth_stream_enrollment is None

        assert cast(Any, response.is_closed) is True
