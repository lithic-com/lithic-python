# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import date

from ..._models import BaseModel

__all__ = ["PrimeRateRetrieveResponse", "Data"]


class Data(BaseModel):
    effective_date: date
    """Date the rate goes into effect"""

    rate: str
    """The rate in decimal format"""


class PrimeRateRetrieveResponse(BaseModel):
    data: List[Data]
    """List of prime rates"""

    has_more: bool
    """Whether there are more prime rates"""
