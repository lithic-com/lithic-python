# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DisputesV2ListParams"]


class DisputesV2ListParams(TypedDict, total=False):
    account_token: str
    """Filter by account token."""

    begin: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp for filtering by created date, inclusive."""

    card_token: str
    """Filter by card token."""

    disputed_transaction_token: str
    """Filter by the token of the transaction being disputed.

    Corresponds with transaction_series.related_transaction_token in the Dispute.
    """

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """RFC 3339 timestamp for filtering by created date, inclusive."""

    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    page_size: int
    """Number of items to return."""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """
