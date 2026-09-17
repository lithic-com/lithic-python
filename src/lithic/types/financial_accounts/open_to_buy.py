# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel
from .open_to_buy_summary import OpenToBuySummary

__all__ = ["OpenToBuy"]


class OpenToBuy(BaseModel):
    """Open to Buy"""

    open_to_buy: int
    """
    Funds available for card spend backed by this Security Account, in the
    currency's smallest unit (e.g., cents for USD). Equal to the sum of the amounts
    in `summary`, and reaches zero once outstanding spend has consumed all available
    funding
    """

    summary: OpenToBuySummary
    """Balances that open to buy is derived from"""
