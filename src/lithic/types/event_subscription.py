# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EventSubscription"]


class EventSubscription(BaseModel):
    description: str
    """A description of the subscription."""

    disabled: bool
    """Whether the subscription is disabled."""

    event_types: Optional[List[Literal["dispute.updated", "digital_wallet.token_approval_request"]]]

    token: str
    """Globally unique identifier."""

    url: str
