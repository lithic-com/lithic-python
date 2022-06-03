# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
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
