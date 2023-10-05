# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import Account
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccounts:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        account = client.accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        account = client.accounts.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        account = client.accounts.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            daily_spend_limit=1000,
            lifetime_spend_limit=0,
            monthly_spend_limit=0,
            state="ACTIVE",
            verification_address={
                "address1": "string",
                "address2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        account = client.accounts.list()
        assert_matches_type(SyncCursorPage[Account], account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        account = client.accounts.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(SyncCursorPage[Account], account, path=["response"])


class TestAsyncAccounts:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        account = await client.accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    async def test_method_update(self, client: AsyncLithic) -> None:
        account = await client.accounts.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncLithic) -> None:
        account = await client.accounts.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            daily_spend_limit=1000,
            lifetime_spend_limit=0,
            monthly_spend_limit=0,
            state="ACTIVE",
            verification_address={
                "address1": "string",
                "address2": "string",
                "city": "string",
                "state": "string",
                "postal_code": "string",
                "country": "string",
            },
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        account = await client.accounts.list()
        assert_matches_type(AsyncCursorPage[Account], account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        account = await client.accounts.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            page_size=1,
            starting_after="string",
        )
        assert_matches_type(AsyncCursorPage[Account], account, path=["response"])
