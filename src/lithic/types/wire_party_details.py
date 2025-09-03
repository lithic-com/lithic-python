# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WirePartyDetails"]


class WirePartyDetails(BaseModel):
    account_number: Optional[str] = None
    """Account number"""

    agent_id: Optional[str] = None
    """Routing number or BIC of the financial institution"""

    agent_name: Optional[str] = None
    """Name of the financial institution"""

    name: Optional[str] = None
    """Name of the person or company"""
