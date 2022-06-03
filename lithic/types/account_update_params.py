# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["VerificationAddress", "AccountUpdateParams"]


class VerificationAddress(TypedDict, total=False):
    address1: str

    address2: str

    city: str

    country: str

    postal_code: str

    state: str


class AccountUpdateParams(TypedDict, total=False):
    daily_spend_limit: int
    """Amount (in cents) for the account's new daily spend limit."""

    lifetime_spend_limit: int
    """Amount (in cents) for the account's new lifetime limit.

    Once this limit is reached, no transactions will be accepted on any card created
    for this account until the limit is updated.
    """

    monthly_spend_limit: int
    """Amount (in cents) for the account's new monthly spend limit."""

    state: Literal["ACTIVE", "PAUSED"]
    """Account states."""

    verification_address: VerificationAddress
    """
    Address used during Address Verification Service (AVS) checks during
    transactions if enabled via Auth Rules.
    """
