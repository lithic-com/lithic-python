# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["FinancialAccountListParams"]


class FinancialAccountListParams(TypedDict, total=False):
    account_token: str
    """List financial accounts for a given account_token or business_account_token"""

    business_account_token: str
    """List financial accounts for a given business_account_token"""

    type: Literal["ISSUING", "OPERATING", "RESERVE"]
    """List financial accounts of a given type"""
