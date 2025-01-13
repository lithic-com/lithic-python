# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from .spend_limit_duration import SpendLimitDuration

__all__ = ["CardUpdateParams"]


class CardUpdateParams(TypedDict, total=False):
    digital_card_art_token: str
    """
    Specifies the digital card art to be displayed in the user’s digital wallet
    after tokenization. This artwork must be approved by Mastercard and configured
    by Lithic to use. See
    [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).
    """

    memo: str
    """Friendly name to identify the card."""

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
