# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    begin: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created after the specified date will be included. UTC time zone.
    """

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created before the specified date will be included. UTC time zone.
    """

    ending_before: str
    """The unique identifier of the first item in the previous page.

    Used to retrieve the previous page.
    """

    event_types: Annotated[
        List[Literal["dispute.updated", "digital_wallet.tokenization_approval_request"]],
        PropertyInfo(alias="event_types[]"),
    ]

    page_size: int
    """Page size (for pagination)."""

    starting_after: str
    """The unique identifier of the last item in the previous page.

    Used to retrieve the next page.
    """
