# File generated from our OpenAPI spec by Stainless.

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
    ] = None
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


class FinancialTransaction(BaseModel):
    token: str
    """Globally unique identifier."""

    category: Literal["ACH", "CARD", "TRANSFER"]
    """Status types:

    - `CARD` - Issuing card transaction.
    - `ACH` - Transaction over ACH.
    - `TRANSFER` - Internal transfer of funds between financial accounts in your
      program.
    """

    created: datetime
    """Date and time when the financial transaction first occurred. UTC time zone."""

    currency: str
    """3-digit alphabetic ISO 4217 code for the settling currency of the transaction."""

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

    status: Literal["DECLINED", "EXPIRED", "PENDING", "SETTLED", "VOIDED"]
    """Status types:

    - `DECLINED` - The card transaction was declined.
    - `EXPIRED` - Lithic reversed the card authorization as it has passed its
      expiration time.
    - `PENDING` - Authorization is pending completion from the merchant or pending
      release from ACH hold period
    - `SETTLED` - The financial transaction is completed.
    - `VOIDED` - The merchant has voided the previously pending card authorization.
    """

    updated: datetime
    """Date and time when the financial transaction was last updated. UTC time zone."""
