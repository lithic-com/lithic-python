# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CardGetEmbedHTMLParams"]


class CardGetEmbedHTMLParams(TypedDict, total=False):
    token: Required[str]
    """Globally unique identifier for the card to be displayed."""

    css: str
    """
    A publicly available URI, so the white-labeled card element can be styled with
    the client's branding.
    """

    expiration: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """An RFC 3339 timestamp for when the request should expire. UTC time zone.

    If no timezone is specified, UTC will be used. If payload does not contain an
    expiration, the request will never expire.

    Using an `expiration` reduces the risk of a
    [replay attack](https://en.wikipedia.org/wiki/Replay_attack). Without supplying
    the `expiration`, in the event that a malicious user gets a copy of your request
    in transit, they will be able to obtain the response data indefinitely.
    """

    target_origin: str
    """Required if you want to post the element clicked to the parent iframe.

    If you supply this param, you can also capture click events in the parent iframe
    by adding an event listener.
    """
