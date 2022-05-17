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
                "validation_method": "PLAID",
                "account_token": "6c060042-dfd3-4ad4-978e-712450f29275",
                "processor_token": "sghoosrcoha",
            }
        )
        assert isinstance(resource, FundingSource)

    def test_method_update(self) -> None:
        resource = self.client.funding_sources.update("36b1e36a-a903-4246-aa6a-23d22f253751", {})
        assert isinstance(resource, FundingSource)

    def test_method_update_with_optional_params(self) -> None:
        resource = self.client.funding_sources.update(
            "36b1e36a-a903-4246-aa6a-23d22f253751",
            {"account_token": "deea88c6-b003-4bdd-9a32-3f5c968c88db", "state": "ENABLED"},
        )
        assert isinstance(resource, FundingSource)

    def test_method_list(self) -> None:
        resource = self.client.funding_sources.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.funding_sources.list({"account_token": "bdcb0604-ffb0-4d92-954f-f0eb3246ee17"})
        assert isinstance(resource, SyncPage)

    def test_method_verify(self) -> None:
        resource = self.client.funding_sources.verify(
            "3c912590-9e9b-442d-bf14-9de4f57cd2c0", {"micro_deposits": [0, 8, 3]}
        )
        assert isinstance(resource, FundingSource)

    def test_method_verify_with_optional_params(self) -> None:
        resource = self.client.funding_sources.verify(
            "3c912590-9e9b-442d-bf14-9de4f57cd2c0",
            {"account_token": "23119425-46be-418f-a478-8c43954346db", "micro_deposits": [8, 15, 10]},
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
                "validation_method": "PLAID",
                "account_token": "79b9bca4-3cd8-44e5-a81d-6aeb73e5028b",
                "processor_token": "yftldz",
            }
        )
        assert isinstance(resource, FundingSource)

    async def test_method_update(self) -> None:
        resource = await self.client.funding_sources.update("b46d13fb-b490-4de5-8af7-b138aab7d2c1", {})
        assert isinstance(resource, FundingSource)

    async def test_method_update_with_optional_params(self) -> None:
        resource = await self.client.funding_sources.update(
            "b46d13fb-b490-4de5-8af7-b138aab7d2c1",
            {"account_token": "aa3d0e36-4f7d-4664-aa53-1d0d3d41bc2c", "state": "ENABLED"},
        )
        assert isinstance(resource, FundingSource)

    async def test_method_list(self) -> None:
        resource = await self.client.funding_sources.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.funding_sources.list({"account_token": "8ba7d10b-6e45-46c0-ba0f-04aed2e22894"})
        assert isinstance(resource, AsyncPage)

    async def test_method_verify(self) -> None:
        resource = await self.client.funding_sources.verify(
            "4836be62-76dc-4328-8db2-89ed7c3e40cb", {"micro_deposits": [17, 4, 15]}
        )
        assert isinstance(resource, FundingSource)

    async def test_method_verify_with_optional_params(self) -> None:
        resource = await self.client.funding_sources.verify(
            "4836be62-76dc-4328-8db2-89ed7c3e40cb",
            {"account_token": "82c76cb1-d7fe-4825-b62d-d32e103f81ee", "micro_deposits": [2, 11, 20]},
        )
        assert isinstance(resource, FundingSource)
