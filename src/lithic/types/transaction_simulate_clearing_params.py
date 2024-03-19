# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransactionSimulateClearingParams"]


class TransactionSimulateClearingParams(TypedDict, total=False):
    token: Required[str]
    """The transaction token returned from the /v1/simulate/authorize response."""

    amount: int
    """Amount (in cents) to complete.

    Typically this will match the original authorization, but may be more or less.

    If no amount is supplied to this endpoint, the amount of the transaction will be
    captured. Any transaction that has any amount completed at all do not have
    access to this behavior.
    """
