# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardAuthorizationChallengeResponseParams"]


class CardAuthorizationChallengeResponseParams(TypedDict, total=False):
    response: Required[Literal["APPROVE", "DECLINE"]]
    """Whether the cardholder has approved or declined the issued challenge"""
