# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .dispute import Dispute

__all__ = ["DisputeUpdatedWebhookEvent"]


class DisputeUpdatedWebhookEvent(Dispute):
    """Dispute."""

    event_type: Literal["dispute.updated"]
    """The type of event that occurred."""
