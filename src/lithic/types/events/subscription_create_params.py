# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SubscriptionCreateParams"]


class SubscriptionCreateParams(TypedDict, total=False):
    url: Required[str]
    """URL to which event webhooks will be sent. URL must be a valid HTTPS address."""

    description: str
    """Event subscription description."""

    disabled: bool
    """Whether the event subscription is active (false) or inactive (true)."""

    event_types: List[Literal["dispute.updated", "digital_wallet.token_approval_request"]]
    """Indicates types of events that will be sent to this subscription.

    If left blank, all types will be sent.
    """
