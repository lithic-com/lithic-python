# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic._client import Lithic, AsyncLithic
from lithic.types.external_bank_accounts import MicroDepositCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestMicroDeposits:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        micro_deposit = client.external_bank_accounts.micro_deposits.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            micro_deposits=[0, 0, 0],
        )
        assert_matches_type(MicroDepositCreateResponse, micro_deposit, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.external_bank_accounts.micro_deposits.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            micro_deposits=[0, 0, 0],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        micro_deposit = response.parse()
        assert_matches_type(MicroDepositCreateResponse, micro_deposit, path=["response"])


class TestAsyncMicroDeposits:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncLithic) -> None:
        micro_deposit = await client.external_bank_accounts.micro_deposits.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            micro_deposits=[0, 0, 0],
        )
        assert_matches_type(MicroDepositCreateResponse, micro_deposit, path=["response"])

    @parametrize
    async def test_raw_response_create(self, client: AsyncLithic) -> None:
        response = await client.external_bank_accounts.micro_deposits.with_raw_response.create(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            micro_deposits=[0, 0, 0],
        )
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        micro_deposit = response.parse()
        assert_matches_type(MicroDepositCreateResponse, micro_deposit, path=["response"])
