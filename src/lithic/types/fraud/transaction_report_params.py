# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransactionReportParams"]


class TransactionReportParams(TypedDict, total=False):
    fraud_status: Required[Literal["SUSPECTED_FRAUD", "FRAUDULENT", "NOT_FRAUDULENT"]]
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
    """

    comment: str
    """
    Optional field providing additional information or context about why the
    transaction is considered fraudulent.
    """

    fraud_type: Literal[
        "FIRST_PARTY_FRAUD", "ACCOUNT_TAKEOVER", "CARD_COMPROMISED", "IDENTITY_THEFT", "CARDHOLDER_MANIPULATION"
    ]
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
