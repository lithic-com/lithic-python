# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SubscriptionListParams"]


class SubscriptionListParams(TypedDict, total=False):
    ending_before: str
    """The unique identifier of the first item in the previous page.

    Used to retrieve the previous page.
    """

    page_size: int
    """Page size (for pagination)."""

    starting_after: str
    """The unique identifier of the last item in the previous page.

    Used to retrieve the next page.
    """
