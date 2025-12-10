# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardReissuedWebhookEvent"]


class CardReissuedWebhookEvent(BaseModel):
    event_type: Literal["card.reissued"]
    """The type of event that occurred."""

    card_token: Optional[str] = None
    """The token of the card that was reissued."""
