# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResponderEndpointDeleteParams"]


class ResponderEndpointDeleteParams(TypedDict, total=False):
    type: Required[Literal["AUTH_STREAM_ACCESS", "THREE_DS_DECISIONING", "TOKENIZATION_DECISIONING"]]
    """The type of the endpoint."""
