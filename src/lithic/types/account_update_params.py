# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AccountUpdateParams", "VerificationAddress"]


class AccountUpdateParams(TypedDict, total=False):
    daily_spend_limit: int
    """
    Amount (in cents) for the account's daily spend limit. By default the daily
    spend limit is set to $1,250.
    """

    lifetime_spend_limit: int
    """Amount (in cents) for the account's lifetime spend limit.

    Once this limit is reached, no transactions will be accepted on any card created
    for this account until the limit is updated. Note that a spend limit of 0 is
    effectively no limit, and should only be used to reset or remove a prior limit.
    Only a limit of 1 or above will result in declined transactions due to checks
    against the account limit. This behavior differs from the daily spend limit and
    the monthly spend limit.
    """

    monthly_spend_limit: int
    """
    Amount (in cents) for the account's monthly spend limit. By default the monthly
    spend limit is set to $5,000.
    """

    state: Literal["ACTIVE", "PAUSED"]
    """Account states."""

    verification_address: VerificationAddress
    """
    Address used during Address Verification Service (AVS) checks during
    transactions if enabled via Auth Rules.
    """


class VerificationAddress(TypedDict, total=False):
    address1: str

    address2: str

    city: str

    country: str

    postal_code: str

    state: str
