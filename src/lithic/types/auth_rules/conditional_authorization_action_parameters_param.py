# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .conditional_operation import ConditionalOperation
from .conditional_value_param import ConditionalValueParam

__all__ = ["ConditionalAuthorizationActionParametersParam", "Condition", "ConditionParameters"]


class ConditionParameters(TypedDict, total=False):
    """Additional parameters required for transaction history signal attributes.

    Required when
    `attribute` is one of `AMOUNT_Z_SCORE`, `AVG_TRANSACTION_AMOUNT`,
    `STDEV_TRANSACTION_AMOUNT`, `IS_NEW_COUNTRY`, `IS_NEW_MCC`, `IS_FIRST_TRANSACTION`,
    `CONSECUTIVE_DECLINES`, `TIME_SINCE_LAST_TRANSACTION`, or `DISTINCT_COUNTRY_COUNT`.
    Not used for other attributes.
    """

    interval: Literal["LIFETIME", "7D", "30D", "90D"]
    """
    The time window for statistical attributes (`AMOUNT_Z_SCORE`,
    `AVG_TRANSACTION_AMOUNT`, `STDEV_TRANSACTION_AMOUNT`). Use `LIFETIME` for
    all-time history or a specific window (`7D`, `30D`, `90D`).
    """

    scope: Literal["CARD", "ACCOUNT", "BUSINESS_ACCOUNT"]
    """The entity scope to evaluate the attribute against."""


