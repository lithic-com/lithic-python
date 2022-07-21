# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TransactionListParams"]


class TransactionListParams(TypedDict, total=False):
    account_token: str
    """Only required for multi-account users.

    Returns transactions associated with this account. Only applicable if using
    account holder enrollment. See
    [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
    more information.
    """

    begin: str
    """Date string in 8601 format.

    Only entries created after the specified date will be included. UTC time zone.
    """

    card_token: str
    """Filters transactions associated with a specific card."""

    end: str
    """Date string in 8601 format.

    Only entries created before the specified date will be included. UTC time zone.
    """

    page: int
    """Page (for pagination)."""

    page_size: int
    """Page size (for pagination)."""

    result: Literal["APPROVED", "DECLINED"]
    """List specific transactions. Filters include `APPROVED`, and `DECLINED`."""
