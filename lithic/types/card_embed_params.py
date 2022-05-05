# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import Optional, Union, List
from typing_extensions import Literal, TypedDict, Required
from ..types import shared_params

__all__ = ["CardEmbedParams"]


class CardEmbedParams(TypedDict, total=False):
    embed_request: str
    """A base64 encoded JSON string of an EmbedRequest to specify which card to load."""

    hmac: str
    """SHA2 HMAC of the embed_request JSON string with base64 digest."""
