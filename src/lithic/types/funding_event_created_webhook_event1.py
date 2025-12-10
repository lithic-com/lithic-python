# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .funding_event import FundingEvent

__all__ = ["FundingEventCreatedWebhookEvent"]


class FundingEventCreatedWebhookEvent(FundingEvent):
    event_type: Literal["funding_event.created"]
    """The type of event that occurred."""
