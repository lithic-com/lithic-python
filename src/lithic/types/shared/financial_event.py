# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FinancialEvent"]


class FinancialEvent(BaseModel):
    """Financial Event"""

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
            "ACH_ORIGINATION_REJECTED",
            "ACH_ORIGINATION_REVIEWED",
            "ACH_ORIGINATION_SETTLED",
            "ACH_RECEIPT_PROCESSED",
            "ACH_RECEIPT_RELEASED",
            "ACH_RECEIPT_SETTLED",
            "ACH_RETURN_INITIATED",
            "ACH_RETURN_PROCESSED",
            "ACH_RETURN_REJECTED",
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
            "COLLECTION",
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
            "EXTERNAL_FEDNOW_CANCELED",
            "EXTERNAL_FEDNOW_INITIATED",
            "EXTERNAL_FEDNOW_RELEASED",
            "EXTERNAL_FEDNOW_REVERSED",
            "EXTERNAL_FEDNOW_SETTLED",
            "EXTERNAL_RTP_CANCELED",
            "EXTERNAL_RTP_INITIATED",
            "EXTERNAL_RTP_RELEASED",
            "EXTERNAL_RTP_REVERSED",
            "EXTERNAL_RTP_SETTLED",
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
            "LOSS_WRITE_OFF",
            "PROVISIONAL_CREDIT",
            "PROVISIONAL_CREDIT_REVERSAL",
            "SERVICE",
            "RETURN",
            "RETURN_REVERSAL",
            "TRANSFER",
            "TRANSFER_INSUFFICIENT_FUNDS",
            "RETURNED_PAYMENT",
            "RETURNED_PAYMENT_REVERSAL",
            "LITHIC_NETWORK_PAYMENT",
            "ANNUAL",
            "ANNUAL_REVERSAL",
            "QUARTERLY",
            "QUARTERLY_REVERSAL",
            "MONTHLY",
            "MONTHLY_REVERSAL",
        ]
    ] = None
