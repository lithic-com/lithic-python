# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import BlockchainRecipient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlockchainRecipients:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        blockchain_recipient = client.blockchain_recipients.create(
            account_token="dabadb3b-700c-41e3-8801-d5dfc84ebea0",
            address="0x45bfcf1a6289a0b77b4d3f7d12005a05949fd8c3",
            chain="ETHEREUM",
            owner="John Doe",
            owner_type="INDIVIDUAL",
        )
        assert_matches_type(BlockchainRecipient, blockchain_recipient, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        blockchain_recipient = client.blockchain_recipients.create(
            account_token="dabadb3b-700c-41e3-8801-d5dfc84ebea0",
            address="0x45bfcf1a6289a0b77b4d3f7d12005a05949fd8c3",
            chain="ETHEREUM",
            owner="John Doe",
            owner_type="INDIVIDUAL",
            address_tag="address_tag",
            name="Cold wallet",
        )
        assert_matches_type(BlockchainRecipient, blockchain_recipient, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.blockchain_recipients.with_raw_response.create(
            account_token="dabadb3b-700c-41e3-8801-d5dfc84ebea0",
            address="0x45bfcf1a6289a0b77b4d3f7d12005a05949fd8c3",
            chain="ETHEREUM",
            owner="John Doe",
            owner_type="INDIVIDUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_recipient = response.parse()
        assert_matches_type(BlockchainRecipient, blockchain_recipient, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.blockchain_recipients.with_streaming_response.create(
            account_token="dabadb3b-700c-41e3-8801-d5dfc84ebea0",
            address="0x45bfcf1a6289a0b77b4d3f7d12005a05949fd8c3",
            chain="ETHEREUM",
            owner="John Doe",
            owner_type="INDIVIDUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_recipient = response.parse()
            assert_matches_type(BlockchainRecipient, blockchain_recipient, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBlockchainRecipients:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        blockchain_recipient = await async_client.blockchain_recipients.create(
            account_token="dabadb3b-700c-41e3-8801-d5dfc84ebea0",
            address="0x45bfcf1a6289a0b77b4d3f7d12005a05949fd8c3",
            chain="ETHEREUM",
            owner="John Doe",
            owner_type="INDIVIDUAL",
        )
        assert_matches_type(BlockchainRecipient, blockchain_recipient, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        blockchain_recipient = await async_client.blockchain_recipients.create(
            account_token="dabadb3b-700c-41e3-8801-d5dfc84ebea0",
            address="0x45bfcf1a6289a0b77b4d3f7d12005a05949fd8c3",
            chain="ETHEREUM",
            owner="John Doe",
            owner_type="INDIVIDUAL",
            address_tag="address_tag",
            name="Cold wallet",
        )
        assert_matches_type(BlockchainRecipient, blockchain_recipient, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.blockchain_recipients.with_raw_response.create(
            account_token="dabadb3b-700c-41e3-8801-d5dfc84ebea0",
            address="0x45bfcf1a6289a0b77b4d3f7d12005a05949fd8c3",
            chain="ETHEREUM",
            owner="John Doe",
            owner_type="INDIVIDUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        blockchain_recipient = response.parse()
        assert_matches_type(BlockchainRecipient, blockchain_recipient, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.blockchain_recipients.with_streaming_response.create(
            account_token="dabadb3b-700c-41e3-8801-d5dfc84ebea0",
            address="0x45bfcf1a6289a0b77b4d3f7d12005a05949fd8c3",
            chain="ETHEREUM",
            owner="John Doe",
            owner_type="INDIVIDUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            blockchain_recipient = await response.parse()
            assert_matches_type(BlockchainRecipient, blockchain_recipient, path=["response"])

        assert cast(Any, response.is_closed) is True
