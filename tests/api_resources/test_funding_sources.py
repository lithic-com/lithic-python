# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage
from lithic.types.funding_source import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestFundingSources:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        resource = client.funding_sources.create(
            {
                "validation_method": "BANK",
                "account_number": "13719713158835300",
                "routing_number": "011103093",
            },
        )
        assert isinstance(resource, FundingSource)

    @parametrize
    def test_method_create_with_optional_params(self, client: Lithic) -> None:
        resource = client.funding_sources.create(
            {
                "validation_method": "BANK",
                "account_name": "Sandbox",
                "account_number": "13719713158835300",
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "routing_number": "011103093",
            },
        )
        assert isinstance(resource, FundingSource)

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        resource = client.funding_sources.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, FundingSource)

    @parametrize
    def test_method_update_with_optional_params(self, client: Lithic) -> None:
        resource = client.funding_sources.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "state": "DELETED",
            },
        )
        assert isinstance(resource, FundingSource)

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        resource = client.funding_sources.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_optional_params(self, client: Lithic) -> None:
        resource = client.funding_sources.list(
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "page": 0,
                "page_size": 0,
            },
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_verify(self, client: Lithic) -> None:
        resource = client.funding_sources.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {"micro_deposits": [0, 0, 0]},
        )
        assert isinstance(resource, FundingSource)

    @parametrize
    def test_method_verify_with_optional_params(self, client: Lithic) -> None:
        resource = client.funding_sources.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "micro_deposits": [0, 0, 0],
            },
        )
        assert isinstance(resource, FundingSource)


class TestAsyncFundingSources:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncLithic) -> None:
        resource = await client.funding_sources.create(
            {
                "validation_method": "BANK",
                "account_number": "13719713158835300",
                "routing_number": "011103093",
            },
        )
        assert isinstance(resource, FundingSource)

    @parametrize
    async def test_method_create_with_optional_params(self, client: AsyncLithic) -> None:
        resource = await client.funding_sources.create(
            {
                "validation_method": "BANK",
                "account_name": "Sandbox",
                "account_number": "13719713158835300",
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "routing_number": "011103093",
            },
        )
        assert isinstance(resource, FundingSource)

    @parametrize
    async def test_method_update(self, client: AsyncLithic) -> None:
        resource = await client.funding_sources.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, FundingSource)

    @parametrize
    async def test_method_update_with_optional_params(self, client: AsyncLithic) -> None:
        resource = await client.funding_sources.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "state": "DELETED",
            },
        )
        assert isinstance(resource, FundingSource)

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        resource = await client.funding_sources.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_optional_params(self, client: AsyncLithic) -> None:
        resource = await client.funding_sources.list(
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "page": 0,
                "page_size": 0,
            },
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_verify(self, client: AsyncLithic) -> None:
        resource = await client.funding_sources.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {"micro_deposits": [0, 0, 0]},
        )
        assert isinstance(resource, FundingSource)

    @parametrize
    async def test_method_verify_with_optional_params(self, client: AsyncLithic) -> None:
        resource = await client.funding_sources.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "micro_deposits": [0, 0, 0],
            },
        )
        assert isinstance(resource, FundingSource)
