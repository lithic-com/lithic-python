# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["InstallmentPlanListParams"]


class InstallmentPlanListParams(TypedDict, total=False):
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

    state: Optional[Literal["PENDING", "ACTIVE", "REBUILD_IN_PROGRESS", "FULLY_PAID", "CANCELLED"]]
    """Only installment plans in this state will be included."""
