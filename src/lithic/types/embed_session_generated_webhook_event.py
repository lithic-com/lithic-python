# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmbedSessionGeneratedWebhookEvent", "DeviceDetails"]


class DeviceDetails(BaseModel):
    """Details about the request that generated the embed session"""

    ip_address: str
    """The IP address recorded for the request that generated the event"""


class EmbedSessionGeneratedWebhookEvent(BaseModel):
    account_token: str
    """The token of the account associated with the card"""

    card_token: str
    """The token of the card associated with the embed session"""

    device_details: DeviceDetails
    """Details about the request that generated the embed session"""

    event_type: Literal["embed.session_generated"]
    """The type of event"""

    session_id: str
    """The identifier shared by webhook events for the same embed session."""

    session_type: Literal["CARD_EMBED", "PIN_SETTING_EMBED"]
    """The type of embed session that was generated"""
