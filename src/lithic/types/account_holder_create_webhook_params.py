# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountHolderCreateWebhookParams"]


class AccountHolderCreateWebhookParams(TypedDict, total=False):
    url: Required[str]
    """URL to receive webhook requests. Must be a valid HTTPS address."""
