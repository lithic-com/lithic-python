# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..types import funding_source
from .._models import BaseModel

__all__ = ["Card"]


class Card(BaseModel):
    created: str
    """An ISO 8601 timestamp for when the card was created. UTC time zone."""

    funding: funding_source.FundingSource

    last_four: str
    """Last four digits of the card number."""

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

    state: Literal["CLOSED", "OPEN", "PAUSED", "PENDING_ACTIVATION", "PENDING_FULFILLMENT"]
    """Card state values:

    - `CLOSED` - Card will no longer approve authorizations. Closing a card cannot
      be undone.
    - `OPEN` - Card will approve authorizations (if they match card and account
      parameters).
    - `PAUSED` - Card will decline authorizations, but can be resumed at a later
      time.
    - `PENDING_FULFILLMENT` - The initial state for cards of type `PHYSICAL`. The
      card is provisioned pending manufacturing and fulfillment. Cards in this state
      can accept authorizations for e-commerce purchases, but not for "Card Present"
      purchases where the physical card itself is present.
    - `PENDING_ACTIVATION` - Each business day at 2pm Eastern Time Zone (ET), cards
      of type `PHYSICAL` in state `PENDING_FULFILLMENT` are sent to the card
      production warehouse and updated to state `PENDING_ACTIVATION` . Similar to
      `PENDING_FULFILLMENT`, cards in this state can be used for e-commerce
      transactions. API clients should update the card's state to `OPEN` only after
      the cardholder confirms receipt of the card.

    In sandbox, the same daily batch fulfillment occurs, but no cards are actually
    manufactured.
    """

    token: str
    """Globally unique identifier."""

    type: Literal["MERCHANT_LOCKED", "PHYSICAL", "SINGLE_USE", "VIRTUAL"]
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

    auth_rule_tokens: Optional[List[str]]
    """List of identifiers for the Auth Rule(s) that are applied on the card."""

    cvv: Optional[str]
    """Three digit cvv printed on the back of the card."""

    exp_month: Optional[str]
    """Two digit (MM) expiry month."""

    exp_year: Optional[str]
    """Four digit (yyyy) expiry year."""

    hostname: Optional[str]
    """Hostname of card’s locked merchant (will be empty if not applicable)."""

    memo: Optional[str]
    """Friendly name to identify the card."""

    pan: Optional[str]
    """Primary Account Number (PAN) (i.e.

    the card number). Customers must be PCI compliant to have PAN returned as a
    field in production. Please contact
    [support@lithic.com](mailto:support@lithic.com) for questions.
    """
