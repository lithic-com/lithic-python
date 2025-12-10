# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardShippedWebhookEvent"]


class CardShippedWebhookEvent(BaseModel):
    bulk_order_token: Optional[str] = None
    """The token of the bulk order associated with this card shipment, if applicable."""

    card_token: str
    """The token of the card that was shipped."""

    event_type: Literal["card.shipped"]
    """The type of event that occurred."""

    shipping_method: Literal[
        "Ex-US expedited with tracking",
        "Ex-US standard with tracking",
        "Ex-US standard without tracking",
        "FedEx 2 days",
        "FedEx express",
        "FedEx overnight",
        "USPS priority",
        "USPS with tracking",
        "USPS without tracking envelope",
        "USPS without tracking envelope non-machine",
        "USPS without tracking flat",
    ]
    """The specific shipping method used to ship the card."""

    tracking_number: Optional[str] = None
    """The tracking number of the shipment."""
