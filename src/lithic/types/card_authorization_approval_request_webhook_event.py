# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .token_info import TokenInfo
from .shared.merchant import Merchant
from .cardholder_authentication import CardholderAuthentication

__all__ = [
    "CardAuthorizationApprovalRequestWebhookEvent",
    "Avs",
    "Card",
    "FleetInfo",
    "LatestChallenge",
    "NetworkSpecificData",
    "NetworkSpecificDataMastercard",
    "NetworkSpecificDataMastercardOnBehalfServiceResult",
    "NetworkSpecificDataVisa",
    "Pos",
    "PosEntryMode",
    "PosTerminal",
]


class Avs(BaseModel):
    address: str
    """Cardholder address"""

    address_on_file_match: Literal["MATCH", "MATCH_ADDRESS_ONLY", "MATCH_ZIP_ONLY", "MISMATCH", "NOT_PRESENT"]
    """
    Lithic's evaluation result comparing the transaction's address data with the
    cardholder KYC data if it exists. In the event Lithic does not have any
    Cardholder KYC data, or the transaction does not contain any address data,
    NOT_PRESENT will be returned
    """

    zipcode: str
    """Cardholder ZIP code"""


class Card(BaseModel):
    """Card object in ASA"""

    token: Optional[str] = None
    """Globally unique identifier for the card."""

    hostname: Optional[str] = None
    """Hostname of card’s locked merchant (will be empty if not applicable)"""

    last_four: Optional[str] = None
    """Last four digits of the card number"""

    memo: Optional[str] = None
    """Customizable name to identify the card.

    We recommend against using this field to store JSON data as it can cause
    unexpected behavior.
    """

    spend_limit: Optional[int] = None
    """Amount (in cents) to limit approved authorizations.

    Purchase requests above the spend limit will be declined (refunds and credits
    will be approved).

    Note that while spend limits are enforced based on authorized and settled volume
    on a card, they are not recommended to be used for balance or
    reconciliation-level accuracy. Spend limits also cannot block force posted
    charges (i.e., when a merchant sends a clearing message without a prior
    authorization).
    """

    spend_limit_duration: Optional[Literal["ANNUALLY", "FOREVER", "MONTHLY", "TRANSACTION"]] = None
    """
    Note that to support recurring monthly payments, which can occur on different
    day every month, the time window we consider for MONTHLY velocity starts 6 days
    after the current calendar date one month prior.
    """

    state: Optional[Literal["CLOSED", "OPEN", "PAUSED", "PENDING_ACTIVATION", "PENDING_FULFILLMENT"]] = None

    type: Optional[Literal["SINGLE_USE", "MERCHANT_LOCKED", "UNLOCKED", "PHYSICAL", "DIGITAL_WALLET", "VIRTUAL"]] = None


class FleetInfo(BaseModel):
    """
    Optional Object containing information if the Card is a part of a Fleet managed program
    """

    fleet_prompt_code: Literal["NO_PROMPT", "VEHICLE_NUMBER", "DRIVER_NUMBER"]
    """Code indicating what the driver was prompted to enter at time of purchase.

    This is configured at a program level and is a static configuration, and does
    not change on a request to request basis
    """

    fleet_restriction_code: Literal["NO_RESTRICTIONS", "FUEL_ONLY"]
    """Code indicating which restrictions, if any, there are on purchase.

    This is configured at a program level and is a static configuration, and does
    not change on a request to request basis
    """

    driver_number: Optional[str] = None
    """Number representing the driver"""

    vehicle_number: Optional[str] = None
    """Number associated with the vehicle"""


class LatestChallenge(BaseModel):
    """
    The latest Authorization Challenge that was issued to the cardholder for this merchant.
    """

    phone_number: str
    """The phone number used for sending Authorization Challenge SMS."""

    status: Literal["COMPLETED", "PENDING", "EXPIRED", "ERROR"]
    """The status of the Authorization Challenge

    - `COMPLETED` - Challenge was successfully completed by the cardholder
    - `PENDING` - Challenge is still open
    - `EXPIRED` - Challenge has expired without being completed
    - `ERROR` - There was an error processing the challenge
    """

    completed_at: Optional[datetime] = None
    """The date and time when the Authorization Challenge was completed in UTC.

    Present only if the status is `COMPLETED`.
    """


