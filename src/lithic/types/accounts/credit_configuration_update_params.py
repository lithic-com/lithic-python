# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CreditConfigurationUpdateParams"]


class CreditConfigurationUpdateParams(TypedDict, total=False):
    billing_period: int
    """Number of days within the billing period"""

    credit_limit: int
    """Credit limit extended to the Business Account"""

    external_bank_account_token: str
    """The external bank account token to use for auto-collections"""

    payment_period: int
    """Number of days after the billing period ends that a payment is required"""
