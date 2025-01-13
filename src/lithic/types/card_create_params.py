# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .spend_limit_duration import SpendLimitDuration
from .shared_params.carrier import Carrier
from .shared_params.shipping_address import ShippingAddress

__all__ = ["CardCreateParams"]


class CardCreateParams(TypedDict, total=False):
    type: Required[Literal["MERCHANT_LOCKED", "PHYSICAL", "SINGLE_USE", "VIRTUAL", "UNLOCKED", "DIGITAL_WALLET"]]
    """Card types:

    - `VIRTUAL` - Card will authorize at any merchant and can be added to a digital
      wallet like Apple Pay or Google Pay (if the card program is digital
      wallet-enabled).
    - `PHYSICAL` - Manufactured and sent to the cardholder. We offer white label
      branding, credit, ATM, PIN debit, chip/EMV, NFC and magstripe functionality.
      Reach out at [lithic.com/contact](https://lithic.com/contact) for more
      information.
    - `SINGLE_USE` - Card is closed upon first successful authorization.
    - `MERCHANT_LOCKED` - _[Deprecated]_ Card is locked to the first merchant that
      successfully authorizes the card.
    - `UNLOCKED` - _[Deprecated]_ Similar behavior to VIRTUAL cards, please use
      VIRTUAL instead.
    - `DIGITAL_WALLET` - _[Deprecated]_ Similar behavior to VIRTUAL cards, please
      use VIRTUAL instead.
    """

    account_token: str
    """Globally unique identifier for the account that the card will be associated
    with.

    Required for programs enrolling users using the
    [/account_holders endpoint](https://docs.lithic.com/docs/account-holders-kyc).
    See [Managing Your Program](doc:managing-your-program) for more information.
    """

    card_program_token: str
    """For card programs with more than one BIN range.

    This must be configured with Lithic before use. Identifies the card program/BIN
    range under which to create the card. If omitted, will utilize the program's
    default `card_program_token`. In Sandbox, use
    00000000-0000-0000-1000-000000000000 and 00000000-0000-0000-2000-000000000000 to
    test creating cards on specific card programs.
    """

    carrier: Carrier

    digital_card_art_token: str
    """
    Specifies the digital card art to be displayed in the user’s digital wallet
    after tokenization. This artwork must be approved by Mastercard and configured
    by Lithic to use. See
    [Flexible Card Art Guide](https://docs.lithic.com/docs/about-digital-wallets#flexible-card-art).
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

    memo: str
    """Friendly name to identify the card."""

    pin: str
    """Encrypted PIN block (in base64).

    Applies to cards of type `PHYSICAL` and `VIRTUAL`. See
    [Encrypted PIN Block](https://docs.lithic.com/docs/cards#encrypted-pin-block).
    """

    product_id: str
    """Only applicable to cards of type `PHYSICAL`.

    This must be configured with Lithic before use. Specifies the configuration
    (i.e., physical card art) that the card should be manufactured with.
    """

    replacement_account_token: str
    """Restricted field limited to select use cases.

    Lithic will reach out directly if this field should be used. Globally unique
    identifier for the replacement card's account. If this field is specified,
    `replacement_for` must also be specified. If `replacement_for` is specified and
    this field is omitted, the replacement card's account will be inferred from the
    card being replaced.
    """

    replacement_for: str
    """Globally unique identifier for the card that this card will replace.

    If the card type is `PHYSICAL` it will be replaced by a `PHYSICAL` card. If the
    card type is `VIRTUAL` it will be replaced by a `VIRTUAL` card.
    """

    shipping_address: ShippingAddress

    shipping_method: Literal["2_DAY", "EXPEDITED", "EXPRESS", "PRIORITY", "STANDARD", "STANDARD_WITH_TRACKING"]
    """Shipping method for the card.

    Only applies to cards of type PHYSICAL. Use of options besides `STANDARD`
    require additional permissions.

    - `STANDARD` - USPS regular mail or similar international option, with no
      tracking
    - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
      with tracking
    - `PRIORITY` - USPS Priority, 1-3 day shipping, with tracking
    - `EXPRESS` - FedEx Express, 3-day shipping, with tracking
    - `2_DAY` - FedEx 2-day shipping, with tracking
    - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
      tracking
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

    state: Literal["OPEN", "PAUSED"]
    """Card state values:

    - `OPEN` - Card will approve authorizations (if they match card and account
      parameters).
    - `PAUSED` - Card will decline authorizations, but can be resumed at a later
      time.
    """
