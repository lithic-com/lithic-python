# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types.financial_accounts import FinancialAccountCreditConfig

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCreditConfiguration:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        credit_configuration = client.financial_accounts.credit_configuration.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.financial_accounts.credit_configuration.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_configuration = response.parse()
        assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.financial_accounts.credit_configuration.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_configuration = response.parse()
            assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.financial_accounts.credit_configuration.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        credit_configuration = client.financial_accounts.credit_configuration.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        credit_configuration = client.financial_accounts.credit_configuration.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_limit=0,
            credit_product_token="credit_product_token",
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tier="x",
        )
        assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.financial_accounts.credit_configuration.with_raw_response.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_configuration = response.parse()
        assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.financial_accounts.credit_configuration.with_streaming_response.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_configuration = response.parse()
            assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.financial_accounts.credit_configuration.with_raw_response.update(
                financial_account_token="",
            )


class TestAsyncCreditConfiguration:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        credit_configuration = await async_client.financial_accounts.credit_configuration.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.credit_configuration.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_configuration = response.parse()
        assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.credit_configuration.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_configuration = await response.parse()
            assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.financial_accounts.credit_configuration.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLithic) -> None:
        credit_configuration = await async_client.financial_accounts.credit_configuration.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLithic) -> None:
        credit_configuration = await async_client.financial_accounts.credit_configuration.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_limit=0,
            credit_product_token="credit_product_token",
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tier="x",
        )
        assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.credit_configuration.with_raw_response.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credit_configuration = response.parse()
        assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.credit_configuration.with_streaming_response.update(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credit_configuration = await response.parse()
            assert_matches_type(FinancialAccountCreditConfig, credit_configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.financial_accounts.credit_configuration.with_raw_response.update(
                financial_account_token="",
            )
