# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.currency import Currency

__all__ = [
    "Transaction",
    "Amounts",
    "AmountsCardholder",
    "AmountsHold",
    "AmountsMerchant",
    "AmountsSettlement",
    "Avs",
    "CardholderAuthentication",
    "Merchant",
    "Pos",
    "PosEntryMode",
    "PosTerminal",
    "TokenInfo",
    "Event",
    "EventAmounts",
    "EventAmountsCardholder",
    "EventAmountsMerchant",
    "EventAmountsSettlement",
]


class AmountsCardholder(BaseModel):
    amount: int
    """The aggregate settled amount in the cardholder's local currency."""

    conversion_rate: str
    """
    The conversion rate used to convert the merchant amount to the cardholder
    amount.
    """

    currency: Currency
    """ISO 4217 currency.

    Its enumerants are ISO 4217 currencies except for some special currencies like
    `XXX`. Enumerants names are lowercase currency code e.g. `EUR`, `USD`.
    """


class AmountsHold(BaseModel):
    amount: int
    """The aggregate pending amount in the anticipated settlement currency."""

    currency: Currency
    """ISO 4217 currency.

    Its enumerants are ISO 4217 currencies except for some special currencies like
    `XXX`. Enumerants names are lowercase currency code e.g. `EUR`, `USD`.
    """


class AmountsMerchant(BaseModel):
    amount: int
    """The aggregate settled amount in the merchant's local currency."""

    currency: Currency
    """ISO 4217 currency.

    Its enumerants are ISO 4217 currencies except for some special currencies like
    `XXX`. Enumerants names are lowercase currency code e.g. `EUR`, `USD`.
    """


class AmountsSettlement(BaseModel):
    amount: int
    """The aggregate settled amount in the settlement currency."""

    currency: Currency
    """ISO 4217 currency.

    Its enumerants are ISO 4217 currencies except for some special currencies like
    `XXX`. Enumerants names are lowercase currency code e.g. `EUR`, `USD`.
    """


class Amounts(BaseModel):
    cardholder: AmountsCardholder

    hold: AmountsHold

    merchant: AmountsMerchant

    settlement: AmountsSettlement


class Avs(BaseModel):
    address: str
    """Cardholder address"""

    zipcode: str
    """Cardholder ZIP code"""


class CardholderAuthentication(BaseModel):
    three_ds_version: Optional[str] = FieldInfo(alias="3ds_version", default=None)
    """The 3DS version used for the authentication"""

    acquirer_exemption: Literal[
        "AUTHENTICATION_OUTAGE_EXCEPTION",
        "LOW_VALUE",
        "MERCHANT_INITIATED_TRANSACTION",
        "NONE",
        "RECURRING_PAYMENT",
        "SECURE_CORPORATE_PAYMENT",
        "STRONG_CUSTOMER_AUTHENTICATION_DELEGATION",
        "TRANSACTION_RISK_ANALYSIS",
    ]
    """Whether an acquirer exemption applied to the transaction."""

    authentication_result: Literal["ATTEMPTS", "DECLINE", "NONE", "SUCCESS"]
    """Indicates what the outcome of the 3DS authentication process is."""

    decision_made_by: Literal["CUSTOMER_ENDPOINT", "LITHIC_DEFAULT", "LITHIC_RULES", "NETWORK", "UNKNOWN"]
    """Indicates which party made the 3DS authentication decision."""

    liability_shift: Literal["3DS_AUTHENTICATED", "ACQUIRER_EXEMPTION", "NONE", "TOKEN_AUTHENTICATED"]
    """Indicates whether chargeback liability shift applies to the transaction.

    Possible enum values:

        * `3DS_AUTHENTICATED`: The transaction was fully authenticated through a 3-D Secure flow, chargeback liability shift applies.

        * `ACQUIRER_EXEMPTION`: The acquirer utilised an exemption to bypass Strong Customer Authentication (`transStatus = N`, or `transStatus = I`). Liability remains with the acquirer and in this case the `acquirer_exemption` field is expected to be not `NONE`.

        * `NONE`: Chargeback liability shift has not shifted to the issuer, i.e. the merchant is liable.

    - `TOKEN_AUTHENTICATED`: The transaction was a tokenized payment with validated
      cryptography, possibly recurring. Chargeback liability shift to the issuer
      applies.
    """

    three_ds_authentication_token: Optional[str] = None
    """
    Unique identifier you can use to match a given 3DS authentication (available via
    the three_ds_authentication.created event webhook) and the transaction. Note
    that in cases where liability shift does not occur, this token is matched to the
    transaction on a best-effort basis.
    """

    verification_attempted: Literal["NONE", "OTHER"]
    """
    Indicates whether a 3DS challenge flow was used, and if so, what the
    verification method was. (deprecated, use `authentication_result`)
    """

    verification_result: Literal["CANCELLED", "FAILED", "FRICTIONLESS", "NOT_ATTEMPTED", "REJECTED", "SUCCESS"]
    """Indicates whether a transaction is considered 3DS authenticated.

    (deprecated, use `authentication_result`)
    """


