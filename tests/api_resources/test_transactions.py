# File generated from our OpenAPI spec by Stainless.
import os

import pytest

from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage
from lithic.types.transaction import *
from lithic.types.transaction_simulate_void_response import *
from lithic.types.transaction_simulate_return_response import *
from lithic.types.transaction_simulate_clearing_response import *
from lithic.types.transaction_simulate_authorization_response import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestTransactions:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_retrieve(self) -> None:
        resource = self.client.transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, Transaction)

    def test_method_list(self) -> None:
        resource = self.client.transactions.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.transactions.list(
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "card_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "result": "APPROVED",
                "begin": "2019-12-27T18:11:19.117Z",
                "end": "2019-12-27T18:11:19.117Z",
                "page": 0,
                "page_size": 1,
            }
        )
        assert isinstance(resource, SyncPage)

    def test_method_simulate_authorization(self) -> None:
        resource = self.client.transactions.simulate_authorization(
            {"amount": 0, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    def test_method_simulate_authorization_with_optional_params(self) -> None:
        resource = self.client.transactions.simulate_authorization(
            {
                "amount": 0,
                "descriptor": "COFFEE SHOP",
                "pan": "4111111289144142",
                "status": "AUTHORIZATION",
                "merchant_currency": "GBP",
                "merchant_amount": 0,
            }
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    def test_method_simulate_clearing(self) -> None:
        resource = self.client.transactions.simulate_clearing({"token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"})
        assert isinstance(resource, TransactionSimulateClearingResponse)

    def test_method_simulate_clearing_with_optional_params(self) -> None:
        resource = self.client.transactions.simulate_clearing(
            {"amount": 0, "token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}
        )
        assert isinstance(resource, TransactionSimulateClearingResponse)

    def test_method_simulate_return(self) -> None:
        resource = self.client.transactions.simulate_return(
            {"amount": 0, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    def test_method_simulate_return_with_optional_params(self) -> None:
        resource = self.client.transactions.simulate_return(
            {"amount": 0, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    def test_method_simulate_void(self) -> None:
        resource = self.client.transactions.simulate_void({"token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"})
        assert isinstance(resource, TransactionSimulateVoidResponse)

    def test_method_simulate_void_with_optional_params(self) -> None:
        resource = self.client.transactions.simulate_void(
            {"amount": 0, "token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}
        )
        assert isinstance(resource, TransactionSimulateVoidResponse)


class TestAsyncTransactions:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.transactions.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert isinstance(resource, Transaction)

    async def test_method_list(self) -> None:
        resource = await self.client.transactions.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.transactions.list(
            {
                "account_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "card_token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "result": "APPROVED",
                "begin": "2019-12-27T18:11:19.117Z",
                "end": "2019-12-27T18:11:19.117Z",
                "page": 0,
                "page_size": 1,
            }
        )
        assert isinstance(resource, AsyncPage)

    async def test_method_simulate_authorization(self) -> None:
        resource = await self.client.transactions.simulate_authorization(
            {"amount": 0, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    async def test_method_simulate_authorization_with_optional_params(self) -> None:
        resource = await self.client.transactions.simulate_authorization(
            {
                "amount": 0,
                "descriptor": "COFFEE SHOP",
                "pan": "4111111289144142",
                "status": "AUTHORIZATION",
                "merchant_currency": "GBP",
                "merchant_amount": 0,
            }
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    async def test_method_simulate_clearing(self) -> None:
        resource = await self.client.transactions.simulate_clearing({"token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"})
        assert isinstance(resource, TransactionSimulateClearingResponse)

    async def test_method_simulate_clearing_with_optional_params(self) -> None:
        resource = await self.client.transactions.simulate_clearing(
            {"amount": 0, "token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}
        )
        assert isinstance(resource, TransactionSimulateClearingResponse)

    async def test_method_simulate_return(self) -> None:
        resource = await self.client.transactions.simulate_return(
            {"amount": 0, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    async def test_method_simulate_return_with_optional_params(self) -> None:
        resource = await self.client.transactions.simulate_return(
            {"amount": 0, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    async def test_method_simulate_void(self) -> None:
        resource = await self.client.transactions.simulate_void({"token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"})
        assert isinstance(resource, TransactionSimulateVoidResponse)

    async def test_method_simulate_void_with_optional_params(self) -> None:
        resource = await self.client.transactions.simulate_void(
            {"amount": 0, "token": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"}
        )
        assert isinstance(resource, TransactionSimulateVoidResponse)
