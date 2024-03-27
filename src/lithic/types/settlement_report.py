# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .settlement_summary_details import SettlementSummaryDetails

__all__ = ["SettlementReport"]


class SettlementReport(BaseModel):
    created: datetime
    """Date and time when the transaction first occurred. UTC time zone."""

    currency: str
    """Three-digit alphabetic ISO 4217 code."""

    details: List[SettlementSummaryDetails]

    disputes_gross_amount: int
    """The total gross amount of disputes settlements."""

    interchange_gross_amount: int
    """The total amount of interchange."""

    other_fees_gross_amount: int
    """Total amount of gross other fees outside of interchange."""

    report_date: str
    """Date of when the report was first generated."""

    settled_net_amount: int
    """The total net amount of cash moved.

    (net value of settled_gross_amount, interchange, fees).
    """

    transactions_gross_amount: int
    """
    The total amount of settlement impacting transactions (excluding interchange,
    fees, and disputes).
    """

    updated: datetime
    """Date and time when the transaction first occurred. UTC time zone."""
