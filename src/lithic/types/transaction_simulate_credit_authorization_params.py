# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransactionSimulateCreditAuthorizationParams"]


class TransactionSimulateCreditAuthorizationParams(TypedDict, total=False):
    amount: Required[int]
    """Amount (in cents).

    Any value entered will be converted into a negative amount in the simulated
    transaction. For example, entering 100 in this field will appear as a -100
    amount in the transaction.
    """

    descriptor: Required[str]
    """Merchant descriptor."""

    pan: Required[str]
    """Sixteen digit card number."""
