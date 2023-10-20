# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import ResponderEndpointStatus, ResponderEndpointCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestResponderEndpoints:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

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

    @pytest.mark.skip(reason="Prism errors when accept header set but no request body is defined")
    @parametrize
    def test_method_delete(self, client: Lithic) -> None:
        responder_endpoint = client.responder_endpoints.delete(
            type="AUTH_STREAM_ACCESS",
        )
        assert responder_endpoint is None

    @parametrize
    def test_method_check_status(self, client: Lithic) -> None:
        responder_endpoint = client.responder_endpoints.check_status(
            type="AUTH_STREAM_ACCESS",
        )
        assert_matches_type(ResponderEndpointStatus, responder_endpoint, path=["response"])


class TestAsyncResponderEndpoints:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncLithic) -> None:
        responder_endpoint = await client.responder_endpoints.create()
        assert_matches_type(ResponderEndpointCreateResponse, responder_endpoint, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncLithic) -> None:
        responder_endpoint = await client.responder_endpoints.create(
            type="AUTH_STREAM_ACCESS",
            url="https://example.com",
        )
        assert_matches_type(ResponderEndpointCreateResponse, responder_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism errors when accept header set but no request body is defined")
    @parametrize
    async def test_method_delete(self, client: AsyncLithic) -> None:
        responder_endpoint = await client.responder_endpoints.delete(
            type="AUTH_STREAM_ACCESS",
        )
        assert responder_endpoint is None

    @parametrize
    async def test_method_check_status(self, client: AsyncLithic) -> None:
        responder_endpoint = await client.responder_endpoints.check_status(
            type="AUTH_STREAM_ACCESS",
        )
        assert_matches_type(ResponderEndpointStatus, responder_endpoint, path=["response"])