class Merchant(BaseModel):
    acceptor_id: str
    """Unique alphanumeric identifier for the payment card acceptor (merchant)."""

    acquiring_institution_id: str
    """Unique numeric identifier of the acquiring institution."""

    city: str
    """City of card acceptor.

    Note that in many cases, particularly in card-not-present transactions,
    merchants may send through a phone number or URL in this field.
    """

    country: str
    """Country or entity of card acceptor.

    Possible values are: (1) all ISO 3166-1 alpha-3 country codes, (2) QZZ for
    Kosovo, and (3) ANT for Netherlands Antilles.
    """

    descriptor: str
    """Short description of card acceptor."""

    mcc: str
    """Merchant category code (MCC).

    A four-digit number listed in ISO 18245. An MCC is used to classify a business
    by the types of goods or services it provides.
    """

    state: str
    """Geographic state of card acceptor."""


class PosEntryMode(BaseModel):
    card: Literal["NOT_PRESENT", "PREAUTHORIZED", "PRESENT", "UNKNOWN"]
    """Card presence indicator"""

    cardholder: Literal[
        "DEFERRED_BILLING",
        "ELECTRONIC_ORDER",
        "INSTALLMENT",
        "MAIL_ORDER",
        "NOT_PRESENT",
        "PREAUTHORIZED",
        "PRESENT",
        "REOCCURRING",
        "TELEPHONE_ORDER",
        "UNKNOWN",
    ]
    """Cardholder presence indicator"""

    pan: Literal[
        "AUTO_ENTRY",
        "BAR_CODE",
        "CONTACTLESS",
        "CREDENTIAL_ON_FILE",
        "ECOMMERCE",
        "ERROR_KEYED",
        "ERROR_MAGNETIC_STRIPE",
        "ICC",
        "KEY_ENTERED",
        "MAGNETIC_STRIPE",
        "MANUAL",
        "OCR",
        "SECURE_CARDLESS",
        "UNKNOWN",
        "UNSPECIFIED",
    ]
    """Method of entry for the PAN"""

    pin_entered: bool
    """Indicates whether the cardholder entered the PIN. True if the PIN was entered."""


class PosTerminal(BaseModel):
    attended: bool
    """True if a clerk is present at the sale."""

    card_retention_capable: bool
    """True if the terminal is capable of retaining the card."""

    on_premise: bool
    """True if the sale was made at the place of business (vs. mobile)."""

    operator: Literal["ADMINISTRATIVE", "CARDHOLDER", "CARD_ACCEPTOR", "UNKNOWN"]
    """The person that is designated to swipe the card"""

    partial_approval_capable: bool
    """True if the terminal is capable of partial approval.

    Partial approval is when part of a transaction is approved and another payment
    must be used for the remainder. Example scenario: A $40 transaction is attempted
    on a prepaid card with a $25 balance. If partial approval is enabled, $25 can be
    authorized, at which point the POS will prompt the user for an additional
    payment of $15.
    """

    pin_capability: Literal["CAPABLE", "INOPERATIVE", "NOT_CAPABLE", "UNSPECIFIED"]
    """Status of whether the POS is able to accept PINs"""

    type: Literal[
        "ADMINISTRATIVE",
        "ATM",
        "AUTHORIZATION",
        "COUPON_MACHINE",
        "DIAL_TERMINAL",
        "ECOMMERCE",
        "ECR",
        "FUEL_MACHINE",
        "HOME_TERMINAL",
        "MICR",
        "OFF_PREMISE",
        "PAYMENT",
        "PDA",
        "PHONE",
        "POINT",
        "POS_TERMINAL",
        "PUBLIC_UTILITY",
        "SELF_SERVICE",
        "TELEVISION",
        "TELLER",
        "TRAVELERS_CHECK_MACHINE",
        "VENDING",
        "VOICE",
        "UNKNOWN",
    ]
    """POS Type"""


class Pos(BaseModel):
    entry_mode: PosEntryMode

    terminal: PosTerminal


class TokenInfo(BaseModel):
    wallet_type: Literal["APPLE_PAY", "GOOGLE_PAY", "MASTERPASS", "MERCHANT", "OTHER", "SAMSUNG_PAY"]
    """The wallet_type field will indicate the source of the token.

    Possible token sources include digital wallets (Apple, Google, or Samsung Pay),
    merchant tokenization, and “other” sources like in-flight commerce. Masterpass
    is not currently supported and is included for future use.
    """


