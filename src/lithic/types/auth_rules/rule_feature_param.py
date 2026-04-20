# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .velocity_limit_period_param import VelocityLimitPeriodParam
from .velocity_limit_filters_param import VelocityLimitFiltersParam

__all__ = [
    "RuleFeatureParam",
    "AuthorizationFeature",
    "AuthenticationFeature",
    "TokenizationFeature",
    "ACHReceiptFeature",
    "CardFeature",
    "AccountHolderFeature",
    "IPMetadataFeature",
    "SpendVelocityFeature",
    "TransactionHistorySignalsFeature",
]


class AuthorizationFeature(TypedDict, total=False):
    type: Required[Literal["AUTHORIZATION"]]

    name: str
    """The variable name for this feature in the rule function signature"""


class AuthenticationFeature(TypedDict, total=False):
    type: Required[Literal["AUTHENTICATION"]]

    name: str
    """The variable name for this feature in the rule function signature"""


class TokenizationFeature(TypedDict, total=False):
    type: Required[Literal["TOKENIZATION"]]

    name: str
    """The variable name for this feature in the rule function signature"""


class ACHReceiptFeature(TypedDict, total=False):
    type: Required[Literal["ACH_RECEIPT"]]

    name: str
    """The variable name for this feature in the rule function signature"""


class CardFeature(TypedDict, total=False):
    type: Required[Literal["CARD"]]

    name: str
    """The variable name for this feature in the rule function signature"""


class AccountHolderFeature(TypedDict, total=False):
    type: Required[Literal["ACCOUNT_HOLDER"]]

    name: str
    """The variable name for this feature in the rule function signature"""


class IPMetadataFeature(TypedDict, total=False):
    type: Required[Literal["IP_METADATA"]]

    name: str
    """The variable name for this feature in the rule function signature"""


class SpendVelocityFeature(TypedDict, total=False):
    period: Required[VelocityLimitPeriodParam]
    """Velocity over the current day since 00:00 / 12 AM in Eastern Time"""

    scope: Required[Literal["CARD", "ACCOUNT"]]
    """The scope the velocity is calculated for"""

    type: Required[Literal["SPEND_VELOCITY"]]

    filters: VelocityLimitFiltersParam

    name: str
    """The variable name for this feature in the rule function signature"""


class TransactionHistorySignalsFeature(TypedDict, total=False):
    scope: Required[Literal["CARD", "ACCOUNT", "BUSINESS_ACCOUNT"]]
    """The entity scope to load transaction history signals for."""

    type: Required[Literal["TRANSACTION_HISTORY_SIGNALS"]]

    name: str
    """The variable name for this feature in the rule function signature"""


RuleFeatureParam: TypeAlias = Union[
    AuthorizationFeature,
    AuthenticationFeature,
    TokenizationFeature,
    ACHReceiptFeature,
    CardFeature,
    AccountHolderFeature,
    IPMetadataFeature,
    SpendVelocityFeature,
    TransactionHistorySignalsFeature,
]
