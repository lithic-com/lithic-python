# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountActivityListParams"]


class AccountActivityListParams(TypedDict, total=False):
    begin: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created after the specified time will be included. UTC time zone.
    """

    business_account_token: str
    """Filter by business account token"""

    category: Literal[
        "ACH",
        "BALANCE_OR_FUNDING",
        "CARD",
        "EXTERNAL_ACH",
        "EXTERNAL_CHECK",
        "EXTERNAL_TRANSFER",
        "EXTERNAL_WIRE",
        "MANAGEMENT_ADJUSTMENT",
        "MANAGEMENT_DISPUTE",
        "MANAGEMENT_FEE",
        "MANAGEMENT_REWARD",
        "MANAGEMENT_DISBURSEMENT",
        "PROGRAM_FUNDING",
    ]
    """Filter by transaction category"""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created before the specified time will be included. UTC time zone.
    """

    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    financial_account_token: str
    """Filter by financial account token"""

    page_size: int
    """Page size (for pagination)."""

    result: List[Literal["APPROVED", "DECLINED"]]
    """Filter by transaction result"""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """

    status: List[Literal["DECLINED", "EXPIRED", "PENDING", "SETTLED", "VOIDED", "RETURNED", "REVERSED"]]
    """Filter by transaction status"""
