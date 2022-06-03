# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..types import card
from .._models import BaseModel

__all__ = ["Events", "Funding", "Merchant", "Transaction"]


class Events(BaseModel):
    amount: int
    """Amount (in cents) of the transaction event."""

    created: str
    """ISO 8601 date and time this event entered the system. UTC time zone."""

    result: Literal[
        "ACCOUNT_STATE_TRANSACTION",
        "APPROVED",
        "BANK_CONNECTION_ERROR",
        "BANK_NOT_VERIFIED",
        "CARD_CLOSED",
        "CARD_PAUSED",
        "FRAUD_ADVICE",
        "GLOBAL_TRANSACTION_LIMIT",
        "GLOBAL_WEEKLY_LIMIT",
        "GLOBAL_MONTHLY_LIMIT",
        "INACTIVE_ACCOUNT",
        "INCORRECT_PIN",
        "INVALID_CARD_DETAILS",
        "INSUFFICIENT_FUNDS",
        "MERCHANT_BLACKLIST",
        "SINGLE_USE_RECHARGED",
        "SWITCH_INOPERATIVE_ADVICE",
        "UNAUTHORIZED_MERCHANT",
        "UNKNOWN_HOST_TIMEOUT",
        "USER_TRANSACTION_LIMIT",
    ]
    """`APPROVED` or decline reason.

    Result types:

    - `ACCOUNT_STATE_TRANSACTION_FAIL` - Contact
      [support@lithic.com](mailto:support@lithic.com).
    - `APPROVED` - Transaction is approved.
    - `BANK_CONNECTION_ERROR` - Please reconnect a funding source.
    - `BANK_NOT_VERIFIED` - Please confirm the funding source.
    - `CARD_CLOSED` - Card state was closed at the time of authorization.
    - `CARD_PAUSED` - Card state was paused at the time of authorization.
    - `FRAUD_ADVICE` - Transaction declined due to risk.
    - `GLOBAL_TRANSACTION_LIMIT` - Platform spend limit exceeded, contact
      [support@lithic.com](mailto:support@lithic.com).
    - `GLOBAL_WEEKLY_LIMIT` - Platform spend limit exceeded, contact
      [support@lithic.com](mailto:support@lithic.com).
    - `GLOBAL_MONTHLY_LIMIT` - Platform spend limit exceeded, contact
      [support@lithic.com](mailto:support@lithic.com).
    - `INACTIVE_ACCOUNT` - Account is inactive. Contact
      [support@lithic.com](mailto:support@lithic.com).
    - `INCORRECT_PIN` - PIN verification failed.
    - `INVALID_CARD_DETAILS` - Incorrect CVV or expiry date.
    - `INSUFFICIENT_FUNDS` - Please ensure the funding source is connected and up to
      date.
    - `MERCHANT_BLACKLIST` - This merchant is disallowed on the platform.
    - `SINGLE_USE_RECHARGED` - Single use card attempted multiple times.
    - `SWITCH_INOPERATIVE_ADVICE` - Network error, re-attempt the transaction.
    - `UNAUTHORIZED_MERCHANT` - Merchant locked card attempted at different
      merchant.
    - `UNKNOWN_HOST_TIMEOUT` - Network error, re-attempt the transaction.
    - `USER_TRANSACTION_LIMIT` - User-set spend limit exceeded.
    """

    token: str
    """Globally unique identifier."""

    type: Literal[
        "AUTHORIZATION", "AUTHORIZATION_ADVICE", "CLEARING", "RETURN", "VOID", "CORRECTION_DEBIT", "CORRECTION_CREDIT"
    ]
    """Event types:

    - `AUTHORIZATION` - Authorize a transaction.
    - `AUTHORIZATION_ADVICE` - Advice on a transaction.
    - `CLEARING` - Transaction is settled.
    - `RETURN` - A return authorization.
    - `VOID` - Transaction is voided.
    - `CORRECTION_DEBIT` - Manual transaction correction (Debit).
    - `CORRECTION_CREDIT` - Manual transaction correction (Credit).
    """


class Funding(BaseModel):
    amount: Optional[int]
    """Funding amount (in cents)."""

    token: Optional[str]
    """Funding account token."""

    type: Optional[Literal["DEPOSITORY_CHECKING", "DEPOSITORY_SAVINGS", "PROMO"]]
    """Types of funding:

    - `DEPOSITORY_CHECKING` - Bank checking account.
    - `DEPOSITORY_SAVINGS` - Bank savings account.
    - `PROMO` - Any promotional credit was used in paying for this transaction.
    """