class EventAmountsCardholder(BaseModel):
    amount: int
    """The amount in the cardholder's local currency."""

    conversion_rate: str
    """
    The conversion rate used to convert the merchant amount to the cardholder
    amount.
    """

    currency: Currency
    """ISO 4217 currency.

    Its enumerants are ISO 4217 currencies except for some special currencies like
    `XXX`. Enumerants names are lowercase currency code e.g. `EUR`, `USD`.
    """


class EventAmountsMerchant(BaseModel):
    amount: int
    """The amount in the merchant's local currency."""

    currency: Currency
    """ISO 4217 currency.

    Its enumerants are ISO 4217 currencies except for some special currencies like
    `XXX`. Enumerants names are lowercase currency code e.g. `EUR`, `USD`.
    """


class EventAmountsSettlement(BaseModel):
    amount: int
    """The amount in the settlement currency."""

    conversion_rate: str
    """Conversion rate used to convert the merchant amount to the settlement amount."""

    currency: Currency
    """ISO 4217 currency.

    Its enumerants are ISO 4217 currencies except for some special currencies like
    `XXX`. Enumerants names are lowercase currency code e.g. `EUR`, `USD`.
    """


class EventAmounts(BaseModel):
    cardholder: EventAmountsCardholder

    merchant: EventAmountsMerchant

    settlement: Optional[EventAmountsSettlement] = None


