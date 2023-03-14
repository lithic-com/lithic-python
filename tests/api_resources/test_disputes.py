# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import Dispute, DisputeEvidence, DisputeInitiateEvidenceUploadResponse
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestDisputes:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        dispute = client.disputes.create(
            amount=0,
            reason="ATM_CASH_MISDISPENSE",
            transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        dispute = client.disputes.create(
            amount=0,
            customer_filed_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            reason="ATM_CASH_MISDISPENSE",
            transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_note="string",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        dispute = client.disputes.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_method_update(self, client: Lithic) -> None:
        dispute = client.disputes.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Lithic) -> None:
        dispute = client.disputes.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            customer_filed_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_note="string",
            reason="ATM_CASH_MISDISPENSE",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        dispute = client.disputes.list()
        assert_matches_type(SyncCursorPage[Dispute], dispute, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        dispute = client.disputes.list(
            transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="NEW",
            page_size=1,
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_after="string",
            ending_before="string",
        )
        assert_matches_type(SyncCursorPage[Dispute], dispute, path=["response"])

    @parametrize
    def test_method_delete(self, client: Lithic) -> None:
        dispute = client.disputes.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    def test_method_delete_evidence(self, client: Lithic) -> None:
        dispute = client.disputes.delete_evidence(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    def test_method_initiate_evidence_upload(self, client: Lithic) -> None:
        dispute = client.disputes.initiate_evidence_upload(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisputeInitiateEvidenceUploadResponse, dispute, path=["response"])

    @parametrize
    def test_method_list_evidences(self, client: Lithic) -> None:
        dispute = client.disputes.list_evidences(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncCursorPage[DisputeEvidence], dispute, path=["response"])

    @parametrize
    def test_method_list_evidences_with_all_params(self, client: Lithic) -> None:
        dispute = client.disputes.list_evidences(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_after="string",
            ending_before="string",
        )
        assert_matches_type(SyncCursorPage[DisputeEvidence], dispute, path=["response"])

    @parametrize
    def test_method_retrieve_evidence(self, client: Lithic) -> None:
        dispute = client.disputes.retrieve_evidence(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisputeEvidence, dispute, path=["response"])


class TestAsyncDisputes:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncLithic) -> None:
        dispute = await client.disputes.create(
            amount=0,
            reason="ATM_CASH_MISDISPENSE",
            transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncLithic) -> None:
        dispute = await client.disputes.create(
            amount=0,
            customer_filed_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            reason="ATM_CASH_MISDISPENSE",
            transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_note="string",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        dispute = await client.disputes.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_method_update(self, client: AsyncLithic) -> None:
        dispute = await client.disputes.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, client: AsyncLithic) -> None:
        dispute = await client.disputes.update(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
            customer_filed_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            customer_note="string",
            reason="ATM_CASH_MISDISPENSE",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        dispute = await client.disputes.list()
        assert_matches_type(AsyncCursorPage[Dispute], dispute, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        dispute = await client.disputes.list(
            transaction_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="NEW",
            page_size=1,
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_after="string",
            ending_before="string",
        )
        assert_matches_type(AsyncCursorPage[Dispute], dispute, path=["response"])

    @parametrize
    async def test_method_delete(self, client: AsyncLithic) -> None:
        dispute = await client.disputes.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dispute, dispute, path=["response"])

    @parametrize
    async def test_method_delete_evidence(self, client: AsyncLithic) -> None:
        dispute = await client.disputes.delete_evidence(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisputeEvidence, dispute, path=["response"])

    @parametrize
    async def test_method_initiate_evidence_upload(self, client: AsyncLithic) -> None:
        dispute = await client.disputes.initiate_evidence_upload(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisputeInitiateEvidenceUploadResponse, dispute, path=["response"])

    @parametrize
    async def test_method_list_evidences(self, client: AsyncLithic) -> None:
        dispute = await client.disputes.list_evidences(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncCursorPage[DisputeEvidence], dispute, path=["response"])

    @parametrize
    async def test_method_list_evidences_with_all_params(self, client: AsyncLithic) -> None:
        dispute = await client.disputes.list_evidences(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            starting_after="string",
            ending_before="string",
        )
        assert_matches_type(AsyncCursorPage[DisputeEvidence], dispute, path=["response"])

    @parametrize
    async def test_method_retrieve_evidence(self, client: AsyncLithic) -> None:
        dispute = await client.disputes.retrieve_evidence(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            dispute_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DisputeEvidence, dispute, path=["response"])
