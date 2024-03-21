# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

    type: Literal["ISSUING", "OPERATING", "RESERVE"]
    """Type of financial account"""

    updated: datetime
    """Date and time for when the financial account was last updated."""

    account_number: Optional[str] = None
    """Account number for your Lithic-assigned bank account number, if applicable."""

    account_token: Optional[str] = None
    """Account token of the financial account if applicable."""

    nickname: Optional[str] = None
    """User-defined nickname for the financial account."""

    routing_number: Optional[str] = None
    """Routing number for your Lithic-assigned bank account number, if applicable."""
