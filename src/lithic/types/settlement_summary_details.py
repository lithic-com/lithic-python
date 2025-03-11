# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SettlementSummaryDetails"]


class SettlementSummaryDetails(BaseModel):
    currency: Optional[str] = None
    """3-character alphabetic ISO 4217 code."""

    disputes_gross_amount: Optional[int] = None
    """The total gross amount of disputes settlements."""

    institution: Optional[str] = None
    """
    The most granular ID the network settles with (e.g., ICA for Mastercard, FTSRE
    for Visa).
    """

    interchange_gross_amount: Optional[int] = None
    """The total amount of interchange."""

    network: Optional[Literal["INTERLINK", "MAESTRO", "MASTERCARD", "UNKNOWN", "VISA"]] = None
    """Card network where the transaction took place"""

    other_fees_gross_amount: Optional[int] = None
    """Total amount of gross other fees outside of interchange."""

    settled_net_amount: Optional[int] = None
    """The total net amount of cash moved.

    (net value of settled_gross_amount, interchange, fees).
    """

    transactions_gross_amount: Optional[int] = None
    """
    The total amount of settlement impacting transactions (excluding interchange,
    fees, and disputes).
    """
