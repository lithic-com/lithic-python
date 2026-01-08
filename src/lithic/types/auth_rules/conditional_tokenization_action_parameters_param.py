# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .conditional_operation import ConditionalOperation
from .conditional_value_param import ConditionalValueParam

__all__ = [
    "ConditionalTokenizationActionParametersParam",
    "Action",
    "ActionDeclineAction",
    "ActionRequireTfaAction",
    "Condition",
]


class ActionDeclineAction(TypedDict, total=False):
    type: Required[Literal["DECLINE"]]
    """Decline the tokenization request"""

    reason: Literal[
        "ACCOUNT_SCORE_1",
        "DEVICE_SCORE_1",
        "ALL_WALLET_DECLINE_REASONS_PRESENT",
        "WALLET_RECOMMENDED_DECISION_RED",
        "CVC_MISMATCH",
        "CARD_EXPIRY_MONTH_MISMATCH",
        "CARD_EXPIRY_YEAR_MISMATCH",
        "CARD_INVALID_STATE",
        "CUSTOMER_RED_PATH",
        "INVALID_CUSTOMER_RESPONSE",
        "NETWORK_FAILURE",
        "GENERIC_DECLINE",
        "DIGITAL_CARD_ART_REQUIRED",
    ]
    """Reason code for declining the tokenization request"""


class ActionRequireTfaAction(TypedDict, total=False):
    type: Required[Literal["REQUIRE_TFA"]]
    """Require two-factor authentication for the tokenization request"""

    reason: Literal[
        "WALLET_RECOMMENDED_TFA",
        "SUSPICIOUS_ACTIVITY",
        "DEVICE_RECENTLY_LOST",
        "TOO_MANY_RECENT_ATTEMPTS",
        "TOO_MANY_RECENT_TOKENS",
        "TOO_MANY_DIFFERENT_CARDHOLDERS",
        "OUTSIDE_HOME_TERRITORY",
        "HAS_SUSPENDED_TOKENS",
        "HIGH_RISK",
        "ACCOUNT_SCORE_LOW",
        "DEVICE_SCORE_LOW",
        "CARD_STATE_TFA",
        "HARDCODED_TFA",
        "CUSTOMER_RULE_TFA",
        "DEVICE_HOST_CARD_EMULATION",
    ]
    """Reason code for requiring two-factor authentication"""


Action: TypeAlias = Union[ActionDeclineAction, ActionRequireTfaAction]


class Condition(TypedDict, total=False):
    attribute: Required[
        Literal[
            "TIMESTAMP",
            "TOKENIZATION_CHANNEL",
            "TOKENIZATION_SOURCE",
            "TOKEN_REQUESTOR_NAME",
            "WALLET_ACCOUNT_SCORE",
            "WALLET_DEVICE_SCORE",
            "WALLET_RECOMMENDED_DECISION",
            "WALLET_RECOMMENDATION_REASONS",
            "TOKEN_REQUESTOR_ID",
            "WALLET_TOKEN_STATUS",
            "CARD_STATE",
        ]
    ]
    """The attribute to target.

    The following attributes may be targeted:

    - `TIMESTAMP`: The timestamp of the tokenization request in ISO 8601 format.
    - `TOKENIZATION_CHANNEL`: The channel through which the tokenization request was
      initiated (e.g., DIGITAL_WALLET, ECOMMERCE).
    - `TOKENIZATION_SOURCE`: The source of the tokenization request.
    - `TOKEN_REQUESTOR_NAME`: The name of the entity requesting the token. Valid
      values are `ALT_ID`, `AMAZON_ONE`, `AMERICAN_EXPRESS_TOKEN_SERVICE`,
      `ANDROID_PAY`, `APPLE_PAY`, `FACEBOOK`, `FITBIT_PAY`, `GARMIN_PAY`,
      `GOOGLE_PAY`, `GOOGLE_VCN`, `ISSUER_HCE`, `MICROSOFT_PAY`, `NETFLIX`,
      `SAMSUNG_PAY`, `UNKNOWN`, `VISA_CHECKOUT`.
    - `WALLET_ACCOUNT_SCORE`: Risk score for the account in the digital wallet.
      Numeric value where lower numbers indicate higher risk (e.g., 1 = high risk, 2
      = medium risk).
    - `WALLET_DEVICE_SCORE`: Risk score for the device in the digital wallet.
      Numeric value where lower numbers indicate higher risk (e.g., 1 = high risk, 2
      = medium risk).
    - `WALLET_RECOMMENDED_DECISION`: The decision recommended by the digital wallet
      provider. Valid values include APPROVE, DECLINE,
      REQUIRE_ADDITIONAL_AUTHENTICATION.
    - `WALLET_RECOMMENDATION_REASONS`: List of reasons provided by the digital
      wallet provider for the recommended decision. Valid values are
      `ACCOUNT_CARD_TOO_NEW`, `ACCOUNT_RECENTLY_CHANGED`, `ACCOUNT_TOO_NEW`,
      `ACCOUNT_TOO_NEW_SINCE_LAUNCH`, `DEVICE_RECENTLY_LOST`,
      `HAS_SUSPENDED_TOKENS`, `HIGH_RISK`, `INACTIVE_ACCOUNT`, `LOW_ACCOUNT_SCORE`,
      `LOW_DEVICE_SCORE`, `OUTSIDE_HOME_TERRITORY`, `SUSPICIOUS_ACTIVITY`,
      `TOO_MANY_DIFFERENT_CARDHOLDERS`, `TOO_MANY_RECENT_ATTEMPTS`,
      `TOO_MANY_RECENT_TOKENS`, `UNABLE_TO_ASSESS`.
    - `TOKEN_REQUESTOR_ID`: Unique identifier for the entity requesting the token.
    - `WALLET_TOKEN_STATUS`: The current status of the wallet token.
    - `CARD_STATE`: The state of the card being tokenized. Valid values are
      `CLOSED`, `OPEN`, `PAUSED`, `PENDING_ACTIVATION`, `PENDING_FULFILLMENT`.
    """

    operation: Required[ConditionalOperation]
    """The operation to apply to the attribute"""

    value: Required[Annotated[ConditionalValueParam, PropertyInfo(format="iso8601")]]
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class ConditionalTokenizationActionParametersParam(TypedDict, total=False):
    action: Required[Action]
    """The action to take if the conditions are met"""

    conditions: Required[Iterable[Condition]]
