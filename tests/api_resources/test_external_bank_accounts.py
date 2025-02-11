# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    ExternalBankAccountListResponse,
    ExternalBankAccountCreateResponse,
    ExternalBankAccountUpdateResponse,
    ExternalBankAccountRetrieveResponse,
    ExternalBankAccountRetryPrenoteResponse,
    ExternalBankAccountRetryMicroDepositsResponse,
)
from lithic._utils import parse_date
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalBankAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="MANUAL",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="MANUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "x",
                "city": "x",
                "country": "USD",
                "postal_code": "11201",
                "state": "xx",
                "address2": "x",
            },
            company_id="sq",
            dob=parse_date("2019-12-27"),
            doing_business_as="x",
            name="name",
            user_defined_id="x",
            verification_enforcement=True,
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: Lithic) -> None:
        response = client.external_bank_accounts.with_raw_response.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="MANUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: Lithic) -> None:
        with client.external_bank_accounts.with_streaming_response.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="MANUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = response.parse()
            assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.create(
            owner="owner",
            owner_type="INDIVIDUAL",
            processor_token="x",
            verification_method="MANUAL",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.create(
            owner="owner",
            owner_type="INDIVIDUAL",
            processor_token="x",
            verification_method="MANUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="sq",
            dob=parse_date("2019-12-27"),
            doing_business_as="x",
            user_defined_id="x",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_raw_response_create_overload_2(self, client: Lithic) -> None:
        response = client.external_bank_accounts.with_raw_response.create(
            owner="owner",
            owner_type="INDIVIDUAL",
            processor_token="x",
            verification_method="MANUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_2(self, client: Lithic) -> None:
        with client.external_bank_accounts.with_streaming_response.create(
            owner="owner",
            owner_type="INDIVIDUAL",
            processor_token="x",
            verification_method="MANUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = response.parse()
            assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_3(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="EXTERNALLY_VERIFIED",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="EXTERNALLY_VERIFIED",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "x",
                "city": "x",
                "country": "USD",
                "postal_code": "11201",
                "state": "xx",
                "address2": "x",
            },
            company_id="sq",
            dob=parse_date("2019-12-27"),
            doing_business_as="x",
            name="name",
            user_defined_id="x",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_raw_response_create_overload_3(self, client: Lithic) -> None:
        response = client.external_bank_accounts.with_raw_response.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="EXTERNALLY_VERIFIED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_3(self, client: Lithic) -> None:
        with client.external_bank_accounts.with_streaming_response.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="EXTERNALLY_VERIFIED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = response.parse()
            assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountRetrieveResponse, external_bank_account, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.external_bank_accounts.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountRetrieveResponse, external_bank_account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.external_bank_accounts.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = response.parse()
            assert_matches_type(ExternalBankAccountRetrieveResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_bank_account_token` but received ''"
        ):
            client.external_bank_accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.update(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountUpdateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.update(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "x",
                "city": "x",
                "country": "USD",
                "postal_code": "11201",
                "state": "xx",
                "address2": "x",
            },
            company_id="sq",
            dob=parse_date("2019-12-27"),
            doing_business_as="x",
            name="name",
            owner="owner",
            owner_type="INDIVIDUAL",
            type="CHECKING",
            user_defined_id="x",
        )
        assert_matches_type(ExternalBankAccountUpdateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.external_bank_accounts.with_raw_response.update(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountUpdateResponse, external_bank_account, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.external_bank_accounts.with_streaming_response.update(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = response.parse()
            assert_matches_type(ExternalBankAccountUpdateResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_bank_account_token` but received ''"
        ):
            client.external_bank_accounts.with_raw_response.update(
                external_bank_account_token="",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.list()
        assert_matches_type(SyncCursorPage[ExternalBankAccountListResponse], external_bank_account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_types=["CHECKING"],
            countries=["string"],
            ending_before="ending_before",
            owner_types=["INDIVIDUAL"],
            page_size=1,
            starting_after="starting_after",
            states=["ENABLED"],
            verification_states=["PENDING"],
        )
        assert_matches_type(SyncCursorPage[ExternalBankAccountListResponse], external_bank_account, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.external_bank_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(SyncCursorPage[ExternalBankAccountListResponse], external_bank_account, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.external_bank_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = response.parse()
            assert_matches_type(
                SyncCursorPage[ExternalBankAccountListResponse], external_bank_account, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retry_micro_deposits(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.retry_micro_deposits(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountRetryMicroDepositsResponse, external_bank_account, path=["response"])

    @parametrize
    def test_method_retry_micro_deposits_with_all_params(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.retry_micro_deposits(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountRetryMicroDepositsResponse, external_bank_account, path=["response"])

    @parametrize
    def test_raw_response_retry_micro_deposits(self, client: Lithic) -> None:
        response = client.external_bank_accounts.with_raw_response.retry_micro_deposits(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountRetryMicroDepositsResponse, external_bank_account, path=["response"])

    @parametrize
    def test_streaming_response_retry_micro_deposits(self, client: Lithic) -> None:
        with client.external_bank_accounts.with_streaming_response.retry_micro_deposits(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = response.parse()
            assert_matches_type(ExternalBankAccountRetryMicroDepositsResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retry_micro_deposits(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_bank_account_token` but received ''"
        ):
            client.external_bank_accounts.with_raw_response.retry_micro_deposits(
                external_bank_account_token="",
            )

    @parametrize
    def test_method_retry_prenote(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.retry_prenote(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountRetryPrenoteResponse, external_bank_account, path=["response"])

    @parametrize
    def test_method_retry_prenote_with_all_params(self, client: Lithic) -> None:
        external_bank_account = client.external_bank_accounts.retry_prenote(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountRetryPrenoteResponse, external_bank_account, path=["response"])

    @parametrize
    def test_raw_response_retry_prenote(self, client: Lithic) -> None:
        response = client.external_bank_accounts.with_raw_response.retry_prenote(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountRetryPrenoteResponse, external_bank_account, path=["response"])

    @parametrize
    def test_streaming_response_retry_prenote(self, client: Lithic) -> None:
        with client.external_bank_accounts.with_streaming_response.retry_prenote(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = response.parse()
            assert_matches_type(ExternalBankAccountRetryPrenoteResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retry_prenote(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_bank_account_token` but received ''"
        ):
            client.external_bank_accounts.with_raw_response.retry_prenote(
                external_bank_account_token="",
            )


class TestAsyncExternalBankAccounts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="MANUAL",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="MANUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "x",
                "city": "x",
                "country": "USD",
                "postal_code": "11201",
                "state": "xx",
                "address2": "x",
            },
            company_id="sq",
            dob=parse_date("2019-12-27"),
            doing_business_as="x",
            name="name",
            user_defined_id="x",
            verification_enforcement=True,
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_bank_accounts.with_raw_response.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="MANUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncLithic) -> None:
        async with async_client.external_bank_accounts.with_streaming_response.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="MANUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = await response.parse()
            assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.create(
            owner="owner",
            owner_type="INDIVIDUAL",
            processor_token="x",
            verification_method="MANUAL",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.create(
            owner="owner",
            owner_type="INDIVIDUAL",
            processor_token="x",
            verification_method="MANUAL",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            company_id="sq",
            dob=parse_date("2019-12-27"),
            doing_business_as="x",
            user_defined_id="x",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_bank_accounts.with_raw_response.create(
            owner="owner",
            owner_type="INDIVIDUAL",
            processor_token="x",
            verification_method="MANUAL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncLithic) -> None:
        async with async_client.external_bank_accounts.with_streaming_response.create(
            owner="owner",
            owner_type="INDIVIDUAL",
            processor_token="x",
            verification_method="MANUAL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = await response.parse()
            assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="EXTERNALLY_VERIFIED",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="EXTERNALLY_VERIFIED",
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "x",
                "city": "x",
                "country": "USD",
                "postal_code": "11201",
                "state": "xx",
                "address2": "x",
            },
            company_id="sq",
            dob=parse_date("2019-12-27"),
            doing_business_as="x",
            name="name",
            user_defined_id="x",
        )
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_bank_accounts.with_raw_response.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="EXTERNALLY_VERIFIED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncLithic) -> None:
        async with async_client.external_bank_accounts.with_streaming_response.create(
            account_number="12345678901234567",
            country="USD",
            currency="USD",
            owner="owner",
            owner_type="INDIVIDUAL",
            routing_number="123456789",
            type="CHECKING",
            verification_method="EXTERNALLY_VERIFIED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = await response.parse()
            assert_matches_type(ExternalBankAccountCreateResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountRetrieveResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_bank_accounts.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountRetrieveResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.external_bank_accounts.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = await response.parse()
            assert_matches_type(ExternalBankAccountRetrieveResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_bank_account_token` but received ''"
        ):
            await async_client.external_bank_accounts.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.update(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountUpdateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.update(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            address={
                "address1": "x",
                "city": "x",
                "country": "USD",
                "postal_code": "11201",
                "state": "xx",
                "address2": "x",
            },
            company_id="sq",
            dob=parse_date("2019-12-27"),
            doing_business_as="x",
            name="name",
            owner="owner",
            owner_type="INDIVIDUAL",
            type="CHECKING",
            user_defined_id="x",
        )
        assert_matches_type(ExternalBankAccountUpdateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_bank_accounts.with_raw_response.update(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountUpdateResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLithic) -> None:
        async with async_client.external_bank_accounts.with_streaming_response.update(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = await response.parse()
            assert_matches_type(ExternalBankAccountUpdateResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_bank_account_token` but received ''"
        ):
            await async_client.external_bank_accounts.with_raw_response.update(
                external_bank_account_token="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.list()
        assert_matches_type(AsyncCursorPage[ExternalBankAccountListResponse], external_bank_account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_types=["CHECKING"],
            countries=["string"],
            ending_before="ending_before",
            owner_types=["INDIVIDUAL"],
            page_size=1,
            starting_after="starting_after",
            states=["ENABLED"],
            verification_states=["PENDING"],
        )
        assert_matches_type(AsyncCursorPage[ExternalBankAccountListResponse], external_bank_account, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_bank_accounts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(AsyncCursorPage[ExternalBankAccountListResponse], external_bank_account, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.external_bank_accounts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = await response.parse()
            assert_matches_type(
                AsyncCursorPage[ExternalBankAccountListResponse], external_bank_account, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retry_micro_deposits(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.retry_micro_deposits(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountRetryMicroDepositsResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_method_retry_micro_deposits_with_all_params(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.retry_micro_deposits(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountRetryMicroDepositsResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_raw_response_retry_micro_deposits(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_bank_accounts.with_raw_response.retry_micro_deposits(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountRetryMicroDepositsResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_streaming_response_retry_micro_deposits(self, async_client: AsyncLithic) -> None:
        async with async_client.external_bank_accounts.with_streaming_response.retry_micro_deposits(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = await response.parse()
            assert_matches_type(ExternalBankAccountRetryMicroDepositsResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retry_micro_deposits(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_bank_account_token` but received ''"
        ):
            await async_client.external_bank_accounts.with_raw_response.retry_micro_deposits(
                external_bank_account_token="",
            )

    @parametrize
    async def test_method_retry_prenote(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.retry_prenote(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountRetryPrenoteResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_method_retry_prenote_with_all_params(self, async_client: AsyncLithic) -> None:
        external_bank_account = await async_client.external_bank_accounts.retry_prenote(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalBankAccountRetryPrenoteResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_raw_response_retry_prenote(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_bank_accounts.with_raw_response.retry_prenote(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_bank_account = response.parse()
        assert_matches_type(ExternalBankAccountRetryPrenoteResponse, external_bank_account, path=["response"])

    @parametrize
    async def test_streaming_response_retry_prenote(self, async_client: AsyncLithic) -> None:
        async with async_client.external_bank_accounts.with_streaming_response.retry_prenote(
            external_bank_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_bank_account = await response.parse()
            assert_matches_type(ExternalBankAccountRetryPrenoteResponse, external_bank_account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retry_prenote(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_bank_account_token` but received ''"
        ):
            await async_client.external_bank_accounts.with_raw_response.retry_prenote(
                external_bank_account_token="",
            )
