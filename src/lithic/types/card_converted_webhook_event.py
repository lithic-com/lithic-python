# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardConvertedWebhookEvent"]


class CardConvertedWebhookEvent(BaseModel):
    card_token: str
    """The token of the card that was created."""

    event_type: Literal["card.converted"]
    """The type of event that occurred."""
