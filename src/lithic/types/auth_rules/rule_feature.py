# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
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
    "CardFeature",
    "AccountHolderFeature",
    "IPMetadataFeature",
    "SpendVelocityFeature",
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


RuleFeature: TypeAlias = Union[
    AuthorizationFeature,
    AuthenticationFeature,
    TokenizationFeature,
    ACHReceiptFeature,
    CardFeature,
    AccountHolderFeature,
    IPMetadataFeature,
    SpendVelocityFeature,
]
