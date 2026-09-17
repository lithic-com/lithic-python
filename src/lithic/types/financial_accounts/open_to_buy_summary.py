# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["OpenToBuySummary"]


class OpenToBuySummary(BaseModel):
    """Open to Buy Summary"""

    security: int
    """
    Available balance of the Security Account backing card spend, in the currency's
    smallest unit (e.g., cents for USD)
    """

    settled_funds: Optional[int] = None
    """
    Funding that has moved out of the Security Account to cover card spend Lithic
    has already paid out to the networks, in the currency's smallest unit (e.g.,
    cents for USD). Open to buy counts it alongside `security`, and it clears once
    collected from your business clients. Only Commercial Charge tracks this
    separately, so this is `null` for every other program setup
    """

    total_outstanding_spend: int
    """
    Customer card spend that has not yet been collected, in the currency's smallest
    unit (e.g., cents for USD). Reported as a negative amount, because it reduces
    open to buy
    """
