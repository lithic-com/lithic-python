# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from tests.utils import assert_matches_type
from lithic.types import AuthStreamSecret, AuthStreamEnrollment
from lithic._client import Lithic, AsyncLithic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")
api_key = "My Lithic API Key"


class TestAuthStreamEnrollment:
    strict_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Lithic) -> None:
        auth_stream_enrollment = client.auth_stream_enrollment.retrieve()
        assert_matches_type(AuthStreamEnrollment, auth_stream_enrollment, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Lithic) -> None:
        response = client.auth_stream_enrollment.with_raw_response.retrieve()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert_matches_type(AuthStreamEnrollment, auth_stream_enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_method_disenroll(self, client: Lithic) -> None:
        auth_stream_enrollment = client.auth_stream_enrollment.disenroll()
        assert auth_stream_enrollment is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_raw_response_disenroll(self, client: Lithic) -> None:
        response = client.auth_stream_enrollment.with_raw_response.disenroll()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert auth_stream_enrollment is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_method_enroll(self, client: Lithic) -> None:
        auth_stream_enrollment = client.auth_stream_enrollment.enroll()
        assert auth_stream_enrollment is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_method_enroll_with_all_params(self, client: Lithic) -> None:
        auth_stream_enrollment = client.auth_stream_enrollment.enroll(
            webhook_url="https://example.com",
        )
        assert auth_stream_enrollment is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    def test_raw_response_enroll(self, client: Lithic) -> None:
        response = client.auth_stream_enrollment.with_raw_response.enroll()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert auth_stream_enrollment is None

    @parametrize
    def test_method_retrieve_secret(self, client: Lithic) -> None:
        auth_stream_enrollment = client.auth_stream_enrollment.retrieve_secret()
        assert_matches_type(AuthStreamSecret, auth_stream_enrollment, path=["response"])

    @parametrize
    def test_raw_response_retrieve_secret(self, client: Lithic) -> None:
        response = client.auth_stream_enrollment.with_raw_response.retrieve_secret()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert_matches_type(AuthStreamSecret, auth_stream_enrollment, path=["response"])

    @parametrize
    def test_method_rotate_secret(self, client: Lithic) -> None:
        auth_stream_enrollment = client.auth_stream_enrollment.rotate_secret()
        assert auth_stream_enrollment is None

    @parametrize
    def test_raw_response_rotate_secret(self, client: Lithic) -> None:
        response = client.auth_stream_enrollment.with_raw_response.rotate_secret()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert auth_stream_enrollment is None


class TestAsyncAuthStreamEnrollment:
    strict_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncLithic) -> None:
        auth_stream_enrollment = await client.auth_stream_enrollment.retrieve()
        assert_matches_type(AuthStreamEnrollment, auth_stream_enrollment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, client: AsyncLithic) -> None:
        response = await client.auth_stream_enrollment.with_raw_response.retrieve()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert_matches_type(AuthStreamEnrollment, auth_stream_enrollment, path=["response"])

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_disenroll(self, client: AsyncLithic) -> None:
        auth_stream_enrollment = await client.auth_stream_enrollment.disenroll()
        assert auth_stream_enrollment is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_raw_response_disenroll(self, client: AsyncLithic) -> None:
        response = await client.auth_stream_enrollment.with_raw_response.disenroll()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert auth_stream_enrollment is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_enroll(self, client: AsyncLithic) -> None:
        auth_stream_enrollment = await client.auth_stream_enrollment.enroll()
        assert auth_stream_enrollment is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_method_enroll_with_all_params(self, client: AsyncLithic) -> None:
        auth_stream_enrollment = await client.auth_stream_enrollment.enroll(
            webhook_url="https://example.com",
        )
        assert auth_stream_enrollment is None

    @pytest.mark.skip(reason="Prism Mock server doesnt want Accept header, but server requires it.")
    @parametrize
    async def test_raw_response_enroll(self, client: AsyncLithic) -> None:
        response = await client.auth_stream_enrollment.with_raw_response.enroll()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert auth_stream_enrollment is None

    @parametrize
    async def test_method_retrieve_secret(self, client: AsyncLithic) -> None:
        auth_stream_enrollment = await client.auth_stream_enrollment.retrieve_secret()
        assert_matches_type(AuthStreamSecret, auth_stream_enrollment, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_secret(self, client: AsyncLithic) -> None:
        response = await client.auth_stream_enrollment.with_raw_response.retrieve_secret()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert_matches_type(AuthStreamSecret, auth_stream_enrollment, path=["response"])

    @parametrize
    async def test_method_rotate_secret(self, client: AsyncLithic) -> None:
        auth_stream_enrollment = await client.auth_stream_enrollment.rotate_secret()
        assert auth_stream_enrollment is None

    @parametrize
    async def test_raw_response_rotate_secret(self, client: AsyncLithic) -> None:
        response = await client.auth_stream_enrollment.with_raw_response.rotate_secret()
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth_stream_enrollment = response.parse()
        assert auth_stream_enrollment is None
