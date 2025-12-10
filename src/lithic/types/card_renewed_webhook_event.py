# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardRenewedWebhookEvent"]


class CardRenewedWebhookEvent(BaseModel):
    event_type: Literal["card.renewed"]
    """The type of event that occurred."""

    card_token: Optional[str] = None
    """The token of the card that was renewed."""

    exp_month: Optional[str] = None
    """The new expiration month of the card."""

    exp_year: Optional[str] = None
    """The new expiration year of the card."""

    previous_exp_month: Optional[str] = None
    """The previous expiration month of the card."""

    previous_exp_year: Optional[str] = None
    """The previous expiration year of the card."""
