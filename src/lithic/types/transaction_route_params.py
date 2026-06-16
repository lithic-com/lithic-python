# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransactionRouteParams"]


class TransactionRouteParams(TypedDict, total=False):
    financial_account_token: Required[str]
    """The token of the financial account to route the transaction to."""
