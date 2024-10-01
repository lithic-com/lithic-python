# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import (
    ExternalPayment,
)
from lithic._utils import parse_date, parse_datetime
from lithic.pagination import SyncCursorPage, AsyncCursorPage

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExternalPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Lithic) -> None:
        external_payment = client.external_payments.create(
            amount=0,
            category="EXTERNAL_WIRE",
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="DEPOSIT",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Lithic) -> None:
        external_payment = client.external_payments.create(
            amount=0,
            category="EXTERNAL_WIRE",
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="DEPOSIT",
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            memo="memo",
            progress_to="SETTLED",
            user_defined_id="user_defined_id",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Lithic) -> None:
        response = client.external_payments.with_raw_response.create(
            amount=0,
            category="EXTERNAL_WIRE",
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="DEPOSIT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Lithic) -> None:
        with client.external_payments.with_streaming_response.create(
            amount=0,
            category="EXTERNAL_WIRE",
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="DEPOSIT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = response.parse()
            assert_matches_type(ExternalPayment, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        external_payment = client.external_payments.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.external_payments.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Lithic) -> None:
        with client.external_payments.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = response.parse()
            assert_matches_type(ExternalPayment, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_payment_token` but received ''"
        ):
            client.external_payments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Lithic) -> None:
        external_payment = client.external_payments.list()
        assert_matches_type(SyncCursorPage[ExternalPayment], external_payment, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Lithic) -> None:
        external_payment = client.external_payments.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            business_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category="EXTERNAL_WIRE",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            result="APPROVED",
            starting_after="starting_after",
            status="PENDING",
        )
        assert_matches_type(SyncCursorPage[ExternalPayment], external_payment, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Lithic) -> None:
        response = client.external_payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(SyncCursorPage[ExternalPayment], external_payment, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Lithic) -> None:
        with client.external_payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = response.parse()
            assert_matches_type(SyncCursorPage[ExternalPayment], external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: Lithic) -> None:
        external_payment = client.external_payments.cancel(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_method_cancel_with_all_params(self, client: Lithic) -> None:
        external_payment = client.external_payments.cancel(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
            memo="memo",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_raw_response_cancel(self, client: Lithic) -> None:
        response = client.external_payments.with_raw_response.cancel(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_streaming_response_cancel(self, client: Lithic) -> None:
        with client.external_payments.with_streaming_response.cancel(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = response.parse()
            assert_matches_type(ExternalPayment, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_payment_token` but received ''"
        ):
            client.external_payments.with_raw_response.cancel(
                external_payment_token="",
                effective_date=parse_date("2019-12-27"),
            )

    @parametrize
    def test_method_release(self, client: Lithic) -> None:
        external_payment = client.external_payments.release(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_method_release_with_all_params(self, client: Lithic) -> None:
        external_payment = client.external_payments.release(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
            memo="memo",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_raw_response_release(self, client: Lithic) -> None:
        response = client.external_payments.with_raw_response.release(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_streaming_response_release(self, client: Lithic) -> None:
        with client.external_payments.with_streaming_response.release(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = response.parse()
            assert_matches_type(ExternalPayment, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_release(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_payment_token` but received ''"
        ):
            client.external_payments.with_raw_response.release(
                external_payment_token="",
                effective_date=parse_date("2019-12-27"),
            )

    @parametrize
    def test_method_reverse(self, client: Lithic) -> None:
        external_payment = client.external_payments.reverse(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_method_reverse_with_all_params(self, client: Lithic) -> None:
        external_payment = client.external_payments.reverse(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
            memo="memo",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_raw_response_reverse(self, client: Lithic) -> None:
        response = client.external_payments.with_raw_response.reverse(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_streaming_response_reverse(self, client: Lithic) -> None:
        with client.external_payments.with_streaming_response.reverse(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = response.parse()
            assert_matches_type(ExternalPayment, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_reverse(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_payment_token` but received ''"
        ):
            client.external_payments.with_raw_response.reverse(
                external_payment_token="",
                effective_date=parse_date("2019-12-27"),
            )

    @parametrize
    def test_method_settle(self, client: Lithic) -> None:
        external_payment = client.external_payments.settle(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_method_settle_with_all_params(self, client: Lithic) -> None:
        external_payment = client.external_payments.settle(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
            memo="memo",
            progress_to="SETTLED",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_raw_response_settle(self, client: Lithic) -> None:
        response = client.external_payments.with_raw_response.settle(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    def test_streaming_response_settle(self, client: Lithic) -> None:
        with client.external_payments.with_streaming_response.settle(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = response.parse()
            assert_matches_type(ExternalPayment, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_settle(self, client: Lithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_payment_token` but received ''"
        ):
            client.external_payments.with_raw_response.settle(
                external_payment_token="",
                effective_date=parse_date("2019-12-27"),
            )


class TestAsyncExternalPayments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLithic) -> None:
        external_payment = await async_client.external_payments.create(
            amount=0,
            category="EXTERNAL_WIRE",
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="DEPOSIT",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLithic) -> None:
        external_payment = await async_client.external_payments.create(
            amount=0,
            category="EXTERNAL_WIRE",
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="DEPOSIT",
            token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            memo="memo",
            progress_to="SETTLED",
            user_defined_id="user_defined_id",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_payments.with_raw_response.create(
            amount=0,
            category="EXTERNAL_WIRE",
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="DEPOSIT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLithic) -> None:
        async with async_client.external_payments.with_streaming_response.create(
            amount=0,
            category="EXTERNAL_WIRE",
            effective_date=parse_date("2019-12-27"),
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            payment_type="DEPOSIT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = await response.parse()
            assert_matches_type(ExternalPayment, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLithic) -> None:
        external_payment = await async_client.external_payments.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_payments.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLithic) -> None:
        async with async_client.external_payments.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = await response.parse()
            assert_matches_type(ExternalPayment, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_payment_token` but received ''"
        ):
            await async_client.external_payments.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncLithic) -> None:
        external_payment = await async_client.external_payments.list()
        assert_matches_type(AsyncCursorPage[ExternalPayment], external_payment, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLithic) -> None:
        external_payment = await async_client.external_payments.list(
            begin=parse_datetime("2019-12-27T18:11:19.117Z"),
            business_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            category="EXTERNAL_WIRE",
            end=parse_datetime("2019-12-27T18:11:19.117Z"),
            ending_before="ending_before",
            financial_account_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=1,
            result="APPROVED",
            starting_after="starting_after",
            status="PENDING",
        )
        assert_matches_type(AsyncCursorPage[ExternalPayment], external_payment, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_payments.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(AsyncCursorPage[ExternalPayment], external_payment, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLithic) -> None:
        async with async_client.external_payments.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = await response.parse()
            assert_matches_type(AsyncCursorPage[ExternalPayment], external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncLithic) -> None:
        external_payment = await async_client.external_payments.cancel(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncLithic) -> None:
        external_payment = await async_client.external_payments.cancel(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
            memo="memo",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_payments.with_raw_response.cancel(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncLithic) -> None:
        async with async_client.external_payments.with_streaming_response.cancel(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = await response.parse()
            assert_matches_type(ExternalPayment, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_payment_token` but received ''"
        ):
            await async_client.external_payments.with_raw_response.cancel(
                external_payment_token="",
                effective_date=parse_date("2019-12-27"),
            )

    @parametrize
    async def test_method_release(self, async_client: AsyncLithic) -> None:
        external_payment = await async_client.external_payments.release(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_method_release_with_all_params(self, async_client: AsyncLithic) -> None:
        external_payment = await async_client.external_payments.release(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
            memo="memo",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_raw_response_release(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_payments.with_raw_response.release(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_streaming_response_release(self, async_client: AsyncLithic) -> None:
        async with async_client.external_payments.with_streaming_response.release(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = await response.parse()
            assert_matches_type(ExternalPayment, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_release(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_payment_token` but received ''"
        ):
            await async_client.external_payments.with_raw_response.release(
                external_payment_token="",
                effective_date=parse_date("2019-12-27"),
            )

    @parametrize
    async def test_method_reverse(self, async_client: AsyncLithic) -> None:
        external_payment = await async_client.external_payments.reverse(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_method_reverse_with_all_params(self, async_client: AsyncLithic) -> None:
        external_payment = await async_client.external_payments.reverse(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
            memo="memo",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_raw_response_reverse(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_payments.with_raw_response.reverse(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_streaming_response_reverse(self, async_client: AsyncLithic) -> None:
        async with async_client.external_payments.with_streaming_response.reverse(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = await response.parse()
            assert_matches_type(ExternalPayment, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_reverse(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_payment_token` but received ''"
        ):
            await async_client.external_payments.with_raw_response.reverse(
                external_payment_token="",
                effective_date=parse_date("2019-12-27"),
            )

    @parametrize
    async def test_method_settle(self, async_client: AsyncLithic) -> None:
        external_payment = await async_client.external_payments.settle(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_method_settle_with_all_params(self, async_client: AsyncLithic) -> None:
        external_payment = await async_client.external_payments.settle(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
            memo="memo",
            progress_to="SETTLED",
        )
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_raw_response_settle(self, async_client: AsyncLithic) -> None:
        response = await async_client.external_payments.with_raw_response.settle(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        external_payment = response.parse()
        assert_matches_type(ExternalPayment, external_payment, path=["response"])

    @parametrize
    async def test_streaming_response_settle(self, async_client: AsyncLithic) -> None:
        async with async_client.external_payments.with_streaming_response.settle(
            external_payment_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            effective_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            external_payment = await response.parse()
            assert_matches_type(ExternalPayment, external_payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_settle(self, async_client: AsyncLithic) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `external_payment_token` but received ''"
        ):
            await async_client.external_payments.with_raw_response.settle(
                external_payment_token="",
                effective_date=parse_date("2019-12-27"),
            )
