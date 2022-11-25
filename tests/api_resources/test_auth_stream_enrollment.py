# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from lithic.types.auth_stream_enrollment import AuthStreamEnrollment

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAuthStreamEnrollment:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        resource = client.auth_stream_enrollment.retrieve()
        assert isinstance(resource, AuthStreamEnrollment)

    @parametrize
    def test_method_disenroll(self, client: Lithic) -> None:
        resource = client.auth_stream_enrollment.disenroll()
        assert resource is None

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_enroll(self, client: Lithic) -> None:
        resource = client.auth_stream_enrollment.enroll()
        assert resource is None

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_enroll_with_all_params(self, client: Lithic) -> None:
        resource = client.auth_stream_enrollment.enroll(
            webhook_url="https://example.com",
        )
        assert resource is None


class TestAsyncAuthStreamEnrollment:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        resource = await client.auth_stream_enrollment.retrieve()
        assert isinstance(resource, AuthStreamEnrollment)

    @parametrize
    async def test_method_disenroll(self, client: AsyncLithic) -> None:
        resource = await client.auth_stream_enrollment.disenroll()
        assert resource is None

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_enroll(self, client: AsyncLithic) -> None:
        resource = await client.auth_stream_enrollment.enroll()
        assert resource is None

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_enroll_with_all_params(self, client: AsyncLithic) -> None:
        resource = await client.auth_stream_enrollment.enroll(
            webhook_url="https://example.com",
        )
        assert resource is None
