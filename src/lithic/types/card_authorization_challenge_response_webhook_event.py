# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardAuthorizationChallengeResponseWebhookEvent"]


class CardAuthorizationChallengeResponseWebhookEvent(BaseModel):
    card_token: Optional[str] = None
    """The token of the card associated with the challenge"""

    challenge_method: Literal["SMS"]
    """The method used to deliver the challenge to the cardholder"""

    completed: Optional[datetime] = None
    """The timestamp of when the challenge was completed"""

    created: datetime
    """The timestamp of when the challenge was created"""

    event_token: str
    """Globally unique identifier for the event"""

    event_type: Literal["card_authorization.challenge_response"]
    """Event type"""

    response: Literal["APPROVE", "DECLINE"]
    """The cardholder's response to the challenge"""

    transaction_token: Optional[str] = None
    """
    The token of the transaction associated with the authorization event being
    challenged
    """
