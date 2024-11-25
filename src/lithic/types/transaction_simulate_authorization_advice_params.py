# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransactionSimulateAuthorizationAdviceParams"]


class TransactionSimulateAuthorizationAdviceParams(TypedDict, total=False):
    token: Required[str]
    """The transaction token returned from the /v1/simulate/authorize. response."""

    amount: Required[int]
    """Amount (in cents) to authorize.

    This amount will override the transaction's amount that was originally set by
    /v1/simulate/authorize.
    """
