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
    """3-character alphabetic ISO 4217 code.

    (This field is deprecated and will be removed in a future version of the API.)
    """

    details: List[SettlementSummaryDetails]

    disputes_gross_amount: int
    """The total gross amount of disputes settlements.

    (This field is deprecated and will be removed in a future version of the API. To
    compute total amounts, Lithic recommends that customers sum the relevant
    settlement amounts found within `details`.)
    """

    interchange_gross_amount: int
    """The total amount of interchange.

    (This field is deprecated and will be removed in a future version of the API. To
    compute total amounts, Lithic recommends that customers sum the relevant
    settlement amounts found within `details`.)
    """

    is_complete: bool
    """Indicates that all data expected on the given report date is available."""

    other_fees_gross_amount: int
    """Total amount of gross other fees outside of interchange.

    (This field is deprecated and will be removed in a future version of the API. To
    compute total amounts, Lithic recommends that customers sum the relevant
    settlement amounts found within `details`.)
    """

    report_date: str
    """Date of when the report was first generated."""

    settled_net_amount: int
    """The total net amount of cash moved.

    (net value of settled_gross_amount, interchange, fees). (This field is
    deprecated and will be removed in a future version of the API. To compute total
    amounts, Lithic recommends that customers sum the relevant settlement amounts
    found within `details`.)
    """

    transactions_gross_amount: int
    """
    The total amount of settlement impacting transactions (excluding interchange,
    fees, and disputes). (This field is deprecated and will be removed in a future
    version of the API. To compute total amounts, Lithic recommends that customers
    sum the relevant settlement amounts found within `details`.)
    """

    updated: datetime
    """Date and time when the transaction first occurred. UTC time zone."""
