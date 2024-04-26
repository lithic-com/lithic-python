# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    ResponderEndpointStatus,
    ResponderEndpointCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResponderEndpoints:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        responder_endpoint = client.responder_endpoints.create()
        assert_matches_type(ResponderEndpointCreateResponse, responder_endpoint, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        responder_endpoint = client.responder_endpoints.create(
            type="AUTH_STREAM_ACCESS",
            url="https://example.com",
        )
        assert_matches_type(ResponderEndpointCreateResponse, responder_endpoint, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.responder_endpoints.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        responder_endpoint = response.parse()
        assert_matches_type(ResponderEndpointCreateResponse, responder_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.responder_endpoints.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            responder_endpoint = response.parse()
            assert_matches_type(ResponderEndpointCreateResponse, responder_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism errors when accept header set but no request body is defined")
    @parametrize
    def test_method_delete(self, client: Lithic) -> None:
        responder_endpoint = client.responder_endpoints.delete(
            type="AUTH_STREAM_ACCESS",
        )
        assert responder_endpoint is None

    @pytest.mark.skip(reason="Prism errors when accept header set but no request body is defined")
    @parametrize
    def test_raw_response_delete(self, client: Lithic) -> None:
        response = client.responder_endpoints.with_raw_response.delete(
            type="AUTH_STREAM_ACCESS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        responder_endpoint = response.parse()
        assert responder_endpoint is None

    @pytest.mark.skip(reason="Prism errors when accept header set but no request body is defined")
    @parametrize
    def test_streaming_response_delete(self, client: Lithic) -> None:
        with client.responder_endpoints.with_streaming_response.delete(
            type="AUTH_STREAM_ACCESS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            responder_endpoint = response.parse()
            assert responder_endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_check_status(self, client: Lithic) -> None:
        responder_endpoint = client.responder_endpoints.check_status(
            type="AUTH_STREAM_ACCESS",
        )
        assert_matches_type(ResponderEndpointStatus, responder_endpoint, path=["response"])

    @parametrize
    def test_raw_response_check_status(self, client: Lithic) -> None:
        response = client.responder_endpoints.with_raw_response.check_status(
            type="AUTH_STREAM_ACCESS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        responder_endpoint = response.parse()
        assert_matches_type(ResponderEndpointStatus, responder_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_check_status(self, client: Lithic) -> None:
        with client.responder_endpoints.with_streaming_response.check_status(
            type="AUTH_STREAM_ACCESS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            responder_endpoint = response.parse()
            assert_matches_type(ResponderEndpointStatus, responder_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncResponderEndpoints:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        responder_endpoint = await async_client.responder_endpoints.create()
        assert_matches_type(ResponderEndpointCreateResponse, responder_endpoint, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        responder_endpoint = await async_client.responder_endpoints.create(
            type="AUTH_STREAM_ACCESS",
            url="https://example.com",
        )
        assert_matches_type(ResponderEndpointCreateResponse, responder_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.responder_endpoints.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        responder_endpoint = response.parse()
        assert_matches_type(ResponderEndpointCreateResponse, responder_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.responder_endpoints.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            responder_endpoint = await response.parse()
            assert_matches_type(ResponderEndpointCreateResponse, responder_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism errors when accept header set but no request body is defined")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLithic) -> None:
        responder_endpoint = await async_client.responder_endpoints.delete(
            type="AUTH_STREAM_ACCESS",
        )
        assert responder_endpoint is None

    @pytest.mark.skip(reason="Prism errors when accept header set but no request body is defined")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLithic) -> None:
        response = await async_client.responder_endpoints.with_raw_response.delete(
            type="AUTH_STREAM_ACCESS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        responder_endpoint = response.parse()
        assert responder_endpoint is None

    @pytest.mark.skip(reason="Prism errors when accept header set but no request body is defined")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLithic) -> None:
        async with async_client.responder_endpoints.with_streaming_response.delete(
            type="AUTH_STREAM_ACCESS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            responder_endpoint = await response.parse()
            assert responder_endpoint is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_check_status(self, async_client: AsyncLithic) -> None:
        responder_endpoint = await async_client.responder_endpoints.check_status(
            type="AUTH_STREAM_ACCESS",
        )
        assert_matches_type(ResponderEndpointStatus, responder_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_check_status(self, async_client: AsyncLithic) -> None:
        response = await async_client.responder_endpoints.with_raw_response.check_status(
            type="AUTH_STREAM_ACCESS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        responder_endpoint = response.parse()
        assert_matches_type(ResponderEndpointStatus, responder_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_check_status(self, async_client: AsyncLithic) -> None:
        async with async_client.responder_endpoints.with_streaming_response.check_status(
            type="AUTH_STREAM_ACCESS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            responder_endpoint = await response.parse()
            assert_matches_type(ResponderEndpointStatus, responder_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True
