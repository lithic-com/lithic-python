# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import Account, AccountSpendLimits
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        account = client.accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.accounts.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.accounts.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_token` but received ''"):
            client.accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        account = client.accounts.update(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        account = client.accounts.update(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            daily_spend_limit=1000,
            lifetime_spend_limit=0,
            monthly_spend_limit=0,
            state="ACTIVE",
            verification_address={
                "address1": "address1",
                "address2": "address2",
                "city": "city",
                "country": "country",
                "postal_code": "postal_code",
                "state": "state",
            },
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.accounts.with_raw_response.update(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.accounts.with_streaming_response.update(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    def test_path_params_update(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_token` but received ''"):
            client.accounts.with_raw_response.update(
                account_token="",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        account = client.accounts.list()
        assert_matches_type(SyncCursorPage[Account], account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        account = client.accounts.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(SyncCursorPage[Account], account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(SyncCursorPage[Account], account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(SyncCursorPage[Account], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_spend_limits(self, client: Lithic) -> None:
        account = client.accounts.retrieve_spend_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountSpendLimits, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve_spend_limits(self, client: Lithic) -> None:
        response = client.accounts.with_raw_response.retrieve_spend_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountSpendLimits, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_spend_limits(self, client: Lithic) -> None:
        with client.accounts.with_streaming_response.retrieve_spend_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountSpendLimits, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_spend_limits(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_token` but received ''"):
            client.accounts.with_raw_response.retrieve_spend_limits(
                "",
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        account = await async_client.accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.accounts.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.accounts.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_token` but received ''"):
            await async_client.accounts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    async def test_method_update(self, async_client: AsyncLithic) -> None:
        account = await async_client.accounts.update(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLithic) -> None:
        account = await async_client.accounts.update(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            daily_spend_limit=1000,
            lifetime_spend_limit=0,
            monthly_spend_limit=0,
            state="ACTIVE",
            verification_address={
                "address1": "address1",
                "address2": "address2",
                "city": "city",
                "country": "country",
                "postal_code": "postal_code",
                "state": "state",
            },
        )
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLithic) -> None:
        response = await async_client.accounts.with_raw_response.update(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(Account, account, path=["response"])

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLithic) -> None:
        async with async_client.accounts.with_streaming_response.update(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(Account, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism returns invalid data")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_token` but received ''"):
            await async_client.accounts.with_raw_response.update(
                account_token="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        account = await async_client.accounts.list()
        assert_matches_type(AsyncCursorPage[Account], account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        account = await async_client.accounts.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(AsyncCursorPage[Account], account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AsyncCursorPage[Account], account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AsyncCursorPage[Account], account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_spend_limits(self, async_client: AsyncLithic) -> None:
        account = await async_client.accounts.retrieve_spend_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountSpendLimits, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_spend_limits(self, async_client: AsyncLithic) -> None:
        response = await async_client.accounts.with_raw_response.retrieve_spend_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountSpendLimits, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_spend_limits(self, async_client: AsyncLithic) -> None:
        async with async_client.accounts.with_streaming_response.retrieve_spend_limits(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountSpendLimits, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_spend_limits(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_token` but received ''"):
            await async_client.accounts.with_raw_response.retrieve_spend_limits(
                "",
            )
