# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .velocity_limit_params_param import VelocityLimitParamsParam
from .merchant_lock_parameters_param import MerchantLockParametersParam
from .conditional_block_parameters_param import ConditionalBlockParametersParam
from .conditional_3ds_action_parameters_param import Conditional3DSActionParametersParam

__all__ = [
    "V2DraftParams",
    "Parameters",
    "ParametersConditionalAuthorizationActionParameters",
    "ParametersConditionalAuthorizationActionParametersCondition",
]


class V2DraftParams(TypedDict, total=False):
    parameters: Optional[Parameters]
    """Parameters for the Auth Rule"""


class ParametersConditionalAuthorizationActionParametersCondition(TypedDict, total=False):
    attribute: Literal[
        "MCC",
        "COUNTRY",
        "CURRENCY",
        "MERCHANT_ID",
        "DESCRIPTOR",
        "LIABILITY_SHIFT",
        "PAN_ENTRY_MODE",
        "TRANSACTION_AMOUNT",
        "RISK_SCORE",
        "CARD_TRANSACTION_COUNT_15M",
        "CARD_TRANSACTION_COUNT_1H",
        "CARD_TRANSACTION_COUNT_24H",
        "CARD_STATE",
        "PIN_ENTERED",
        "PIN_STATUS",
        "WALLET_TYPE",
        "TRANSACTION_INITIATOR",
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
    """

    operation: Literal[
        "IS_ONE_OF",
        "IS_NOT_ONE_OF",
        "MATCHES",
        "DOES_NOT_MATCH",
        "IS_EQUAL_TO",
        "IS_NOT_EQUAL_TO",
        "IS_GREATER_THAN",
        "IS_GREATER_THAN_OR_EQUAL_TO",
        "IS_LESS_THAN",
        "IS_LESS_THAN_OR_EQUAL_TO",
    ]
    """The operation to apply to the attribute"""

    value: Union[str, int, SequenceNotStr[str]]
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class ParametersConditionalAuthorizationActionParameters(TypedDict, total=False):
    action: Required[Literal["DECLINE", "CHALLENGE"]]
    """The action to take if the conditions are met."""

    conditions: Required[Iterable[ParametersConditionalAuthorizationActionParametersCondition]]


Parameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    MerchantLockParametersParam,
    Conditional3DSActionParametersParam,
    ParametersConditionalAuthorizationActionParameters,
]
