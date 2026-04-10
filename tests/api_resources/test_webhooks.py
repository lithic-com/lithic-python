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

    @pytest.mark.parametrize(
        "client_opt,method_opt",
        [
            ("whsec_c2VjcmV0Cg==", None),
            ("wrong", b"secret\n"),
            ("wrong", "whsec_c2VjcmV0Cg=="),
            (None, b"secret\n"),
            (None, "whsec_c2VjcmV0Cg=="),
        ],
    )
    def test_method_parsed(self, client: Lithic, client_opt: str | None, method_opt: str | bytes | None) -> None:
        hook = standardwebhooks.Webhook(b"secret\n")

        client = client.with_options(webhook_secret=client_opt)

        data = """{"account_token":"00000000-0000-0000-0000-000000000002","card_token":"00000000-0000-0000-0000-000000000001","created":"2023-09-18T12:34:56Z","digital_wallet_token_metadata":{"payment_account_info":{"account_holder_data":{"phone_number":"+15555555555"},"pan_unique_reference":"pan_unique_ref_1234567890123456789012345678","payment_account_reference":"ref_1234567890123456789012","token_unique_reference":"token_unique_ref_1234567890123456789012345678"},"status":"Pending","payment_app_instance_id":"app_instance_123456789012345678901234567890","token_requestor_id":"12345678901","token_requestor_name":"APPLE_PAY"},"event_type":"digital_wallet.tokenization_approval_request","issuer_decision":"APPROVED","tokenization_channel":"DIGITAL_WALLET","tokenization_token":"tok_1234567890abcdef","wallet_decisioning_info":{"account_score":"100","device_score":"100","recommended_decision":"Decision1","recommendation_reasons":["Reason1"]},"customer_tokenization_decision":{"outcome":"APPROVED","responder_url":"https://example.com","latency":"100","response_code":"123456"},"device":{"imei":"123456789012345","ip_address":"1.1.1.1","location":"37.3860517/-122.0838511"},"rule_results":[{"auth_rule_token":"550e8400-e29b-41d4-a716-446655440003","explanation":"Account risk too high","name":"CustomerAccountRule","result":"DECLINED"}],"tokenization_decline_reasons":["ACCOUNT_SCORE_1"],"tokenization_source":"PUSH_PROVISION","tokenization_tfa_reasons":["WALLET_RECOMMENDED_TFA"]}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.parsed(data, headers=headers, key=method_opt)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.parsed(data, headers=bad_header, key=method_opt)


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.parametrize(
        "client_opt,method_opt",
        [
            ("whsec_c2VjcmV0Cg==", None),
            ("wrong", b"secret\n"),
            ("wrong", "whsec_c2VjcmV0Cg=="),
            (None, b"secret\n"),
            (None, "whsec_c2VjcmV0Cg=="),
        ],
    )
    def test_method_parsed(self, async_client: Lithic, client_opt: str | None, method_opt: str | bytes | None) -> None:
        hook = standardwebhooks.Webhook(b"secret\n")

        async_client = async_client.with_options(webhook_secret=client_opt)

        data = """{"account_token":"00000000-0000-0000-0000-000000000002","card_token":"00000000-0000-0000-0000-000000000001","created":"2023-09-18T12:34:56Z","digital_wallet_token_metadata":{"payment_account_info":{"account_holder_data":{"phone_number":"+15555555555"},"pan_unique_reference":"pan_unique_ref_1234567890123456789012345678","payment_account_reference":"ref_1234567890123456789012","token_unique_reference":"token_unique_ref_1234567890123456789012345678"},"status":"Pending","payment_app_instance_id":"app_instance_123456789012345678901234567890","token_requestor_id":"12345678901","token_requestor_name":"APPLE_PAY"},"event_type":"digital_wallet.tokenization_approval_request","issuer_decision":"APPROVED","tokenization_channel":"DIGITAL_WALLET","tokenization_token":"tok_1234567890abcdef","wallet_decisioning_info":{"account_score":"100","device_score":"100","recommended_decision":"Decision1","recommendation_reasons":["Reason1"]},"customer_tokenization_decision":{"outcome":"APPROVED","responder_url":"https://example.com","latency":"100","response_code":"123456"},"device":{"imei":"123456789012345","ip_address":"1.1.1.1","location":"37.3860517/-122.0838511"},"rule_results":[{"auth_rule_token":"550e8400-e29b-41d4-a716-446655440003","explanation":"Account risk too high","name":"CustomerAccountRule","result":"DECLINED"}],"tokenization_decline_reasons":["ACCOUNT_SCORE_1"],"tokenization_source":"PUSH_PROVISION","tokenization_tfa_reasons":["WALLET_RECOMMENDED_TFA"]}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = async_client.webhooks.parsed(data, headers=headers, key=method_opt)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = async_client.webhooks.parsed(data, headers=bad_header, key=method_opt)
