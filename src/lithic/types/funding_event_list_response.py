# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FundingEventListResponse", "SettlementBreakdown"]


class SettlementBreakdown(BaseModel):
    amount: int

    settlement_date: date


class FundingEventListResponse(BaseModel):
    token: str
    """Unique token ID"""

    collection_resource_type: Literal["BOOK_TRANSFER", "PAYMENT"]
    """Collection resource type"""

    collection_tokens: List[str]
    """IDs of collections"""

    created: datetime
    """Time of the creation"""

    high_watermark: datetime
    """Time of the high watermark"""

    previous_high_watermark: datetime
    """Time of the previous high watermark"""

    settlement_breakdowns: List[SettlementBreakdown]
    """List of settlements"""

    updated: datetime
    """Time of the update"""
