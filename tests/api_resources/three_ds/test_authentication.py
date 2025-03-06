# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types.three_ds import (
    AuthenticationRetrieveResponse,
    AuthenticationSimulateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthentication:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        authentication = client.three_ds.authentication.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthenticationRetrieveResponse, authentication, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.three_ds.authentication.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationRetrieveResponse, authentication, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.three_ds.authentication.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert_matches_type(AuthenticationRetrieveResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `three_ds_authentication_token` but received ''"
        ):
            client.three_ds.authentication.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_simulate(self, client: Lithic) -> None:
        authentication = client.three_ds.authentication.simulate(
            merchant={
                "id": "OODKZAPJVN4YS7O",
                "country": "USA",
                "mcc": "5812",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 100,
                "currency": "USD",
            },
        )
        assert_matches_type(AuthenticationSimulateResponse, authentication, path=["response"])

    @parametrize
    def test_method_simulate_with_all_params(self, client: Lithic) -> None:
        authentication = client.three_ds.authentication.simulate(
            merchant={
                "id": "OODKZAPJVN4YS7O",
                "country": "USA",
                "mcc": "5812",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 100,
                "currency": "USD",
            },
            card_expiry_check="MATCH",
        )
        assert_matches_type(AuthenticationSimulateResponse, authentication, path=["response"])

    @parametrize
    def test_raw_response_simulate(self, client: Lithic) -> None:
        response = client.three_ds.authentication.with_raw_response.simulate(
            merchant={
                "id": "OODKZAPJVN4YS7O",
                "country": "USA",
                "mcc": "5812",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 100,
                "currency": "USD",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationSimulateResponse, authentication, path=["response"])

    @parametrize
    def test_streaming_response_simulate(self, client: Lithic) -> None:
        with client.three_ds.authentication.with_streaming_response.simulate(
            merchant={
                "id": "OODKZAPJVN4YS7O",
                "country": "USA",
                "mcc": "5812",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 100,
                "currency": "USD",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert_matches_type(AuthenticationSimulateResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_simulate_otp_entry(self, client: Lithic) -> None:
        authentication = client.three_ds.authentication.simulate_otp_entry(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
            otp="123456",
        )
        assert authentication is None

    @parametrize
    def test_raw_response_simulate_otp_entry(self, client: Lithic) -> None:
        response = client.three_ds.authentication.with_raw_response.simulate_otp_entry(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
            otp="123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert authentication is None

    @parametrize
    def test_streaming_response_simulate_otp_entry(self, client: Lithic) -> None:
        with client.three_ds.authentication.with_streaming_response.simulate_otp_entry(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
            otp="123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert authentication is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAuthentication:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        authentication = await async_client.three_ds.authentication.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AuthenticationRetrieveResponse, authentication, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.three_ds.authentication.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationRetrieveResponse, authentication, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.three_ds.authentication.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert_matches_type(AuthenticationRetrieveResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `three_ds_authentication_token` but received ''"
        ):
            await async_client.three_ds.authentication.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_simulate(self, async_client: AsyncLithic) -> None:
        authentication = await async_client.three_ds.authentication.simulate(
            merchant={
                "id": "OODKZAPJVN4YS7O",
                "country": "USA",
                "mcc": "5812",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 100,
                "currency": "USD",
            },
        )
        assert_matches_type(AuthenticationSimulateResponse, authentication, path=["response"])

    @parametrize
    async def test_method_simulate_with_all_params(self, async_client: AsyncLithic) -> None:
        authentication = await async_client.three_ds.authentication.simulate(
            merchant={
                "id": "OODKZAPJVN4YS7O",
                "country": "USA",
                "mcc": "5812",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 100,
                "currency": "USD",
            },
            card_expiry_check="MATCH",
        )
        assert_matches_type(AuthenticationSimulateResponse, authentication, path=["response"])

    @parametrize
    async def test_raw_response_simulate(self, async_client: AsyncLithic) -> None:
        response = await async_client.three_ds.authentication.with_raw_response.simulate(
            merchant={
                "id": "OODKZAPJVN4YS7O",
                "country": "USA",
                "mcc": "5812",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 100,
                "currency": "USD",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationSimulateResponse, authentication, path=["response"])

    @parametrize
    async def test_streaming_response_simulate(self, async_client: AsyncLithic) -> None:
        async with async_client.three_ds.authentication.with_streaming_response.simulate(
            merchant={
                "id": "OODKZAPJVN4YS7O",
                "country": "USA",
                "mcc": "5812",
                "name": "COFFEE SHOP",
            },
            pan="4111111289144142",
            transaction={
                "amount": 100,
                "currency": "USD",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert_matches_type(AuthenticationSimulateResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_simulate_otp_entry(self, async_client: AsyncLithic) -> None:
        authentication = await async_client.three_ds.authentication.simulate_otp_entry(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
            otp="123456",
        )
        assert authentication is None

    @parametrize
    async def test_raw_response_simulate_otp_entry(self, async_client: AsyncLithic) -> None:
        response = await async_client.three_ds.authentication.with_raw_response.simulate_otp_entry(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
            otp="123456",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert authentication is None

    @parametrize
    async def test_streaming_response_simulate_otp_entry(self, async_client: AsyncLithic) -> None:
        async with async_client.three_ds.authentication.with_streaming_response.simulate_otp_entry(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
            otp="123456",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert authentication is None

        assert cast(Any, response.is_closed) is True
