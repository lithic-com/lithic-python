# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .challenge_result import ChallengeResult

__all__ = ["DecisioningSimulateChallengeResponseParams"]


class DecisioningSimulateChallengeResponseParams(TypedDict, total=False):
    token: Required[str]
    """Globally unique identifier for the 3DS authentication.

    This token is sent as part of the initial 3DS Decisioning Request and as part of
    the 3DS Challenge Event in the
    [ThreeDSAuthentication](#/components/schemas/ThreeDSAuthentication) object
    """

    challenge_response: Required[ChallengeResult]
    """Whether the Cardholder has Approved or Declined the issued Challenge"""
