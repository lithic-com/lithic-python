# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["InterestTierScheduleUpdateParams"]


class InterestTierScheduleUpdateParams(TypedDict, total=False):
    financial_account_token: Required[str]

    tier_name: str
    """Name of a tier contained in the credit product.

    Mutually exclusive with tier_rates
    """

    tier_rates: object
    """Custom rates per category. Mutually exclusive with tier_name"""
