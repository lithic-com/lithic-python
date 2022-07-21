# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CardUpdateParams"]


class CardUpdateParams(TypedDict, total=False):
    account_token: str
    """Only required for multi-account users.

    Token identifying the account the card will be associated with. Only applicable
    if using account holder enrollment. See
    [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
    more information.
    """

    auth_rule_token: str
    """
    Identifier for any Auth Rules that will be applied to transactions taking place
    with the card.
    """

    funding_token: str
    """
    The token for the desired `FundingAccount` to use when making transactions with
    this card.
    """

    memo: str
    """Friendly name to identify the card."""

    pin: str
    """Encrypted PIN block (in base64).

    Only applies to cards of type `PHYSICAL` and `VIRTUAL`. See
    [Encrypted PIN Block](https://docs.lithic.com/docs/cards#encrypted-pin-block-enterprise).
    """

    spend_limit: int
    """Amount (in cents) to limit approved authorizations.

    Transaction requests above the spend limit will be declined.
    """

    spend_limit_duration: Literal["ANNUALLY", "FOREVER", "MONTHLY", "TRANSACTION"]
    """Spend limit duration values:

    - `ANNUALLY` - Card will authorize transactions up to spend limit in a calendar
      year.
    - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
      of the card.
    - `MONTHLY` - Card will authorize transactions up to spend limit for the
      trailing month. Month is calculated as this calendar date one month prior.
    - `TRANSACTION` - Card will authorizate multiple transactions if each individual
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
