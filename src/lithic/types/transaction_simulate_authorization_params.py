# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransactionSimulateAuthorizationParams"]


class TransactionSimulateAuthorizationParams(TypedDict, total=False):
    amount: Required[int]
    """Amount (in cents) to authorize.

    For credit authorizations and financial credit authorizations, any value entered
    will be converted into a negative amount in the simulated transaction. For
    example, entering 100 in this field will appear as a -100 amount in the
    transaction. For balance inquiries, this field must be set to 0.
    """

    descriptor: Required[str]
    """Merchant descriptor."""

    pan: Required[str]
    """Sixteen digit card number."""

    merchant_acceptor_id: str
    """Unique identifier to identify the payment card acceptor."""

    merchant_amount: int
    """
    Amount of the transaction to be simulated in currency specified in
    merchant_currency, including any acquirer fees.
    """

    merchant_currency: str
    """3-digit alphabetic ISO 4217 currency code."""

    partial_approval_capable: bool
    """
    Set to true if the terminal is capable of partial approval otherwise false.
    Partial approval is when part of a transaction is approved and another payment
    must be used for the remainder.
    """

    status: Literal[
        "AUTHORIZATION",
        "BALANCE_INQUIRY",
        "CREDIT_AUTHORIZATION",
        "FINANCIAL_AUTHORIZATION",
        "FINANCIAL_CREDIT_AUTHORIZATION",
    ]
    """Type of event to simulate.

    - `AUTHORIZATION` is a dual message purchase authorization, meaning a subsequent
      clearing step is required to settle the transaction.
    - `BALANCE_INQUIRY` is a $0 authorization that includes a request for the
      balance held on the card, and is most typically seen when a cardholder
      requests to view a card's balance at an ATM.
    - `CREDIT_AUTHORIZATION` is a dual message request from a merchant to authorize
      a refund or credit, meaning a subsequent clearing step is required to settle
      the transaction.
    - `FINANCIAL_AUTHORIZATION` is a single message request from a merchant to debit
      funds immediately (such as an ATM withdrawal), and no subsequent clearing is
      required to settle the transaction.
    - `FINANCIAL_CREDIT_AUTHORIZATION` is a single message request from a merchant
      to credit funds immediately, and no subsequent clearing is required to settle
      the transaction.
    """
