# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date

from ..._models import BaseModel

__all__ = ["InterestTierSchedule"]


class InterestTierSchedule(BaseModel):
    """Entry in the Tier Schedule of an account"""

    credit_product_token: str
    """Globally unique identifier for a credit product"""

    effective_date: date
    """Date the tier should be effective in YYYY-MM-DD format"""

    tier_name: Optional[str] = None
    """Name of a tier contained in the credit product.

    Mutually exclusive with tier_rates
    """

    tier_rates: Optional[object] = None
    """Custom rates per category. Mutually exclusive with tier_name"""
