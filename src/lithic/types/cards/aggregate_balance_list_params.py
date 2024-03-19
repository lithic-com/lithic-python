# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AggregateBalanceListParams"]


class AggregateBalanceListParams(TypedDict, total=False):
    account_token: str
    """Cardholder to retrieve aggregate balances for."""

    business_account_token: str
    """Business to retrieve aggregate balances for."""
