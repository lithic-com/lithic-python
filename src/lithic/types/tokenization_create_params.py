# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TokenizationCreateParams"]


class TokenizationCreateParams(TypedDict, total=False):
    agent_token: Required[str]
    """Globally unique identifier for the active agent configured for your program"""

    type: Required[Literal["AGENT"]]
    """Type of tokenization to create"""
