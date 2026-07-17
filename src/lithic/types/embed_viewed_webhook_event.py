# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmbedViewedWebhookEvent", "DeviceDetails"]


class DeviceDetails(BaseModel):
    """Details about the request that revealed the card detail"""

    ip_address: str
    """The IP address recorded for the request that generated the event"""


class EmbedViewedWebhookEvent(BaseModel):
    account_token: str
    """The token of the account associated with the card"""

    card_token: str
    """The token of the card whose details were revealed"""

    device_details: DeviceDetails
    """Details about the request that revealed the card detail"""

    embed_type: Literal["PAN", "CVV", "EXP_MONTH", "EXP_YEAR"]
    """The type of card detail that was revealed"""

    event_type: Literal["embed.viewed"]
    """The type of event"""

    session_id: str
    """The identifier shared by webhook events for the same embed session."""
