# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DecisioningSimulateChallengeParams"]


class DecisioningSimulateChallengeParams(TypedDict, total=False):
    token: str
    """
    A unique token returned as part of a /v1/three_ds_authentication/simulate call
    that responded with a CHALLENGE_REQUESTED status.
    """