class NetworkSpecificDataMastercardOnBehalfServiceResult(BaseModel):
    result_1: str
    """Indicates the results of the service processing."""

    result_2: str
    """Identifies the results of the service processing."""

    service: str
    """Indicates the service performed on the transaction."""


class NetworkSpecificDataMastercard(BaseModel):
    ecommerce_security_level_indicator: Optional[str] = None
    """Indicates the electronic commerce security level and UCAF collection."""

    on_behalf_service_result: Optional[List[NetworkSpecificDataMastercardOnBehalfServiceResult]] = None
    """The On-behalf Service performed on the transaction and the results.

    Contains all applicable, on-behalf service results that were performed on a
    given transaction.
    """

    transaction_type_identifier: Optional[str] = None
    """Indicates the type of additional transaction purpose."""


class NetworkSpecificDataVisa(BaseModel):
    business_application_identifier: Optional[str] = None
    """
    Identifies the purpose or category of a transaction, used to classify and
    process transactions according to Visa’s rules.
    """


class NetworkSpecificData(BaseModel):
    """
    Contains raw data provided by the card network, including attributes that provide further context about the authorization. If populated by the network, data is organized by Lithic and passed through without further modification. Please consult the official network documentation for more details about these values and how to use them. This object is only available to certain programs- contact your Customer Success Manager to discuss enabling access.
    """

    mastercard: Optional[NetworkSpecificDataMastercard] = None

    visa: Optional[NetworkSpecificDataVisa] = None


class PosEntryMode(BaseModel):
    """POS > Entry Mode object in ASA"""

    card: Optional[Literal["PRESENT", "NOT_PRESENT", "UNKNOWN"]] = None
    """Card Presence Indicator"""

    cardholder: Optional[
        Literal[
            "DEFERRED_BILLING",
            "ELECTRONIC_ORDER",
            "INSTALLMENT",
            "MAIL_ORDER",
            "NOT_PRESENT",
            "PRESENT",
            "REOCCURRING",
            "TELEPHONE_ORDER",
            "UNKNOWN",
        ]
    ] = None
    """Cardholder Presence Indicator"""

    pan: Optional[
        Literal[
            "AUTO_ENTRY",
            "BAR_CODE",
            "CONTACTLESS",
            "ECOMMERCE",
            "ERROR_KEYED",
            "ERROR_MAGNETIC_STRIPE",
            "ICC",
            "KEY_ENTERED",
            "MAGNETIC_STRIPE",
            "MANUAL",
            "OCR",
            "SECURE_CARDLESS",
            "UNSPECIFIED",
            "UNKNOWN",
            "CREDENTIAL_ON_FILE",
        ]
    ] = None
    """Method of entry for the PAN"""

    pin_entered: Optional[bool] = None
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

    acceptor_terminal_id: Optional[str] = None
    """
    Uniquely identifies a terminal at the card acceptor location of acquiring
    institutions or merchant POS Systems. Left justified with trailing spaces.
    """


class Pos(BaseModel):
    entry_mode: Optional[PosEntryMode] = None
    """POS > Entry Mode object in ASA"""

    terminal: Optional[PosTerminal] = None


