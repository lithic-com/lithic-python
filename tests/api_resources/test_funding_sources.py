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
            {"validation_method": "kuakbahevyv", "account_number": "13719713158835300", "routing_number": "011103093"}
        )
        assert isinstance(resource, FundingSource)

    def test_method_create_with_optional_params(self) -> None:
        resource = self.client.funding_sources.create(
            {
                "validation_method": "whjmnymcdgjbz",
                "account_name": "Sandbox",
                "account_number": "13719713158835300",
                "account_token": "292758b4-499b-4a19-8036-b1e36aa90324",
                "routing_number": "011103093",
            }
        )
        assert isinstance(resource, FundingSource)

    def test_method_update(self) -> None:
        resource = self.client.funding_sources.update("62a6a23d-22f2-4537-91de-ea88c6b003bd", {})
        assert isinstance(resource, FundingSource)

    def test_method_update_with_optional_params(self) -> None:
        resource = self.client.funding_sources.update(
            "62a6a23d-22f2-4537-91de-ea88c6b003bd",
            {"account_token": "d9a323f5-c968-4c88-9bdb-dcb0604ffb0d", "state": "ENABLED"},
        )
        assert isinstance(resource, FundingSource)

    def test_method_list(self) -> None:
        resource = self.client.funding_sources.list()
        assert isinstance(resource, SyncPage[FundingSource])

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.funding_sources.list({"account_token": "2d54ff0e-b324-46ee-973c-9125909e9b42"})
        assert isinstance(resource, SyncPage[FundingSource])

    def test_method_verify(self) -> None:
        resource = self.client.funding_sources.verify(
            "d7f149de-4f57-4cd2-8006-22311942546b", {"micro_deposits": [19, 1, 10]}
        )
        assert isinstance(resource, FundingSource)

    def test_method_verify_with_optional_params(self) -> None:
        resource = self.client.funding_sources.verify(
            "d7f149de-4f57-4cd2-8006-22311942546b",
            {"account_token": "f24788c4-3954-4346-9b6b-82979b9bca43", "micro_deposits": [16, 18, 11]},
        )
        assert isinstance(resource, FundingSource)


class TestAsyncFundingSources:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_create(self) -> None:
        resource = await self.client.funding_sources.create(
            {
                "validation_method": "jyobwkqwslfxjadoth",
                "account_number": "13719713158835300",
                "routing_number": "011103093",
            }
        )
        assert isinstance(resource, FundingSource)

    async def test_method_create_with_optional_params(self) -> None:
        resource = await self.client.funding_sources.create(
            {
                "validation_method": "tldz",
                "account_token": "b46d13fb-b490-4de5-8af7-b138aab7d2c1",
                "processor_token": "rfvbygkiymvllh",
            }
        )
        assert isinstance(resource, FundingSource)

    async def test_method_update(self) -> None:
        resource = await self.client.funding_sources.update("6a531d0d-3d41-4bc2-8b8b-a7d10b6e456c", {})
        assert isinstance(resource, FundingSource)

    async def test_method_update_with_optional_params(self) -> None:
        resource = await self.client.funding_sources.update(
            "6a531d0d-3d41-4bc2-8b8b-a7d10b6e456c",
            {"account_token": "0ba0f04a-ed2e-4228-9448-36be6276dc32", "state": "ENABLED"},
        )
        assert isinstance(resource, FundingSource)

    async def test_method_list(self) -> None:
        resource = await self.client.funding_sources.list()
        assert isinstance(resource, AsyncPage[FundingSource])

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.funding_sources.list({"account_token": "8db289ed-7c3e-440c-bd3b-82c76cb1d7fe"})
        assert isinstance(resource, AsyncPage[FundingSource])

    async def test_method_verify(self) -> None:
        resource = await self.client.funding_sources.verify(
            "825762dd-32e1-403f-81ee-18f8ff1fecfa", {"micro_deposits": [20, 14, 8]}
        )
        assert isinstance(resource, FundingSource)

    async def test_method_verify_with_optional_params(self) -> None:
        resource = await self.client.funding_sources.verify(
            "825762dd-32e1-403f-81ee-18f8ff1fecfa",
            {"account_token": "29716a13-0204-4b67-9794-1842629d707e", "micro_deposits": [9, 7, 17]},
        )
        assert isinstance(resource, FundingSource)
