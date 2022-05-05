# File generated from our OpenAPI spec by Stainless.
import os
import pytest
from lithic import Lithic, AsyncLithic
from lithic.pagination import SyncPage, AsyncPage

from lithic.types.transaction import *
from lithic.types.transaction_simulate_authorization_response import *
from lithic.types.transaction_simulate_clearing_response import *
from lithic.types.transaction_simulate_return_response import *
from lithic.types.transaction_simulate_void_response import *


base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestTransactions:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_retrieve(self) -> None:
        resource = self.client.transactions.retrieve(
            "e31e559e-f21c-4c09-aaff-05c528aae4eb",
        )
        assert isinstance(resource, Transaction)

    def test_method_list(self) -> None:
        resource = self.client.transactions.list()
        assert isinstance(resource, SyncPage[Transaction])

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.transactions.list(
            {
                "account_token": "3113a0ab-5ffc-4223-87a9-4d6f408ed531",
                "card_token": "85ae0545-99da-438e-bdf6-cdcd2411f11e",
                "result": "DECLINED",
                "begin": "2019-12-27T18:11:19.117Z",
                "end": "2019-12-27T18:11:19.117Z",
                "page": 10,
                "page_size": 48,
            }
        )
        assert isinstance(resource, SyncPage[Transaction])

    def test_method_simulate_authorization(self) -> None:
        resource = self.client.transactions.simulate_authorization(
            {"amount": 14, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    def test_method_simulate_authorization_with_optional_params(self) -> None:
        resource = self.client.transactions.simulate_authorization(
            {
                "amount": 3,
                "descriptor": "COFFEE SHOP",
                "pan": "4111111289144142",
                "status": "AUTHORIZATION",
                "merchant_currency": "GBP",
                "merchant_amount": 8,
            }
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    def test_method_simulate_clearing(self) -> None:
        resource = self.client.transactions.simulate_clearing({"token": "cfd6e2a2-eadf-4409-948a-2e97bd90edaf"})
        assert isinstance(resource, TransactionSimulateClearingResponse)

    def test_method_simulate_clearing_with_optional_params(self) -> None:
        resource = self.client.transactions.simulate_clearing(
            {"amount": 8, "token": "54b6d416-6537-4b16-a0d4-93e158d523fe"}
        )
        assert isinstance(resource, TransactionSimulateClearingResponse)

    def test_method_simulate_return(self) -> None:
        resource = self.client.transactions.simulate_return(
            {"amount": 8, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    def test_method_simulate_return_with_optional_params(self) -> None:
        resource = self.client.transactions.simulate_return(
            {"amount": 6, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    def test_method_simulate_void(self) -> None:
        resource = self.client.transactions.simulate_void({"token": "92389e3c-d2e4-4238-ab45-267195280b12"})
        assert isinstance(resource, TransactionSimulateVoidResponse)

    def test_method_simulate_void_with_optional_params(self) -> None:
        resource = self.client.transactions.simulate_void(
            {"amount": 13, "token": "c234ca2d-bfe6-423a-b8b6-fb1be525bcfc"}
        )
        assert isinstance(resource, TransactionSimulateVoidResponse)


class TestAsyncTransactions:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.transactions.retrieve(
            "3fbfce4e-ed1a-4324-81e3-fcb408d229b9",
        )
        assert isinstance(resource, Transaction)

    async def test_method_list(self) -> None:
        resource = await self.client.transactions.list()
        assert isinstance(resource, AsyncPage[Transaction])

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.transactions.list(
            {
                "account_token": "53212b2a-f78e-46f3-b6fd-2228f86d84f4",
                "card_token": "96d0b1db-79f1-426c-a3e9-acbb473ef24b",
                "result": "DECLINED",
                "begin": "2019-12-27T18:11:19.117Z",
                "end": "2019-12-27T18:11:19.117Z",
                "page": 5,
                "page_size": 137,
            }
        )
        assert isinstance(resource, AsyncPage[Transaction])

    async def test_method_simulate_authorization(self) -> None:
        resource = await self.client.transactions.simulate_authorization(
            {"amount": 14, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    async def test_method_simulate_authorization_with_optional_params(self) -> None:
        resource = await self.client.transactions.simulate_authorization(
            {
                "amount": 16,
                "descriptor": "COFFEE SHOP",
                "pan": "4111111289144142",
                "status": "AUTHORIZATION",
                "merchant_currency": "GBP",
                "merchant_amount": 12,
            }
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    async def test_method_simulate_clearing(self) -> None:
        resource = await self.client.transactions.simulate_clearing({"token": "0ec4d12f-c657-4989-8e69-ed26aa73cbce"})
        assert isinstance(resource, TransactionSimulateClearingResponse)

    async def test_method_simulate_clearing_with_optional_params(self) -> None:
        resource = await self.client.transactions.simulate_clearing(
            {"amount": 6, "token": "6ca5850f-e2cc-46e1-95d8-731df4d332fb"}
        )
        assert isinstance(resource, TransactionSimulateClearingResponse)

    async def test_method_simulate_return(self) -> None:
        resource = await self.client.transactions.simulate_return(
            {"amount": 9, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    async def test_method_simulate_return_with_optional_params(self) -> None:
        resource = await self.client.transactions.simulate_return(
            {"amount": 11, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    async def test_method_simulate_void(self) -> None:
        resource = await self.client.transactions.simulate_void({"token": "0b94465e-557e-49f6-807c-97065b069370"})
        assert isinstance(resource, TransactionSimulateVoidResponse)

    async def test_method_simulate_void_with_optional_params(self) -> None:
        resource = await self.client.transactions.simulate_void(
            {"amount": 5, "token": "8c38750e-2f62-4bfd-95ef-4b0e0062037f"}
        )
        assert isinstance(resource, TransactionSimulateVoidResponse)
