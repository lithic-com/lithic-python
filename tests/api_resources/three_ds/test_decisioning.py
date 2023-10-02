# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types.three_ds import DecisioningRetrieveSecretResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestDecisioning:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve_secret(self, client: Lithic) -> None:
        decisioning = client.three_ds.decisioning.retrieve_secret()
        assert_matches_type(DecisioningRetrieveSecretResponse, decisioning, path=["response"])

    @parametrize
    def test_method_rotate_secret(self, client: Lithic) -> None:
        decisioning = client.three_ds.decisioning.rotate_secret()
        assert decisioning is None


class TestAsyncDecisioning:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve_secret(self, client: AsyncLithic) -> None:
        decisioning = await client.three_ds.decisioning.retrieve_secret()
        assert_matches_type(DecisioningRetrieveSecretResponse, decisioning, path=["response"])

    @parametrize
    async def test_method_rotate_secret(self, client: AsyncLithic) -> None:
        decisioning = await client.three_ds.decisioning.rotate_secret()
        assert decisioning is None
