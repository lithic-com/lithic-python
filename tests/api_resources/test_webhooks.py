<<<<<<< HEAD
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
||||||| parent of 49e654d (feat(api): add webhook schemas to SDKs - add parse and parse_unsafe)
=======
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from datetime import datetime, timezone

import pytest
import standardwebhooks

from lithic import Lithic

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    def test_method_parsed(self, client: Lithic) -> None:
        key = b"secret"
        hook = standardwebhooks.Webhook(key)

        data = """{"event_type":"account_holder.created","token":"00000000-0000-0000-0000-000000000001","account_token":"00000000-0000-0000-0000-000000000001","created":"2019-12-27T18:11:19.117Z","required_documents":[{"entity_token":"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e","status_reasons":["string"],"valid_documents":["string"]}],"status":"ACCEPTED","status_reason":["string"]}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.parsed(data, headers=headers, key=key)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.parsed(data, headers=bad_header, key=key)


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    def test_method_parsed(self, client: Lithic) -> None:
        key = b"secret"
        hook = standardwebhooks.Webhook(key)

        data = """{"event_type":"account_holder.created","token":"00000000-0000-0000-0000-000000000001","account_token":"00000000-0000-0000-0000-000000000001","created":"2019-12-27T18:11:19.117Z","required_documents":[{"entity_token":"182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e","status_reasons":["string"],"valid_documents":["string"]}],"status":"ACCEPTED","status_reason":["string"]}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.parsed(data, headers=headers, key=key)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.parsed(data, headers=bad_header, key=key)
>>>>>>> 49e654d (feat(api): add webhook schemas to SDKs - add parse and parse_unsafe)
