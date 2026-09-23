# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransactionSimulateAuthorizationParams"]


class TransactionSimulateAuthorizationParams(TypedDict, total=False):
    amount: Required[int]
    """Amount (in cents) to authorize.

    For credit authorizations and financial credit authorizations, any value entered
    will be converted into a negative amount in the simulated transaction. For
    example, entering 100 in this field will result in a -100 amount in the
    transaction. For balance inquiries, this field must be set to 0.
    """

    descriptor: Required[str]
    """Merchant descriptor."""

    pan: Required[str]
    """Sixteen digit card number."""

    billing_currency: str
    """3-character alphabetic ISO 4217 currency code for the cardholder billing amount.

    Permitted values are USD, GBP, EUR and CAD, and any other ISO 4217 code returns
    a 422. Defaults to USD
    """

    mcc: str
    """Merchant category code for the transaction to be simulated.

    A four-digit number listed in ISO 18245. Supported merchant category codes can
    be found
    [here](https://docs.lithic.com/docs/transactions#merchant-category-codes-mccs).
    """

    merchant_acceptor_city: str
    """Merchant acceptor city"""

    merchant_acceptor_country: str
    """Merchant acceptor country code (ISO 3166-1 alpha-3)"""

    merchant_acceptor_id: str
    """Unique identifier to identify the payment card acceptor."""

    merchant_acceptor_state: str
    """Merchant acceptor state/province (ISO 3166-2 subdivision code)"""

    merchant_amount: int
    """
    Amount of the transaction to be simulated in currency specified in
    merchant_currency, including any acquirer fees.
    """

    merchant_currency: str
    """3-character alphabetic ISO 4217 currency code for the merchant amount.

    Only used when merchant_amount is set, and defaults to GBP in that case. Without
    merchant_amount, the merchant amount uses the billing currency. Permitted values
    are USD, GBP, EUR and CAD, and any other ISO 4217 code returns a 422
    """

    partial_approval_capable: bool
    """
    Set to true if the terminal is capable of partial approval otherwise false.
    Partial approval is when part of a transaction is approved and another payment
    must be used for the remainder.
    """

    pin: str
    """Simulate entering a PIN. If omitted, PIN check will not be performed."""

    settlement_currency: str
    """3-character alphabetic ISO 4217 currency code for the settlement amount.

    Permitted values are USD, GBP, EUR and CAD, and any other ISO 4217 code returns
    a 422. Defaults to the value of billing_currency. Only single message
    (financial) authorizations carry a settlement amount, and the value is ignored
    for dual message authorizations
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
    - `BALANCE_INQUIRY` is a $0 authorization requesting the balance held on the
      card, and is most often observed when a cardholder requests to view a card's
      balance at an ATM.
    - `CREDIT_AUTHORIZATION` is a dual message request from a merchant to authorize
      a refund, meaning a subsequent clearing step is required to settle the
      transaction.
    - `FINANCIAL_AUTHORIZATION` is a single message request from a merchant to debit
      funds immediately (such as an ATM withdrawal), and no subsequent clearing is
      required to settle the transaction.
    - `FINANCIAL_CREDIT_AUTHORIZATION` is a single message request from a merchant
      to credit funds immediately, and no subsequent clearing is required to settle
      the transaction.
    """
