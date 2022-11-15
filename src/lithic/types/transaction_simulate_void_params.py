# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransactionSimulateVoidParams"]


class TransactionSimulateVoidParams(TypedDict, total=False):
    token: Required[str]
    """The transaction token returned from the /v1/simulate/authorize response."""

    amount: int
    """Amount (in cents) to void.

    Typically this will match the original authorization, but may be less.
    """