class Merchant(BaseModel):
    acceptor_id: Optional[str]
    """Unique identifier to identify the payment card acceptor."""

    city: Optional[str]
    """City of card acceptor."""

    country: Optional[str]
    """Uppercase country of card acceptor (see ISO 8583 specs)."""

    descriptor: Optional[str]
    """Short description of card acceptor."""

    mcc: Optional[str]
    """Merchant category code (MCC).

    A four-digit number listed in ISO 18245. An MCC is used to classify a business
    by the types of goods or services it provides.
    """

    state: Optional[str]
    """Geographic state of card acceptor (see ISO 8583 specs)."""


class Transaction(BaseModel):
    amount: Optional[int]
    """Authorization amount (in USD cents) of the transaction.

    This may change over time, and will represent the settled amount once the
    transaction is settled.
    """

    authorization_amount: Optional[int]
    """Authorization amount (in USD cents) of the transaction.

    This amount always represents the amount authorized for the transaction,
    unaffected by settlement.
    """

    authorization_code: Optional[str]
    """
    A fixed-width 6-digit numeric identifier that can be used to identify a
    transaction with networks.
    """

    card: Optional[card.Card]

    created: Optional[str]
    """Date and time when the transaction first occurred. UTC time zone."""

    events: Optional[List[Events]]
    """A list of all events that have modified this transaction."""

    funding: Optional[List[Funding]]
    """
    A list of objects that describe how this transaction was funded, with the
    `amount` represented in cents. A reference to the funding account for the `card`
    that made this transaction may appear here and the `token` will match the
    `token` for the funding account in the `card` field. If any promotional credit
    was used in paying for this transaction, its `type` will be `PROMO`.
    """

    merchant: Optional[Merchant]

    merchant_amount: Optional[int]
    """
    Analogous to the "amount" property, but represents the amount in the local
    currency at the time of the transaction.
    """

    merchant_authorization_amount: Optional[int]
    """
    Analogous to the "authorization_amount" property, but represents the amount in
    the local currency at the time of the transaction.
    """

    merchant_currency: Optional[str]
    """3-digit alphabetic ISO 4217 code for the local currency of the transaction."""

    network: Optional[Optional[Literal["INTERLINK", "MAESTRO", "MASTERCARD", "VISA", "UNKNOWN"]]]
    """Card network of the authorization.

    Can be `INTERLINK`, `MAESTRO`, `MASTERCARD`, `VISA`, or `UNKNOWN`. Value is
    `UNKNOWN` when Lithic cannot determine the network code from the upstream
    provider.
    """

    result: Optional[
        Literal[
            "ACCOUNT_STATE_TRANSACTION",
            "APPROVED",
            "BANK_CONNECTION_ERROR",
            "BANK_NOT_VERIFIED",
            "CARD_CLOSED",
            "CARD_PAUSED",
            "FRAUD_ADVICE",
            "GLOBAL_TRANSACTION_LIMIT",
            "GLOBAL_WEEKLY_LIMIT",
            "GLOBAL_MONTHLY_LIMIT",
            "INACTIVE_ACCOUNT",
            "INCORRECT_PIN",
            "INVALID_CARD_DETAILS",
            "INSUFFICIENT_FUNDS",
            "MERCHANT_BLACKLIST",
            "SINGLE_USE_RECHARGED",
            "SWITCH_INOPERATIVE_ADVICE",
            "UNAUTHORIZED_MERCHANT",
            "UNKNOWN_HOST_TIMEOUT",
            "USER_TRANSACTION_LIMIT",
        ]
    ]
    """`APPROVED` or decline reason. See Event result types"""

    settled_amount: Optional[int]
    """Amount (in cents) of the transaction that has been settled.

    This may change over time.
    """

    status: Optional[Literal["BOUNCED", "DECLINED", "PENDING", "SETTLED", "SETTLING", "VOIDED"]]
    """Status types:

    - `BOUNCED` - There was an error settling the transaction against the funding
      source. Your API account may be disabled.
    - `DECLINED` - The transaction was declined.
    - `PENDING` - Authorization is pending completion from the merchant.
    - `SETTLED` - The transaction is complete.
    - `SETTLING` - The merchant has completed the transaction and the funding source
      is being debited.
    - `VOIDED` - The merchant has voided the previously pending authorization.
    """

    token: Optional[str]
    """Globally unique identifier."""
