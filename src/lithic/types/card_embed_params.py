# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CardEmbedParams"]


class CardEmbedParams(TypedDict, total=False):
    embed_request: Required[str]
    """A base64 encoded JSON string of an EmbedRequest to specify which card to load."""

    hmac: Required[str]
    """SHA256 HMAC of the embed_request JSON string with base64 digest."""
