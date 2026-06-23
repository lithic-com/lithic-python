# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .velocity_limit_period_param import VelocityLimitPeriodParam
from .velocity_limit_filters_param import VelocityLimitFiltersParam

__all__ = [
    "RuleFeatureParam",
    "AuthorizationFeature",
    "AuthenticationFeature",
    "TokenizationFeature",
    "ACHReceiptFeature",
    "CardTransactionFeature",
    "ACHPaymentFeature",
    "ExternalBankAccountFeature",
    "CardFeature",
    "AccountHolderFeature",
    "IPMetadataFeature",
    "SpendVelocityFeature",
    "PaymentVelocityFeature",
    "PaymentVelocityFeatureFilters",
    "TransactionHistorySignalsFeature",
    "ConsecutiveDeclinesFeature",
    "ACHPaymentHistoryFeature",
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


class CardTransactionFeature(TypedDict, total=False):
    type: Required[Literal["CARD_TRANSACTION"]]

    name: str
    """The variable name for this feature in the rule function signature"""


class ACHPaymentFeature(TypedDict, total=False):
    type: Required[Literal["ACH_PAYMENT"]]

    name: str
    """The variable name for this feature in the rule function signature"""


class ExternalBankAccountFeature(TypedDict, total=False):
    type: Required[Literal["EXTERNAL_BANK_ACCOUNT"]]

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


class PaymentVelocityFeatureFilters(TypedDict, total=False):
    """Optional filters applied when aggregating ACH payment velocity.

    Payments not matching the provided filters are excluded from the calculated velocity.
    """

    exclude_tags: Optional[Dict[str, str]]
    """Exclude payments matching any of the provided tag key-value pairs."""

    include_payment_types: Optional[List[Literal["ORIGINATION", "RECEIPT"]]]
    """Payment types to include in the velocity calculation."""

    include_polarities: Optional[List[Literal["CREDIT", "DEBIT"]]]
    """Payment polarities to include in the velocity calculation."""

    include_statuses: Optional[List[Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED", "RETURNED"]]]
    """Payment statuses to include in the velocity calculation."""

    include_tags: Optional[Dict[str, str]]
    """Only include payments matching all of the provided tag key-value pairs."""

    result: Literal["APPROVED", "DECLINED"]
    """Only include payments with the given result."""


class PaymentVelocityFeature(TypedDict, total=False):
    period: Required[VelocityLimitPeriodParam]
    """Velocity over the current day since 00:00 / 12 AM in Eastern Time"""

    scope: Required[Literal["FINANCIAL_ACCOUNT", "GLOBAL"]]
    """The scope over which the ACH payment velocity is aggregated."""

    type: Required[Literal["PAYMENT_VELOCITY"]]

    filters: PaymentVelocityFeatureFilters
    """Optional filters applied when aggregating ACH payment velocity.

    Payments not matching the provided filters are excluded from the calculated
    velocity.
    """

    name: str
    """The variable name for this feature in the rule function signature"""


class TransactionHistorySignalsFeature(TypedDict, total=False):
    scope: Required[Literal["CARD", "ACCOUNT", "BUSINESS_ACCOUNT"]]
    """The entity scope to load transaction history signals for."""

    type: Required[Literal["TRANSACTION_HISTORY_SIGNALS"]]

    name: str
    """The variable name for this feature in the rule function signature"""


class ConsecutiveDeclinesFeature(TypedDict, total=False):
    scope: Required[Literal["CARD", "ACCOUNT"]]
    """The entity scope to count consecutive declines for."""

    type: Required[Literal["CONSECUTIVE_DECLINES"]]

    name: str
    """The variable name for this feature in the rule function signature"""


class ACHPaymentHistoryFeature(TypedDict, total=False):
    scope: Required[Literal["FINANCIAL_ACCOUNT"]]
    """The entity scope to load ACH payment history for."""

    type: Required[Literal["ACH_PAYMENT_HISTORY"]]

    name: str
    """The variable name for this feature in the rule function signature"""


RuleFeatureParam: TypeAlias = Union[
    AuthorizationFeature,
    AuthenticationFeature,
    TokenizationFeature,
    ACHReceiptFeature,
    CardTransactionFeature,
    ACHPaymentFeature,
    ExternalBankAccountFeature,
    CardFeature,
    AccountHolderFeature,
    IPMetadataFeature,
    SpendVelocityFeature,
    PaymentVelocityFeature,
    TransactionHistorySignalsFeature,
    ConsecutiveDeclinesFeature,
    ACHPaymentHistoryFeature,
]
