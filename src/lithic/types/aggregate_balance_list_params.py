# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AggregateBalanceListParams"]


class AggregateBalanceListParams(TypedDict, total=False):
    financial_account_type: Literal["ISSUING", "OPERATING", "RESERVE"]
    """Get the aggregate balance for a given Financial Account type."""
