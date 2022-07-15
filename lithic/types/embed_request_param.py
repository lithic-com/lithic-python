# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["EmbedRequestParams"]


class EmbedRequestParams(BaseModel):
    token: str
    """Globally unique identifier for the card to be displayed."""

    account_token: Optional[str]
    """Only needs to be included if one or more end-users have been enrolled."""

    css: Optional[str]
    """
    A publicly available URI, so the white-labeled card element can be styled with
    the client's branding.
    """

    expiration: Optional[str]
    """An ISO 8601 timestamp for when the request should expire. UTC time zone.

    If no timezone is specified, UTC will be used. If payload does not contain an
    expiration, the request will never expire.

    Using an `expiration` reduces the risk of a
    [replay attack](https://en.wikipedia.org/wiki/Replay_attack). Without supplying
    the `expiration`, in the event that a malicious user gets a copy of your request
    in transit, they will be able to obtain the response data indefinitely.
    """

    target_origin: Optional[str]
    """Required if you want to post the element clicked to the parent iframe.

    If you supply this param, you can also capture click events in the parent iframe
    by adding an event listener.
    """
