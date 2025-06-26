# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TransactionRetrieveResponse"]


class TransactionRetrieveResponse(BaseModel):
    fraud_status: Literal["SUSPECTED_FRAUD", "FRAUDULENT", "NOT_FRAUDULENT", "NO_REPORTED_FRAUD"]
    """
    The fraud status of the transaction, string (enum) supporting the following
    values:

    - `SUSPECTED_FRAUD`: The transaction is suspected to be fraudulent, but this
      hasn’t been confirmed.
    - `FRAUDULENT`: The transaction is confirmed to be fraudulent. A transaction may
      immediately be moved into this state, or be graduated into this state from the
      `SUSPECTED_FRAUD` state.
    - `NOT_FRAUDULENT`: The transaction is (explicitly) marked as not fraudulent. A
      transaction may immediately be moved into this state, or be graduated into
      this state from the `SUSPECTED_FRAUD` state.
    - `NO_REPORTED_FRAUD`: Indicates that no fraud report exists for the
      transaction. It is the default state for transactions that have not been
      analyzed or associated with any known fraudulent activity.
    """

    transaction_token: str
    """
    The universally unique identifier (UUID) associated with the transaction being
    reported.
    """

    comment: Optional[str] = None
    """Provides additional context or details about the fraud report."""

    created_at: Optional[datetime] = None
    """Timestamp representing when the fraud report was created."""

    fraud_type: Optional[
        Literal[
            "FIRST_PARTY_FRAUD", "ACCOUNT_TAKEOVER", "CARD_COMPROMISED", "IDENTITY_THEFT", "CARDHOLDER_MANIPULATION"
        ]
    ] = None
    """
    Specifies the type or category of fraud that the transaction is suspected or
    confirmed to involve, string (enum) supporting the following values:

    - `FIRST_PARTY_FRAUD`: First-party fraud occurs when a legitimate account or
      cardholder intentionally misuses financial services for personal gain. This
      includes actions such as disputing legitimate transactions to obtain a refund,
      abusing return policies, or defaulting on credit obligations without intent to
      repay.
    - `ACCOUNT_TAKEOVER`: Account takeover fraud occurs when a fraudster gains
      unauthorized access to an existing account, modifies account settings, and
      carries out fraudulent transactions.
    - `CARD_COMPROMISED`: Card compromised fraud occurs when a fraudster gains
      access to card details without taking over the account, such as through
      physical card theft, cloning, or online data breaches.
    - `IDENTITY_THEFT`: Identity theft fraud occurs when a fraudster uses stolen
      personal information, such as Social Security numbers or addresses, to open
      accounts, apply for loans, or conduct financial transactions in someone's
      name.
    - `CARDHOLDER_MANIPULATION`: This type of fraud occurs when a fraudster
      manipulates or coerces a legitimate cardholder into unauthorized transactions,
      often through social engineering tactics.
    """

    updated_at: Optional[datetime] = None
    """Timestamp representing the last update to the fraud report."""
