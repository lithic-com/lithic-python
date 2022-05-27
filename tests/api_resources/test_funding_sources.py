# File generated from our OpenAPI spec by Stainless.
import os

import pytest

from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage
from lithic.types.funding_source import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestFundingSources:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_create(self) -> None:
        resource = self.client.funding_sources.create(
            {"validation_method": "BANK", "account_number": "13719713158835300", "routing_number": "011103093"}
        )
        assert isinstance(resource, FundingSource)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.funding_sources.create(
            {
                "validation_method": "BANK",
                "account_name": "Sandbox",
                "account_number": "13719713158835300",
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "routing_number": "011103093",
            }
        )
        assert isinstance(resource, FundingSource)

    def test_method_update(self) -> None:
        resource = self.client.funding_sources.update("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", {})
        assert isinstance(resource, FundingSource)

    def test_method_update_with_optional_params(self) -> None:
        resource = self.client.funding_sources.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {"account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "state": "DELETED"},
        )
        assert isinstance(resource, FundingSource)

    def test_method_list(self) -> None:
        resource = self.client.funding_sources.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.funding_sources.list({"account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"})
        assert isinstance(resource, SyncPage)

    def test_method_verify(self) -> None:
        resource = self.client.funding_sources.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", {"micro_deposits": [0, 0, 0]}
        )
        assert isinstance(resource, FundingSource)

    def test_method_verify_with_optional_params(self) -> None:
        resource = self.client.funding_sources.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {"account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "micro_deposits": [0, 0, 0]},
        )
        assert isinstance(resource, FundingSource)


class TestAsyncFundingSources:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.funding_sources.create(
            {"validation_method": "BANK", "account_number": "13719713158835300", "routing_number": "011103093"}
        )
        assert isinstance(resource, FundingSource)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.funding_sources.create(
            {
                "validation_method": "BANK",
                "account_name": "Sandbox",
                "account_number": "13719713158835300",
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "routing_number": "011103093",
            }
        )
        assert isinstance(resource, FundingSource)

    async def test_method_update(self) -> None:
        resource = await self.client.funding_sources.update("182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", {})
        assert isinstance(resource, FundingSource)

    async def test_method_update_with_optional_params(self) -> None:
        resource = await self.client.funding_sources.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {"account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "state": "DELETED"},
        )
        assert isinstance(resource, FundingSource)

    async def test_method_list(self) -> None:
        resource = await self.client.funding_sources.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.funding_sources.list({"account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"})
        assert isinstance(resource, AsyncPage)

    async def test_method_verify(self) -> None:
        resource = await self.client.funding_sources.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", {"micro_deposits": [0, 0, 0]}
        )
        assert isinstance(resource, FundingSource)

    async def test_method_verify_with_optional_params(self) -> None:
        resource = await self.client.funding_sources.verify(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {"account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e", "micro_deposits": [0, 0, 0]},
        )
        assert isinstance(resource, FundingSource)
