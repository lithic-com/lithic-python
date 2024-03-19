# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransactionSimulateReturnParams"]


class TransactionSimulateReturnParams(TypedDict, total=False):
    amount: Required[int]
    """Amount (in cents) to authorize."""

    descriptor: Required[str]
    """Merchant descriptor."""

    pan: Required[str]
    """Sixteen digit card number."""
