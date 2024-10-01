# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ManagementOperationListParams"]


class ManagementOperationListParams(TypedDict, total=False):
    begin: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created after the specified time will be included. UTC time zone.
    """

    business_account_token: str

    category: Literal["MANAGEMENT_FEE", "MANAGEMENT_DISPUTE", "MANAGEMENT_REWARD", "MANAGEMENT_ADJUSTMENT"]
    """Management operation category to be returned."""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created before the specified time will be included. UTC time zone.
    """

    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    financial_account_token: str
    """Globally unique identifier for the financial account.

    Accepted type dependent on the program's use case.
    """

    page_size: int
    """Page size (for pagination)."""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """

    status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED"]
    """Management operation status to be returned."""
