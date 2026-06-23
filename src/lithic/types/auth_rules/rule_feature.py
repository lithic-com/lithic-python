# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .velocity_limit_period import VelocityLimitPeriod
from .velocity_limit_filters import VelocityLimitFilters

__all__ = [
    "RuleFeature",
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


class AuthorizationFeature(BaseModel):
    type: Literal["AUTHORIZATION"]

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class AuthenticationFeature(BaseModel):
    type: Literal["AUTHENTICATION"]

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class TokenizationFeature(BaseModel):
    type: Literal["TOKENIZATION"]

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class ACHReceiptFeature(BaseModel):
    type: Literal["ACH_RECEIPT"]

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class CardTransactionFeature(BaseModel):
    type: Literal["CARD_TRANSACTION"]

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class ACHPaymentFeature(BaseModel):
    type: Literal["ACH_PAYMENT"]

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class ExternalBankAccountFeature(BaseModel):
    type: Literal["EXTERNAL_BANK_ACCOUNT"]

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class CardFeature(BaseModel):
    type: Literal["CARD"]

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class AccountHolderFeature(BaseModel):
    type: Literal["ACCOUNT_HOLDER"]

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class IPMetadataFeature(BaseModel):
    type: Literal["IP_METADATA"]

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class SpendVelocityFeature(BaseModel):
    period: VelocityLimitPeriod
    """Velocity over the current day since 00:00 / 12 AM in Eastern Time"""

    scope: Literal["CARD", "ACCOUNT"]
    """The scope the velocity is calculated for"""

    type: Literal["SPEND_VELOCITY"]

    filters: Optional[VelocityLimitFilters] = None

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class PaymentVelocityFeatureFilters(BaseModel):
    """Optional filters applied when aggregating ACH payment velocity.

    Payments not matching the provided filters are excluded from the calculated velocity.
    """

    exclude_tags: Optional[Dict[str, str]] = None
    """Exclude payments matching any of the provided tag key-value pairs."""

    include_payment_types: Optional[List[Literal["ORIGINATION", "RECEIPT"]]] = None
    """Payment types to include in the velocity calculation."""

    include_polarities: Optional[List[Literal["CREDIT", "DEBIT"]]] = None
    """Payment polarities to include in the velocity calculation."""

    include_statuses: Optional[List[Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED", "RETURNED"]]] = (
        None
    )
    """Payment statuses to include in the velocity calculation."""

    include_tags: Optional[Dict[str, str]] = None
    """Only include payments matching all of the provided tag key-value pairs."""

    result: Optional[Literal["APPROVED", "DECLINED"]] = None
    """Only include payments with the given result."""


class PaymentVelocityFeature(BaseModel):
    period: VelocityLimitPeriod
    """Velocity over the current day since 00:00 / 12 AM in Eastern Time"""

    scope: Literal["FINANCIAL_ACCOUNT", "GLOBAL"]
    """The scope over which the ACH payment velocity is aggregated."""

    type: Literal["PAYMENT_VELOCITY"]

    filters: Optional[PaymentVelocityFeatureFilters] = None
    """Optional filters applied when aggregating ACH payment velocity.

    Payments not matching the provided filters are excluded from the calculated
    velocity.
    """

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class TransactionHistorySignalsFeature(BaseModel):
    scope: Literal["CARD", "ACCOUNT", "BUSINESS_ACCOUNT"]
    """The entity scope to load transaction history signals for."""

    type: Literal["TRANSACTION_HISTORY_SIGNALS"]

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class ConsecutiveDeclinesFeature(BaseModel):
    scope: Literal["CARD", "ACCOUNT"]
    """The entity scope to count consecutive declines for."""

    type: Literal["CONSECUTIVE_DECLINES"]

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


class ACHPaymentHistoryFeature(BaseModel):
    scope: Literal["FINANCIAL_ACCOUNT"]
    """The entity scope to load ACH payment history for."""

    type: Literal["ACH_PAYMENT_HISTORY"]

    name: Optional[str] = None
    """The variable name for this feature in the rule function signature"""


RuleFeature: TypeAlias = Union[
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
