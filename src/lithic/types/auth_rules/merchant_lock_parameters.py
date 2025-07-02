# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MerchantLockParameters", "Merchant"]


class Merchant(BaseModel):
    comment: Optional[str] = None
    """
    A comment or explanation about the merchant, used internally for rule management
    purposes.
    """

    descriptor: Optional[str] = None
    """
    Short description of the merchant, often used to provide more human-readable
    context about the transaction merchant. This is typically the name or label
    shown on transaction summaries.
    """

    merchant_id: Optional[str] = None
    """Unique alphanumeric identifier for the payment card acceptor (merchant).

    This attribute specifies the merchant entity that will be locked or referenced
    for authorization rules.
    """


class MerchantLockParameters(BaseModel):
    merchants: List[Merchant]
    """
    A list of merchant locks defining specific merchants or groups of merchants
    (based on descriptors or IDs) that the lock applies to.
    """
