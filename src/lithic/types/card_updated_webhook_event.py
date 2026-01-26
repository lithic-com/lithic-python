# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardUpdatedWebhookEvent"]


class CardUpdatedWebhookEvent(BaseModel):
    card_token: str
    """The token of the card that was updated."""

    event_type: Literal["card.updated"]
    """The type of event that occurred."""

    previous_fields: object
    """The previous values of the fields that were updated."""

    state: str
    """The current state of the card."""
