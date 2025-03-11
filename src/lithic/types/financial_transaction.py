# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FinancialTransaction", "Event"]


class Event(BaseModel):
    token: Optional[str] = None
    """Globally unique identifier."""

    amount: Optional[int] = None
    """
    Amount of the financial event that has been settled in the currency's smallest
    unit (e.g., cents).
    """

    created: Optional[datetime] = None
    """Date and time when the financial event occurred. UTC time zone."""

    result: Optional[Literal["APPROVED", "DECLINED"]] = None
    """
    APPROVED financial events were successful while DECLINED financial events were
    declined by user, Lithic, or the network.
    """

    type: Optional[
        Literal[
            "ACH_ORIGINATION_CANCELLED",
            "ACH_ORIGINATION_INITIATED",
            "ACH_ORIGINATION_PROCESSED",
            "ACH_ORIGINATION_RELEASED",
            "ACH_ORIGINATION_REVIEWED",
            "ACH_ORIGINATION_SETTLED",
            "ACH_RECEIPT_PROCESSED",
            "ACH_RECEIPT_SETTLED",
            "ACH_RETURN_INITIATED",
            "ACH_RETURN_PROCESSED",
            "ACH_RETURN_SETTLED",
            "AUTHORIZATION",
            "AUTHORIZATION_ADVICE",
            "AUTHORIZATION_EXPIRY",
            "AUTHORIZATION_REVERSAL",
            "BALANCE_INQUIRY",
            "BILLING_ERROR",
            "BILLING_ERROR_REVERSAL",
            "CARD_TO_CARD",
            "CASH_BACK",
            "CASH_BACK_REVERSAL",
            "CLEARING",
            "CORRECTION_CREDIT",
            "CORRECTION_DEBIT",
            "CREDIT_AUTHORIZATION",
            "CREDIT_AUTHORIZATION_ADVICE",
            "CURRENCY_CONVERSION",
            "CURRENCY_CONVERSION_REVERSAL",
            "DISPUTE_WON",
            "EXTERNAL_ACH_CANCELED",
            "EXTERNAL_ACH_INITIATED",
            "EXTERNAL_ACH_RELEASED",
            "EXTERNAL_ACH_REVERSED",
            "EXTERNAL_ACH_SETTLED",
            "EXTERNAL_CHECK_CANCELED",
            "EXTERNAL_CHECK_INITIATED",
            "EXTERNAL_CHECK_RELEASED",
            "EXTERNAL_CHECK_REVERSED",
            "EXTERNAL_CHECK_SETTLED",
            "EXTERNAL_TRANSFER_CANCELED",
            "EXTERNAL_TRANSFER_INITIATED",
            "EXTERNAL_TRANSFER_RELEASED",
            "EXTERNAL_TRANSFER_REVERSED",
            "EXTERNAL_TRANSFER_SETTLED",
            "EXTERNAL_WIRE_CANCELED",
            "EXTERNAL_WIRE_INITIATED",
            "EXTERNAL_WIRE_RELEASED",
            "EXTERNAL_WIRE_REVERSED",
            "EXTERNAL_WIRE_SETTLED",
            "FINANCIAL_AUTHORIZATION",
            "FINANCIAL_CREDIT_AUTHORIZATION",
            "INTEREST",
            "INTEREST_REVERSAL",
            "INTERNAL_ADJUSTMENT",
            "LATE_PAYMENT",
            "LATE_PAYMENT_REVERSAL",
            "PROVISIONAL_CREDIT",
            "PROVISIONAL_CREDIT_REVERSAL",
            "RETURN",
            "RETURN_REVERSAL",
            "TRANSFER",
            "TRANSFER_INSUFFICIENT_FUNDS",
            "RETURNED_PAYMENT",
            "RETURNED_PAYMENT_REVERSAL",
        ]
    ] = None


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

    events: List[Event]
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
