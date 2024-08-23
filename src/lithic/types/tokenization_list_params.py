# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TokenizationListParams"]


class TokenizationListParams(TypedDict, total=False):
    account_token: str
    """Filters for tokenizations associated with a specific account."""

    begin: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Filter for tokenizations created after this date."""

    card_token: str
    """Filters for tokenizations associated with a specific card."""

    end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Filter for tokenizations created before this date."""

    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    page_size: int
    """Page size (for pagination)."""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """

    tokenization_channel: Literal["DIGITAL_WALLET", "MERCHANT", "ALL"]
    """Filter for tokenizations by tokenization channel.

    If this is not specified, only DIGITAL_WALLET tokenizations will be returned.
    """
