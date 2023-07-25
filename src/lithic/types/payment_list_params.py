# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["PaymentListParams"]


class PaymentListParams(TypedDict, total=False):
    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    financial_account_token: str

    page_size: int
    """Page size (for pagination)."""

    result: Literal["APPROVED", "DECLINED"]

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """

    status: Literal["PENDING", "VOIDED", "SETTLED", "DECLINED", "EXPIRED"]
