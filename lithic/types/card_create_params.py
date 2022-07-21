# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..types import shared_params

__all__ = ["CardCreateParams"]


class CardCreateParams(TypedDict, total=False):
    type: Required[Literal["MERCHANT_LOCKED", "PHYSICAL", "SINGLE_USE", "VIRTUAL"]]
    """Card types:

    - `MERCHANT_LOCKED` - Card is locked to first merchant that successfully
      authorizes the card.
    - `PHYSICAL` - Manufactured and sent to the cardholder. We offer white label
      branding, credit, ATM, PIN debit, chip/EMV, NFC and magstripe functionality.
      Reach out at [lithic.com/contact](https://lithic.com/contact) for more
      information.
    - `SINGLE_USE` - Card will close shortly after the first transaction.
    - `VIRTUAL` - Card will authorize at any merchant and can be added to a digital
      wallet like Apple Pay or Google Pay (if the card program is digital
      wallet-enabled).
    """

    account_token: str
    """Only required for multi-account users.

    Token identifying the account the card will be associated with. Only applicable
    if using account holder enrollment. See
    [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
    more information.
    """

    card_program_token: str
    """Identifies the card program under which to create the card.

    Different card programs may have their own configurations (e.g., digital wallet
    card art, BIN type). This must be configured with Lithic before use.
    """

    exp_month: str
    """Two digit (MM) expiry month.

    If neither `exp_month` nor `exp_year` is provided, an expiration date will be
    generated.
    """

    exp_year: str
    """Four digit (yyyy) expiry year.

    If neither `exp_month` nor `exp_year` is provided, an expiration date will be
    generated.
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

    product_id: str
    """
    Specifies the configuration (e.g., physical card art) that the card should be
    manufactured with, and only applies to cards of type `PHYSICAL` [beta]. This
    must be configured with Lithic before use.
    """

    shipping_address: shared_params.ShippingAddress

    shipping_method: Literal["STANDARD", "STANDARD_WITH_TRACKING", "EXPEDITED"]
    """Shipping method for the card.

    Only applies to cards of type PHYSICAL [beta]. Use of options besides `STANDARD`
    require additional permissions.

    - `STANDARD` - USPS regular mail or similar international option, with no
      tracking
    - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
      with tracking
    - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
      tracking
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

    state: Literal["OPEN", "PAUSED"]
    """Card state values:

    - `OPEN` - Card will approve authorizations (if they match card and account
      parameters).
    - `PAUSED` - Card will decline authorizations, but can be resumed at a later
      time.
    """
