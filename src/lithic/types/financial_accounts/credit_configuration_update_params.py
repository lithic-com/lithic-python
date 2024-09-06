# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CreditConfigurationUpdateParams"]


class CreditConfigurationUpdateParams(TypedDict, total=False):
    credit_limit: int

    credit_product_token: str
    """Globally unique identifier for the credit product"""

    external_bank_account_token: str

    tier: str
    """Tier to assign to a financial account"""
