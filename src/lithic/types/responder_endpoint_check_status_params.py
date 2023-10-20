# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResponderEndpointCheckStatusParams"]


class ResponderEndpointCheckStatusParams(TypedDict, total=False):
    type: Required[Literal["AUTH_STREAM_ACCESS", "TOKENIZATION_DECISIONING", "THREE_DS_DECISIONING"]]
    """The type of the endpoint."""
