# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V2ListResultsParams"]


class V2ListResultsParams(TypedDict, total=False):
    auth_rule_token: str
    """Filter by Auth Rule token"""

    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    event_uuid: str
    """Filter by event UUID"""

    has_actions: bool
    """Filter by whether the rule evaluation produced any actions.

    When not provided, all results are returned.
    """

    page_size: int
    """Page size (for pagination)."""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """
