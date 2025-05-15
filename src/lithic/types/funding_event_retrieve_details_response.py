# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FundingEventRetrieveDetailsResponse"]


class FundingEventRetrieveDetailsResponse(BaseModel):
    token: str
    """Unique token ID"""

    settlement_details_url: str
    """URL of the settlement details"""

    settlement_summary_url: str
    """URL of the settlement summary"""
