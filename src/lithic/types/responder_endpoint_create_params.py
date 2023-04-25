# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ResponderEndpointCreateParams"]


class ResponderEndpointCreateParams(TypedDict, total=False):
    type: Literal["TOKENIZATION_DECISIONING"]
    """The type of the endpoint."""

    url: str
    """The URL for the responder endpoint (must be http(s))."""
