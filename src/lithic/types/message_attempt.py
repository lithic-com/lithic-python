# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessageAttempt"]


class MessageAttempt(BaseModel):
    token: str
    """Globally unique identifier."""

    created: datetime
    """An RFC 3339 timestamp for when the event was created. UTC time zone.

    If no timezone is specified, UTC will be used.
    """

    event_subscription_token: str
    """Globally unique identifier."""

    event_token: str
    """Globally unique identifier."""

    response: str
    """The response body from the event subscription's URL."""

    response_status_code: int
    """The response status code from the event subscription's URL."""

    status: Literal["FAILED", "PENDING", "SENDING", "SUCCESS"]
    """The status of the event attempt."""

    url: str
