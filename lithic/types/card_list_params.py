# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CardListParams"]


class CardListParams(TypedDict, total=False):
    account_token: str
    """Only required for multi-account users.

    Returns cards associated with this account. Only applicable if using account
    enrollment. See
    [Managing Accounts](https://docs.lithic.com/docs/managing-accounts) for more
    information.
    """

    begin: str
    """Date string in 8601 format.

    Only entries created after the specified date will be included. UTC time zone.
    """

    end: str
    """Date string in 8601 format.

    Only entries created before the specified date will be included. UTC time zone.
    """

    page: int
    """Page (for pagination)."""

    page_size: int
    """Page size (for pagination)."""
