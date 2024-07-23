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

    category: Literal["ACH", "CARD", "TRANSFER"]

    created: datetime
    """Timestamp of when the line item was generated"""

    currency: str
    """3-digit alphabetic ISO 4217 code for the settling currency of the transaction"""

    event_type: Literal[
        "ACH_ORIGINATION_CANCELLED",
        "ACH_ORIGINATION_INITIATED",
        "ACH_ORIGINATION_PROCESSED",
        "ACH_ORIGINATION_SETTLED",
        "ACH_ORIGINATION_RELEASED",
        "ACH_ORIGINATION_REVIEWED",
        "ACH_RECEIPT_PROCESSED",
        "ACH_RECEIPT_SETTLED",
        "ACH_RETURN_INITIATED",
        "ACH_RETURN_PROCESSED",
        "AUTHORIZATION",
        "AUTHORIZATION_ADVICE",
        "AUTHORIZATION_EXPIRY",
        "AUTHORIZATION_REVERSAL",
        "BALANCE_INQUIRY",
        "CLEARING",
        "CORRECTION_CREDIT",
        "CORRECTION_DEBIT",
        "CREDIT_AUTHORIZATION",
        "CREDIT_AUTHORIZATION_ADVICE",
        "FINANCIAL_AUTHORIZATION",
        "FINANCIAL_CREDIT_AUTHORIZATION",
        "RETURN",
        "RETURN_REVERSAL",
        "TRANSFER",
        "TRANSFER_INSUFFICIENT_FUNDS",
    ]
    """
    Event types: _ `ACH_ORIGINATION_INITIATED` - ACH origination received and
    pending approval/release from an ACH hold. _ `ACH_ORIGINATION_REVIEWED` - ACH
    origination has completed the review process. _ `ACH_ORIGINATION_CANCELLED` -
    ACH origination has been cancelled. _ `ACH_ORIGINATION_PROCESSED` - ACH
    origination has been processed and sent to the fed. _
    `ACH_ORIGINATION_SETTLED` - ACH origination has settled. _
    `ACH_ORIGINATION_RELEASED` - ACH origination released from pending to available
    balance. _ `ACH_RETURN_PROCESSED` - ACH origination returned by the Receiving
    Depository Financial Institution. _ `ACH_RECEIPT_PROCESSED` - ACH receipt
    pending release from an ACH holder. _ `ACH_RETURN_INITIATED` - ACH initiated
    return for a ACH receipt. _ `ACH_RECEIPT_SETTLED` - ACH receipt funds have
    settled. _ `ACH_RECEIPT_RELEASED` - ACH receipt released from pending to
    available balance. _ `AUTHORIZATION` - Authorize a card transaction. _
    `AUTHORIZATION_ADVICE` - Advice on a card transaction. _
    `AUTHORIZATION_EXPIRY` - Card Authorization has expired and reversed by Lithic.
    _ `AUTHORIZATION_REVERSAL` - Card Authorization was reversed by the merchant. _
    `BALANCE_INQUIRY` - A card balance inquiry (typically a $0 authorization) has
    occurred on a card. _ `CLEARING` - Card Transaction is settled. _
    `CORRECTION_DEBIT` - Manual card transaction correction (Debit). _
    `CORRECTION_CREDIT` - Manual card transaction correction (Credit). _
    `CREDIT_AUTHORIZATION` - A refund or credit card authorization from a merchant.
    _ `CREDIT_AUTHORIZATION_ADVICE` - A credit card authorization was approved on
    your behalf by the network. _ `FINANCIAL_AUTHORIZATION` - A request from a
    merchant to debit card funds without additional clearing. _
    `FINANCIAL_CREDIT_AUTHORIZATION` - A request from a merchant to refund or credit
    card funds without additional clearing. _ `RETURN` - A card refund has been
    processed on the transaction. _ `RETURN_REVERSAL` - A card refund has been
    reversed (e.g., when a merchant reverses an incorrect refund). _ `TRANSFER` -
    Successful internal transfer of funds between financial accounts. \\**
    `TRANSFER_INSUFFICIENT_FUNDS` - Declined internal transfer of funds due to
    insufficient balance of the sender.
    """

    financial_account_token: str
    """Globally unique identifier for a financial account"""

    financial_transaction_token: str
    """Globally unique identifier for a financial transaction"""

    settled_date: date
    """Date that the transaction settled"""

    card_token: Optional[str] = None
    """Globally unique identifier for a card"""

    descriptor: Optional[str] = None


class StatementLineItems(BaseModel):
    data: List[Data]

    has_more: bool
