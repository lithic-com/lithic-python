# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.financial_event import FinancialEvent

__all__ = ["FinancialTransaction"]


class FinancialTransaction(BaseModel):
    token: str
    """Globally unique identifier."""

    category: Literal["ACH", "CARD", "INTERNAL", "TRANSFER"]
    """Status types:

    - `CARD` - Issuing card transaction.
    - `ACH` - Transaction over ACH.
    - `INTERNAL` - Transaction for internal adjustment.
    - `TRANSFER` - Internal transfer of funds between financial accounts in your
      program.
    """

    created: datetime
    """Date and time when the financial transaction first occurred. UTC time zone."""

    currency: str
    """
    3-character alphabetic ISO 4217 code for the settling currency of the
    transaction.
    """

    descriptor: str
    """
    A string that provides a description of the financial transaction; may be useful
    to display to users.
    """

    events: List[FinancialEvent]
    """A list of all financial events that have modified this financial transaction."""

    pending_amount: int
    """
    Pending amount of the transaction in the currency's smallest unit (e.g., cents),
    including any acquirer fees. The value of this field will go to zero over time
    once the financial transaction is settled.
    """

    result: Literal["APPROVED", "DECLINED"]
    """
    APPROVED transactions were successful while DECLINED transactions were declined
    by user, Lithic, or the network.
    """

    settled_amount: int
    """
    Amount of the transaction that has been settled in the currency's smallest unit
    (e.g., cents), including any acquirer fees. This may change over time.
    """

    status: Literal["DECLINED", "EXPIRED", "PENDING", "RETURNED", "SETTLED", "VOIDED"]
    """Status types:

    - `DECLINED` - The transaction was declined.
    - `EXPIRED` - The authorization as it has passed its expiration time. Card
      transaction only.
    - `PENDING` - The transaction is expected to settle.
    - `RETURNED` - The transaction has been returned.
    - `SETTLED` - The transaction is completed.
    - `VOIDED` - The transaction was voided. Card transaction only.
    """

    updated: datetime
    """Date and time when the financial transaction was last updated. UTC time zone."""
