# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FinancialTransactionListParams"]


class FinancialTransactionListParams(TypedDict, total=False):
    begin: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created after the specified time will be included. UTC time zone.
    """

    category: Literal["ACH", "CARD", "INTERNAL", "TRANSFER"]
    """Financial Transaction category to be returned."""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created before the specified time will be included. UTC time zone.
    """

    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    result: Literal["APPROVED", "DECLINED"]
    """Financial Transaction result to be returned."""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """

    status: Literal["DECLINED", "EXPIRED", "PENDING", "RETURNED", "SETTLED", "VOIDED"]
    """Financial Transaction status to be returned."""
