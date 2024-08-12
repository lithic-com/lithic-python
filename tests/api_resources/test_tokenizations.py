# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    Tokenization,
    TokenizationRetrieveResponse,
    TokenizationSimulateResponse,
    TokenizationUpdateDigitalCardArtResponse,
)
from lithic._utils import parse_date
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokenizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        tokenization = client.tokenizations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TokenizationRetrieveResponse, tokenization, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.tokenizations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(TokenizationRetrieveResponse, tokenization, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.tokenizations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = response.parse()
            assert_matches_type(TokenizationRetrieveResponse, tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            client.tokenizations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        tokenization = client.tokenizations.list()
        assert_matches_type(SyncCursorPage[Tokenization], tokenization, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        tokenization = client.tokenizations.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_date("2019-12-27"),
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end=parse_date("2019-12-27"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
            tokenization_channel="DIGITAL_WALLET",
        )
        assert_matches_type(SyncCursorPage[Tokenization], tokenization, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.tokenizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(SyncCursorPage[Tokenization], tokenization, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.tokenizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = response.parse()
            assert_matches_type(SyncCursorPage[Tokenization], tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_activate(self, client: Lithic) -> None:
        tokenization = client.tokenizations.activate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tokenization is None

    @parametrize
    def test_raw_response_activate(self, client: Lithic) -> None:
        response = client.tokenizations.with_raw_response.activate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert tokenization is None

    @parametrize
    def test_streaming_response_activate(self, client: Lithic) -> None:
        with client.tokenizations.with_streaming_response.activate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = response.parse()
            assert tokenization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_activate(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            client.tokenizations.with_raw_response.activate(
                "",
            )

    @parametrize
    def test_method_deactivate(self, client: Lithic) -> None:
        tokenization = client.tokenizations.deactivate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tokenization is None

    @parametrize
    def test_raw_response_deactivate(self, client: Lithic) -> None:
        response = client.tokenizations.with_raw_response.deactivate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert tokenization is None

    @parametrize
    def test_streaming_response_deactivate(self, client: Lithic) -> None:
        with client.tokenizations.with_streaming_response.deactivate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = response.parse()
            assert tokenization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_deactivate(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            client.tokenizations.with_raw_response.deactivate(
                "",
            )

    @parametrize
    def test_method_pause(self, client: Lithic) -> None:
        tokenization = client.tokenizations.pause(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tokenization is None

    @parametrize
    def test_raw_response_pause(self, client: Lithic) -> None:
        response = client.tokenizations.with_raw_response.pause(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert tokenization is None

    @parametrize
    def test_streaming_response_pause(self, client: Lithic) -> None:
        with client.tokenizations.with_streaming_response.pause(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = response.parse()
            assert tokenization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_pause(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            client.tokenizations.with_raw_response.pause(
                "",
            )

    @parametrize
    def test_method_resend_activation_code(self, client: Lithic) -> None:
        tokenization = client.tokenizations.resend_activation_code(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tokenization is None

    @parametrize
    def test_method_resend_activation_code_with_all_params(self, client: Lithic) -> None:
        tokenization = client.tokenizations.resend_activation_code(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_method_type="EMAIL_TO_CARDHOLDER_ADDRESS",
        )
        assert tokenization is None

    @parametrize
    def test_raw_response_resend_activation_code(self, client: Lithic) -> None:
        response = client.tokenizations.with_raw_response.resend_activation_code(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert tokenization is None

    @parametrize
    def test_streaming_response_resend_activation_code(self, client: Lithic) -> None:
        with client.tokenizations.with_streaming_response.resend_activation_code(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = response.parse()
            assert tokenization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_resend_activation_code(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            client.tokenizations.with_raw_response.resend_activation_code(
                tokenization_token="",
            )

    @parametrize
    def test_method_simulate(self, client: Lithic) -> None:
        tokenization = client.tokenizations.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
        )
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

    @parametrize
    def test_method_simulate_with_all_params(self, client: Lithic) -> None:
        tokenization = client.tokenizations.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
            account_score=5,
            device_score=5,
            entity="entity",
            wallet_recommended_decision="APPROVED",
        )
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

    @parametrize
    def test_raw_response_simulate(self, client: Lithic) -> None:
        response = client.tokenizations.with_raw_response.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

    @parametrize
    def test_streaming_response_simulate(self, client: Lithic) -> None:
        with client.tokenizations.with_streaming_response.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = response.parse()
            assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unpause(self, client: Lithic) -> None:
        tokenization = client.tokenizations.unpause(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tokenization is None

    @parametrize
    def test_raw_response_unpause(self, client: Lithic) -> None:
        response = client.tokenizations.with_raw_response.unpause(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert tokenization is None

    @parametrize
    def test_streaming_response_unpause(self, client: Lithic) -> None:
        with client.tokenizations.with_streaming_response.unpause(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = response.parse()
            assert tokenization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_unpause(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            client.tokenizations.with_raw_response.unpause(
                "",
            )

    @parametrize
    def test_method_update_digital_card_art(self, client: Lithic) -> None:
        tokenization = client.tokenizations.update_digital_card_art(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TokenizationUpdateDigitalCardArtResponse, tokenization, path=["response"])

    @parametrize
    def test_method_update_digital_card_art_with_all_params(self, client: Lithic) -> None:
        tokenization = client.tokenizations.update_digital_card_art(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            digital_card_art_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TokenizationUpdateDigitalCardArtResponse, tokenization, path=["response"])

    @parametrize
    def test_raw_response_update_digital_card_art(self, client: Lithic) -> None:
        response = client.tokenizations.with_raw_response.update_digital_card_art(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(TokenizationUpdateDigitalCardArtResponse, tokenization, path=["response"])

    @parametrize
    def test_streaming_response_update_digital_card_art(self, client: Lithic) -> None:
        with client.tokenizations.with_streaming_response.update_digital_card_art(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = response.parse()
            assert_matches_type(TokenizationUpdateDigitalCardArtResponse, tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_digital_card_art(self, client: Lithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            client.tokenizations.with_raw_response.update_digital_card_art(
                tokenization_token="",
            )


class TestAsyncTokenizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TokenizationRetrieveResponse, tokenization, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenizations.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(TokenizationRetrieveResponse, tokenization, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenizations.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = await response.parse()
            assert_matches_type(TokenizationRetrieveResponse, tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            await async_client.tokenizations.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.list()
        assert_matches_type(AsyncCursorPage[Tokenization], tokenization, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.list(
            account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            begin=parse_date("2019-12-27"),
            card_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end=parse_date("2019-12-27"),
            ending_before="ending_before",
            page_size=1,
            starting_after="starting_after",
            tokenization_channel="DIGITAL_WALLET",
        )
        assert_matches_type(AsyncCursorPage[Tokenization], tokenization, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenizations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(AsyncCursorPage[Tokenization], tokenization, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenizations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = await response.parse()
            assert_matches_type(AsyncCursorPage[Tokenization], tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_activate(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.activate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tokenization is None

    @parametrize
    async def test_raw_response_activate(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenizations.with_raw_response.activate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert tokenization is None

    @parametrize
    async def test_streaming_response_activate(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenizations.with_streaming_response.activate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = await response.parse()
            assert tokenization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_activate(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            await async_client.tokenizations.with_raw_response.activate(
                "",
            )

    @parametrize
    async def test_method_deactivate(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.deactivate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tokenization is None

    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenizations.with_raw_response.deactivate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert tokenization is None

    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenizations.with_streaming_response.deactivate(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = await response.parse()
            assert tokenization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            await async_client.tokenizations.with_raw_response.deactivate(
                "",
            )

    @parametrize
    async def test_method_pause(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.pause(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tokenization is None

    @parametrize
    async def test_raw_response_pause(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenizations.with_raw_response.pause(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert tokenization is None

    @parametrize
    async def test_streaming_response_pause(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenizations.with_streaming_response.pause(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = await response.parse()
            assert tokenization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_pause(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            await async_client.tokenizations.with_raw_response.pause(
                "",
            )

    @parametrize
    async def test_method_resend_activation_code(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.resend_activation_code(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tokenization is None

    @parametrize
    async def test_method_resend_activation_code_with_all_params(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.resend_activation_code(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            activation_method_type="EMAIL_TO_CARDHOLDER_ADDRESS",
        )
        assert tokenization is None

    @parametrize
    async def test_raw_response_resend_activation_code(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenizations.with_raw_response.resend_activation_code(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert tokenization is None

    @parametrize
    async def test_streaming_response_resend_activation_code(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenizations.with_streaming_response.resend_activation_code(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = await response.parse()
            assert tokenization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_resend_activation_code(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            await async_client.tokenizations.with_raw_response.resend_activation_code(
                tokenization_token="",
            )

    @parametrize
    async def test_method_simulate(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
        )
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

    @parametrize
    async def test_method_simulate_with_all_params(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
            account_score=5,
            device_score=5,
            entity="entity",
            wallet_recommended_decision="APPROVED",
        )
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

    @parametrize
    async def test_raw_response_simulate(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenizations.with_raw_response.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

    @parametrize
    async def test_streaming_response_simulate(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenizations.with_streaming_response.simulate(
            cvv="776",
            expiration_date="08/29",
            pan="4111111289144142",
            tokenization_source="APPLE_PAY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = await response.parse()
            assert_matches_type(TokenizationSimulateResponse, tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unpause(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.unpause(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert tokenization is None

    @parametrize
    async def test_raw_response_unpause(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenizations.with_raw_response.unpause(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert tokenization is None

    @parametrize
    async def test_streaming_response_unpause(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenizations.with_streaming_response.unpause(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = await response.parse()
            assert tokenization is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_unpause(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            await async_client.tokenizations.with_raw_response.unpause(
                "",
            )

    @parametrize
    async def test_method_update_digital_card_art(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.update_digital_card_art(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TokenizationUpdateDigitalCardArtResponse, tokenization, path=["response"])

    @parametrize
    async def test_method_update_digital_card_art_with_all_params(self, async_client: AsyncLithic) -> None:
        tokenization = await async_client.tokenizations.update_digital_card_art(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            digital_card_art_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TokenizationUpdateDigitalCardArtResponse, tokenization, path=["response"])

    @parametrize
    async def test_raw_response_update_digital_card_art(self, async_client: AsyncLithic) -> None:
        response = await async_client.tokenizations.with_raw_response.update_digital_card_art(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tokenization = response.parse()
        assert_matches_type(TokenizationUpdateDigitalCardArtResponse, tokenization, path=["response"])

    @parametrize
    async def test_streaming_response_update_digital_card_art(self, async_client: AsyncLithic) -> None:
        async with async_client.tokenizations.with_streaming_response.update_digital_card_art(
            tokenization_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tokenization = await response.parse()
            assert_matches_type(TokenizationUpdateDigitalCardArtResponse, tokenization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_digital_card_art(self, async_client: AsyncLithic) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tokenization_token` but received ''"):
            await async_client.tokenizations.with_raw_response.update_digital_card_art(
                tokenization_token="",
            )
