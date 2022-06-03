# File generated from our OpenAPI spec by Stainless.
import os

from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage
from lithic.types.account import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccounts:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_retrieve(self) -> None:
        resource = self.client.accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, Account)

    def test_method_update(self) -> None:
        resource = self.client.accounts.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, Account)

    def test_method_update_with_optional_params(self) -> None:
        resource = self.client.accounts.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "daily_spend_limit": 0,
                "lifetime_spend_limit": 0,
                "monthly_spend_limit": 0,
                "verification_address": {
                    "address1": "string",
                    "address2": "string",
                    "city": "string",
                    "state": "string",
                    "postal_code": "string",
                    "country": "string",
                },
                "state": "ACTIVE",
            },
        )
        assert isinstance(resource, Account)

    def test_method_list(self) -> None:
        resource = self.client.accounts.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.accounts.list(
            {
                "begin": "2019-12-27T18:11:19.117Z",
                "end": "2019-12-27T18:11:19.117Z",
                "page": 0,
                "page_size": 1,
            },
        )
        assert isinstance(resource, SyncPage)


class TestAsyncAccounts:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, Account)

    async def test_method_update(self) -> None:
        resource = await self.client.accounts.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {},
        )
        assert isinstance(resource, Account)

    async def test_method_update_with_optional_params(self) -> None:
        resource = await self.client.accounts.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            {
                "daily_spend_limit": 0,
                "lifetime_spend_limit": 0,
                "monthly_spend_limit": 0,
                "verification_address": {
                    "address1": "string",
                    "address2": "string",
                    "city": "string",
                    "state": "string",
                    "postal_code": "string",
                    "country": "string",
                },
                "state": "ACTIVE",
            },
        )
        assert isinstance(resource, Account)

    async def test_method_list(self) -> None:
        resource = await self.client.accounts.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.accounts.list(
            {
                "begin": "2019-12-27T18:11:19.117Z",
                "end": "2019-12-27T18:11:19.117Z",
                "page": 0,
                "page_size": 1,
            },
        )
        assert isinstance(resource, AsyncPage)
