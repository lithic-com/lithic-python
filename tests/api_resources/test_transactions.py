# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage
from lithic.types.transaction import Transaction
from lithic.types.transaction_simulate_void_response import (
    TransactionSimulateVoidResponse,
)
from lithic.types.transaction_simulate_return_response import (
    TransactionSimulateReturnResponse,
)
from lithic.types.transaction_simulate_clearing_response import (
    TransactionSimulateClearingResponse,
)
from lithic.types.transaction_simulate_authorization_response import (
    TransactionSimulateAuthorizationResponse,
)

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestTransactions:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        resource = client.transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, Transaction)

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        resource = client.transactions.list()
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        resource = client.transactions.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            result="APPROVED",
            begin="2019-12-27T18:11:19.117Z",
            end="2019-12-27T18:11:19.117Z",
            page=0,
            page_size=1,
        )
        assert isinstance(resource, SyncPage)

    @parametrize
    def test_method_simulate_authorization(self, client: Lithic) -> None:
        resource = client.transactions.simulate_authorization(
            amount=0,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    @parametrize
    def test_method_simulate_authorization_with_all_params(self, client: Lithic) -> None:
        resource = client.transactions.simulate_authorization(
            amount=0,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
            status="AUTHORIZATION",
            merchant_currency="GBP",
            merchant_amount=0,
            partial_approval_capable=True,
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    @parametrize
    def test_method_simulate_clearing(self, client: Lithic) -> None:
        resource = client.transactions.simulate_clearing(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, TransactionSimulateClearingResponse)

    @parametrize
    def test_method_simulate_clearing_with_all_params(self, client: Lithic) -> None:
        resource = client.transactions.simulate_clearing(
            amount=0,
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, TransactionSimulateClearingResponse)

    @parametrize
    def test_method_simulate_return(self, client: Lithic) -> None:
        resource = client.transactions.simulate_return(
            amount=0,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    @parametrize
    def test_method_simulate_return_with_all_params(self, client: Lithic) -> None:
        resource = client.transactions.simulate_return(
            amount=0,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    @parametrize
    def test_method_simulate_void(self, client: Lithic) -> None:
        resource = client.transactions.simulate_void(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, TransactionSimulateVoidResponse)

    @parametrize
    def test_method_simulate_void_with_all_params(self, client: Lithic) -> None:
        resource = client.transactions.simulate_void(
            amount=0,
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, TransactionSimulateVoidResponse)


class TestAsyncTransactions:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        resource = await client.transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, Transaction)

    @parametrize
    async def test_method_list(self, client: AsyncLithic) -> None:
        resource = await client.transactions.list()
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncLithic) -> None:
        resource = await client.transactions.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            result="APPROVED",
            begin="2019-12-27T18:11:19.117Z",
            end="2019-12-27T18:11:19.117Z",
            page=0,
            page_size=1,
        )
        assert isinstance(resource, AsyncPage)

    @parametrize
    async def test_method_simulate_authorization(self, client: AsyncLithic) -> None:
        resource = await client.transactions.simulate_authorization(
            amount=0,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    @parametrize
    async def test_method_simulate_authorization_with_all_params(self, client: AsyncLithic) -> None:
        resource = await client.transactions.simulate_authorization(
            amount=0,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
            status="AUTHORIZATION",
            merchant_currency="GBP",
            merchant_amount=0,
            partial_approval_capable=True,
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    @parametrize
    async def test_method_simulate_clearing(self, client: AsyncLithic) -> None:
        resource = await client.transactions.simulate_clearing(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, TransactionSimulateClearingResponse)

    @parametrize
    async def test_method_simulate_clearing_with_all_params(self, client: AsyncLithic) -> None:
        resource = await client.transactions.simulate_clearing(
            amount=0,
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, TransactionSimulateClearingResponse)

    @parametrize
    async def test_method_simulate_return(self, client: AsyncLithic) -> None:
        resource = await client.transactions.simulate_return(
            amount=0,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    @parametrize
    async def test_method_simulate_return_with_all_params(self, client: AsyncLithic) -> None:
        resource = await client.transactions.simulate_return(
            amount=0,
            descriptor="COFFEE SHOP",
            pan="4111111289144142",
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    @parametrize
    async def test_method_simulate_void(self, client: AsyncLithic) -> None:
        resource = await client.transactions.simulate_void(
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, TransactionSimulateVoidResponse)

    @parametrize
    async def test_method_simulate_void_with_all_params(self, client: AsyncLithic) -> None:
        resource = await client.transactions.simulate_void(
            amount=0,
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, TransactionSimulateVoidResponse)