class Event(BaseModel):
    token: str
    """Transaction event identifier."""

    amount: int
    """Amount of the transaction event (in cents), including any acquirer fees."""

    amounts: EventAmounts

    created: datetime
    """RFC 3339 date and time this event entered the system. UTC time zone."""

    detailed_results: List[
        Literal[
            "ACCOUNT_DAILY_SPEND_LIMIT_EXCEEDED",
            "ACCOUNT_DELINQUENT",
            "ACCOUNT_INACTIVE",
            "ACCOUNT_LIFETIME_SPEND_LIMIT_EXCEEDED",
            "ACCOUNT_MONTHLY_SPEND_LIMIT_EXCEEDED",
            "ACCOUNT_UNDER_REVIEW",
            "ADDRESS_INCORRECT",
            "APPROVED",
            "AUTH_RULE_ALLOWED_COUNTRY",
            "AUTH_RULE_ALLOWED_MCC",
            "AUTH_RULE_BLOCKED_COUNTRY",
            "AUTH_RULE_BLOCKED_MCC",
            "CARD_CLOSED",
            "CARD_CRYPTOGRAM_VALIDATION_FAILURE",
            "CARD_EXPIRED",
            "CARD_EXPIRY_DATE_INCORRECT",
            "CARD_INVALID",
            "CARD_NOT_ACTIVATED",
            "CARD_PAUSED",
            "CARD_PIN_INCORRECT",
            "CARD_RESTRICTED",
            "CARD_SECURITY_CODE_INCORRECT",
            "CARD_SPEND_LIMIT_EXCEEDED",
            "CONTACT_CARD_ISSUER",
            "CUSTOMER_ASA_TIMEOUT",
            "CUSTOM_ASA_RESULT",
            "DECLINED",
            "DO_NOT_HONOR",
            "DRIVER_NUMBER_INVALID",
            "FORMAT_ERROR",
            "INSUFFICIENT_FUNDING_SOURCE_BALANCE",
            "INSUFFICIENT_FUNDS",
            "LITHIC_SYSTEM_ERROR",
            "LITHIC_SYSTEM_RATE_LIMIT",
            "MALFORMED_ASA_RESPONSE",
            "MERCHANT_INVALID",
            "MERCHANT_LOCKED_CARD_ATTEMPTED_ELSEWHERE",
            "MERCHANT_NOT_PERMITTED",
            "OVER_REVERSAL_ATTEMPTED",
            "PROGRAM_CARD_SPEND_LIMIT_EXCEEDED",
            "PROGRAM_SUSPENDED",
            "PROGRAM_USAGE_RESTRICTION",
            "REVERSAL_UNMATCHED",
            "SECURITY_VIOLATION",
            "SINGLE_USE_CARD_REATTEMPTED",
            "TRANSACTION_INVALID",
            "TRANSACTION_NOT_PERMITTED_TO_ACQUIRER_OR_TERMINAL",
            "TRANSACTION_NOT_PERMITTED_TO_ISSUER_OR_CARDHOLDER",
            "TRANSACTION_PREVIOUSLY_COMPLETED",
            "UNAUTHORIZED_MERCHANT",
            "VEHICLE_NUMBER_INVALID",
        ]
    ]

    effective_polarity: Literal["CREDIT", "DEBIT"]
    """Indicates whether the transaction event is a credit or debit to the account."""

    result: Literal[
        "ACCOUNT_STATE_TRANSACTION_FAIL",
        "APPROVED",
        "BANK_CONNECTION_ERROR",
        "BANK_NOT_VERIFIED",
        "CARD_CLOSED",
        "CARD_PAUSED",
        "FRAUD_ADVICE",
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
    """Result of the transaction."""

    type: Literal[
        "AUTHORIZATION",
        "AUTHORIZATION_ADVICE",
        "AUTHORIZATION_EXPIRY",
        "AUTHORIZATION_REVERSAL",
        "BALANCE_INQUIRY",
        "CLEARING",
        "CORRECTION_CREDIT",
        "CORRECTION_DEBIT",
        "CREDIT_AUTHORIZATION",
        "CREDIT_AUTHORIZATION_ADVICE",
        "FINANCIAL_AUTHORIZATION",
        "FINANCIAL_CREDIT_AUTHORIZATION",
        "RETURN",
        "RETURN_REVERSAL",
    ]
    """Type of transaction event"""


class Transaction(BaseModel):
    token: str
    """Globally unique identifier."""

    account_token: str
    """The token for the account associated with this transaction."""

    acquirer_fee: Optional[int] = None
    """
    Fee assessed by the merchant and paid for by the cardholder in the smallest unit
    of the currency. Will be zero if no fee is assessed. Rebates may be transmitted
    as a negative value to indicate credited fees.
    """

    acquirer_reference_number: Optional[str] = None
    """
    Unique identifier assigned to a transaction by the acquirer that can be used in
    dispute and chargeback filing.
    """

    amount: int
    """Authorization amount of the transaction (in cents), including any acquirer fees.

    This may change over time, and will represent the settled amount once the
    transaction is settled.
    """

    amounts: Amounts

    authorization_amount: Optional[int] = None
    """Authorization amount (in cents) of the transaction, including any acquirer fees.

    This amount always represents the amount authorized for the transaction,
    unaffected by settlement.
    """

    authorization_code: Optional[str] = None
    """
    A fixed-width 6-digit numeric identifier that can be used to identify a
    transaction with networks.
    """

    avs: Optional[Avs] = None

    card_token: str
    """Token for the card used in this transaction."""

    cardholder_authentication: Optional[CardholderAuthentication] = None

    created: datetime
    """Date and time when the transaction first occurred. UTC time zone."""

    merchant: Merchant

    merchant_amount: Optional[int] = None
    """
    Analogous to the 'amount' property, but will represent the amount in the
    transaction's local currency (smallest unit), including any acquirer fees.
    """

    merchant_authorization_amount: Optional[int] = None
    """
    Analogous to the 'authorization_amount' property, but will represent the amount
    in the transaction's local currency (smallest unit), including any acquirer
    fees.
    """

    merchant_currency: str
    """3-digit alphabetic ISO 4217 code for the local currency of the transaction."""

    network: Optional[Literal["INTERLINK", "MAESTRO", "MASTERCARD", "UNKNOWN", "VISA"]] = None
    """Card network of the authorization.

    Can be `INTERLINK`, `MAESTRO`, `MASTERCARD`, `VISA`, or `UNKNOWN`. Value is
    `UNKNOWN` when Lithic cannot determine the network code from the upstream
    provider.
    """

    network_risk_score: Optional[int] = None
    """
    Network-provided score assessing risk level associated with a given
    authorization. Scores are on a range of 0-999, with 0 representing the lowest
    risk and 999 representing the highest risk. For Visa transactions, where the raw
    score has a range of 0-99, Lithic will normalize the score by multiplying the
    raw score by 10x.
    """

    pos: Pos

    result: Literal[
        "APPROVED",
        "BANK_CONNECTION_ERROR",
        "BANK_NOT_VERIFIED",
        "CARD_CLOSED",
        "CARD_PAUSED",
        "DECLINED",
        "FRAUD_ADVICE",
        "INACTIVE_ACCOUNT",
        "INCORRECT_PIN",
        "INSUFFICIENT_FUNDS",
        "INVALID_CARD_DETAILS",
        "MERCHANT_BLACKLIST",
        "SINGLE_USE_RECHARGED",
        "SWITCH_INOPERATIVE_ADVICE",
        "UNAUTHORIZED_MERCHANT",
        "UNKNOWN_HOST_TIMEOUT",
        "USER_TRANSACTION_LIMIT",
    ]
    """`APPROVED` or decline reason. See Event result types"""

    settled_amount: int
    """
    Amount of the transaction that has been settled (in cents), including any
    acquirer fees. This may change over time.
    """

    status: Literal["DECLINED", "EXPIRED", "PENDING", "SETTLED", "VOIDED"]
    """Status of the transaction."""

    token_info: Optional[TokenInfo] = None

    updated: datetime
    """Date and time when the transaction last updated. UTC time zone."""

    events: Optional[List[Event]] = None
