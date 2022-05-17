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
            "8ff1fecf-afa6-4297-96a1-30204b675794",
        )
        assert isinstance(resource, Transaction)

    def test_method_list(self) -> None:
        resource = self.client.transactions.list()
        assert isinstance(resource, SyncPage)

    def test_method_list_with_optional_params(self) -> None:
        resource = self.client.transactions.list(
            {
                "account_token": "1842629d-707e-475d-a31e-559ef21cc09e",
                "card_token": "aff05c52-8aae-44eb-b113-a0ab5ffc2234",
                "result": "APPROVED",
                "begin": "2019-12-27T18:11:19.117Z",
                "end": "2019-12-27T18:11:19.117Z",
                "page": 14,
                "page_size": 586,
            }
        )
        assert isinstance(resource, SyncPage)

    def test_method_simulate_authorization(self) -> None:
        resource = self.client.transactions.simulate_authorization(
            {"amount": 6, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    def test_method_simulate_authorization_with_optional_params(self) -> None:
        resource = self.client.transactions.simulate_authorization(
            {
                "amount": 17,
                "descriptor": "COFFEE SHOP",
                "pan": "4111111289144142",
                "status": "CREDIT_AUTHORIZATION",
                "merchant_currency": "GBP",
                "merchant_amount": 19,
            }
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    def test_method_simulate_clearing(self) -> None:
        resource = self.client.transactions.simulate_clearing({"token": "408ed531-85ae-4054-999d-a38efdf6cdcd"})
        assert isinstance(resource, TransactionSimulateClearingResponse)

    def test_method_simulate_clearing_with_optional_params(self) -> None:
        resource = self.client.transactions.simulate_clearing(
            {"amount": 3, "token": "411f11ec-70a2-466c-bd6e-2a2eadf409d4"}
        )
        assert isinstance(resource, TransactionSimulateClearingResponse)

    def test_method_simulate_return(self) -> None:
        resource = self.client.transactions.simulate_return(
            {"amount": 11, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    def test_method_simulate_return_with_optional_params(self) -> None:
        resource = self.client.transactions.simulate_return(
            {"amount": 13, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    def test_method_simulate_void(self) -> None:
        resource = self.client.transactions.simulate_void({"token": "2e97bd90-edaf-4654-b6d4-166537b16e0d"})
        assert isinstance(resource, TransactionSimulateVoidResponse)

    def test_method_simulate_void_with_optional_params(self) -> None:
        resource = self.client.transactions.simulate_void(
            {"amount": 5, "token": "93e158d5-23fe-4659-a389-e3cd2e4238eb"}
        )
        assert isinstance(resource, TransactionSimulateVoidResponse)


class TestAsyncTransactions:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.transactions.retrieve(
            "45267195-280b-412a-8234-ca2dbfe623ab",
        )
        assert isinstance(resource, Transaction)

    async def test_method_list(self) -> None:
        resource = await self.client.transactions.list()
        assert isinstance(resource, AsyncPage)

    async def test_method_list_with_optional_params(self) -> None:
        resource = await self.client.transactions.list(
            {
                "account_token": "8b6fb1be-525b-4cfc-bfbf-ce4eed1a3244",
                "card_token": "1e3fcb40-8d22-49b9-9321-2b2af78e6f3b",
                "result": "APPROVED",
                "begin": "2019-12-27T18:11:19.117Z",
                "end": "2019-12-27T18:11:19.117Z",
                "page": 20,
                "page_size": 870,
            }
        )
        assert isinstance(resource, AsyncPage)

    async def test_method_simulate_authorization(self) -> None:
        resource = await self.client.transactions.simulate_authorization(
            {"amount": 3, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    async def test_method_simulate_authorization_with_optional_params(self) -> None:
        resource = await self.client.transactions.simulate_authorization(
            {
                "amount": 3,
                "descriptor": "COFFEE SHOP",
                "pan": "4111111289144142",
                "status": "AUTHORIZATION",
                "merchant_currency": "GBP",
                "merchant_amount": 10,
            }
        )
        assert isinstance(resource, TransactionSimulateAuthorizationResponse)

    async def test_method_simulate_clearing(self) -> None:
        resource = await self.client.transactions.simulate_clearing({"token": "f86d84f4-96d0-4b1d-b79f-126c63e9acbb"})
        assert isinstance(resource, TransactionSimulateClearingResponse)

    async def test_method_simulate_clearing_with_optional_params(self) -> None:
        resource = await self.client.transactions.simulate_clearing(
            {"amount": 6, "token": "73ef24bf-42bc-4390-ac4d-12fc6579898e"}
        )
        assert isinstance(resource, TransactionSimulateClearingResponse)

    async def test_method_simulate_return(self) -> None:
        resource = await self.client.transactions.simulate_return(
            {"amount": 8, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    async def test_method_simulate_return_with_optional_params(self) -> None:
        resource = await self.client.transactions.simulate_return(
            {"amount": 11, "descriptor": "COFFEE SHOP", "pan": "4111111289144142"}
        )
        assert isinstance(resource, TransactionSimulateReturnResponse)

    async def test_method_simulate_void(self) -> None:
        resource = await self.client.transactions.simulate_void({"token": "ed26aa73-cbce-456c-a585-0fe2cc6e115d"})
        assert isinstance(resource, TransactionSimulateVoidResponse)

    async def test_method_simulate_void_with_optional_params(self) -> None:
        resource = await self.client.transactions.simulate_void(
            {"amount": 11, "token": "731df4d3-32fb-4780-b944-65e557e9f600"}
        )
        assert isinstance(resource, TransactionSimulateVoidResponse)
