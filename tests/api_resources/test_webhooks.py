# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
import base64
from typing import Any, cast
from datetime import datetime, timezone, timedelta

import pytest
import time_machine

from lithic import Lithic, AsyncLithic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    timestamp = "1676312382"
    fake_now = datetime.fromtimestamp(float(timestamp), tz=timezone.utc)

    payload = """{"card_token":"sit Lorem ipsum, accusantium repellendus possimus","created_at":"elit. placeat libero architecto molestias, sit","account_token":"elit.","issuer_decision":"magnam, libero esse Lorem ipsum magnam, magnam,","tokenization_attempt_id":"illum dolor repellendus libero esse accusantium","wallet_decisioning_info":{"device_score":"placeat architecto"},"digital_wallet_token_metadata":{"status":"reprehenderit dolor","token_requestor_id":"possimus","payment_account_info":{"account_holder_data":{"phone_number":"libero","email_address":"nobis molestias, veniam culpa! quas elit. quas libero esse architecto placeat"},"pan_unique_reference":"adipisicing odit magnam, odit"}}}"""
    signature = "Dwa0AHInLL3XFo2sxcHamOQDrJNi7F654S3L6skMAOI="
    headers = {
        "webhook-id": "msg_2Lh9KRb0pzN4LePd3XiA4v12Axj",
        "webhook-timestamp": timestamp,
        "webhook-signature": f"v1,{signature}",
    }
    secret = "whsec_zlFsbBZ8Xcodlpcu6NDTdSzZRLSdhkst"

    @time_machine.travel(fake_now)
    def test_unwrap(self, client: Lithic) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret

        client.webhooks.unwrap(payload, headers, secret=secret)

    @time_machine.travel(fake_now)
    def test_verify_signature(self, client: Lithic) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret
        signature = self.signature
        verify = client.webhooks.verify_signature

        assert verify(payload=payload, headers=headers, secret=secret) is None

        with pytest.raises(ValueError, match="Webhook timestamp is too old"):
            with time_machine.travel(self.fake_now + timedelta(minutes=6)):
                assert verify(payload=payload, headers=headers, secret=secret) is False

        with pytest.raises(ValueError, match="Webhook timestamp is too new"):
            with time_machine.travel(self.fake_now - timedelta(minutes=6)):
                assert verify(payload=payload, headers=headers, secret=secret) is False

        # wrong secret
        with pytest.raises(ValueError, match=r"Bad secret"):
            verify(payload=payload, headers=headers, secret="invalid secret")

        invalid_signature_message = "None of the given webhook signatures match the expected signature"
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers=headers,
                secret=f"whsec_{base64.b64encode(b'foo').decode('utf-8')}",
            )

        # multiple signatures
        invalid_signature = base64.b64encode(b"my_sig").decode("utf-8")
        assert (
            verify(
                payload=payload,
                headers={**headers, "webhook-signature": f"v1,{invalid_signature} v1,{signature}"},
                secret=secret,
            )
            is None
        )

        # different signature version
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "webhook-signature": f"v2,{signature}"},
                secret=secret,
            )

        assert (
            verify(
                payload=payload,
                headers={**headers, "webhook-signature": f"v2,{signature} v1,{signature}"},
                secret=secret,
            )
            is None
        )

        # missing version
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "webhook-signature": signature},
                secret=secret,
            )

        # non-string payload
        with pytest.raises(ValueError, match=r"Webhook body should be a string"):
            verify(
                payload=cast(Any, {"payload": payload}),
                headers=headers,
                secret=secret,
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    timestamp = "1676312382"
    fake_now = datetime.fromtimestamp(float(timestamp), tz=timezone.utc)

    payload = """{"card_token":"sit Lorem ipsum, accusantium repellendus possimus","created_at":"elit. placeat libero architecto molestias, sit","account_token":"elit.","issuer_decision":"magnam, libero esse Lorem ipsum magnam, magnam,","tokenization_attempt_id":"illum dolor repellendus libero esse accusantium","wallet_decisioning_info":{"device_score":"placeat architecto"},"digital_wallet_token_metadata":{"status":"reprehenderit dolor","token_requestor_id":"possimus","payment_account_info":{"account_holder_data":{"phone_number":"libero","email_address":"nobis molestias, veniam culpa! quas elit. quas libero esse architecto placeat"},"pan_unique_reference":"adipisicing odit magnam, odit"}}}"""
    signature = "Dwa0AHInLL3XFo2sxcHamOQDrJNi7F654S3L6skMAOI="
    headers = {
        "webhook-id": "msg_2Lh9KRb0pzN4LePd3XiA4v12Axj",
        "webhook-timestamp": timestamp,
        "webhook-signature": f"v1,{signature}",
    }
    secret = "whsec_zlFsbBZ8Xcodlpcu6NDTdSzZRLSdhkst"

    @time_machine.travel(fake_now)
    def test_unwrap(self, async_client: AsyncLithic) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret

        async_client.webhooks.unwrap(payload, headers, secret=secret)

    @time_machine.travel(fake_now)
    def test_verify_signature(self, async_client: Lithic) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret
        signature = self.signature
        verify = async_client.webhooks.verify_signature

        assert verify(payload=payload, headers=headers, secret=secret) is None

        with pytest.raises(ValueError, match="Webhook timestamp is too old"):
            with time_machine.travel(self.fake_now + timedelta(minutes=6)):
                assert verify(payload=payload, headers=headers, secret=secret) is False

        with pytest.raises(ValueError, match="Webhook timestamp is too new"):
            with time_machine.travel(self.fake_now - timedelta(minutes=6)):
                assert verify(payload=payload, headers=headers, secret=secret) is False

        # wrong secret
        with pytest.raises(ValueError, match=r"Bad secret"):
            verify(payload=payload, headers=headers, secret="invalid secret")

        invalid_signature_message = "None of the given webhook signatures match the expected signature"
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers=headers,
                secret=f"whsec_{base64.b64encode(b'foo').decode('utf-8')}",
            )

        # multiple signatures
        invalid_signature = base64.b64encode(b"my_sig").decode("utf-8")
        assert (
            verify(
                payload=payload,
                headers={**headers, "webhook-signature": f"v1,{invalid_signature} v1,{signature}"},
                secret=secret,
            )
            is None
        )

        # different signature version
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "webhook-signature": f"v2,{signature}"},
                secret=secret,
            )

        assert (
            verify(
                payload=payload,
                headers={**headers, "webhook-signature": f"v2,{signature} v1,{signature}"},
                secret=secret,
            )
            is None
        )

        # missing version
        with pytest.raises(ValueError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "webhook-signature": signature},
                secret=secret,
            )

        # non-string payload
        with pytest.raises(ValueError, match=r"Webhook body should be a string"):
            verify(
                payload=cast(Any, {"payload": payload}),
                headers=headers,
                secret=secret,
            )
