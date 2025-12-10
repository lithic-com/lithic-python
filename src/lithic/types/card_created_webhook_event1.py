# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardCreatedWebhookEvent"]


class CardCreatedWebhookEvent(BaseModel):
    card_token: str
    """The token of the card that was created."""

    event_type: Literal["card.created"]
    """The type of event that occurred."""

    replacement_for: Optional[str] = None
    """The token of the card that was replaced, if the new card is a replacement card."""
