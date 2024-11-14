# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic._utils import parse_date
from lithic.types.credit_products import PrimeRateRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrimeRates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        prime_rate = client.credit_products.prime_rates.create(
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
            rate="rate",
        )
        assert prime_rate is None

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.credit_products.prime_rates.with_raw_response.create(
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
            rate="rate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prime_rate = response.parse()
        assert prime_rate is None

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.credit_products.prime_rates.with_streaming_response.create(
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
            rate="rate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prime_rate = response.parse()
            assert prime_rate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_product_token` but received ''"):
            client.credit_products.prime_rates.with_raw_response.create(
                credit_product_token="",
                effective_date=parse_date("2019-12-27"),
                rate="rate",
            )

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        prime_rate = client.credit_products.prime_rates.retrieve(
            credit_product_token="credit_product_token",
        )
        assert_matches_type(PrimeRateRetrieveResponse, prime_rate, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Lithic) -> None:
        prime_rate = client.credit_products.prime_rates.retrieve(
            credit_product_token="credit_product_token",
            ending_before=parse_date("2019-12-27"),
            starting_after=parse_date("2019-12-27"),
        )
        assert_matches_type(PrimeRateRetrieveResponse, prime_rate, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.credit_products.prime_rates.with_raw_response.retrieve(
            credit_product_token="credit_product_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prime_rate = response.parse()
        assert_matches_type(PrimeRateRetrieveResponse, prime_rate, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.credit_products.prime_rates.with_streaming_response.retrieve(
            credit_product_token="credit_product_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prime_rate = response.parse()
            assert_matches_type(PrimeRateRetrieveResponse, prime_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_product_token` but received ''"):
            client.credit_products.prime_rates.with_raw_response.retrieve(
                credit_product_token="",
            )


class TestAsyncPrimeRates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        prime_rate = await async_client.credit_products.prime_rates.create(
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
            rate="rate",
        )
        assert prime_rate is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.credit_products.prime_rates.with_raw_response.create(
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
            rate="rate",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prime_rate = response.parse()
        assert prime_rate is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.credit_products.prime_rates.with_streaming_response.create(
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
            rate="rate",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prime_rate = await response.parse()
            assert prime_rate is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_product_token` but received ''"):
            await async_client.credit_products.prime_rates.with_raw_response.create(
                credit_product_token="",
                effective_date=parse_date("2019-12-27"),
                rate="rate",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        prime_rate = await async_client.credit_products.prime_rates.retrieve(
            credit_product_token="credit_product_token",
        )
        assert_matches_type(PrimeRateRetrieveResponse, prime_rate, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLithic) -> None:
        prime_rate = await async_client.credit_products.prime_rates.retrieve(
            credit_product_token="credit_product_token",
            ending_before=parse_date("2019-12-27"),
            starting_after=parse_date("2019-12-27"),
        )
        assert_matches_type(PrimeRateRetrieveResponse, prime_rate, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.credit_products.prime_rates.with_raw_response.retrieve(
            credit_product_token="credit_product_token",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prime_rate = response.parse()
        assert_matches_type(PrimeRateRetrieveResponse, prime_rate, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.credit_products.prime_rates.with_streaming_response.retrieve(
            credit_product_token="credit_product_token",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prime_rate = await response.parse()
            assert_matches_type(PrimeRateRetrieveResponse, prime_rate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `credit_product_token` but received ''"):
            await async_client.credit_products.prime_rates.with_raw_response.retrieve(
                credit_product_token="",
            )
