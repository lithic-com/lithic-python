# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
from typing import Mapping, cast

from .._types import (
    HeadersLike,
)
from .._utils import (
    get_required_header,
)
from .._models import construct_type
from .._resource import SyncAPIResource, AsyncAPIResource
from .._exceptions import LithicError
from ..types.parsed_webhook_event import ParsedWebhookEvent

__all__ = ["Webhooks", "AsyncWebhooks"]


class Webhooks(SyncAPIResource):
    def unwrap(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> object:
        """Validates that the given payload was sent by Lithic and parses the payload."""
        self.verify_signature(payload=payload, headers=headers, secret=secret)
        return json.loads(payload)

    def verify_signature(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> None:
        """Verifies that the given payload was sent by Lithic."""
        try:
            from standardwebhooks import Webhook
        except ImportError as exc:
            raise LithicError("You need to install `lithic[webhooks]` to use this method") from exc

        if secret is None:
            secret = self._client.webhook_secret
            if secret is None:
                raise ValueError(
                    "Cannot verify a webhook without a secret on either the client's webhook_secret or passed in as an argument"
                )

        headers = {
            "webhook-id": get_required_header(headers, "webhook-id"),
            "webhook-timestamp": get_required_header(headers, "webhook-timestamp"),
            "webhook-signature": get_required_header(headers, "webhook-signature"),
        }
        Webhook(secret).verify(payload, headers)

    def parse(
        self,
        payload: str,
        *,
        headers: Mapping[str, str],
        secret: str | bytes | None = None,
    ) -> ParsedWebhookEvent:
        secret = secret.decode("utf-8") if isinstance(secret, bytes) else secret
        self.verify_signature(payload=payload, headers=headers, secret=secret)
        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )

    def parse_unsafe(self, payload: str) -> ParsedWebhookEvent:
        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )


class AsyncWebhooks(AsyncAPIResource):
    def unwrap(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> object:
        """Validates that the given payload was sent by Lithic and parses the payload."""
        self.verify_signature(payload=payload, headers=headers, secret=secret)
        return json.loads(payload)

    def verify_signature(
        self,
        payload: str | bytes,
        headers: HeadersLike,
        *,
        secret: str | None = None,
    ) -> None:
        """Verifies that the given payload was sent by Lithic."""
        try:
            from standardwebhooks import Webhook
        except ImportError as exc:
            raise LithicError("You need to install `lithic[webhooks]` to use this method") from exc

        if secret is None:
            secret = self._client.webhook_secret
            if secret is None:
                raise ValueError(
                    "Cannot verify a webhook without a secret on either the client's webhook_secret or passed in as an argument"
                )

        headers = {
            "webhook-id": get_required_header(headers, "webhook-id"),
            "webhook-timestamp": get_required_header(headers, "webhook-timestamp"),
            "webhook-signature": get_required_header(headers, "webhook-signature"),
        }
        Webhook(secret).verify(payload, headers)

    def parse(
        self,
        payload: str,
        *,
        headers: Mapping[str, str],
        secret: str | bytes | None = None,
    ) -> ParsedWebhookEvent:
        secret = secret.decode("utf-8") if isinstance(secret, bytes) else secret
        self.verify_signature(payload=payload, headers=headers, secret=secret)
        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )

    def parse_unsafe(self, payload: str) -> ParsedWebhookEvent:
        return cast(
            ParsedWebhookEvent,
            construct_type(
                type_=ParsedWebhookEvent,
                value=json.loads(payload),
            ),
        )
