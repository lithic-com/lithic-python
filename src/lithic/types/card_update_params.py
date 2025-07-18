# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .spend_limit_duration import SpendLimitDuration

__all__ = ["CardUpdateParams"]


class CardUpdateParams(TypedDict, total=False):
    comment: str
    """Additional context or information related to the card."""

    digital_card_art_token: str
    """
    Specifies the digital card art to be displayed in the user’s digital wallet
    after tokenization. This artwork must be approved by Mastercard and configured
    by Lithic to use. See
    [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).
    """

    memo: str
    """Friendly name to identify the card."""

    network_program_token: str
    """Globally unique identifier for the card's network program.

    Currently applicable to Visa cards participating in Account Level Management
    only.
    """

    pin: str
    """Encrypted PIN block (in base64).

    Only applies to cards of type `PHYSICAL` and `VIRTUAL`. Changing PIN also resets
    PIN status to `OK`. See
    [Encrypted PIN Block](https://docs.lithic.com/docs/cards#encrypted-pin-block).
    """

    pin_status: Literal["OK"]
    """Indicates if a card is blocked due a PIN status issue (e.g.

    excessive incorrect attempts). Can only be set to `OK` to unblock a card.
    """

    spend_limit: int
    """Amount (in cents) to limit approved authorizations (e.g.

    100000 would be a $1,000 limit). Transaction requests above the spend limit will
    be declined. Note that a spend limit of 0 is effectively no limit, and should
    only be used to reset or remove a prior limit. Only a limit of 1 or above will
    result in declined transactions due to checks against the card limit.
    """

    spend_limit_duration: SpendLimitDuration
    """Spend limit duration values:

    - `ANNUALLY` - Card will authorize transactions up to spend limit for the
      trailing year.
    - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
      of the card.
    - `MONTHLY` - Card will authorize transactions up to spend limit for the
      trailing month. To support recurring monthly payments, which can occur on
      different day every month, the time window we consider for monthly velocity
      starts 6 days after the current calendar date one month prior.
    - `TRANSACTION` - Card will authorize multiple transactions if each individual
      transaction is under the spend limit.
    """

    state: Literal["CLOSED", "OPEN", "PAUSED"]
    """Card state values:

    - `CLOSED` - Card will no longer approve authorizations. Closing a card cannot
      be undone.
    - `OPEN` - Card will approve authorizations (if they match card and account
      parameters).
    - `PAUSED` - Card will decline authorizations, but can be resumed at a later
      time.
    """

    substatus: Literal[
        "LOST",
        "COMPROMISED",
        "DAMAGED",
        "END_USER_REQUEST",
        "ISSUER_REQUEST",
        "NOT_ACTIVE",
        "SUSPICIOUS_ACTIVITY",
        "INTERNAL_REVIEW",
        "EXPIRED",
        "UNDELIVERABLE",
        "OTHER",
    ]
    """Card state substatus values:

    - `LOST` - The physical card is no longer in the cardholder's possession due to
      being lost or never received by the cardholder.
    - `COMPROMISED` - Card information has been exposed, potentially leading to
      unauthorized access. This may involve physical card theft, cloning, or online
      data breaches.
    - `DAMAGED` - The physical card is not functioning properly, such as having chip
      failures or a demagnetized magnetic stripe.
    - `END_USER_REQUEST` - The cardholder requested the closure of the card for
      reasons unrelated to fraud or damage, such as switching to a different product
      or closing the account.
    - `ISSUER_REQUEST` - The issuer closed the card for reasons unrelated to fraud
      or damage, such as account inactivity, product or policy changes, or
      technology upgrades.
    - `NOT_ACTIVE` - The card hasn’t had any transaction activity for a specified
      period, applicable to statuses like `PAUSED` or `CLOSED`.
    - `SUSPICIOUS_ACTIVITY` - The card has one or more suspicious transactions or
      activities that require review. This can involve prompting the cardholder to
      confirm legitimate use or report confirmed fraud.
    - `INTERNAL_REVIEW` - The card is temporarily paused pending further internal
      review.
    - `EXPIRED` - The card has expired and has been closed without being reissued.
    - `UNDELIVERABLE` - The card cannot be delivered to the cardholder and has been
      returned.
    - `OTHER` - The reason for the status does not fall into any of the above
      categories. A comment should be provided to specify the reason.
    """
