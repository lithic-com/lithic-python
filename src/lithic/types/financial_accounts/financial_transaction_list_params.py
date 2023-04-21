# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FinancialTransactionListParams"]


class FinancialTransactionListParams(TypedDict, total=False):
    begin: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created after the specified date will be included. UTC time zone.
    """

    category: Literal["ACH", "CARD", "TRANSFER"]
    """Financial Transaction category to be returned."""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created before the specified date will be included. UTC time zone.
    """

    ending_before: str
    """The unique identifier of the first item in the previous page.

    Used to retrieve the previous page.
    """

    result: Literal["APPROVED", "DECLINED"]
    """Financial Transaction result to be returned."""

    starting_after: str
    """The unique identifier of the last item in the previous page.

    Used to retrieve the next page.
    """

    status: Literal["DECLINED", "EXPIRED", "PENDING", "SETTLED", "VOIDED"]
    """Financial Transaction status to be returned."""
