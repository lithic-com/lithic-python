# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FinancialAccount"]


class FinancialAccount(BaseModel):
    token: str
    """Globally unique identifier for the financial account."""

    created: datetime
    """Date and time for when the financial account was first created."""

    type: Literal["ISSUING", "RESERVE"]
    """Type of financial account"""

    updated: datetime
    """Date and time for when the financial account was last updated."""

    account_number: Optional[str] = None
    """Account number for your Lithic-assigned bank account number, if applicable."""

    routing_number: Optional[str] = None
    """Routing number for your Lithic-assigned bank account number, if applicable."""
