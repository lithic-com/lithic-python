# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SettlementDetail", "OtherFeesDetails"]


class OtherFeesDetails(BaseModel):
    isa: Optional[int] = FieldInfo(alias="ISA", default=None)


class SettlementDetail(BaseModel):
    token: str
    """Globally unique identifier denoting the Settlement Detail."""

    account_token: str
    """
    The most granular ID the network settles with (e.g., ICA for Mastercard, FTSRE
    for Visa).
    """

    card_program_token: str
    """
    Globally unique identifier denoting the card program that the associated
    Transaction occurred on.
    """

    card_token: str
    """
    Globally unique identifier denoting the card that the associated Transaction
    occurred on.
    """

    created: datetime
    """Date and time when the transaction first occurred. UTC time zone."""

    currency: str
    """Three-digit alphabetic ISO 4217 code."""

    disputes_gross_amount: int
    """The total gross amount of disputes settlements."""

    event_tokens: List[str]
    """
    Globally unique identifiers denoting the Events associated with this settlement.
    """

    institution: str
    """
    The most granular ID the network settles with (e.g., ICA for Mastercard, FTSRE
    for Visa).
    """

    interchange_gross_amount: int
    """The total amount of interchange."""

    network: Literal["MASTERCARD", "VISA", "INTERLINK", "MAESTRO", "UNKNOWN"]
    """Card network where the transaction took place."""

    other_fees_details: OtherFeesDetails
    """The total gross amount of other fees by type."""

    other_fees_gross_amount: int
    """Total amount of gross other fees outside of interchange."""

    report_date: str
    """Date of when the report was first generated."""

    settlement_date: str
    """Date of when money movement is triggered for the transaction."""

    transaction_token: str
    """Globally unique identifier denoting the associated Transaction object."""

    transactions_gross_amount: int
    """
    The total amount of settlement impacting transactions (excluding interchange,
    fees, and disputes).
    """

    updated: datetime
    """Date and time when the transaction first occurred. UTC time zone."""
