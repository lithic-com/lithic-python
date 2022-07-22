# File generated from our OpenAPI spec by Stainless.
from __future__ import annotations

import os

import pytest

from lithic import Lithic, AsyncLithic
from lithic.types.auth_stream_enrollment import *

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAuthStreamEnrollment:
    client = Lithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    def test_method_retrieve(self) -> None:
        resource = self.client.auth_stream_enrollment.retrieve()
        assert isinstance(resource, AuthStreamEnrollment)

    def test_method_disenroll(self) -> None:
        resource = self.client.auth_stream_enrollment.disenroll()
        assert resource is None

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    def test_method_enroll(self) -> None:
        resource = self.client.auth_stream_enrollment.enroll()
        assert resource is None

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    def test_method_enroll_with_optional_params(self) -> None:
        resource = self.client.auth_stream_enrollment.enroll(
            {"webhook_url": "https://example.com"},
        )
        assert resource is None


class TestAsyncAuthStreamEnrollment:
    client = AsyncLithic(base_url=base_url, api_key=api_key, _strict_response_validation=True)

    async def test_method_retrieve(self) -> None:
        resource = await self.client.auth_stream_enrollment.retrieve()
        assert isinstance(resource, AuthStreamEnrollment)

    async def test_method_disenroll(self) -> None:
        resource = await self.client.auth_stream_enrollment.disenroll()
        assert resource is None

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    async def test_method_enroll(self) -> None:
        resource = await self.client.auth_stream_enrollment.enroll()
        assert resource is None

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    async def test_method_enroll_with_optional_params(self) -> None:
        resource = await self.client.auth_stream_enrollment.enroll(
            {"webhook_url": "https://example.com"},
        )
        assert resource is None
