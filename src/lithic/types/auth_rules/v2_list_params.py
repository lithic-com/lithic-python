# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["V2ListParams"]


class V2ListParams(TypedDict, total=False):
    account_token: str
    """Only return Auth Rules that are bound to the provided account token."""

    card_token: str
    """Only return Auth Rules that are bound to the provided card token."""

    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"]
    """Only return Auth rules that are executed during the provided event stream."""

    page_size: int
    """Page size (for pagination)."""

    scope: Literal["PROGRAM", "ACCOUNT", "CARD", "ANY"]
    """Only return Auth Rules that are bound to the provided scope."""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """
