# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardPinUpdatedWebhookEvent"]


class CardPinUpdatedWebhookEvent(BaseModel):
    card_token: str
    """The token of the card whose PIN or PIN status was updated"""

    event_type: Literal["card.pin_updated"]
    """The type of event that occurred."""

    pin_status: Literal["OK", "BLOCKED"]
    """The card's PIN status after the update"""

    status_reason: Literal["PIN_SET", "PIN_CHANGED", "PIN_UNBLOCKED", "EXCESSIVE_PIN_ATTEMPTS"]
    """The reason for the PIN update:

    - `PIN_SET` - The PIN was set for the first time; `pin_status` is `OK`
    - `PIN_CHANGED` - The PIN was changed, including when changing a blocked PIN;
      `pin_status` is `OK`
    - `PIN_UNBLOCKED` - The PIN was unblocked without changing it; `pin_status` is
      `OK`
    - `EXCESSIVE_PIN_ATTEMPTS` - The PIN was blocked due to excessive incorrect PIN
      attempts; `pin_status` is `BLOCKED`
    """
