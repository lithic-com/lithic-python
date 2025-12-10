# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .network_total import NetworkTotal

__all__ = ["NetworkTotalUpdatedWebhookEvent"]


class NetworkTotalUpdatedWebhookEvent(NetworkTotal):
    event_type: Literal["network_total.updated"]
    """The type of event that occurred."""
