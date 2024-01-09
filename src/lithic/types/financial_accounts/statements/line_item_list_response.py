# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import date, datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["LineItemListResponse"]


class LineItemListResponse(BaseModel):
    token: str
    """Globally unique identifier for a Statement Line Item"""

    amount: int

    category: Literal["ACH", "CARD", "TRANSFER"]

    created: datetime
    """Timestamp of when the line item was generated"""

    currency: str
    """3-digit alphabetic ISO 4217 code for the settling currency of the transaction"""

    event_type: Literal[
        "ACH_INSUFFICIENT_FUNDS",
        "ACH_ORIGINATION_PENDING",
        "ACH_ORIGINATION_RELEASED",
        "ACH_RECEIPT_PENDING",
        "ACH_RECEIPT_RELEASED",
        "ACH_RETURN",
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
    """Event types:

    - `ACH_INSUFFICIENT_FUNDS` - Attempted ACH origination declined due to
      insufficient balance.
    - `ACH_ORIGINATION_PENDING` - ACH origination pending release from an ACH hold.
    - `ACH_ORIGINATION_RELEASED` - ACH origination released from pending to
      available balance.
    - `ACH_RECEIPT_PENDING` - ACH receipt pending release from an ACH holder.
    - `ACH_RECEIPT_RELEASED` - ACH receipt released from pending to available
      balance.
    - `ACH_RETURN` - ACH origination returned by the Receiving Depository Financial
      Institution.
    - `AUTHORIZATION` - Authorize a card transaction.
    - `AUTHORIZATION_ADVICE` - Advice on a card transaction.
    - `AUTHORIZATION_EXPIRY` - Card Authorization has expired and reversed by
      Lithic.
    - `AUTHORIZATION_REVERSAL` - Card Authorization was reversed by the merchant.
    - `BALANCE_INQUIRY` - A card balance inquiry (typically a $0 authorization) has
      occurred on a card.
    - `CLEARING` - Card Transaction is settled.
    - `CORRECTION_DEBIT` - Manual card transaction correction (Debit).
    - `CORRECTION_CREDIT` - Manual card transaction correction (Credit).
    - `CREDIT_AUTHORIZATION` - A refund or credit card authorization from a
      merchant.
    - `CREDIT_AUTHORIZATION_ADVICE` - A credit card authorization was approved on
      your behalf by the network.
    - `FINANCIAL_AUTHORIZATION` - A request from a merchant to debit card funds
      without additional clearing.
    - `FINANCIAL_CREDIT_AUTHORIZATION` - A request from a merchant to refund or
      credit card funds without additional clearing.
    - `RETURN` - A card refund has been processed on the transaction.
    - `RETURN_REVERSAL` - A card refund has been reversed (e.g., when a merchant
      reverses an incorrect refund).
    - `TRANSFER` - Successful internal transfer of funds between financial accounts.
    - `TRANSFER_INSUFFICIENT_FUNDS` - Declined internl transfer of funds due to
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
