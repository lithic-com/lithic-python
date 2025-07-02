# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["MerchantLockParametersParam", "Merchant"]


class Merchant(TypedDict, total=False):
    comment: str
    """
    A comment or explanation about the merchant, used internally for rule management
    purposes.
    """

    descriptor: str
    """
    Short description of the merchant, often used to provide more human-readable
    context about the transaction merchant. This is typically the name or label
    shown on transaction summaries.
    """

    merchant_id: str
    """Unique alphanumeric identifier for the payment card acceptor (merchant).

    This attribute specifies the merchant entity that will be locked or referenced
    for authorization rules.
    """


class MerchantLockParametersParam(TypedDict, total=False):
    merchants: Required[Iterable[Merchant]]
    """
    A list of merchant locks defining specific merchants or groups of merchants
    (based on descriptors or IDs) that the lock applies to.
    """
