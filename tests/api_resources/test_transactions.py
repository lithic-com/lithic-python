# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    Transaction,
    TransactionSimulateVoidResponse,
    TransactionSimulateReturnResponse,
    TransactionSimulateClearingResponse,
    TransactionSimulateAuthorizationResponse,
    TransactionSimulateReturnReversalResponse,
    TransactionSimulateAuthorizationAdviceResponse,
    TransactionSimulateCreditAuthorizationResponse,
)
from lithic._utils import parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestTransactions:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        transaction = client.transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        transaction = client.transactions.list()
        assert_matches_type(SyncCursorPage[Transaction], transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        transaction = client.transactions.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            page_size=1,
            result="APPROVED",
            starting_after="string",
        )
        assert_matches_type(SyncCursorPage[Transaction], transaction, path=["response"])

    @parametrize
    def test_method_simulate_authorization(self, client: Lithic) -> None:
        transaction = client.transactions.simulate_authorization(
            amount=3831,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
        )
        assert_matches_type(TransactionSimulateAuthorizationResponse, transaction, path=["response"])

    @parametrize
    def test_method_simulate_authorization_with_all_params(self, client: Lithic) -> None:
        transaction = client.transactions.simulate_authorization(
            amount=3831,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
            mcc="5812",
            merchant_acceptor_id="OODKZAPJVN4YS7O",
            merchant_amount=0,
            merchant_currency="GBP",
            partial_approval_capable=True,
            status="AUTHORIZATION",
        )
        assert_matches_type(TransactionSimulateAuthorizationResponse, transaction, path=["response"])

    @parametrize
    def test_method_simulate_authorization_advice(self, client: Lithic) -> None:
        transaction = client.transactions.simulate_authorization_advice(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
            amount=3831,
        )
        assert_matches_type(TransactionSimulateAuthorizationAdviceResponse, transaction, path=["response"])

    @parametrize
    def test_method_simulate_clearing(self, client: Lithic) -> None:
        transaction = client.transactions.simulate_clearing(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TransactionSimulateClearingResponse, transaction, path=["response"])

    @parametrize
    def test_method_simulate_clearing_with_all_params(self, client: Lithic) -> None:
        transaction = client.transactions.simulate_clearing(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
        )
        assert_matches_type(TransactionSimulateClearingResponse, transaction, path=["response"])

    @parametrize
    def test_method_simulate_credit_authorization(self, client: Lithic) -> None:
        transaction = client.transactions.simulate_credit_authorization(
            amount=3831,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
        )
        assert_matches_type(TransactionSimulateCreditAuthorizationResponse, transaction, path=["response"])

    @parametrize
    def test_method_simulate_credit_authorization_with_all_params(self, client: Lithic) -> None:
        transaction = client.transactions.simulate_credit_authorization(
            amount=3831,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
            mcc="5812",
            merchant_acceptor_id="XRKGDPOWEWQRRWU",
        )
        assert_matches_type(TransactionSimulateCreditAuthorizationResponse, transaction, path=["response"])

    @parametrize
    def test_method_simulate_return(self, client: Lithic) -> None:
        transaction = client.transactions.simulate_return(
            amount=3831,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
        )
        assert_matches_type(TransactionSimulateReturnResponse, transaction, path=["response"])

    @parametrize
    def test_method_simulate_return_reversal(self, client: Lithic) -> None:
        transaction = client.transactions.simulate_return_reversal(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
        )
        assert_matches_type(TransactionSimulateReturnReversalResponse, transaction, path=["response"])

    @parametrize
    def test_method_simulate_void(self, client: Lithic) -> None:
        transaction = client.transactions.simulate_void(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
        )
        assert_matches_type(TransactionSimulateVoidResponse, transaction, path=["response"])

    @parametrize
    def test_method_simulate_void_with_all_params(self, client: Lithic) -> None:
        transaction = client.transactions.simulate_void(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
            amount=100,
            type="AUTHORIZATION_EXPIRY",
        )
        assert_matches_type(TransactionSimulateVoidResponse, transaction, path=["response"])


class TestAsyncTransactions:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.list()
        assert_matches_type(AsyncCursorPage[Transaction], transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="string",
            page_size=1,
            result="APPROVED",
            starting_after="string",
        )
        assert_matches_type(AsyncCursorPage[Transaction], transaction, path=["response"])

    @parametrize
    async def test_method_simulate_authorization(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.simulate_authorization(
            amount=3831,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
        )
        assert_matches_type(TransactionSimulateAuthorizationResponse, transaction, path=["response"])

    @parametrize
    async def test_method_simulate_authorization_with_all_params(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.simulate_authorization(
            amount=3831,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
            mcc="5812",
            merchant_acceptor_id="OODKZAPJVN4YS7O",
            merchant_amount=0,
            merchant_currency="GBP",
            partial_approval_capable=True,
            status="AUTHORIZATION",
        )
        assert_matches_type(TransactionSimulateAuthorizationResponse, transaction, path=["response"])

    @parametrize
    async def test_method_simulate_authorization_advice(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.simulate_authorization_advice(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
            amount=3831,
        )
        assert_matches_type(TransactionSimulateAuthorizationAdviceResponse, transaction, path=["response"])

    @parametrize
    async def test_method_simulate_clearing(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.simulate_clearing(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TransactionSimulateClearingResponse, transaction, path=["response"])

    @parametrize
    async def test_method_simulate_clearing_with_all_params(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.simulate_clearing(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            amount=0,
        )
        assert_matches_type(TransactionSimulateClearingResponse, transaction, path=["response"])

    @parametrize
    async def test_method_simulate_credit_authorization(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.simulate_credit_authorization(
            amount=3831,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
        )
        assert_matches_type(TransactionSimulateCreditAuthorizationResponse, transaction, path=["response"])

    @parametrize
    async def test_method_simulate_credit_authorization_with_all_params(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.simulate_credit_authorization(
            amount=3831,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
            mcc="5812",
            merchant_acceptor_id="XRKGDPOWEWQRRWU",
        )
        assert_matches_type(TransactionSimulateCreditAuthorizationResponse, transaction, path=["response"])

    @parametrize
    async def test_method_simulate_return(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.simulate_return(
            amount=3831,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
        )
        assert_matches_type(TransactionSimulateReturnResponse, transaction, path=["response"])

    @parametrize
    async def test_method_simulate_return_reversal(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.simulate_return_reversal(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
        )
        assert_matches_type(TransactionSimulateReturnReversalResponse, transaction, path=["response"])

    @parametrize
    async def test_method_simulate_void(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.simulate_void(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
        )
        assert_matches_type(TransactionSimulateVoidResponse, transaction, path=["response"])

    @parametrize
    async def test_method_simulate_void_with_all_params(self, client: AsyncLithic) -> None:
        transaction = await client.transactions.simulate_void(
            token="fabd829d-7f7b-4432-a8f2-07ea4889aaac",
            amount=100,
            type="AUTHORIZATION_EXPIRY",
        )
        assert_matches_type(TransactionSimulateVoidResponse, transaction, path=["response"])
