# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .case_status import CaseStatus
from .case_sort_order import CaseSortOrder

__all__ = ["CaseListParams"]


class CaseListParams(TypedDict, total=False):
    account_token: str
    """Only return cases that include transactions on the provided account."""

    assignee: str
    """Only return cases assigned to the provided value.

    Pass an empty string to return only unassigned cases.
    """

    begin: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created after the specified time will be included. UTC time zone.
    """

    card_token: str
    """Only return cases that include transactions on the provided card."""

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created before the specified time will be included. UTC time zone.
    """

    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    entity_token: str
    """Only return cases associated with the provided entity."""

    page_size: int
    """Page size (for pagination)."""

    queue_token: str
    """Only return cases belonging to the provided queue."""

    rule_token: str
    """Only return cases triggered by the provided transaction monitoring rule."""

    sort_by: CaseSortOrder
    """Sort order for the returned cases."""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """

    status: CaseStatus
    """Only return cases with the provided status."""

    transaction_token: str
    """Only return cases that include the provided transaction."""
