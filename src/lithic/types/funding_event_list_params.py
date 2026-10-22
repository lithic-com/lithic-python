# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FundingEventListParams"]


class FundingEventListParams(TypedDict, total=False):
    begin: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created after the specified time will be included. UTC time zone.
    """

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created before the specified time will be included. UTC time zone.
    """

    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    network_settlement_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """
    Only funding events with a settlement breakout for this network settlement date
    will be included.
    """

    page_size: int
    """Page size (for pagination)."""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """
