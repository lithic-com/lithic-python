# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BookTransferCreateParams"]


class BookTransferCreateParams(TypedDict, total=False):
    amount: Required[int]
    """Amount to be transferred in the currency’s smallest unit (e.g., cents for USD).

    This should always be a positive value.
    """

    category: Required[
        Literal["ADJUSTMENT", "BALANCE_OR_FUNDING", "DERECOGNITION", "DISPUTE", "FEE", "REWARD", "TRANSFER"]
    ]
    """Category of the book transfer"""

    from_financial_account_token: Required[str]
    """
    Globally unique identifier for the financial account or card that will send the
    funds. Accepted type dependent on the program's use case.
    """

    subtype: Required[str]
    """The program specific subtype code for the specified category/type."""

    to_financial_account_token: Required[str]
    """
    Globally unique identifier for the financial account or card that will receive
    the funds. Accepted type dependent on the program's use case.
    """

    type: Required[
        Literal[
            "ATM_WITHDRAWAL",
            "ATM_DECLINE",
            "INTERNATIONAL_ATM_WITHDRAWAL",
            "INACTIVITY",
            "STATEMENT",
            "MONTHLY",
            "QUARTERLY",
            "ANNUAL",
            "CUSTOMER_SERVICE",
            "ACCOUNT_MAINTENANCE",
            "ACCOUNT_ACTIVATION",
            "ACCOUNT_CLOSURE",
            "CARD_REPLACEMENT",
            "CARD_DELIVERY",
            "CARD_CREATE",
            "CURRENCY_CONVERSION",
            "INTEREST",
            "LATE_PAYMENT",
            "BILL_PAYMENT",
            "CASH_BACK",
            "ACCOUNT_TO_ACCOUNT",
            "CARD_TO_CARD",
            "DISBURSE",
            "BILLING_ERROR",
            "LOSS_WRITE_OFF",
            "EXPIRED_CARD",
            "EARLY_DERECOGNITION",
            "ESCHEATMENT",
            "INACTIVITY_FEE_DOWN",
            "PROVISIONAL_CREDIT",
            "DISPUTE_WON",
            "TRANSFER",
        ]
    ]
    """Type of book_transfer"""

    token: str
    """Customer-provided token that will serve as an idempotency token.

    This token will become the transaction token.
    """

    memo: str
    """Optional descriptor for the transfer."""
