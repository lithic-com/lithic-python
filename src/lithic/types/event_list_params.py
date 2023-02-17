# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    begin: str
    """Date string in 8601 format.

    Only entries created after the specified date will be included. UTC time zone.
    """

    end: str
    """Date string in 8601 format.

    Only entries created before the specified date will be included. UTC time zone.
    """

    ending_before: str
    """The unique identifier of the first item in the previous page.

    Used to retrieve the previous page.
    """

    event_types: List[Literal["dispute.updated", "digital_wallet.token_approval_request"]]

    page_size: int
    """Page size (for pagination)."""

    starting_after: str
    """The unique identifier of the last item in the previous page.

    Used to retrieve the next page.
    """
