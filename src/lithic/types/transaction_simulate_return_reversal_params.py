# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransactionSimulateReturnReversalParams"]


class TransactionSimulateReturnReversalParams(TypedDict, total=False):
    token: Required[str]
    """The transaction token returned from the /v1/simulate/authorize response."""
