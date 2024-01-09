# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Transaction", "Event", "Merchant", "CardholderAuthentication"]


class Event(BaseModel):
    token: str
    """Globally unique identifier."""

    amount: int
    """Amount of the transaction event (in cents), including any acquirer fees."""

    created: datetime
    """RFC 3339 date and time this event entered the system. UTC time zone."""

    detailed_results: List[
        Literal[
            "ACCOUNT_DAILY_SPEND_LIMIT_EXCEEDED",
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
        ]
    ]

    result: Literal[
        "ACCOUNT_STATE_TRANSACTION",
        "APPROVED",
        "BANK_CONNECTION_ERROR",
        "BANK_NOT_VERIFIED",
        "CARD_CLOSED",
        "CARD_PAUSED",
        "FRAUD_ADVICE",
        "GLOBAL_MONTHLY_LIMIT",
        "GLOBAL_TRANSACTION_LIMIT",
        "GLOBAL_WEEKLY_LIMIT",
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
        "VOID",
    ]
    """Event types:

    - `AUTHORIZATION` - Authorize a transaction.
    - `AUTHORIZATION_ADVICE` - Advice on a transaction.
    - `AUTHORIZATION_EXPIRY` - Authorization has expired and reversed by Lithic.
    - `AUTHORIZATION_REVERSAL` - Authorization was reversed by the merchant.
    - `BALANCE_INQUIRY` - A balance inquiry (typically a $0 authorization) has
      occurred on a card.
    - `CLEARING` - Transaction is settled.
    - `CORRECTION_DEBIT` - Manual transaction correction (Debit).
    - `CORRECTION_CREDIT` - Manual transaction correction (Credit).
    - `CREDIT_AUTHORIZATION` - A refund or credit authorization from a merchant.
    - `CREDIT_AUTHORIZATION_ADVICE` - A credit authorization was approved on your
      behalf by the network.
    - `FINANCIAL_AUTHORIZATION` - A request from a merchant to debit funds without
      additional clearing.
    - `FINANCIAL_CREDIT_AUTHORIZATION` - A request from a merchant to refund or
      credit funds without additional clearing.
    - `RETURN` - A refund has been processed on the transaction.
    - `RETURN_REVERSAL` - A refund has been reversed (e.g., when a merchant reverses
      an incorrect refund).
    """


class Merchant(BaseModel):
    acceptor_id: Optional[str] = None
    """Unique identifier to identify the payment card acceptor."""

    city: Optional[str] = None
    """City of card acceptor."""

    country: Optional[str] = None
    """Uppercase country of card acceptor (see ISO 8583 specs)."""

    descriptor: Optional[str] = None
    """Short description of card acceptor."""

    mcc: Optional[str] = None
    """Merchant category code (MCC).

    A four-digit number listed in ISO 18245. An MCC is used to classify a business
    by the types of goods or services it provides.
    """

    state: Optional[str] = None
    """Geographic state of card acceptor (see ISO 8583 specs)."""


