# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InterestTierScheduleCreateParams"]


class InterestTierScheduleCreateParams(TypedDict, total=False):
    credit_product_token: Required[str]
    """Globally unique identifier for a credit product"""

    effective_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Date the tier should be effective in YYYY-MM-DD format"""

    tier_name: str
    """Name of a tier contained in the credit product.

    Mutually exclusive with tier_rates
    """

    tier_rates: object
    """Custom rates per category. Mutually exclusive with tier_name"""
