# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CardListParams"]


class CardListParams(TypedDict, total=False):
    account_token: str
    """Only required for multi-account users.

    Returns cards associated with this account. Only applicable if using account
    holder enrollment. See
    [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
    more information.
    """

    begin: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in 8601 format.

    Only entries created after the specified date will be included. UTC time zone.
    """

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in 8601 format.

    Only entries created before the specified date will be included. UTC time zone.
    """

    page: int
    """Page (for pagination)."""

    page_size: int
    """Page size (for pagination)."""
