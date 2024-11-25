# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransactionSimulateClearingParams"]


class TransactionSimulateClearingParams(TypedDict, total=False):
    token: Required[str]
    """The transaction token returned from the /v1/simulate/authorize response."""

    amount: int
    """Amount (in cents) to clear.

    Typically this will match the amount in the original authorization, but can be
    higher or lower. The sign of this amount will automatically match the sign of
    the original authorization's amount. For example, entering 100 in this field
    will result in a -100 amount in the transaction, if the original authorization
    is a credit authorization.

    If `amount` is not set, the full amount of the transaction will be cleared.
    Transactions that have already cleared, either partially or fully, cannot be
    cleared again using this endpoint.
    """
