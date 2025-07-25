# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .spend_limit_duration import SpendLimitDuration

__all__ = ["NonPCICard", "Funding"]


class Funding(BaseModel):
    token: str
    """A globally unique identifier for this FundingAccount."""

    created: datetime
    """
    An RFC 3339 string representing when this funding source was added to the Lithic
    account. This may be `null`. UTC time zone.
    """

    last_four: str
    """The last 4 digits of the account (e.g.

    bank account, debit card) associated with this FundingAccount. This may be null.
    """

    state: Literal["DELETED", "ENABLED", "PENDING"]
    """State of funding source.

    Funding source states: _ `ENABLED` - The funding account is available to use for
    card creation and transactions. _ `PENDING` - The funding account is still being
    verified e.g. bank micro-deposits verification. \\** `DELETED` - The founding
    account has been deleted.
    """

    type: Literal["DEPOSITORY_CHECKING", "DEPOSITORY_SAVINGS"]
    """Types of funding source: \\** `DEPOSITORY_CHECKING` - Bank checking account.

    - `DEPOSITORY_SAVINGS` - Bank savings account.
    """

    account_name: Optional[str] = None
    """Account name identifying the funding source. This may be `null`."""

    nickname: Optional[str] = None
    """The nickname given to the `FundingAccount` or `null` if it has no nickname."""


