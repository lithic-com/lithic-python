# File generated from our OpenAPI spec by Stainless.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Event"]


class Event(BaseModel):
    created: datetime
    """An RFC 3339 timestamp for when the event was created. UTC time zone.

    If no timezone is specified, UTC will be used.
    """

    event_type: Literal["dispute.updated", "digital_wallet.tokenization_approval_request"]
    """Event types:

    - `dispute.updated` - A dispute has been updated.
    - `digital_wallet.tokenization_approval_request` - Card network's request to
      Lithic to activate a digital wallet token.
    """

    payload: object

    token: str
    """Globally unique identifier."""
