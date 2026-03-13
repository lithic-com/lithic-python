# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic._utils import parse_date
from lithic.pagination import SyncSinglePage, AsyncSinglePage
from lithic.types.financial_accounts import (
    InterestTierSchedule,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInterestTierSchedule:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        interest_tier_schedule = client.financial_accounts.interest_tier_schedule.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        interest_tier_schedule = client.financial_accounts.interest_tier_schedule.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
            tier_name="tier_name",
            tier_rates={},
        )
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.financial_accounts.interest_tier_schedule.with_raw_response.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interest_tier_schedule = response.parse()
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.financial_accounts.interest_tier_schedule.with_streaming_response.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interest_tier_schedule = response.parse()
            assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.financial_accounts.interest_tier_schedule.with_raw_response.create(
                financial_account_token="",
                credit_product_token="credit_product_token",
                effective_date=parse_date("2019-12-27"),
            )

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        interest_tier_schedule = client.financial_accounts.interest_tier_schedule.retrieve(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.financial_accounts.interest_tier_schedule.with_raw_response.retrieve(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interest_tier_schedule = response.parse()
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.financial_accounts.interest_tier_schedule.with_streaming_response.retrieve(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interest_tier_schedule = response.parse()
            assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.financial_accounts.interest_tier_schedule.with_raw_response.retrieve(
                effective_date=parse_date("2019-12-27"),
                financial_account_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `effective_date` but received ''"):
            client.financial_accounts.interest_tier_schedule.with_raw_response.retrieve(
                effective_date="",
                financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        interest_tier_schedule = client.financial_accounts.interest_tier_schedule.update(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        interest_tier_schedule = client.financial_accounts.interest_tier_schedule.update(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tier_name="tier_name",
            tier_rates={},
        )
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.financial_accounts.interest_tier_schedule.with_raw_response.update(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interest_tier_schedule = response.parse()
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.financial_accounts.interest_tier_schedule.with_streaming_response.update(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interest_tier_schedule = response.parse()
            assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.financial_accounts.interest_tier_schedule.with_raw_response.update(
                effective_date=parse_date("2019-12-27"),
                financial_account_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `effective_date` but received ''"):
            client.financial_accounts.interest_tier_schedule.with_raw_response.update(
                effective_date="",
                financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        interest_tier_schedule = client.financial_accounts.interest_tier_schedule.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncSinglePage[InterestTierSchedule], interest_tier_schedule, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        interest_tier_schedule = client.financial_accounts.interest_tier_schedule.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after_date=parse_date("2019-12-27"),
            before_date=parse_date("2019-12-27"),
            for_date=parse_date("2019-12-27"),
        )
        assert_matches_type(SyncSinglePage[InterestTierSchedule], interest_tier_schedule, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.financial_accounts.interest_tier_schedule.with_raw_response.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interest_tier_schedule = response.parse()
        assert_matches_type(SyncSinglePage[InterestTierSchedule], interest_tier_schedule, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.financial_accounts.interest_tier_schedule.with_streaming_response.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interest_tier_schedule = response.parse()
            assert_matches_type(SyncSinglePage[InterestTierSchedule], interest_tier_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.financial_accounts.interest_tier_schedule.with_raw_response.list(
                financial_account_token="",
            )

    @parametrize
    def test_method_delete(self, client: Lithic) -> None:
        interest_tier_schedule = client.financial_accounts.interest_tier_schedule.delete(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert interest_tier_schedule is None

    @parametrize
    def test_raw_response_delete(self, client: Lithic) -> None:
        response = client.financial_accounts.interest_tier_schedule.with_raw_response.delete(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interest_tier_schedule = response.parse()
        assert interest_tier_schedule is None

    @parametrize
    def test_streaming_response_delete(self, client: Lithic) -> None:
        with client.financial_accounts.interest_tier_schedule.with_streaming_response.delete(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interest_tier_schedule = response.parse()
            assert interest_tier_schedule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.financial_accounts.interest_tier_schedule.with_raw_response.delete(
                effective_date=parse_date("2019-12-27"),
                financial_account_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `effective_date` but received ''"):
            client.financial_accounts.interest_tier_schedule.with_raw_response.delete(
                effective_date="",
                financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncInterestTierSchedule:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        interest_tier_schedule = await async_client.financial_accounts.interest_tier_schedule.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        interest_tier_schedule = await async_client.financial_accounts.interest_tier_schedule.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
            tier_name="tier_name",
            tier_rates={},
        )
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.interest_tier_schedule.with_raw_response.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interest_tier_schedule = response.parse()
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.interest_tier_schedule.with_streaming_response.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            credit_product_token="credit_product_token",
            effective_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interest_tier_schedule = await response.parse()
            assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.financial_accounts.interest_tier_schedule.with_raw_response.create(
                financial_account_token="",
                credit_product_token="credit_product_token",
                effective_date=parse_date("2019-12-27"),
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        interest_tier_schedule = await async_client.financial_accounts.interest_tier_schedule.retrieve(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.interest_tier_schedule.with_raw_response.retrieve(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interest_tier_schedule = response.parse()
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.interest_tier_schedule.with_streaming_response.retrieve(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interest_tier_schedule = await response.parse()
            assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.financial_accounts.interest_tier_schedule.with_raw_response.retrieve(
                effective_date=parse_date("2019-12-27"),
                financial_account_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `effective_date` but received ''"):
            await async_client.financial_accounts.interest_tier_schedule.with_raw_response.retrieve(
                effective_date="",
                financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLithic) -> None:
        interest_tier_schedule = await async_client.financial_accounts.interest_tier_schedule.update(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLithic) -> None:
        interest_tier_schedule = await async_client.financial_accounts.interest_tier_schedule.update(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            tier_name="tier_name",
            tier_rates={},
        )
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.interest_tier_schedule.with_raw_response.update(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interest_tier_schedule = response.parse()
        assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.interest_tier_schedule.with_streaming_response.update(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interest_tier_schedule = await response.parse()
            assert_matches_type(InterestTierSchedule, interest_tier_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.financial_accounts.interest_tier_schedule.with_raw_response.update(
                effective_date=parse_date("2019-12-27"),
                financial_account_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `effective_date` but received ''"):
            await async_client.financial_accounts.interest_tier_schedule.with_raw_response.update(
                effective_date="",
                financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        interest_tier_schedule = await async_client.financial_accounts.interest_tier_schedule.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncSinglePage[InterestTierSchedule], interest_tier_schedule, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        interest_tier_schedule = await async_client.financial_accounts.interest_tier_schedule.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after_date=parse_date("2019-12-27"),
            before_date=parse_date("2019-12-27"),
            for_date=parse_date("2019-12-27"),
        )
        assert_matches_type(AsyncSinglePage[InterestTierSchedule], interest_tier_schedule, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.interest_tier_schedule.with_raw_response.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interest_tier_schedule = response.parse()
        assert_matches_type(AsyncSinglePage[InterestTierSchedule], interest_tier_schedule, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.interest_tier_schedule.with_streaming_response.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interest_tier_schedule = await response.parse()
            assert_matches_type(AsyncSinglePage[InterestTierSchedule], interest_tier_schedule, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.financial_accounts.interest_tier_schedule.with_raw_response.list(
                financial_account_token="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncLithic) -> None:
        interest_tier_schedule = await async_client.financial_accounts.interest_tier_schedule.delete(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert interest_tier_schedule is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLithic) -> None:
        response = await async_client.financial_accounts.interest_tier_schedule.with_raw_response.delete(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        interest_tier_schedule = response.parse()
        assert interest_tier_schedule is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLithic) -> None:
        async with async_client.financial_accounts.interest_tier_schedule.with_streaming_response.delete(
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            interest_tier_schedule = await response.parse()
            assert interest_tier_schedule is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.financial_accounts.interest_tier_schedule.with_raw_response.delete(
                effective_date=parse_date("2019-12-27"),
                financial_account_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `effective_date` but received ''"):
            await async_client.financial_accounts.interest_tier_schedule.with_raw_response.delete(
                effective_date="",
                financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
