# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TransactionListParams"]


class TransactionListParams(TypedDict, total=False):
    account_token: str
    """Filters for transactions associated with a specific account."""

    begin: str
    """Date string in 8601 format.

    Only entries created after the specified date will be included. UTC time zone.
    """

    card_token: str
    """Filters for transactions associated with a specific card."""

    end: str
    """Date string in 8601 format.

    Only entries created before the specified date will be included. UTC time zone.
    """

    page: int
    """Page (for pagination)."""

    page_size: int
    """Page size (for pagination)."""

    result: Literal["APPROVED", "DECLINED"]
    """Filters for transactions using transaction result field.

    Can filter by `APPROVED`, and `DECLINED`.
    """
