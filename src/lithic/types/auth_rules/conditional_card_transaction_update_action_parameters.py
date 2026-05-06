# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .conditional_value import ConditionalValue
from .conditional_operation import ConditionalOperation
from .velocity_limit_period import VelocityLimitPeriod
from .spend_velocity_filters import SpendVelocityFilters
from .card_transaction_update_action import CardTransactionUpdateAction

__all__ = ["ConditionalCardTransactionUpdateActionParameters", "Condition", "ConditionParameters"]


class ConditionParameters(BaseModel):
    """Additional parameters for spend velocity attributes.

    Required when `attribute` is
    `SPEND_VELOCITY_COUNT` or `SPEND_VELOCITY_AMOUNT`. Not used for other attributes.
    """

    filters: Optional[SpendVelocityFilters] = None

    period: Optional[VelocityLimitPeriod] = None
    """The time period over which to calculate the spend velocity."""

    scope: Optional[Literal["CARD", "ACCOUNT", "GLOBAL"]] = None
    """The entity scope to evaluate the attribute against."""


class Condition(BaseModel):
    attribute: Literal[
        "MCC",
        "COUNTRY",
        "CURRENCY",
        "MERCHANT_ID",
        "DESCRIPTOR",
        "TRANSACTION_AMOUNT",
        "RISK_SCORE",
        "TRANSACTION_STATUS",
        "LAST_EVENT_TYPE",
        "LIABILITY_SHIFT",
        "PAN_ENTRY_MODE",
        "WALLET_TYPE",
        "CARD_AGE",
        "ACCOUNT_AGE",
        "SPEND_VELOCITY_COUNT",
        "SPEND_VELOCITY_AMOUNT",
    ]
    """The attribute to target.

    The following attributes may be targeted:

    - `MCC`: A four-digit number listed in ISO 18245. An MCC is used to classify a
      business by the types of goods or services it provides.
    - `COUNTRY`: Country of entity of card acceptor. Possible values are: (1) all
      ISO 3166-1 alpha-3 country codes, (2) QZZ for Kosovo, and (3) ANT for
      Netherlands Antilles.
    - `CURRENCY`: 3-character alphabetic ISO 4217 code for the merchant currency of
      the transaction.
    - `MERCHANT_ID`: Unique alphanumeric identifier for the payment card acceptor
      (merchant).
    - `DESCRIPTOR`: Short description of card acceptor.
    - `TRANSACTION_AMOUNT`: The base transaction amount (in cents) plus the acquirer
      fee field in the settlement/cardholder billing currency. This is the amount
      the issuer should authorize against unless the issuer is paying the acquirer
      fee on behalf of the cardholder.
    - `RISK_SCORE`: Network-provided score assessing risk level associated with a
      given authorization. Scores are on a range of 0-999, with 0 representing the
      lowest risk and 999 representing the highest risk. For Visa transactions,
      where the raw score has a range of 0-99, Lithic will normalize the score by
      multiplying the raw score by 10x.
    - `TRANSACTION_STATUS`: The status of the transaction. Valid values are
      `PENDING`, `VOIDED`, `SETTLING`, `SETTLED`, `BOUNCED`, `RETURNED`, `DECLINED`,
      `EXPIRED`.
    - `LAST_EVENT_TYPE`: The type of the most recent event on the transaction. Valid
      values are `AUTHORIZATION`, `AUTHORIZATION_ADVICE`, `AUTHORIZATION_EXPIRY`,
      `AUTHORIZATION_REVERSAL`, `BALANCE_INQUIRY`, `CLEARING`, `CORRECTION_CREDIT`,
      `CORRECTION_DEBIT`, `CREDIT_AUTHORIZATION`, `CREDIT_AUTHORIZATION_ADVICE`,
      `FINANCIAL_AUTHORIZATION`, `FINANCIAL_CREDIT_AUTHORIZATION`, `RETURN`,
      `RETURN_REVERSAL`.
    - `LIABILITY_SHIFT`: Indicates whether chargeback liability shift to the issuer
      applies to the transaction. Valid values are `NONE`, `3DS_AUTHENTICATED`, or
      `TOKEN_AUTHENTICATED`.
    - `PAN_ENTRY_MODE`: The method by which the cardholder's primary account number
      (PAN) was entered. Valid values are `AUTO_ENTRY`, `BAR_CODE`, `CONTACTLESS`,
      `ECOMMERCE`, `ERROR_KEYED`, `ERROR_MAGNETIC_STRIPE`, `ICC`, `KEY_ENTERED`,
      `MAGNETIC_STRIPE`, `MANUAL`, `OCR`, `SECURE_CARDLESS`, `UNSPECIFIED`,
      `UNKNOWN`, or `CREDENTIAL_ON_FILE`.
    - `WALLET_TYPE`: For transactions using a digital wallet token, indicates the
      source of the token. Valid values are `APPLE_PAY`, `GOOGLE_PAY`,
      `SAMSUNG_PAY`, `MASTERPASS`, `MERCHANT`, `OTHER`, `NONE`.
    - `CARD_AGE`: The age of the card in seconds at the time of the transaction.
    - `ACCOUNT_AGE`: The age of the account in seconds at the time of the
      transaction.
    - `SPEND_VELOCITY_COUNT`: The number of transactions matching the specified
      filters within the given period. Requires `parameters` with `scope`, `period`,
      and optional `filters`.
    - `SPEND_VELOCITY_AMOUNT`: The total spend amount (in cents) of transactions
      matching the specified filters within the given period. Requires `parameters`
      with `scope`, `period`, and optional `filters`.
    """

    operation: ConditionalOperation
    """The operation to apply to the attribute"""

    value: ConditionalValue
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""

    parameters: Optional[ConditionParameters] = None
    """Additional parameters for spend velocity attributes.

    Required when `attribute` is `SPEND_VELOCITY_COUNT` or `SPEND_VELOCITY_AMOUNT`.
    Not used for other attributes.
    """


class ConditionalCardTransactionUpdateActionParameters(BaseModel):
    action: CardTransactionUpdateAction
    """The action to take if the conditions are met."""

    conditions: List[Condition]
