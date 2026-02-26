# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types.account_holders import AccountHolderEntity, EntityCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntities:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        entity = client.account_holders.entities.create(
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "300 Normal Forest Way",
                "city": "Portland",
                "country": "USA",
                "postal_code": "90210",
                "state": "OR",
            },
            dob="1991-03-08T08:00:00Z",
            email="tim@left-earth.com",
            first_name="Timmy",
            government_id="211-23-1412",
            last_name="Turner",
            phone_number="+15555555555",
            type="BENEFICIAL_OWNER_INDIVIDUAL",
        )
        assert_matches_type(EntityCreateResponse, entity, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        entity = client.account_holders.entities.create(
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "300 Normal Forest Way",
                "city": "Portland",
                "country": "USA",
                "postal_code": "90210",
                "state": "OR",
                "address2": "address2",
            },
            dob="1991-03-08T08:00:00Z",
            email="tim@left-earth.com",
            first_name="Timmy",
            government_id="211-23-1412",
            last_name="Turner",
            phone_number="+15555555555",
            type="BENEFICIAL_OWNER_INDIVIDUAL",
        )
        assert_matches_type(EntityCreateResponse, entity, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.account_holders.entities.with_raw_response.create(
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "300 Normal Forest Way",
                "city": "Portland",
                "country": "USA",
                "postal_code": "90210",
                "state": "OR",
            },
            dob="1991-03-08T08:00:00Z",
            email="tim@left-earth.com",
            first_name="Timmy",
            government_id="211-23-1412",
            last_name="Turner",
            phone_number="+15555555555",
            type="BENEFICIAL_OWNER_INDIVIDUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityCreateResponse, entity, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.account_holders.entities.with_streaming_response.create(
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "300 Normal Forest Way",
                "city": "Portland",
                "country": "USA",
                "postal_code": "90210",
                "state": "OR",
            },
            dob="1991-03-08T08:00:00Z",
            email="tim@left-earth.com",
            first_name="Timmy",
            government_id="211-23-1412",
            last_name="Turner",
            phone_number="+15555555555",
            type="BENEFICIAL_OWNER_INDIVIDUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(EntityCreateResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            client.account_holders.entities.with_raw_response.create(
                account_holder_token="",
                address={
                    "address1": "300 Normal Forest Way",
                    "city": "Portland",
                    "country": "USA",
                    "postal_code": "90210",
                    "state": "OR",
                },
                dob="1991-03-08T08:00:00Z",
                email="tim@left-earth.com",
                first_name="Timmy",
                government_id="211-23-1412",
                last_name="Turner",
                phone_number="+15555555555",
                type="BENEFICIAL_OWNER_INDIVIDUAL",
            )

    @parametrize
    def test_method_delete(self, client: Lithic) -> None:
        entity = client.account_holders.entities.delete(
            entity_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolderEntity, entity, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Lithic) -> None:
        response = client.account_holders.entities.with_raw_response.delete(
            entity_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(AccountHolderEntity, entity, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Lithic) -> None:
        with client.account_holders.entities.with_streaming_response.delete(
            entity_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = response.parse()
            assert_matches_type(AccountHolderEntity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            client.account_holders.entities.with_raw_response.delete(
                entity_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_holder_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_token` but received ''"):
            client.account_holders.entities.with_raw_response.delete(
                entity_token="",
                account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncEntities:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        entity = await async_client.account_holders.entities.create(
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "300 Normal Forest Way",
                "city": "Portland",
                "country": "USA",
                "postal_code": "90210",
                "state": "OR",
            },
            dob="1991-03-08T08:00:00Z",
            email="tim@left-earth.com",
            first_name="Timmy",
            government_id="211-23-1412",
            last_name="Turner",
            phone_number="+15555555555",
            type="BENEFICIAL_OWNER_INDIVIDUAL",
        )
        assert_matches_type(EntityCreateResponse, entity, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        entity = await async_client.account_holders.entities.create(
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "300 Normal Forest Way",
                "city": "Portland",
                "country": "USA",
                "postal_code": "90210",
                "state": "OR",
                "address2": "address2",
            },
            dob="1991-03-08T08:00:00Z",
            email="tim@left-earth.com",
            first_name="Timmy",
            government_id="211-23-1412",
            last_name="Turner",
            phone_number="+15555555555",
            type="BENEFICIAL_OWNER_INDIVIDUAL",
        )
        assert_matches_type(EntityCreateResponse, entity, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_holders.entities.with_raw_response.create(
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "300 Normal Forest Way",
                "city": "Portland",
                "country": "USA",
                "postal_code": "90210",
                "state": "OR",
            },
            dob="1991-03-08T08:00:00Z",
            email="tim@left-earth.com",
            first_name="Timmy",
            government_id="211-23-1412",
            last_name="Turner",
            phone_number="+15555555555",
            type="BENEFICIAL_OWNER_INDIVIDUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(EntityCreateResponse, entity, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.account_holders.entities.with_streaming_response.create(
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "300 Normal Forest Way",
                "city": "Portland",
                "country": "USA",
                "postal_code": "90210",
                "state": "OR",
            },
            dob="1991-03-08T08:00:00Z",
            email="tim@left-earth.com",
            first_name="Timmy",
            government_id="211-23-1412",
            last_name="Turner",
            phone_number="+15555555555",
            type="BENEFICIAL_OWNER_INDIVIDUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(EntityCreateResponse, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            await async_client.account_holders.entities.with_raw_response.create(
                account_holder_token="",
                address={
                    "address1": "300 Normal Forest Way",
                    "city": "Portland",
                    "country": "USA",
                    "postal_code": "90210",
                    "state": "OR",
                },
                dob="1991-03-08T08:00:00Z",
                email="tim@left-earth.com",
                first_name="Timmy",
                government_id="211-23-1412",
                last_name="Turner",
                phone_number="+15555555555",
                type="BENEFICIAL_OWNER_INDIVIDUAL",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncLithic) -> None:
        entity = await async_client.account_holders.entities.delete(
            entity_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AccountHolderEntity, entity, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLithic) -> None:
        response = await async_client.account_holders.entities.with_raw_response.delete(
            entity_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entity = response.parse()
        assert_matches_type(AccountHolderEntity, entity, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLithic) -> None:
        async with async_client.account_holders.entities.with_streaming_response.delete(
            entity_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entity = await response.parse()
            assert_matches_type(AccountHolderEntity, entity, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_holder_token` but received ''"):
            await async_client.account_holders.entities.with_raw_response.delete(
                entity_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_holder_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_token` but received ''"):
            await async_client.account_holders.entities.with_raw_response.delete(
                entity_token="",
                account_holder_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
