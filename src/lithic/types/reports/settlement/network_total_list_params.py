# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date, datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["NetworkTotalListParams"]


class NetworkTotalListParams(TypedDict, total=False):
    begin: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Datetime in RFC 3339 format.

    Only entries created after the specified time will be included. UTC time zone.
    """

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Datetime in RFC 3339 format.

    Only entries created before the specified time will be included. UTC time zone.
    """

    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    institution_id: str
    """Institution ID to filter on."""

    network: Literal["VISA", "MASTERCARD", "MAESTRO", "INTERLINK"]
    """Network to filter on."""

    page_size: int
    """Number of records per page."""

    report_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Singular report date to filter on (YYYY-MM-DD).

    Cannot be populated in conjunction with report_date_begin or report_date_end.
    """

    report_date_begin: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Earliest report date to filter on, inclusive (YYYY-MM-DD)."""

    report_date_end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Latest report date to filter on, inclusive (YYYY-MM-DD)."""

    settlement_institution_id: str
    """Settlement institution ID to filter on."""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """
