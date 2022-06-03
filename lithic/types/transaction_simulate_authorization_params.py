# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TransactionSimulateAuthorizationParams"]


class TransactionSimulateAuthorizationParams(TypedDict, total=False):
    amount: Required[int]
    """Amount (in cents) to authorize."""

    descriptor: Required[str]
    """Merchant descriptor."""

    pan: Required[str]
    """Sixteen digit card number."""

    merchant_amount: int
    """
    Amount of the transaction to be simlated in currency specified in
    merchant_currency.
    """

    merchant_currency: str
    """3-digit alphabetic ISO 4217 currency code."""

    status: Literal[
        "AUTHORIZATION", "CREDIT_AUTHORIZATION", "FINANCIAL_AUTHORIZATION", "FINANCIAL_CREDIT_AUTHORIZATION"
    ]
    """Type of event to simulate.

    - `CREDIT` indicates funds flow towards the user rather than towards the
      merchant.
    - `FINANCIAL` indicates that this is a single message transaction that completes
      immediately if approved.
    """
