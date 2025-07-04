# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    FinancialAccount,
)
from lithic.pagination import SyncSinglePage, AsyncSinglePage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFinancialAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        financial_account = client.financial_accounts.create(
            nickname="nickname",
            type="OPERATING",
        )
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        financial_account = client.financial_accounts.create(
            nickname="nickname",
            type="OPERATING",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_for_benefit_of=True,
        )
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.financial_accounts.with_raw_response.create(
            nickname="nickname",
            type="OPERATING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.financial_accounts.with_streaming_response.create(
            nickname="nickname",
            type="OPERATING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = response.parse()
            assert_matches_type(FinancialAccount, financial_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        financial_account = client.financial_accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.financial_accounts.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.financial_accounts.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = response.parse()
            assert_matches_type(FinancialAccount, financial_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.financial_accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        financial_account = client.financial_accounts.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        financial_account = client.financial_accounts.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            nickname="nickname",
        )
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.financial_accounts.with_raw_response.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.financial_accounts.with_streaming_response.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = response.parse()
            assert_matches_type(FinancialAccount, financial_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.financial_accounts.with_raw_response.update(
                financial_account_token="",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        financial_account = client.financial_accounts.list()
        assert_matches_type(SyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        financial_account = client.financial_accounts.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            business_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ISSUING",
        )
        assert_matches_type(SyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.financial_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(SyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.financial_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = response.parse()
            assert_matches_type(SyncSinglePage[FinancialAccount], financial_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register_account_number(self, client: Lithic) -> None:
        financial_account = client.financial_accounts.register_account_number(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_number="account_number",
        )
        assert financial_account is None

    @parametrize
    def test_raw_response_register_account_number(self, client: Lithic) -> None:
        response = client.financial_accounts.with_raw_response.register_account_number(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_number="account_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert financial_account is None

    @parametrize
    def test_streaming_response_register_account_number(self, client: Lithic) -> None:
        with client.financial_accounts.with_streaming_response.register_account_number(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_number="account_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = response.parse()
            assert financial_account is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_register_account_number(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.financial_accounts.with_raw_response.register_account_number(
                financial_account_token="",
                account_number="account_number",
            )

    @parametrize
    def test_method_update_status(self, client: Lithic) -> None:
        financial_account = client.financial_accounts.update_status(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="OPEN",
            substatus="CHARGED_OFF_FRAUD",
        )
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    def test_raw_response_update_status(self, client: Lithic) -> None:
        response = client.financial_accounts.with_raw_response.update_status(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="OPEN",
            substatus="CHARGED_OFF_FRAUD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    def test_streaming_response_update_status(self, client: Lithic) -> None:
        with client.financial_accounts.with_streaming_response.update_status(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="OPEN",
            substatus="CHARGED_OFF_FRAUD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = response.parse()
            assert_matches_type(FinancialAccount, financial_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_status(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.financial_accounts.with_raw_response.update_status(
                financial_account_token="",
                status="OPEN",
                substatus="CHARGED_OFF_FRAUD",
            )


class TestAsyncFinancialAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        financial_account = await async_client.financial_accounts.create(
            nickname="nickname",
            type="OPERATING",
        )
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        financial_account = await async_client.financial_accounts.create(
            nickname="nickname",
            type="OPERATING",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            is_for_benefit_of=True,
        )
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.with_raw_response.create(
            nickname="nickname",
            type="OPERATING",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.with_streaming_response.create(
            nickname="nickname",
            type="OPERATING",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = await response.parse()
            assert_matches_type(FinancialAccount, financial_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        financial_account = await async_client.financial_accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = await response.parse()
            assert_matches_type(FinancialAccount, financial_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.financial_accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLithic) -> None:
        financial_account = await async_client.financial_accounts.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLithic) -> None:
        financial_account = await async_client.financial_accounts.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            nickname="nickname",
        )
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.with_raw_response.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.with_streaming_response.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = await response.parse()
            assert_matches_type(FinancialAccount, financial_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.financial_accounts.with_raw_response.update(
                financial_account_token="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        financial_account = await async_client.financial_accounts.list()
        assert_matches_type(AsyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        financial_account = await async_client.financial_accounts.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            business_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            type="ISSUING",
        )
        assert_matches_type(AsyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(AsyncSinglePage[FinancialAccount], financial_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = await response.parse()
            assert_matches_type(AsyncSinglePage[FinancialAccount], financial_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register_account_number(self, async_client: AsyncLithic) -> None:
        financial_account = await async_client.financial_accounts.register_account_number(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_number="account_number",
        )
        assert financial_account is None

    @parametrize
    async def test_raw_response_register_account_number(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.with_raw_response.register_account_number(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_number="account_number",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert financial_account is None

    @parametrize
    async def test_streaming_response_register_account_number(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.with_streaming_response.register_account_number(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_number="account_number",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = await response.parse()
            assert financial_account is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_register_account_number(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.financial_accounts.with_raw_response.register_account_number(
                financial_account_token="",
                account_number="account_number",
            )

    @parametrize
    async def test_method_update_status(self, async_client: AsyncLithic) -> None:
        financial_account = await async_client.financial_accounts.update_status(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="OPEN",
            substatus="CHARGED_OFF_FRAUD",
        )
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    async def test_raw_response_update_status(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.with_raw_response.update_status(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="OPEN",
            substatus="CHARGED_OFF_FRAUD",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        financial_account = response.parse()
        assert_matches_type(FinancialAccount, financial_account, path=["response"])

    @parametrize
    async def test_streaming_response_update_status(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.with_streaming_response.update_status(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="OPEN",
            substatus="CHARGED_OFF_FRAUD",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            financial_account = await response.parse()
            assert_matches_type(FinancialAccount, financial_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_status(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.financial_accounts.with_raw_response.update_status(
                financial_account_token="",
                status="OPEN",
                substatus="CHARGED_OFF_FRAUD",
            )
