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
    """Additional parameters for certain attributes.

    Required when `attribute` is
    `SPEND_VELOCITY_COUNT` or `SPEND_VELOCITY_AMOUNT` (require `scope`, `period`, and
    optional `filters`); `AMOUNT_Z_SCORE`, `AVG_TRANSACTION_AMOUNT`,
    `STDEV_TRANSACTION_AMOUNT`, `IS_NEW_COUNTRY`, `IS_NEW_MCC`, `IS_FIRST_TRANSACTION`,
    `CONSECUTIVE_DECLINES`, `TIME_SINCE_LAST_TRANSACTION`, or `DISTINCT_COUNTRY_COUNT`
    (require `scope`, and additionally `interval` for the statistical attributes); or
    `TRAVEL_SPEED` or `DISTANCE_FROM_LAST_TRANSACTION` (require `unit`). Not used for
    other attributes.
    """

    filters: Optional[SpendVelocityFilters] = None

    interval: Optional[Literal["LIFETIME", "7D", "30D", "90D"]] = None
    """
    The time window for statistical attributes (`AMOUNT_Z_SCORE`,
    `AVG_TRANSACTION_AMOUNT`, `STDEV_TRANSACTION_AMOUNT`). Use `LIFETIME` for
    all-time history or a specific window (`7D`, `30D`, `90D`).
    """

    period: Optional[VelocityLimitPeriod] = None
    """The time period over which to calculate the spend velocity."""

    scope: Optional[Literal["CARD", "ACCOUNT", "GLOBAL"]] = None
    """The entity scope to evaluate the attribute against.

    `GLOBAL` is only valid for spend velocity attributes.
    """

    unit: Optional[Literal["MPH", "KPH", "MILES", "KILOMETERS"]] = None
    """The unit for impossible travel attributes.

    Required when `attribute` is `TRAVEL_SPEED` or `DISTANCE_FROM_LAST_TRANSACTION`.

    For `TRAVEL_SPEED`: `MPH` (miles per hour) or `KPH` (kilometers per hour).

    For `DISTANCE_FROM_LAST_TRANSACTION`: `MILES` or `KILOMETERS`.
    """


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
        "AMOUNT_Z_SCORE",
        "AVG_TRANSACTION_AMOUNT",
        "STDEV_TRANSACTION_AMOUNT",
        "IS_NEW_COUNTRY",
        "IS_NEW_MCC",
        "IS_FIRST_TRANSACTION",
        "CONSECUTIVE_DECLINES",
        "TIME_SINCE_LAST_TRANSACTION",
        "DISTINCT_COUNTRY_COUNT",
        "IS_NEW_MERCHANT",
        "THREE_DS_SUCCESS_RATE",
        "TRAVEL_SPEED",
        "DISTANCE_FROM_LAST_TRANSACTION",
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
      fee on behalf of the cardholder. Use an integer value.
    - `RISK_SCORE`: Network-provided score assessing risk level associated with a
      given authorization. Scores are on a range of 0-999, with 0 representing the
      lowest risk and 999 representing the highest risk. For Visa transactions,
      where the raw score has a range of 0-99, Lithic will normalize the score by
      multiplying the raw score by 10x. Use an integer value.
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
    - `CARD_AGE`: The age of the card in seconds at the time of the transaction. Use
      an integer value.
    - `ACCOUNT_AGE`: The age of the account in seconds at the time of the
      transaction. Use an integer value. For programs where Lithic does not manage
      or retain account holder data, this attribute does not evaluate.
    - `SPEND_VELOCITY_COUNT`: The number of transactions matching the specified
      filters within the given period. Requires `parameters` with `scope`, `period`,
      and optional `filters`. Use an integer value.
    - `SPEND_VELOCITY_AMOUNT`: The total spend amount (in cents) of transactions
      matching the specified filters within the given period. Requires `parameters`
      with `scope`, `period`, and optional `filters`. Use an integer value.
    - `AMOUNT_Z_SCORE`: The z-score of the transaction amount relative to the
      entity's transaction history. Null if fewer than 30 approved transactions in
      the specified window. Requires `parameters.scope` and `parameters.interval`.
      Use a decimal value.
    - `AVG_TRANSACTION_AMOUNT`: The average approved transaction amount for the
      entity over the specified window, in cents. Requires `parameters.scope` and
      `parameters.interval`. Use a decimal value.
    - `STDEV_TRANSACTION_AMOUNT`: The standard deviation of approved transaction
      amounts for the entity over the specified window, in cents. Null if fewer than
      30 approved transactions in the specified window. Requires `parameters.scope`
      and `parameters.interval`. Use a decimal value.
    - `IS_NEW_COUNTRY`: Whether the transaction's merchant country has not been seen
      in the entity's transaction history. Valid values are `TRUE`, `FALSE`.
      Requires `parameters.scope`.
    - `IS_NEW_MCC`: Whether the transaction's MCC has not been seen in the entity's
      transaction history. Valid values are `TRUE`, `FALSE`. Requires
      `parameters.scope`.
    - `IS_FIRST_TRANSACTION`: Whether this is the first transaction for the entity.
      Valid values are `TRUE`, `FALSE`. Requires `parameters.scope`.
    - `CONSECUTIVE_DECLINES`: The number of consecutive declined transactions for
      the entity over the last 30 days (rolling). Requires `parameters.scope`. Use
      an integer value.
    - `TIME_SINCE_LAST_TRANSACTION`: The number of days since the last approved
      transaction for the entity, rounded to the nearest whole day. Requires
      `parameters.scope`. Use an integer value.
    - `DISTINCT_COUNTRY_COUNT`: The number of distinct merchant countries seen in
      the entity's transaction history. Requires `parameters.scope`. Use an integer
      value.
    - `IS_NEW_MERCHANT`: Whether the card acceptor ID has not been seen in the
      card's approved transaction history (capped at the 1000 most recently seen
      merchants). Valid values are `TRUE`, `FALSE`. Card-scoped only; no
      `parameters` required.
    - `THREE_DS_SUCCESS_RATE`: The 3DS authentication success rate for the card, as
      a percentage from 0.0 to 100.0. Card-scoped only; no `parameters` required.
      Use a decimal value.
    - `TRAVEL_SPEED`: The estimated speed of travel derived from the distance
      between the postal code centers of the last card-present transaction and the
      current transaction, divided by the elapsed time. Null if there is no prior
      card-present transaction, if either postal code cannot be geocoded, or if
      elapsed time is zero. Requires `parameters.unit` set to `MPH` or `KPH`. Use a
      decimal value.
    - `DISTANCE_FROM_LAST_TRANSACTION`: The estimated distance between the postal
      code centers of the last card-present transaction and the current transaction.
      Null if there is no prior card-present transaction or if either postal code
      cannot be geocoded. Requires `parameters.unit` set to `MILES` or `KILOMETERS`.
      Use a decimal value.
    """

    operation: ConditionalOperation
    """The operation to apply to the attribute"""

    value: ConditionalValue
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""

    parameters: Optional[ConditionParameters] = None
    """Additional parameters for certain attributes.

    Required when `attribute` is `SPEND_VELOCITY_COUNT` or `SPEND_VELOCITY_AMOUNT`
    (require `scope`, `period`, and optional `filters`); `AMOUNT_Z_SCORE`,
    `AVG_TRANSACTION_AMOUNT`, `STDEV_TRANSACTION_AMOUNT`, `IS_NEW_COUNTRY`,
    `IS_NEW_MCC`, `IS_FIRST_TRANSACTION`, `CONSECUTIVE_DECLINES`,
    `TIME_SINCE_LAST_TRANSACTION`, or `DISTINCT_COUNTRY_COUNT` (require `scope`, and
    additionally `interval` for the statistical attributes); or `TRAVEL_SPEED` or
    `DISTANCE_FROM_LAST_TRANSACTION` (require `unit`). Not used for other
    attributes.
    """


class ConditionalCardTransactionUpdateActionParameters(BaseModel):
    action: CardTransactionUpdateAction
    """The action to take if the conditions are met."""

    conditions: List[Condition]
