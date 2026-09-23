# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransactionSimulateReturnParams"]


class TransactionSimulateReturnParams(TypedDict, total=False):
    amount: Required[int]
    """Amount (in cents) to authorize."""

    descriptor: Required[str]
    """Merchant descriptor."""

    pan: Required[str]
    """Sixteen digit card number."""

    billing_currency: str
    """3-character alphabetic ISO 4217 currency code for the cardholder billing amount.

    Permitted values are USD, GBP, EUR and CAD, and any other ISO 4217 code returns
    a 422. Defaults to USD
    """

    settlement_currency: str
    """3-character alphabetic ISO 4217 currency code for the settlement amount.

    Permitted values are USD, GBP, EUR and CAD, and any other ISO 4217 code returns
    a 422. Defaults to the value of billing_currency
    """
