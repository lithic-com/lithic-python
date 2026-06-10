# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.pagination import SyncCursorPage, AsyncCursorPage
from lithic.types.transaction_monitoring.cases import CaseFile

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        file = client.transaction_monitoring.cases.files.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(CaseFile, file, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.transaction_monitoring.cases.files.with_raw_response.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(CaseFile, file, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.transaction_monitoring.cases.files.with_streaming_response.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(CaseFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            client.transaction_monitoring.cases.files.with_raw_response.create(
                case_token="",
                name="name",
            )

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        file = client.transaction_monitoring.cases.files.retrieve(
            file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CaseFile, file, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.transaction_monitoring.cases.files.with_raw_response.retrieve(
            file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(CaseFile, file, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.transaction_monitoring.cases.files.with_streaming_response.retrieve(
            file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(CaseFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            client.transaction_monitoring.cases.files.with_raw_response.retrieve(
                file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                case_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_token` but received ''"):
            client.transaction_monitoring.cases.files.with_raw_response.retrieve(
                file_token="",
                case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        file = client.transaction_monitoring.cases.files.list(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[CaseFile], file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        file = client.transaction_monitoring.cases.files.list(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[CaseFile], file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.transaction_monitoring.cases.files.with_raw_response.list(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncCursorPage[CaseFile], file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.transaction_monitoring.cases.files.with_streaming_response.list(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(SyncCursorPage[CaseFile], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            client.transaction_monitoring.cases.files.with_raw_response.list(
                case_token="",
            )

    @parametrize
    def test_method_delete(self, client: Lithic) -> None:
        file = client.transaction_monitoring.cases.files.delete(
            file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert file is None

    @parametrize
    def test_raw_response_delete(self, client: Lithic) -> None:
        response = client.transaction_monitoring.cases.files.with_raw_response.delete(
            file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @parametrize
    def test_streaming_response_delete(self, client: Lithic) -> None:
        with client.transaction_monitoring.cases.files.with_streaming_response.delete(
            file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            client.transaction_monitoring.cases.files.with_raw_response.delete(
                file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                case_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_token` but received ''"):
            client.transaction_monitoring.cases.files.with_raw_response.delete(
                file_token="",
                case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        file = await async_client.transaction_monitoring.cases.files.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(CaseFile, file, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.transaction_monitoring.cases.files.with_raw_response.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(CaseFile, file, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.transaction_monitoring.cases.files.with_streaming_response.create(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(CaseFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            await async_client.transaction_monitoring.cases.files.with_raw_response.create(
                case_token="",
                name="name",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        file = await async_client.transaction_monitoring.cases.files.retrieve(
            file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CaseFile, file, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.transaction_monitoring.cases.files.with_raw_response.retrieve(
            file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(CaseFile, file, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.transaction_monitoring.cases.files.with_streaming_response.retrieve(
            file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(CaseFile, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            await async_client.transaction_monitoring.cases.files.with_raw_response.retrieve(
                file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                case_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_token` but received ''"):
            await async_client.transaction_monitoring.cases.files.with_raw_response.retrieve(
                file_token="",
                case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        file = await async_client.transaction_monitoring.cases.files.list(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[CaseFile], file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        file = await async_client.transaction_monitoring.cases.files.list(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[CaseFile], file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.transaction_monitoring.cases.files.with_raw_response.list(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(AsyncCursorPage[CaseFile], file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.transaction_monitoring.cases.files.with_streaming_response.list(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(AsyncCursorPage[CaseFile], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            await async_client.transaction_monitoring.cases.files.with_raw_response.list(
                case_token="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncLithic) -> None:
        file = await async_client.transaction_monitoring.cases.files.delete(
            file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert file is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLithic) -> None:
        response = await async_client.transaction_monitoring.cases.files.with_raw_response.delete(
            file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLithic) -> None:
        async with async_client.transaction_monitoring.cases.files.with_streaming_response.delete(
            file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            await async_client.transaction_monitoring.cases.files.with_raw_response.delete(
                file_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                case_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_token` but received ''"):
            await async_client.transaction_monitoring.cases.files.with_raw_response.delete(
                file_token="",
                case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