class CardAuthorizationApprovalRequestWebhookEvent(BaseModel):
    token: str
    """The provisional transaction group uuid associated with the authorization"""

    acquirer_fee: int
    """Fee (in cents) assessed by the merchant and paid for by the cardholder.

    Will be zero if no fee is assessed. Rebates may be transmitted as a negative
    value to indicate credited fees.
    """

    amount: int
    """Authorization amount of the transaction (in cents), including any acquirer fees.

    The contents of this field are identical to `authorization_amount`.
    """

    authorization_amount: int
    """The base transaction amount (in cents) plus the acquirer fee field.

    This is the amount the issuer should authorize against unless the issuer is
    paying the acquirer fee on behalf of the cardholder.
    """

    avs: Avs

    card: Card
    """Card object in ASA"""

    cardholder_currency: str
    """3-character alphabetic ISO 4217 code for cardholder's billing currency."""

    cash_amount: int
    """
    The portion of the transaction requested as cash back by the cardholder, and
    does not include any acquirer fees. The amount field includes the purchase
    amount, the requested cash back amount, and any acquirer fees.

    If no cash back was requested, the value of this field will be 0, and the field
    will always be present.
    """

    created: datetime
    """Date and time when the transaction first occurred in UTC."""

    event_type: Literal["card_authorization.approval_request"]

    merchant: Merchant

    merchant_amount: int
    """
    The amount that the merchant will receive, denominated in `merchant_currency`
    and in the smallest currency unit. Note the amount includes `acquirer_fee`,
    similar to `authorization_amount`. It will be different from
    `authorization_amount` if the merchant is taking payment in a different
    currency.
    """

    merchant_currency: str
    """3-character alphabetic ISO 4217 code for the local currency of the transaction."""

    settled_amount: int
    """
    Amount (in cents) of the transaction that has been settled, including any
    acquirer fees
    """

    status: Literal[
        "AUTHORIZATION",
        "CREDIT_AUTHORIZATION",
        "FINANCIAL_AUTHORIZATION",
        "FINANCIAL_CREDIT_AUTHORIZATION",
        "BALANCE_INQUIRY",
    ]
    """The type of authorization request that this request is for.

    Note that `CREDIT_AUTHORIZATION` and `FINANCIAL_CREDIT_AUTHORIZATION` is only
    available to users with credit decisioning via ASA enabled.
    """

    transaction_initiator: Literal["CARDHOLDER", "MERCHANT", "UNKNOWN"]
    """The entity that initiated the transaction."""

    account_type: Optional[Literal["CHECKING", "SAVINGS"]] = None

    cardholder_authentication: Optional[CardholderAuthentication] = None

    cashback: Optional[int] = None
    """Deprecated, use `cash_amount`."""

    conversion_rate: Optional[float] = None
    """
    If the transaction was requested in a currency other than the settlement
    currency, this field will be populated to indicate the rate used to translate
    the merchant_amount to the amount (i.e., `merchant_amount` x `conversion_rate` =
    `amount`). Note that the `merchant_amount` is in the local currency and the
    amount is in the settlement currency.
    """

    event_token: Optional[str] = None
    """The event token associated with the authorization.

    This field is only set for programs enrolled into the beta.
    """

    fleet_info: Optional[FleetInfo] = None
    """
    Optional Object containing information if the Card is a part of a Fleet managed
    program
    """

    latest_challenge: Optional[LatestChallenge] = None
    """
    The latest Authorization Challenge that was issued to the cardholder for this
    merchant.
    """

    network: Optional[Literal["AMEX", "INTERLINK", "MAESTRO", "MASTERCARD", "UNKNOWN", "VISA"]] = None
    """Card network of the authorization."""

    network_risk_score: Optional[int] = None
    """
    Network-provided score assessing risk level associated with a given
    authorization. Scores are on a range of 0-999, with 0 representing the lowest
    risk and 999 representing the highest risk. For Visa transactions, where the raw
    score has a range of 0-99, Lithic will normalize the score by multiplying the
    raw score by 10x.
    """

    network_specific_data: Optional[NetworkSpecificData] = None
    """
    Contains raw data provided by the card network, including attributes that
    provide further context about the authorization. If populated by the network,
    data is organized by Lithic and passed through without further modification.
    Please consult the official network documentation for more details about these
    values and how to use them. This object is only available to certain programs-
    contact your Customer Success Manager to discuss enabling access.
    """

    pos: Optional[Pos] = None

    token_info: Optional[TokenInfo] = None

    ttl: Optional[datetime] = None
    """Deprecated: approximate time-to-live for the authorization."""
