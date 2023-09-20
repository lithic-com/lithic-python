# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types.three_ds import (
    AuthenticationRetrieveResponse,
    AuthenticationSimulateResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


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
    def test_method_simulate(self, client: Lithic) -> None:
        authentication = client.three_ds.authentication.simulate(
            merchant={
                "country": "USA",
                "mcc": "5812",
                "id": "OODKZAPJVN4YS7O",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 0,
                "currency": "GBP",
            },
        )
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
    async def test_method_simulate(self, client: AsyncLithic) -> None:
        authentication = await client.three_ds.authentication.simulate(
            merchant={
                "country": "USA",
                "mcc": "5812",
                "id": "OODKZAPJVN4YS7O",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 0,
                "currency": "GBP",
            },
        )
        assert_matches_type(AuthenticationSimulateResponse, authentication, path=["response"])
