# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ResponderEndpointDeleteParams"]


class ResponderEndpointDeleteParams(TypedDict, total=False):
    type: Required[Literal["TOKENIZATION_DECISIONING"]]
    """The type of the endpoint."""
