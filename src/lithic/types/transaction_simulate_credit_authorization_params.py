# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TransactionSimulateCreditAuthorizationParams"]


class TransactionSimulateCreditAuthorizationParams(TypedDict, total=False):
    amount: Required[int]
    """Amount (in cents).

    Any value entered will be converted into a negative amount in the simulated
    transaction. For example, entering 100 in this field will appear as a -100
    amount in the transaction.
    """

    descriptor: Required[str]
    """Merchant descriptor."""

    pan: Required[str]
    """Sixteen digit card number."""

    mcc: str
    """Merchant category code for the transaction to be simulated.

    A four-digit number listed in ISO 18245. Supported merchant category codes can
    be found
    [here](https://docs.lithic.com/docs/transactions#merchant-category-codes-mccs).
    """

    merchant_acceptor_id: str
    """Unique identifier to identify the payment card acceptor."""
