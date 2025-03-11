# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["StatementLineItems", "Data"]


class Data(BaseModel):
    token: str
    """Globally unique identifier for a Statement Line Item"""

    amount: int
    """Transaction amount in cents"""

    category: Literal[
        "ACH",
        "BALANCE_OR_FUNDING",
        "CARD",
        "EXTERNAL_ACH",
        "EXTERNAL_CHECK",
        "EXTERNAL_TRANSFER",
        "EXTERNAL_WIRE",
        "MANAGEMENT_ADJUSTMENT",
        "MANAGEMENT_DISPUTE",
        "MANAGEMENT_FEE",
        "MANAGEMENT_REWARD",
    ]

    created: datetime
    """Timestamp of when the line item was generated"""

    currency: str
    """
    3-character alphabetic ISO 4217 code for the settling currency of the
    transaction
    """

    effective_date: date
    """Date that the transaction effected the account balance"""

    event_type: Literal[
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

    financial_account_token: str
    """Globally unique identifier for a financial account"""

    financial_transaction_event_token: str
    """Globally unique identifier for a financial transaction event"""

    financial_transaction_token: str
    """Globally unique identifier for a financial transaction"""

    card_token: Optional[str] = None
    """Globally unique identifier for a card"""

    descriptor: Optional[str] = None


class StatementLineItems(BaseModel):
    data: List[Data]

    has_more: bool
