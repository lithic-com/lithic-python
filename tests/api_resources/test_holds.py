# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import Hold
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHolds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        hold = client.holds.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
        )
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        hold = client.holds.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expiration_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
            memo="memo",
            user_defined_id="user_defined_id",
        )
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.holds.with_raw_response.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.holds.with_streaming_response.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert_matches_type(Hold, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.holds.with_raw_response.create(
                financial_account_token="",
                amount=1,
            )

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        hold = client.holds.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.holds.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.holds.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert_matches_type(Hold, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hold_token` but received ''"):
            client.holds.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        hold = client.holds.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[Hold], hold, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        hold = client.holds.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
            status="PENDING",
        )
        assert_matches_type(SyncCursorPage[Hold], hold, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.holds.with_raw_response.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(SyncCursorPage[Hold], hold, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.holds.with_streaming_response.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert_matches_type(SyncCursorPage[Hold], hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            client.holds.with_raw_response.list(
                financial_account_token="",
            )

    @parametrize
    def test_method_void(self, client: Lithic) -> None:
        hold = client.holds.void(
            hold_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    def test_method_void_with_all_params(self, client: Lithic) -> None:
        hold = client.holds.void(
            hold_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            memo="memo",
        )
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    def test_raw_response_void(self, client: Lithic) -> None:
        response = client.holds.with_raw_response.void(
            hold_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    def test_streaming_response_void(self, client: Lithic) -> None:
        with client.holds.with_streaming_response.void(
            hold_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert_matches_type(Hold, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_void(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hold_token` but received ''"):
            client.holds.with_raw_response.void(
                hold_token="",
            )


class TestAsyncHolds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        hold = await async_client.holds.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
        )
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        hold = await async_client.holds.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            expiration_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
            memo="memo",
            user_defined_id="user_defined_id",
        )
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.holds.with_raw_response.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.holds.with_streaming_response.create(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=1,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert_matches_type(Hold, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.holds.with_raw_response.create(
                financial_account_token="",
                amount=1,
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        hold = await async_client.holds.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.holds.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.holds.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert_matches_type(Hold, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hold_token` but received ''"):
            await async_client.holds.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        hold = await async_client.holds.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[Hold], hold, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        hold = await async_client.holds.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
            status="PENDING",
        )
        assert_matches_type(AsyncCursorPage[Hold], hold, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.holds.with_raw_response.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(AsyncCursorPage[Hold], hold, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.holds.with_streaming_response.list(
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert_matches_type(AsyncCursorPage[Hold], hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `financial_account_token` but received ''"
        ):
            await async_client.holds.with_raw_response.list(
                financial_account_token="",
            )

    @parametrize
    async def test_method_void(self, async_client: AsyncLithic) -> None:
        hold = await async_client.holds.void(
            hold_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    async def test_method_void_with_all_params(self, async_client: AsyncLithic) -> None:
        hold = await async_client.holds.void(
            hold_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            memo="memo",
        )
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    async def test_raw_response_void(self, async_client: AsyncLithic) -> None:
        response = await async_client.holds.with_raw_response.void(
            hold_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(Hold, hold, path=["response"])

    @parametrize
    async def test_streaming_response_void(self, async_client: AsyncLithic) -> None:
        async with async_client.holds.with_streaming_response.void(
            hold_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert_matches_type(Hold, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_void(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hold_token` but received ''"):
            await async_client.holds.with_raw_response.void(
                hold_token="",
            )