class CardholderAuthentication(BaseModel):
    three_ds_version: Optional[str] = FieldInfo(alias="3ds_version", default=None)
    """3-D Secure Protocol version. Possible enum values:

    - `1`: 3-D Secure Protocol version 1.x applied to the transaction.
    - `2`: 3-D Secure Protocol version 2.x applied to the transaction.
    - `null`: 3-D Secure was not used for the transaction
    """

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
    """
    Exemption applied by the ACS to authenticate the transaction without requesting
    a challenge. Possible enum values:

    - `AUTHENTICATION_OUTAGE_EXCEPTION`: Authentication Outage Exception exemption.
    - `LOW_VALUE`: Low Value Payment exemption.
    - `MERCHANT_INITIATED_TRANSACTION`: Merchant Initiated Transaction (3RI).
    - `NONE`: No exemption applied.
    - `RECURRING_PAYMENT`: Recurring Payment exemption.
    - `SECURE_CORPORATE_PAYMENT`: Secure Corporate Payment exemption.
    - `STRONG_CUSTOMER_AUTHENTICATION_DELEGATION`: Strong Customer Authentication
      Delegation exemption.
    - `TRANSACTION_RISK_ANALYSIS`: Acquirer Low-Fraud and Transaction Risk Analysis
      exemption.

    Maps to the 3-D Secure `transChallengeExemption` field.
    """

    authentication_result: Literal["ATTEMPTS", "DECLINE", "NONE", "SUCCESS"]
    """Outcome of the 3DS authentication process. Possible enum values:

    - `SUCCESS`: 3DS authentication was successful and the transaction is considered
      authenticated.
    - `DECLINE`: 3DS authentication was attempted but was unsuccessful — i.e., the
      issuer declined to authenticate the cardholder; note that Lithic populates
      this value on a best-effort basis based on common data across the 3DS
      authentication and ASA data elements.
    - `ATTEMPTS`: 3DS authentication was attempted but full authentication did not
      occur. A proof of attempted authenticated is provided by the merchant.
    - `NONE`: 3DS authentication was not performed on the transaction.
    """

    decision_made_by: Literal["CUSTOMER_ENDPOINT", "LITHIC_DEFAULT", "LITHIC_RULES", "NETWORK", "UNKNOWN"]
    """Indicator for which party made the 3DS authentication decision.

    Possible enum values:

    - `NETWORK`: A networks tand-in service decided on the outcome; for token
      authentications (as indicated in the `liability_shift` attribute), this is the
      default value
    - `LITHIC_DEFAULT`: A default decision was made by Lithic, without running a
      rules-based authentication; this value will be set on card programs that do
      not participate in one of our two 3DS product tiers
    - `LITHIC_RULES`: A rules-based authentication was conducted by Lithic and
      Lithic decided on the outcome
    - `CUSTOMER_ENDPOINT`: Lithic customer decided on the outcome based on a
      real-time request sent to a configured endpoint
    - `UNKNOWN`: Data on which party decided is unavailable
    """

    liability_shift: Literal["3DS_AUTHENTICATED", "ACQUIRER_EXEMPTION", "NONE", "TOKEN_AUTHENTICATED"]
    """Indicates whether chargeback liability shift applies to the transaction.

    Possible enum values:

    - `3DS_AUTHENTICATED`: The transaction was fully authenticated through a 3-D
      Secure flow, chargeback liability shift applies.
    - `ACQUIRER_EXEMPTION`: The acquirer utilised an exemption to bypass Strong
      Customer Authentication (`transStatus = N`, or `transStatus = I`). Liability
      remains with the acquirer and in this case the `acquirer_exemption` field is
      expected to be not `NONE`.
    - `NONE`: Chargeback liability shift has not shifted to the issuer, i.e. the
      merchant is liable.
    - `TOKEN_AUTHENTICATED`: The transaction was a tokenized payment with validated
      cryptography, possibly recurring. Chargeback liability shift to the issuer
      applies.
    """

    three_ds_authentication_token: str
    """
    Unique identifier you can use to match a given 3DS authentication and the
    transaction. Note that in cases where liability shift does not occur, this token
    is matched to the transaction on a best-effort basis.
    """

    verification_attempted: Literal["APP_LOGIN", "BIOMETRIC", "NONE", "OTHER", "OTP"]
    """Verification attempted values:

    - `APP_LOGIN`: Out-of-band login verification was attempted by the ACS.
    - `BIOMETRIC`: Out-of-band biometric verification was attempted by the ACS.
    - `NONE`: No cardholder verification was attempted by the Access Control Server
      (e.g. frictionless 3-D Secure flow, no 3-D Secure, or stand-in Risk Based
      Analysis).
    - `OTHER`: Other method was used by the ACS to verify the cardholder (e.g.
      Mastercard Identity Check Express, recurring transactions, etc.)
    - `OTP`: One-time password verification was attempted by the ACS.
    """

    verification_result: Literal["CANCELLED", "FAILED", "FRICTIONLESS", "NOT_ATTEMPTED", "REJECTED", "SUCCESS"]
    """
    This field partially maps to the `transStatus` field in the
    [EMVCo 3-D Secure specification](https://www.emvco.com/emv-technologies/3d-secure/)
    and Mastercard SPA2 AAV leading indicators.

    Verification result values:

    - `CANCELLED`: Authentication/Account verification could not be performed,
      `transStatus = U`.
    - `FAILED`: Transaction was not authenticated. `transStatus = N`, note: the
      utilization of exemptions could also result in `transStatus = N`, inspect the
      `acquirer_exemption` field for more information.
    - `FRICTIONLESS`: Attempts processing performed, the transaction was not
      authenticated, but a proof of attempted authentication/verification is
      provided. `transStatus = A` and the leading AAV indicator was one of {`kE`,
      `kF`, `kQ`}.
    - `NOT_ATTEMPTED`: A 3-D Secure flow was not applied to this transaction.
      Leading AAV indicator was one of {`kN`, `kX`} or no AAV was provided for the
      transaction.
    - `REJECTED`: Authentication/Account Verification rejected; `transStatus = R`.
      Issuer is rejecting authentication/verification and requests that
      authorization not be attempted.
    - `SUCCESS`: Authentication verification successful. `transStatus = Y` and
      leading AAV indicator for the transaction was one of {`kA`, `kB`, `kC`, `kD`,
      `kO`, `kP`, `kR`, `kS`}.

    Note that the following `transStatus` values are not represented by this field:

    - `C`: Challenge Required
    - `D`: Challenge Required; decoupled authentication confirmed
    - `I`: Informational only
    - `S`: Challenge using Secure Payment Confirmation (SPC)
    """


