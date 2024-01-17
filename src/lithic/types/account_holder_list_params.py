# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountHolderListParams"]


class AccountHolderListParams(TypedDict, total=False):
    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    external_id: str
    """If applicable, represents the external_id associated with the account_holder."""

    limit: int
    """The number of account_holders to limit the response to."""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """
