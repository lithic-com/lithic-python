# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthenticationSimulateParams", "Merchant", "Transaction"]


class AuthenticationSimulateParams(TypedDict, total=False):
    merchant: Required[Merchant]

    pan: Required[str]
    """Sixteen digit card number."""

    transaction: Required[Transaction]


class Merchant(TypedDict, total=False):
    id: Required[str]
    """Unique identifier to identify the payment card acceptor.

    Corresponds to `merchant_acceptor_id` in authorization.
    """

    country: Required[str]
    """
    Country of the address provided by the cardholder in ISO 3166-1 alpha-3 format
    (e.g. USA)
    """

    mcc: Required[str]
    """Merchant category code for the transaction to be simulated.

    A four-digit number listed in ISO 18245. Supported merchant category codes can
    be found
    [here](https://docs.lithic.com/docs/transactions#merchant-category-codes-mccs).
    """

    name: Required[str]
    """Merchant descriptor, corresponds to `descriptor` in authorization."""


class Transaction(TypedDict, total=False):
    amount: Required[int]
    """Amount (in cents) to authenticate."""

    currency: Required[str]
    """3-digit alphabetic ISO 4217 currency code."""
