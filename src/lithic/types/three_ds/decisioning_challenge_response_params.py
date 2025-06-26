# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .challenge_result import ChallengeResult

__all__ = ["DecisioningChallengeResponseParams"]


class DecisioningChallengeResponseParams(TypedDict, total=False):
    token: Required[str]
    """
    Globally unique identifier for 3DS Authentication that resulted in
    PENDING_CHALLENGE authentication result.
    """

    challenge_response: Required[ChallengeResult]
    """Whether the Cardholder has approved or declined the issued Challenge"""
