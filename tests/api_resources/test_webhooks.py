# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import Any, cast
from datetime import datetime, timezone, timedelta

import pytest
import time_machine
import standardwebhooks

from lithic import Lithic, AsyncLithic
from lithic.types import AccountHolderCreatedWebhookEvent

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

        with pytest.raises(standardwebhooks.WebhookVerificationError, match="timestamp too old"):
            with time_machine.travel(self.fake_now + timedelta(minutes=6)):
                verify(payload=payload, headers=headers, secret=secret)

        with pytest.raises(standardwebhooks.WebhookVerificationError, match="timestamp too new"):
            with time_machine.travel(self.fake_now - timedelta(minutes=6)):
                verify(payload=payload, headers=headers, secret=secret)

        # wrong secret
        wrong_secret = f"whsec_{base64.b64encode(b'wrong').decode('utf-8')}"
        with pytest.raises(standardwebhooks.WebhookVerificationError, match=r"No matching signature"):
            verify(payload=payload, headers=headers, secret=wrong_secret)

        invalid_signature_message = "No matching signature found"
        with pytest.raises(standardwebhooks.WebhookVerificationError, match=invalid_signature_message):
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
                headers={
                    **headers,
                    "webhook-signature": f"v1,{invalid_signature} v1,{signature}",
                },
                secret=secret,
            )
            is None
        )

        # different signature version
        with pytest.raises(standardwebhooks.WebhookVerificationError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "webhook-signature": f"v2,{signature}"},
                secret=secret,
            )

        assert (
            verify(
                payload=payload,
                headers={
                    **headers,
                    "webhook-signature": f"v2,{signature} v1,{signature}",
                },
                secret=secret,
            )
            is None
        )

        # missing version - this throws ValueError not WebhookVerificationError
        with pytest.raises(ValueError, match=r"not enough values to unpack"):
            verify(
                payload=payload,
                headers={**headers, "webhook-signature": signature},
                secret=secret,
            )

        # non-string payload - this throws AttributeError not WebhookVerificationError
        with pytest.raises(AttributeError, match=r"no attribute 'decode'"):
            verify(
                payload=cast(Any, {"payload": payload}),
                headers=headers,
                secret=secret,
            )

    @time_machine.travel(fake_now)
    def test_parse(self, client: Lithic) -> None:
        valid_payload = """{"event_type":"account_holder.created","token":"00000000-0000-0000-0000-000000000001","account_token":"00000000-0000-0000-0000-000000000001","created":"2019-12-27T18:11:19.117Z","status":"ACCEPTED"}"""
        secret = self.secret

        # Generate valid webhook signature for the payload
        hook = standardwebhooks.Webhook(secret)
        msg_id = "msg_test123"
        timestamp = self.fake_now
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=valid_payload)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        result = client.webhooks.parse(valid_payload, headers=headers, secret=secret)
        assert result is not None

        # Test type narrowing with isinstance
        assert isinstance(result, AccountHolderCreatedWebhookEvent)
        assert result.event_type == "account_holder.created"
        assert result.token == "00000000-0000-0000-0000-000000000001"
        assert result.account_token == "00000000-0000-0000-0000-000000000001"
        assert result.status == "ACCEPTED"

        # test with bytes secret
        result_bytes = client.webhooks.parse(valid_payload, headers=headers, secret=secret.encode("utf-8"))
        assert result_bytes is not None

        # test that parse verifies signature - use wrong secret with proper format
        wrong_secret = f"whsec_{base64.b64encode(b'wrong').decode('utf-8')}"
        with pytest.raises(standardwebhooks.WebhookVerificationError):
            client.webhooks.parse(valid_payload, headers=headers, secret=wrong_secret)

    def test_parse_unsafe(self, client: Lithic) -> None:
        valid_payload = """{"event_type":"account_holder.created","token":"00000000-0000-0000-0000-000000000001","account_token":"00000000-0000-0000-0000-000000000001","created":"2019-12-27T18:11:19.117Z","status":"ACCEPTED"}"""

        result = client.webhooks.parse_unsafe(valid_payload)
        assert result is not None

        # Test type narrowing with isinstance
        assert isinstance(result, AccountHolderCreatedWebhookEvent)
        assert result.event_type == "account_holder.created"
        assert result.token == "00000000-0000-0000-0000-000000000001"


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
    def test_verify_signature(self, async_client: AsyncLithic) -> None:
        payload = self.payload
        headers = self.headers
        secret = self.secret
        signature = self.signature
        verify = async_client.webhooks.verify_signature

        assert verify(payload=payload, headers=headers, secret=secret) is None

        with pytest.raises(standardwebhooks.WebhookVerificationError, match="timestamp too old"):
            with time_machine.travel(self.fake_now + timedelta(minutes=6)):
                verify(payload=payload, headers=headers, secret=secret)

        with pytest.raises(standardwebhooks.WebhookVerificationError, match="timestamp too new"):
            with time_machine.travel(self.fake_now - timedelta(minutes=6)):
                verify(payload=payload, headers=headers, secret=secret)

        # wrong secret
        wrong_secret = f"whsec_{base64.b64encode(b'wrong').decode('utf-8')}"
        with pytest.raises(standardwebhooks.WebhookVerificationError, match=r"No matching signature"):
            verify(payload=payload, headers=headers, secret=wrong_secret)

        invalid_signature_message = "No matching signature found"
        with pytest.raises(standardwebhooks.WebhookVerificationError, match=invalid_signature_message):
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
                headers={
                    **headers,
                    "webhook-signature": f"v1,{invalid_signature} v1,{signature}",
                },
                secret=secret,
            )
            is None
        )

        # different signature version
        with pytest.raises(standardwebhooks.WebhookVerificationError, match=invalid_signature_message):
            verify(
                payload=payload,
                headers={**headers, "webhook-signature": f"v2,{signature}"},
                secret=secret,
            )

        assert (
            verify(
                payload=payload,
                headers={
                    **headers,
                    "webhook-signature": f"v2,{signature} v1,{signature}",
                },
                secret=secret,
            )
            is None
        )

        # missing version - this throws ValueError not WebhookVerificationError
        with pytest.raises(ValueError, match=r"not enough values to unpack"):
            verify(
                payload=payload,
                headers={**headers, "webhook-signature": signature},
                secret=secret,
            )

        # non-string payload - this throws AttributeError not WebhookVerificationError
        with pytest.raises(AttributeError, match=r"no attribute 'decode'"):
            verify(
                payload=cast(Any, {"payload": payload}),
                headers=headers,
                secret=secret,
            )

    @time_machine.travel(fake_now)
    def test_parse(self, async_client: AsyncLithic) -> None:
        valid_payload = """{"event_type":"account_holder.created","token":"00000000-0000-0000-0000-000000000001","account_token":"00000000-0000-0000-0000-000000000001","created":"2019-12-27T18:11:19.117Z","status":"ACCEPTED"}"""
        secret = self.secret

        # Generate valid webhook signature for the payload
        hook = standardwebhooks.Webhook(secret)
        msg_id = "msg_test123"
        timestamp = self.fake_now
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=valid_payload)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        result = async_client.webhooks.parse(valid_payload, headers=headers, secret=secret)
        assert result is not None

        # Test type narrowing with isinstance
        assert isinstance(result, AccountHolderCreatedWebhookEvent)
        assert result.event_type == "account_holder.created"
        assert result.token == "00000000-0000-0000-0000-000000000001"
        assert result.account_token == "00000000-0000-0000-0000-000000000001"
        assert result.status == "ACCEPTED"

        # test with bytes secret
        result_bytes = async_client.webhooks.parse(valid_payload, headers=headers, secret=secret.encode("utf-8"))
        assert result_bytes is not None

        # test that parse verifies signature - use wrong secret with proper format
        wrong_secret = f"whsec_{base64.b64encode(b'wrong').decode('utf-8')}"
        with pytest.raises(standardwebhooks.WebhookVerificationError):
            async_client.webhooks.parse(valid_payload, headers=headers, secret=wrong_secret)

    def test_parse_unsafe(self, async_client: AsyncLithic) -> None:
        valid_payload = """{"event_type":"account_holder.created","token":"00000000-0000-0000-0000-000000000001","account_token":"00000000-0000-0000-0000-000000000001","created":"2019-12-27T18:11:19.117Z","status":"ACCEPTED"}"""

        result = async_client.webhooks.parse_unsafe(valid_payload)
        assert result is not None

        # Test type narrowing with isinstance
        assert isinstance(result, AccountHolderCreatedWebhookEvent)
        assert result.event_type == "account_holder.created"
        assert result.token == "00000000-0000-0000-0000-000000000001"
