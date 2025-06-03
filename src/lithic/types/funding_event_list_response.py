# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FundingEventListResponse", "NetworkSettlementSummary"]


class NetworkSettlementSummary(BaseModel):
    network_settlement_date: date

    settled_gross_amount: int


class FundingEventListResponse(BaseModel):
    token: str
    """Unique token ID"""

    collection_resource_type: Literal["BOOK_TRANSFER", "PAYMENT"]
    """Collection resource type"""

    collection_tokens: List[str]
    """
    IDs of collections, further information can be gathered from the appropriate
    collection API based on collection_resource_type
    """

    created: datetime
    """Time of the creation"""

    high_watermark: datetime
    """Time of the high watermark"""

    network_settlement_summary: List[NetworkSettlementSummary]
    """Network settlement summary breakdown by network settlement date"""

    previous_high_watermark: datetime
    """Time of the previous high watermark"""

    updated: datetime
    """Time of the update"""
