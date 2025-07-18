# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AccountUpdateParams", "VerificationAddress"]


class AccountUpdateParams(TypedDict, total=False):
    comment: str
    """Additional context or information related to the account."""

    daily_spend_limit: int
    """Amount (in cents) for the account's daily spend limit (e.g.

    100000 would be a $1,000 limit). By default the daily spend limit is set to
    $1,250.
    """

    lifetime_spend_limit: int
    """Amount (in cents) for the account's lifetime spend limit (e.g.

    100000 would be a $1,000 limit). Once this limit is reached, no transactions
    will be accepted on any card created for this account until the limit is
    updated. Note that a spend limit of 0 is effectively no limit, and should only
    be used to reset or remove a prior limit. Only a limit of 1 or above will result
    in declined transactions due to checks against the account limit. This behavior
    differs from the daily spend limit and the monthly spend limit.
    """

    monthly_spend_limit: int
    """Amount (in cents) for the account's monthly spend limit (e.g.

    100000 would be a $1,000 limit). By default the monthly spend limit is set to
    $5,000.
    """

    state: Literal["ACTIVE", "PAUSED", "CLOSED"]
    """Account states."""

    substatus: Literal[
        "FRAUD_IDENTIFIED",
        "SUSPICIOUS_ACTIVITY",
        "RISK_VIOLATION",
        "END_USER_REQUEST",
        "ISSUER_REQUEST",
        "NOT_ACTIVE",
        "INTERNAL_REVIEW",
        "OTHER",
    ]
    """Account state substatus values:

    - `FRAUD_IDENTIFIED` - The account has been recognized as being created or used
      with stolen or fabricated identity information, encompassing both true
      identity theft and synthetic identities.
    - `SUSPICIOUS_ACTIVITY` - The account has exhibited suspicious behavior, such as
      unauthorized access or fraudulent transactions, necessitating further
      investigation.
    - `RISK_VIOLATION` - The account has been involved in deliberate misuse by the
      legitimate account holder. Examples include disputing valid transactions
      without cause, falsely claiming non-receipt of goods, or engaging in
      intentional bust-out schemes to exploit account services.
    - `END_USER_REQUEST` - The account holder has voluntarily requested the closure
      of the account for personal reasons. This encompasses situations such as
      bankruptcy, other financial considerations, or the account holder's death.
    - `ISSUER_REQUEST` - The issuer has initiated the closure of the account due to
      business strategy, risk management, inactivity, product changes, regulatory
      concerns, or violations of terms and conditions.
    - `NOT_ACTIVE` - The account has not had any transactions or payment activity
      within a specified period. This status applies to accounts that are paused or
      closed due to inactivity.
    - `INTERNAL_REVIEW` - The account is temporarily paused pending further internal
      review. In future implementations, this status may prevent clients from
      activating the account via APIs until the review is completed.
    - `OTHER` - The reason for the account's current status does not fall into any
      of the above categories. A comment should be provided to specify the
      particular reason.
    """

    verification_address: VerificationAddress
    """
    Address used during Address Verification Service (AVS) checks during
    transactions if enabled via Auth Rules. This field is deprecated as AVS checks
    are no longer supported by Auth Rules. The field will be removed from the schema
    in a future release.
    """


class VerificationAddress(TypedDict, total=False):
    address1: str

    address2: str

    city: str

    country: str

    postal_code: str

    state: str
