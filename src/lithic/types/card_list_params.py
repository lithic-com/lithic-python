# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CardListParams"]


class CardListParams(TypedDict, total=False):
    account_token: str
    """Returns cards associated with the specified account."""

    begin: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created after the specified date will be included. UTC time zone.
    """

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created before the specified date will be included. UTC time zone.
    """

    page: int
    """Page (for pagination)."""

    page_size: int
    """Page size (for pagination)."""

    state: Literal["OPEN", "PAUSED", "CLOSED", "PENDING_FULFILLMENT", "PENDING_ACTIVATION"]
    """Returns cards with the specified state."""
