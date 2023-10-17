# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["BusinessAccount", "CollectionsConfiguration"]


class CollectionsConfiguration(BaseModel):
    billing_period: int
    """Number of days within the billing period"""

    payment_period: int
    """Number of days after the billing period ends that a payment is required"""

    external_bank_account_token: Optional[str] = None
    """The external bank account token to use for auto-collections"""


class BusinessAccount(BaseModel):
    token: str
    """Account token"""

    collections_configuration: Optional[CollectionsConfiguration] = None

    credit_limit: Optional[int] = None
    """Credit limit extended to the Account"""
