# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from .owner_type import OwnerType

__all__ = ["ExternalBankAccountListParams"]


class ExternalBankAccountListParams(TypedDict, total=False):
    account_token: str

    account_types: List[Literal["CHECKING", "SAVINGS"]]

    countries: List[str]

    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    owner_types: List[OwnerType]

    page_size: int
    """Page size (for pagination)."""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """

    states: List[Literal["ENABLED", "CLOSED", "PAUSED"]]

    verification_states: List[Literal["PENDING", "ENABLED", "FAILED_VERIFICATION", "INSUFFICIENT_FUNDS"]]
