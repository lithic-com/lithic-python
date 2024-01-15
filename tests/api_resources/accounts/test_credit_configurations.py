# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import BusinessAccount
from lithic._client import Lithic, AsyncLithic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestCreditConfigurations:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        credit_configuration = client.accounts.credit_configurations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.accounts.credit_configurations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_configuration = response.parse()
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.accounts.credit_configurations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_configuration = response.parse()
            assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        credit_configuration = client.accounts.credit_configurations.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        credit_configuration = client.accounts.credit_configurations.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            billing_period=0,
            credit_limit=0,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_period=0,
        )
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.accounts.credit_configurations.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_configuration = response.parse()
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.accounts.credit_configurations.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_configuration = response.parse()
            assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCreditConfigurations:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        credit_configuration = await client.accounts.credit_configurations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncLithic) -> None:
        response = await client.accounts.credit_configurations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_configuration = response.parse()
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, client: AsyncLithic) -> None:
        async with client.accounts.credit_configurations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_configuration = await response.parse()
            assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, client: AsyncLithic) -> None:
        credit_configuration = await client.accounts.credit_configurations.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncLithic) -> None:
        credit_configuration = await client.accounts.credit_configurations.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            billing_period=0,
            credit_limit=0,
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_period=0,
        )
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, client: AsyncLithic) -> None:
        response = await client.accounts.credit_configurations.with_raw_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_configuration = response.parse()
        assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, client: AsyncLithic) -> None:
        async with client.accounts.credit_configurations.with_streaming_response.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_configuration = await response.parse()
            assert_matches_type(BusinessAccount, credit_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True
