# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .card_authorization import CardAuthorization

__all__ = ["CardAuthorizationChallengeWebhookEvent", "Challenge"]


class Challenge(BaseModel):
    """Details of the Authorization Challenge issued during card authorization"""

    event_token: str
    """Globally unique identifier for the event that triggered the challenge.

    Use this token when calling the challenge response endpoint
    """

    expiry_time: datetime
    """ISO-8601 time at which the challenge expires"""

    start_time: datetime
    """ISO-8601 time at which the challenge was issued"""


class CardAuthorizationChallengeWebhookEvent(BaseModel):
    authorization: CardAuthorization
    """The authorization that triggered the challenge"""

    challenge: Challenge
    """Details of the Authorization Challenge issued during card authorization"""

    event_type: Literal["card_authorization.challenge"]
    """The type of event that occurred."""
