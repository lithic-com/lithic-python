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
    ] = None
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
