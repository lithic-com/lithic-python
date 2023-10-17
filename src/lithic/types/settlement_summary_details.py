# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SettlementSummaryDetails"]


class SettlementSummaryDetails(BaseModel):
    disputes_gross_amount: Optional[int] = None
    """The total gross amount of disputes settlements."""

    institution: Optional[str] = None
    """
    The most granular ID the network settles with (e.g., ICA for Mastercard, FTSRE
    for Visa).
    """

    interchange_gross_amount: Optional[int] = None
    """The total amount of interchange."""

    network: Optional[Literal["MASTERCARD", "VISA", "INTERLINK", "MAESTRO", "UNKNOWN"]] = None
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
