# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic._client import Lithic, AsyncLithic
from lithic.types.three_ds import (
    AuthenticationRetrieveResponse,
    AuthenticationSimulateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestAuthentication:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        authentication = client.three_ds.authentication.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthenticationRetrieveResponse, authentication, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.three_ds.authentication.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationRetrieveResponse, authentication, path=["response"])

    @parametrize
    def test_method_simulate(self, client: Lithic) -> None:
        authentication = client.three_ds.authentication.simulate(
            merchant={
                "country": "USA",
                "id": "OODKZAPJVN4YS7O",
                "mcc": "5812",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 100,
                "currency": "USD",
            },
        )
        assert_matches_type(AuthenticationSimulateResponse, authentication, path=["response"])

    @parametrize
    def test_raw_response_simulate(self, client: Lithic) -> None:
        response = client.three_ds.authentication.with_raw_response.simulate(
            merchant={
                "country": "USA",
                "id": "OODKZAPJVN4YS7O",
                "mcc": "5812",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 100,
                "currency": "USD",
            },
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationSimulateResponse, authentication, path=["response"])


class TestAsyncAuthentication:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        authentication = await client.three_ds.authentication.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthenticationRetrieveResponse, authentication, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncLithic) -> None:
        response = await client.three_ds.authentication.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationRetrieveResponse, authentication, path=["response"])

    @parametrize
    async def test_method_simulate(self, client: AsyncLithic) -> None:
        authentication = await client.three_ds.authentication.simulate(
            merchant={
                "country": "USA",
                "id": "OODKZAPJVN4YS7O",
                "mcc": "5812",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 100,
                "currency": "USD",
            },
        )
        assert_matches_type(AuthenticationSimulateResponse, authentication, path=["response"])

    @parametrize
    async def test_raw_response_simulate(self, client: AsyncLithic) -> None:
        response = await client.three_ds.authentication.with_raw_response.simulate(
            merchant={
                "country": "USA",
                "id": "OODKZAPJVN4YS7O",
                "mcc": "5812",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 100,
                "currency": "USD",
            },
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationSimulateResponse, authentication, path=["response"])
