# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic._utils import parse_datetime
from lithic.types.auth_rules.v2 import BacktestResults, BacktestCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBacktests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        backtest = client.auth_rules.v2.backtests.create(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BacktestCreateResponse, backtest, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        backtest = client.auth_rules.v2.backtests.create(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BacktestCreateResponse, backtest, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.auth_rules.v2.backtests.with_raw_response.create(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backtest = response.parse()
        assert_matches_type(BacktestCreateResponse, backtest, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.auth_rules.v2.backtests.with_streaming_response.create(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backtest = response.parse()
            assert_matches_type(BacktestCreateResponse, backtest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.v2.backtests.with_raw_response.create(
                auth_rule_token="",
            )

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        backtest = client.auth_rules.v2.backtests.retrieve(
            auth_rule_backtest_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BacktestResults, backtest, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.auth_rules.v2.backtests.with_raw_response.retrieve(
            auth_rule_backtest_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backtest = response.parse()
        assert_matches_type(BacktestResults, backtest, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.auth_rules.v2.backtests.with_streaming_response.retrieve(
            auth_rule_backtest_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backtest = response.parse()
            assert_matches_type(BacktestResults, backtest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            client.auth_rules.v2.backtests.with_raw_response.retrieve(
                auth_rule_backtest_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                auth_rule_token="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `auth_rule_backtest_token` but received ''"
        ):
            client.auth_rules.v2.backtests.with_raw_response.retrieve(
                auth_rule_backtest_token="",
                auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncBacktests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        backtest = await async_client.auth_rules.v2.backtests.create(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BacktestCreateResponse, backtest, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        backtest = await async_client.auth_rules.v2.backtests.create(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            start=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(BacktestCreateResponse, backtest, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.backtests.with_raw_response.create(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backtest = response.parse()
        assert_matches_type(BacktestCreateResponse, backtest, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.backtests.with_streaming_response.create(
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backtest = await response.parse()
            assert_matches_type(BacktestCreateResponse, backtest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.v2.backtests.with_raw_response.create(
                auth_rule_token="",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        backtest = await async_client.auth_rules.v2.backtests.retrieve(
            auth_rule_backtest_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BacktestResults, backtest, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.auth_rules.v2.backtests.with_raw_response.retrieve(
            auth_rule_backtest_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        backtest = response.parse()
        assert_matches_type(BacktestResults, backtest, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.auth_rules.v2.backtests.with_streaming_response.retrieve(
            auth_rule_backtest_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            backtest = await response.parse()
            assert_matches_type(BacktestResults, backtest, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `auth_rule_token` but received ''"):
            await async_client.auth_rules.v2.backtests.with_raw_response.retrieve(
                auth_rule_backtest_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                auth_rule_token="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `auth_rule_backtest_token` but received ''"
        ):
            await async_client.auth_rules.v2.backtests.with_raw_response.retrieve(
                auth_rule_backtest_token="",
                auth_rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
