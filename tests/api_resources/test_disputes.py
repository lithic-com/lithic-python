# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    Dispute,
    DisputeEvidence,
)
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDisputes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        dispute = client.disputes.create(
            amount=10000,
            reason="ATM_CASH_MISDISPENSE",
            transaction_token="12345624-aa69-4cbc-a946-30d90181b621",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        dispute = client.disputes.create(
            amount=10000,
            reason="ATM_CASH_MISDISPENSE",
            transaction_token="12345624-aa69-4cbc-a946-30d90181b621",
            customer_filed_date=parse_datetime("2021-06-28T22:53:15Z"),
            customer_note="customer_note",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.disputes.with_raw_response.create(
            amount=10000,
            reason="ATM_CASH_MISDISPENSE",
            transaction_token="12345624-aa69-4cbc-a946-30d90181b621",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.disputes.with_streaming_response.create(
            amount=10000,
            reason="ATM_CASH_MISDISPENSE",
            transaction_token="12345624-aa69-4cbc-a946-30d90181b621",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        dispute = client.disputes.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.disputes.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.disputes.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            client.disputes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        dispute = client.disputes.update(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        dispute = client.disputes.update(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            customer_filed_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_note="customer_note",
            reason="ATM_CASH_MISDISPENSE",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Lithic) -> None:
        response = client.disputes.with_raw_response.update(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Lithic) -> None:
        with client.disputes.with_streaming_response.update(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            client.disputes.with_raw_response.update(
                dispute_token="",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        dispute = client.disputes.list()
        assert_matches_type(SyncCursorPage[Dispute], dispute, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        dispute = client.disputes.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
            status="ARBITRATION",
            transaction_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SyncCursorPage[Dispute], dispute, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.disputes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(SyncCursorPage[Dispute], dispute, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.disputes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(SyncCursorPage[Dispute], dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Lithic) -> None:
        dispute = client.disputes.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Lithic) -> None:
        response = client.disputes.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Lithic) -> None:
        with client.disputes.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            client.disputes.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_delete_evidence(self, client: Lithic) -> None:
        dispute = client.disputes.delete_evidence(
            evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    def test_raw_response_delete_evidence(self, client: Lithic) -> None:
        response = client.disputes.with_raw_response.delete_evidence(
            evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    def test_streaming_response_delete_evidence(self, client: Lithic) -> None:
        with client.disputes.with_streaming_response.delete_evidence(
            evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(DisputeEvidence, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_evidence(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            client.disputes.with_raw_response.delete_evidence(
                evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                dispute_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evidence_token` but received ''"):
            client.disputes.with_raw_response.delete_evidence(
                evidence_token="",
                dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    def test_method_initiate_evidence_upload(self, client: Lithic) -> None:
        dispute = client.disputes.initiate_evidence_upload(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    def test_method_initiate_evidence_upload_with_all_params(self, client: Lithic) -> None:
        dispute = client.disputes.initiate_evidence_upload(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filename="filename",
        )
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    def test_raw_response_initiate_evidence_upload(self, client: Lithic) -> None:
        response = client.disputes.with_raw_response.initiate_evidence_upload(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    def test_streaming_response_initiate_evidence_upload(self, client: Lithic) -> None:
        with client.disputes.with_streaming_response.initiate_evidence_upload(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(DisputeEvidence, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_initiate_evidence_upload(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            client.disputes.with_raw_response.initiate_evidence_upload(
                dispute_token="",
            )

    @parametrize
    def test_method_list_evidences(self, client: Lithic) -> None:
        dispute = client.disputes.list_evidences(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[DisputeEvidence], dispute, path=["response"])

    @parametrize
    def test_method_list_evidences_with_all_params(self, client: Lithic) -> None:
        dispute = client.disputes.list_evidences(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(SyncCursorPage[DisputeEvidence], dispute, path=["response"])

    @parametrize
    def test_raw_response_list_evidences(self, client: Lithic) -> None:
        response = client.disputes.with_raw_response.list_evidences(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(SyncCursorPage[DisputeEvidence], dispute, path=["response"])

    @parametrize
    def test_streaming_response_list_evidences(self, client: Lithic) -> None:
        with client.disputes.with_streaming_response.list_evidences(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(SyncCursorPage[DisputeEvidence], dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_evidences(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            client.disputes.with_raw_response.list_evidences(
                dispute_token="",
            )

    @parametrize
    def test_method_retrieve_evidence(self, client: Lithic) -> None:
        dispute = client.disputes.retrieve_evidence(
            evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    def test_raw_response_retrieve_evidence(self, client: Lithic) -> None:
        response = client.disputes.with_raw_response.retrieve_evidence(
            evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_evidence(self, client: Lithic) -> None:
        with client.disputes.with_streaming_response.retrieve_evidence(
            evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = response.parse()
            assert_matches_type(DisputeEvidence, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_evidence(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            client.disputes.with_raw_response.retrieve_evidence(
                evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                dispute_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evidence_token` but received ''"):
            client.disputes.with_raw_response.retrieve_evidence(
                evidence_token="",
                dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncDisputes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.create(
            amount=10000,
            reason="ATM_CASH_MISDISPENSE",
            transaction_token="12345624-aa69-4cbc-a946-30d90181b621",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.create(
            amount=10000,
            reason="ATM_CASH_MISDISPENSE",
            transaction_token="12345624-aa69-4cbc-a946-30d90181b621",
            customer_filed_date=parse_datetime("2021-06-28T22:53:15Z"),
            customer_note="customer_note",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.disputes.with_raw_response.create(
            amount=10000,
            reason="ATM_CASH_MISDISPENSE",
            transaction_token="12345624-aa69-4cbc-a946-30d90181b621",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.disputes.with_streaming_response.create(
            amount=10000,
            reason="ATM_CASH_MISDISPENSE",
            transaction_token="12345624-aa69-4cbc-a946-30d90181b621",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.disputes.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.disputes.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            await async_client.disputes.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.update(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.update(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            customer_filed_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_note="customer_note",
            reason="ATM_CASH_MISDISPENSE",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLithic) -> None:
        response = await async_client.disputes.with_raw_response.update(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLithic) -> None:
        async with async_client.disputes.with_streaming_response.update(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            await async_client.disputes.with_raw_response.update(
                dispute_token="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.list()
        assert_matches_type(AsyncCursorPage[Dispute], dispute, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
            status="ARBITRATION",
            transaction_tokens=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AsyncCursorPage[Dispute], dispute, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.disputes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(AsyncCursorPage[Dispute], dispute, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.disputes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(AsyncCursorPage[Dispute], dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLithic) -> None:
        response = await async_client.disputes.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLithic) -> None:
        async with async_client.disputes.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(Dispute, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            await async_client.disputes.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_delete_evidence(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.delete_evidence(
            evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    async def test_raw_response_delete_evidence(self, async_client: AsyncLithic) -> None:
        response = await async_client.disputes.with_raw_response.delete_evidence(
            evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    async def test_streaming_response_delete_evidence(self, async_client: AsyncLithic) -> None:
        async with async_client.disputes.with_streaming_response.delete_evidence(
            evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(DisputeEvidence, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_evidence(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            await async_client.disputes.with_raw_response.delete_evidence(
                evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                dispute_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evidence_token` but received ''"):
            await async_client.disputes.with_raw_response.delete_evidence(
                evidence_token="",
                dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    async def test_method_initiate_evidence_upload(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.initiate_evidence_upload(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    async def test_method_initiate_evidence_upload_with_all_params(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.initiate_evidence_upload(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filename="filename",
        )
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    async def test_raw_response_initiate_evidence_upload(self, async_client: AsyncLithic) -> None:
        response = await async_client.disputes.with_raw_response.initiate_evidence_upload(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    async def test_streaming_response_initiate_evidence_upload(self, async_client: AsyncLithic) -> None:
        async with async_client.disputes.with_streaming_response.initiate_evidence_upload(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(DisputeEvidence, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_initiate_evidence_upload(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            await async_client.disputes.with_raw_response.initiate_evidence_upload(
                dispute_token="",
            )

    @parametrize
    async def test_method_list_evidences(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.list_evidences(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[DisputeEvidence], dispute, path=["response"])

    @parametrize
    async def test_method_list_evidences_with_all_params(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.list_evidences(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
        )
        assert_matches_type(AsyncCursorPage[DisputeEvidence], dispute, path=["response"])

    @parametrize
    async def test_raw_response_list_evidences(self, async_client: AsyncLithic) -> None:
        response = await async_client.disputes.with_raw_response.list_evidences(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(AsyncCursorPage[DisputeEvidence], dispute, path=["response"])

    @parametrize
    async def test_streaming_response_list_evidences(self, async_client: AsyncLithic) -> None:
        async with async_client.disputes.with_streaming_response.list_evidences(
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(AsyncCursorPage[DisputeEvidence], dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_evidences(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            await async_client.disputes.with_raw_response.list_evidences(
                dispute_token="",
            )

    @parametrize
    async def test_method_retrieve_evidence(self, async_client: AsyncLithic) -> None:
        dispute = await async_client.disputes.retrieve_evidence(
            evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_evidence(self, async_client: AsyncLithic) -> None:
        response = await async_client.disputes.with_raw_response.retrieve_evidence(
            evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dispute = response.parse()
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_evidence(self, async_client: AsyncLithic) -> None:
        async with async_client.disputes.with_streaming_response.retrieve_evidence(
            evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dispute = await response.parse()
            assert_matches_type(DisputeEvidence, dispute, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_evidence(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dispute_token` but received ''"):
            await async_client.disputes.with_raw_response.retrieve_evidence(
                evidence_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                dispute_token="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `evidence_token` but received ''"):
            await async_client.disputes.with_raw_response.retrieve_evidence(
                evidence_token="",
                dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