class Condition(TypedDict, total=False):
    attribute: Required[
        Literal[
            "MCC",
            "COUNTRY",
            "CURRENCY",
            "MERCHANT_ID",
            "DESCRIPTOR",
            "LIABILITY_SHIFT",
            "PAN_ENTRY_MODE",
            "TRANSACTION_AMOUNT",
            "CASH_AMOUNT",
            "RISK_SCORE",
            "CARD_TRANSACTION_COUNT_15M",
            "CARD_TRANSACTION_COUNT_1H",
            "CARD_TRANSACTION_COUNT_24H",
            "CARD_DECLINE_COUNT_15M",
            "CARD_DECLINE_COUNT_1H",
            "CARD_DECLINE_COUNT_24H",
            "CARD_STATE",
            "PIN_ENTERED",
            "PIN_STATUS",
            "WALLET_TYPE",
            "TRANSACTION_INITIATOR",
            "ADDRESS_MATCH",
            "SERVICE_LOCATION_STATE",
            "SERVICE_LOCATION_POSTAL_CODE",
            "CARD_AGE",
            "ACCOUNT_AGE",
            "AMOUNT_Z_SCORE",
            "AVG_TRANSACTION_AMOUNT",
            "STDEV_TRANSACTION_AMOUNT",
            "IS_NEW_COUNTRY",
            "IS_NEW_MCC",
            "IS_FIRST_TRANSACTION",
            "CONSECUTIVE_DECLINES",
            "TIME_SINCE_LAST_TRANSACTION",
            "DISTINCT_COUNTRY_COUNT",
            "THREE_DS_SUCCESS_RATE",
        ]
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
    - `LIABILITY_SHIFT`: Indicates whether chargeback liability shift to the issuer
      applies to the transaction. Valid values are `NONE`, `3DS_AUTHENTICATED`, or
      `TOKEN_AUTHENTICATED`.
    - `PAN_ENTRY_MODE`: The method by which the cardholder's primary account number
      (PAN) was entered. Valid values are `AUTO_ENTRY`, `BAR_CODE`, `CONTACTLESS`,
      `ECOMMERCE`, `ERROR_KEYED`, `ERROR_MAGNETIC_STRIPE`, `ICC`, `KEY_ENTERED`,
      `MAGNETIC_STRIPE`, `MANUAL`, `OCR`, `SECURE_CARDLESS`, `UNSPECIFIED`,
      `UNKNOWN`, `CREDENTIAL_ON_FILE`, or `ECOMMERCE`.
    - `TRANSACTION_AMOUNT`: The base transaction amount (in cents) plus the acquirer
      fee field in the settlement/cardholder billing currency. This is the amount
      the issuer should authorize against unless the issuer is paying the acquirer
      fee on behalf of the cardholder.
    - `CASH_AMOUNT`: The cash amount of the transaction in minor units (cents). This
      represents the amount of cash being withdrawn or advanced.
    - `RISK_SCORE`: Network-provided score assessing risk level associated with a
      given authorization. Scores are on a range of 0-999, with 0 representing the
      lowest risk and 999 representing the highest risk. For Visa transactions,
      where the raw score has a range of 0-99, Lithic will normalize the score by
      multiplying the raw score by 10x.
    - `CARD_TRANSACTION_COUNT_15M`: The number of transactions on the card in the
      trailing 15 minutes before the authorization.
    - `CARD_TRANSACTION_COUNT_1H`: The number of transactions on the card in the
      trailing hour up and until the authorization.
    - `CARD_TRANSACTION_COUNT_24H`: The number of transactions on the card in the
      trailing 24 hours up and until the authorization.
    - `CARD_DECLINE_COUNT_15M`: The number of declined transactions on the card in
      the trailing 15 minutes before the authorization.
    - `CARD_DECLINE_COUNT_1H`: The number of declined transactions on the card in
      the trailing hour up and until the authorization.
    - `CARD_DECLINE_COUNT_24H`: The number of declined transactions on the card in
      the trailing 24 hours up and until the authorization.
    - `CARD_STATE`: The current state of the card associated with the transaction.
      Valid values are `CLOSED`, `OPEN`, `PAUSED`, `PENDING_ACTIVATION`,
      `PENDING_FULFILLMENT`.
    - `PIN_ENTERED`: Indicates whether a PIN was entered during the transaction.
      Valid values are `TRUE`, `FALSE`.
    - `PIN_STATUS`: The current state of card's PIN. Valid values are `NOT_SET`,
      `OK`, `BLOCKED`.
    - `WALLET_TYPE`: For transactions using a digital wallet token, indicates the
      source of the token. Valid values are `APPLE_PAY`, `GOOGLE_PAY`,
      `SAMSUNG_PAY`, `MASTERPASS`, `MERCHANT`, `OTHER`, `NONE`.
    - `TRANSACTION_INITIATOR`: The entity that initiated the transaction indicates
      the source of the token. Valid values are `CARDHOLDER`, `MERCHANT`, `UNKNOWN`.
    - `ADDRESS_MATCH`: Lithic's evaluation result comparing transaction's address
      data with the cardholder KYC data if it exists. Valid values are `MATCH`,
      `MATCH_ADDRESS_ONLY`, `MATCH_ZIP_ONLY`,`MISMATCH`,`NOT_PRESENT`.
    - `SERVICE_LOCATION_STATE`: The state/province code (ISO 3166-2) where the
      cardholder received the service, e.g. "NY". When a service location is present
      in the network data, the service location state is used. Otherwise, falls back
      to the card acceptor state.
    - `SERVICE_LOCATION_POSTAL_CODE`: The postal code where the cardholder received
      the service, e.g. "10001". When a service location is present in the network
      data, the service location postal code is used. Otherwise, falls back to the
      card acceptor postal code.
    - `CARD_AGE`: The age of the card in seconds at the time of the authorization.
    - `ACCOUNT_AGE`: The age of the account holder's account in seconds at the time
      of the authorization.
    - `AMOUNT_Z_SCORE`: The z-score of the transaction amount relative to the
      entity's transaction history. Null if fewer than 30 approved transactions in
      the specified window. Requires `parameters.scope` and `parameters.interval`.
    - `AVG_TRANSACTION_AMOUNT`: The average approved transaction amount for the
      entity over the specified window, in cents. Requires `parameters.scope` and
      `parameters.interval`.
    - `STDEV_TRANSACTION_AMOUNT`: The standard deviation of approved transaction
      amounts for the entity over the specified window, in cents. Null if fewer than
      30 approved transactions in the specified window. Requires `parameters.scope`
      and `parameters.interval`.
    - `IS_NEW_COUNTRY`: Whether the transaction's merchant country has not been seen
      in the entity's transaction history. Valid values are `TRUE`, `FALSE`.
      Requires `parameters.scope`.
    - `IS_NEW_MCC`: Whether the transaction's MCC has not been seen in the entity's
      transaction history. Valid values are `TRUE`, `FALSE`. Requires
      `parameters.scope`.
    - `IS_FIRST_TRANSACTION`: Whether this is the first transaction for the entity.
      Valid values are `TRUE`, `FALSE`. Requires `parameters.scope`.
    - `CONSECUTIVE_DECLINES`: The number of consecutive declined transactions for
      the entity over the last 30 days (rolling). Requires `parameters.scope`. Not
      supported for `BUSINESS_ACCOUNT` scope.
    - `TIME_SINCE_LAST_TRANSACTION`: The number of days since the last approved
      transaction for the entity. Requires `parameters.scope`.
    - `DISTINCT_COUNTRY_COUNT`: The number of distinct merchant countries seen in
      the entity's transaction history. Requires `parameters.scope`.
    - `THREE_DS_SUCCESS_RATE`: The 3DS authentication success rate for the card, as
      a percentage from 0.0 to 100.0. Card-scoped only; no `parameters` required.
    """

    operation: Required[ConditionalOperation]
    """The operation to apply to the attribute"""

    value: Required[Annotated[ConditionalValueParam, PropertyInfo(format="iso8601")]]
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""

    parameters: ConditionParameters
    """Additional parameters required for transaction history signal attributes.

    Required when `attribute` is one of `AMOUNT_Z_SCORE`, `AVG_TRANSACTION_AMOUNT`,
    `STDEV_TRANSACTION_AMOUNT`, `IS_NEW_COUNTRY`, `IS_NEW_MCC`,
    `IS_FIRST_TRANSACTION`, `CONSECUTIVE_DECLINES`, `TIME_SINCE_LAST_TRANSACTION`,
    or `DISTINCT_COUNTRY_COUNT`. Not used for other attributes.
    """


class ConditionalAuthorizationActionParametersParam(TypedDict, total=False):
    action: Required[Literal["DECLINE", "CHALLENGE"]]
    """The action to take if the conditions are met."""

    conditions: Required[Iterable[Condition]]