class Transaction(BaseModel):
    token: str
    """Globally unique identifier."""

    acquirer_fee: int
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

    authorization_amount: int
    """Authorization amount (in cents) of the transaction, including any acquirer fees.

    This amount always represents the amount authorized for the transaction,
    unaffected by settlement.
    """

    authorization_code: str
    """
    A fixed-width 6-digit numeric identifier that can be used to identify a
    transaction with networks.
    """

    card_token: str
    """Token for the card used in this transaction."""

    created: datetime
    """Date and time when the transaction first occurred. UTC time zone."""

    events: List[Event]
    """A list of all events that have modified this transaction."""

    merchant: Merchant

    merchant_amount: int
    """
    Analogous to the "amount" property, but will represent the amount in the
    transaction's local currency (smallest unit), including any acquirer fees.
    """

    merchant_authorization_amount: int
    """
    Analogous to the "authorization_amount" property, but will represent the amount
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

    result: Literal[
        "ACCOUNT_STATE_TRANSACTION",
        "APPROVED",
        "BANK_CONNECTION_ERROR",
        "BANK_NOT_VERIFIED",
        "CARD_CLOSED",
        "CARD_PAUSED",
        "FRAUD_ADVICE",
        "GLOBAL_MONTHLY_LIMIT",
        "GLOBAL_TRANSACTION_LIMIT",
        "GLOBAL_WEEKLY_LIMIT",
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

    status: Literal["BOUNCED", "DECLINED", "EXPIRED", "PENDING", "SETTLED", "VOIDED"]
    """Status types:

    - `DECLINED` - The transaction was declined.
    - `EXPIRED` - Lithic reversed the authorization as it has passed its expiration
      time.
    - `PENDING` - Authorization is pending completion from the merchant.
    - `SETTLED` - The transaction is complete.
    - `VOIDED` - The merchant has voided the previously pending authorization.
    """

    cardholder_authentication: Optional[CardholderAuthentication] = None