class NonPCICard(BaseModel):
    token: str
    """Globally unique identifier."""

    account_token: str
    """Globally unique identifier for the account to which the card belongs."""

    card_program_token: str
    """Globally unique identifier for the card program on which the card exists."""

    created: datetime
    """An RFC 3339 timestamp for when the card was created. UTC time zone."""

    funding: Funding
    """Deprecated: Funding account for the card."""

    last_four: str
    """Last four digits of the card number."""

    pin_status: Literal["OK", "BLOCKED", "NOT_SET"]
    """Indicates if a card is blocked due a PIN status issue (e.g.

    excessive incorrect attempts).
    """

    spend_limit: int
    """Amount (in cents) to limit approved authorizations (e.g.

    100000 would be a $1,000 limit). Transaction requests above the spend limit will
    be declined.
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

    state: Literal["CLOSED", "OPEN", "PAUSED", "PENDING_ACTIVATION", "PENDING_FULFILLMENT"]
    """Card state values: \\** `CLOSED` - Card will no longer approve authorizations.

    Closing a card cannot be undone. _ `OPEN` - Card will approve authorizations (if
    they match card and account parameters). _ `PAUSED` - Card will decline
    authorizations, but can be resumed at a later time. _ `PENDING_FULFILLMENT` -
    The initial state for cards of type `PHYSICAL`. The card is provisioned pending
    manufacturing and fulfillment. Cards in this state can accept authorizations for
    e-commerce purchases, but not for "Card Present" purchases where the physical
    card itself is present. _ `PENDING_ACTIVATION` - At regular intervals, cards of
    type `PHYSICAL` in state `PENDING_FULFILLMENT` are sent to the card production
    warehouse and updated to state `PENDING_ACTIVATION`. Similar to
    `PENDING_FULFILLMENT`, cards in this state can be used for e-commerce
    transactions or can be added to mobile wallets. API clients should update the
    card's state to `OPEN` only after the cardholder confirms receipt of the card.
    In sandbox, the same daily batch fulfillment occurs, but no cards are actually
    manufactured.
    """

    type: Literal["MERCHANT_LOCKED", "PHYSICAL", "SINGLE_USE", "VIRTUAL", "UNLOCKED", "DIGITAL_WALLET"]
    """
    Card types: _ `VIRTUAL` - Card will authorize at any merchant and can be added
    to a digital wallet like Apple Pay or Google Pay (if the card program is digital
    wallet-enabled). _ `PHYSICAL` - Manufactured and sent to the cardholder. We
    offer white label branding, credit, ATM, PIN debit, chip/EMV, NFC and magstripe
    functionality. _ `SINGLE_USE` - Card is closed upon first successful
    authorization. _ `MERCHANT_LOCKED` - _[Deprecated]_ Card is locked to the first
    merchant that successfully authorizes the card. _ `UNLOCKED` - _[Deprecated]_
    Similar behavior to VIRTUAL cards, please use VIRTUAL instead. _
    `DIGITAL_WALLET` - _[Deprecated]_ Similar behavior to VIRTUAL cards, please use
    VIRTUAL instead.
    """

    auth_rule_tokens: Optional[List[str]] = None
    """List of identifiers for the Auth Rule(s) that are applied on the card.

    This field is deprecated and will no longer be populated in the `Card` object.
    The key will be removed from the schema in a future release. Use the
    `/auth_rules` endpoints to fetch Auth Rule information instead.
    """

    cardholder_currency: Optional[str] = None
    """3-character alphabetic ISO 4217 code for the currency of the cardholder."""

    comment: Optional[str] = None
    """Additional context or information related to the card."""

    digital_card_art_token: Optional[str] = None
    """
    Specifies the digital card art to be displayed in the user's digital wallet
    after tokenization. This artwork must be approved by Mastercard and configured
    by Lithic to use.
    """

    exp_month: Optional[str] = None
    """Two digit (MM) expiry month."""

    exp_year: Optional[str] = None
    """Four digit (yyyy) expiry year."""

    hostname: Optional[str] = None
    """Hostname of card's locked merchant (will be empty if not applicable)."""

    memo: Optional[str] = None
    """Friendly name to identify the card."""

    network_program_token: Optional[str] = None
    """Globally unique identifier for the card's network program.

    Null if the card is not associated with a network program. Currently applicable
    to Visa cards participating in Account Level Management only
    """

    pending_commands: Optional[List[str]] = None
    """
    Indicates if there are offline PIN changes pending card interaction with an
    offline PIN terminal. Possible commands are: CHANGE_PIN, UNBLOCK_PIN. Applicable
    only to cards issued in markets supporting offline PINs.
    """

    product_id: Optional[str] = None
    """Only applicable to cards of type `PHYSICAL`.

    This must be configured with Lithic before use. Specifies the configuration
    (i.e., physical card art) that the card should be manufactured with.
    """

    replacement_for: Optional[str] = None
    """
    If the card is a replacement for another card, the globally unique identifier
    for the card that was replaced.
    """

    substatus: Optional[
        Literal[
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
    ] = None
    """
    Card state substatus values: _ `LOST` - The physical card is no longer in the
    cardholder's possession due to being lost or never received by the cardholder. _
    `COMPROMISED` - Card information has been exposed, potentially leading to
    unauthorized access. This may involve physical card theft, cloning, or online
    data breaches. _ `DAMAGED` - The physical card is not functioning properly, such
    as having chip failures or a demagnetized magnetic stripe. _
    `END_USER_REQUEST` - The cardholder requested the closure of the card for
    reasons unrelated to fraud or damage, such as switching to a different product
    or closing the account. _ `ISSUER_REQUEST` - The issuer closed the card for
    reasons unrelated to fraud or damage, such as account inactivity, product or
    policy changes, or technology upgrades. _ `NOT_ACTIVE` - The card hasn’t had any
    transaction activity for a specified period, applicable to statuses like
    `PAUSED` or `CLOSED`. _ `SUSPICIOUS_ACTIVITY` - The card has one or more
    suspicious transactions or activities that require review. This can involve
    prompting the cardholder to confirm legitimate use or report confirmed fraud. _
    `INTERNAL_REVIEW` - The card is temporarily paused pending further internal
    review. _ `EXPIRED` - The card has expired and has been closed without being
    reissued. _ `UNDELIVERABLE` - The card cannot be delivered to the cardholder and
    has been returned. \\** `OTHER` - The reason for the status does not fall into any
    of the above categories. A comment can be provided to specify the reason.
    """
