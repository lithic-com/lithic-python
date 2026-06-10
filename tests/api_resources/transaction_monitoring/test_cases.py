# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage
from lithic.types.transaction_monitoring import (
    MonitoringCase,
    CaseTransaction,
    CaseActivityEntry,
    CaseRetrieveCardsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCases:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        case = client.transaction_monitoring.cases.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MonitoringCase, case, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.transaction_monitoring.cases.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        case = response.parse()
        assert_matches_type(MonitoringCase, case, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.transaction_monitoring.cases.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            case = response.parse()
            assert_matches_type(MonitoringCase, case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            client.transaction_monitoring.cases.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        case = client.transaction_monitoring.cases.update(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MonitoringCase, case, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        case = client.transaction_monitoring.cases.update(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actor_token="actor_token",
            assignee="assignee",
            priority="LOW",
            resolution="CONFIRMED_FRAUD",
            resolution_notes="resolution_notes",
            sla_deadline=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="OPEN",
            tags={"foo": "string"},
            title="title",
        )
        assert_matches_type(MonitoringCase, case, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.transaction_monitoring.cases.with_raw_response.update(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        case = response.parse()
        assert_matches_type(MonitoringCase, case, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.transaction_monitoring.cases.with_streaming_response.update(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            case = response.parse()
            assert_matches_type(MonitoringCase, case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            client.transaction_monitoring.cases.with_raw_response.update(
                case_token="",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        case = client.transaction_monitoring.cases.list()
        assert_matches_type(SyncCursorPage[MonitoringCase], case, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        case = client.transaction_monitoring.cases.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            assignee="assignee",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            queue_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort_by="CREATED_ASC",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="OPEN",
            transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[MonitoringCase], case, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.transaction_monitoring.cases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        case = response.parse()
        assert_matches_type(SyncCursorPage[MonitoringCase], case, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.transaction_monitoring.cases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            case = response.parse()
            assert_matches_type(SyncCursorPage[MonitoringCase], case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_activity(self, client: Lithic) -> None:
        case = client.transaction_monitoring.cases.list_activity(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[CaseActivityEntry], case, path=["response"])

    @parametrize
    def test_method_list_activity_with_all_params(self, client: Lithic) -> None:
        case = client.transaction_monitoring.cases.list_activity(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[CaseActivityEntry], case, path=["response"])

    @parametrize
    def test_raw_response_list_activity(self, client: Lithic) -> None:
        response = client.transaction_monitoring.cases.with_raw_response.list_activity(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        case = response.parse()
        assert_matches_type(SyncCursorPage[CaseActivityEntry], case, path=["response"])

    @parametrize
    def test_streaming_response_list_activity(self, client: Lithic) -> None:
        with client.transaction_monitoring.cases.with_streaming_response.list_activity(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            case = response.parse()
            assert_matches_type(SyncCursorPage[CaseActivityEntry], case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_activity(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            client.transaction_monitoring.cases.with_raw_response.list_activity(
                case_token="",
            )

    @parametrize
    def test_method_list_transactions(self, client: Lithic) -> None:
        case = client.transaction_monitoring.cases.list_transactions(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[CaseTransaction], case, path=["response"])

    @parametrize
    def test_method_list_transactions_with_all_params(self, client: Lithic) -> None:
        case = client.transaction_monitoring.cases.list_transactions(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[CaseTransaction], case, path=["response"])

    @parametrize
    def test_raw_response_list_transactions(self, client: Lithic) -> None:
        response = client.transaction_monitoring.cases.with_raw_response.list_transactions(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        case = response.parse()
        assert_matches_type(SyncCursorPage[CaseTransaction], case, path=["response"])

    @parametrize
    def test_streaming_response_list_transactions(self, client: Lithic) -> None:
        with client.transaction_monitoring.cases.with_streaming_response.list_transactions(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            case = response.parse()
            assert_matches_type(SyncCursorPage[CaseTransaction], case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_transactions(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            client.transaction_monitoring.cases.with_raw_response.list_transactions(
                case_token="",
            )

    @parametrize
    def test_method_retrieve_cards(self, client: Lithic) -> None:
        case = client.transaction_monitoring.cases.retrieve_cards(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CaseRetrieveCardsResponse, case, path=["response"])

    @parametrize
    def test_raw_response_retrieve_cards(self, client: Lithic) -> None:
        response = client.transaction_monitoring.cases.with_raw_response.retrieve_cards(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        case = response.parse()
        assert_matches_type(CaseRetrieveCardsResponse, case, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_cards(self, client: Lithic) -> None:
        with client.transaction_monitoring.cases.with_streaming_response.retrieve_cards(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            case = response.parse()
            assert_matches_type(CaseRetrieveCardsResponse, case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_cards(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            client.transaction_monitoring.cases.with_raw_response.retrieve_cards(
                "",
            )


class TestAsyncCases:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        case = await async_client.transaction_monitoring.cases.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MonitoringCase, case, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.transaction_monitoring.cases.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        case = response.parse()
        assert_matches_type(MonitoringCase, case, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.transaction_monitoring.cases.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            case = await response.parse()
            assert_matches_type(MonitoringCase, case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            await async_client.transaction_monitoring.cases.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLithic) -> None:
        case = await async_client.transaction_monitoring.cases.update(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(MonitoringCase, case, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLithic) -> None:
        case = await async_client.transaction_monitoring.cases.update(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            actor_token="actor_token",
            assignee="assignee",
            priority="LOW",
            resolution="CONFIRMED_FRAUD",
            resolution_notes="resolution_notes",
            sla_deadline=parse_datetime("2019-12-27T18:11:19.117Z"),
            status="OPEN",
            tags={"foo": "string"},
            title="title",
        )
        assert_matches_type(MonitoringCase, case, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLithic) -> None:
        response = await async_client.transaction_monitoring.cases.with_raw_response.update(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        case = response.parse()
        assert_matches_type(MonitoringCase, case, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLithic) -> None:
        async with async_client.transaction_monitoring.cases.with_streaming_response.update(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            case = await response.parse()
            assert_matches_type(MonitoringCase, case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            await async_client.transaction_monitoring.cases.with_raw_response.update(
                case_token="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        case = await async_client.transaction_monitoring.cases.list()
        assert_matches_type(AsyncCursorPage[MonitoringCase], case, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        case = await async_client.transaction_monitoring.cases.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            assignee="assignee",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            entity_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            queue_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            rule_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort_by="CREATED_ASC",
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="OPEN",
            transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[MonitoringCase], case, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.transaction_monitoring.cases.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        case = response.parse()
        assert_matches_type(AsyncCursorPage[MonitoringCase], case, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.transaction_monitoring.cases.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            case = await response.parse()
            assert_matches_type(AsyncCursorPage[MonitoringCase], case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_activity(self, async_client: AsyncLithic) -> None:
        case = await async_client.transaction_monitoring.cases.list_activity(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[CaseActivityEntry], case, path=["response"])

    @parametrize
    async def test_method_list_activity_with_all_params(self, async_client: AsyncLithic) -> None:
        case = await async_client.transaction_monitoring.cases.list_activity(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[CaseActivityEntry], case, path=["response"])

    @parametrize
    async def test_raw_response_list_activity(self, async_client: AsyncLithic) -> None:
        response = await async_client.transaction_monitoring.cases.with_raw_response.list_activity(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        case = response.parse()
        assert_matches_type(AsyncCursorPage[CaseActivityEntry], case, path=["response"])

    @parametrize
    async def test_streaming_response_list_activity(self, async_client: AsyncLithic) -> None:
        async with async_client.transaction_monitoring.cases.with_streaming_response.list_activity(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            case = await response.parse()
            assert_matches_type(AsyncCursorPage[CaseActivityEntry], case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_activity(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            await async_client.transaction_monitoring.cases.with_raw_response.list_activity(
                case_token="",
            )

    @parametrize
    async def test_method_list_transactions(self, async_client: AsyncLithic) -> None:
        case = await async_client.transaction_monitoring.cases.list_transactions(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[CaseTransaction], case, path=["response"])

    @parametrize
    async def test_method_list_transactions_with_all_params(self, async_client: AsyncLithic) -> None:
        case = await async_client.transaction_monitoring.cases.list_transactions(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ending_before="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            starting_after="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[CaseTransaction], case, path=["response"])

    @parametrize
    async def test_raw_response_list_transactions(self, async_client: AsyncLithic) -> None:
        response = await async_client.transaction_monitoring.cases.with_raw_response.list_transactions(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        case = response.parse()
        assert_matches_type(AsyncCursorPage[CaseTransaction], case, path=["response"])

    @parametrize
    async def test_streaming_response_list_transactions(self, async_client: AsyncLithic) -> None:
        async with async_client.transaction_monitoring.cases.with_streaming_response.list_transactions(
            case_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            case = await response.parse()
            assert_matches_type(AsyncCursorPage[CaseTransaction], case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_transactions(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            await async_client.transaction_monitoring.cases.with_raw_response.list_transactions(
                case_token="",
            )

    @parametrize
    async def test_method_retrieve_cards(self, async_client: AsyncLithic) -> None:
        case = await async_client.transaction_monitoring.cases.retrieve_cards(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CaseRetrieveCardsResponse, case, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_cards(self, async_client: AsyncLithic) -> None:
        response = await async_client.transaction_monitoring.cases.with_raw_response.retrieve_cards(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        case = response.parse()
        assert_matches_type(CaseRetrieveCardsResponse, case, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_cards(self, async_client: AsyncLithic) -> None:
        async with async_client.transaction_monitoring.cases.with_streaming_response.retrieve_cards(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            case = await response.parse()
            assert_matches_type(CaseRetrieveCardsResponse, case, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_cards(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `case_token` but received ''"):
            await async_client.transaction_monitoring.cases.with_raw_response.retrieve_cards(
                "",
            )
