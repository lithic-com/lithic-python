# File generated from our OpenAPI spec by Stainless.
import os
import pytest
from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage

from lithic.types.account import *


base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccounts:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_retrieve(self) -> None:
        resource = self.client.accounts.retrieve(
            "bb463b8b-b76c-4f6a-9726-65ab5730b69b",
        )
        assert isinstance(resource, Account)

    def test_method_update(self) -> None:
        resource = self.client.accounts.update("a27218b8-6a4d-47bb-95b6-5a55334fac1c", {})
        assert isinstance(resource, Account)

    def test_method_update_with_optional_params(self) -> None:
        resource = self.client.accounts.update(
            "a27218b8-6a4d-47bb-95b6-5a55334fac1c",
            {
                "daily_spend_limit": 9,
                "lifetime_spend_limit": 0,
                "monthly_spend_limit": 9,
                "verification_address": {
                    "address1": "mel",
                    "address2": "i",
                    "city": "ltxsynnmqodhimkrwx",
                    "state": "cmmzg",
                    "postal_code": "lptdmvupho",
                    "country": "iahikrrww",
                },
                "state": "ACTIVE",
            },
        )
        assert isinstance(resource, Account)

    def test_method_list(self) -> None:
        resource = self.client.accounts.list()
        assert isinstance(resource, SyncPage[Account])

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.accounts.list(
            {"begin": "2019-12-27T18:11:19.117Z", "end": "2019-12-27T18:11:19.117Z", "page": 10, "page_size": 457}
        )
        assert isinstance(resource, SyncPage[Account])


class TestAsyncAccounts:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.accounts.retrieve(
            "a49d94a8-d215-4ce3-a379-318e2aebf079",
        )
        assert isinstance(resource, Account)

    async def test_method_update(self) -> None:
        resource = await self.client.accounts.update("488242cb-158b-4e83-a5ed-db56034668b8", {})
        assert isinstance(resource, Account)

    async def test_method_update_with_optional_params(self) -> None:
        resource = await self.client.accounts.update(
            "488242cb-158b-4e83-a5ed-db56034668b8",
            {
                "daily_spend_limit": 20,
                "lifetime_spend_limit": 0,
                "monthly_spend_limit": 7,
                "verification_address": {
                    "address1": "tbpbrwdhktgji",
                    "address2": "narocgdxilrfwhovwo",
                    "city": "rivjwekv",
                    "state": "i",
                    "postal_code": "onppniaxzr",
                    "country": "jfohlnhxhzogsonujkq",
                },
                "state": "PAUSED",
            },
        )
        assert isinstance(resource, Account)

    async def test_method_list(self) -> None:
        resource = await self.client.accounts.list()
        assert isinstance(resource, AsyncPage[Account])

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.accounts.list(
            {"begin": "2019-12-27T18:11:19.117Z", "end": "2019-12-27T18:11:19.117Z", "page": 18, "page_size": 162}
        )
        assert isinstance(resource, AsyncPage[Account])
