# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.velocity_limit_params import VelocityLimitParams

__all__ = [
    "AuthRuleMigrateV1ToV2Response",
    "CurrentVersion",
    "CurrentVersionParameters",
    "CurrentVersionParametersConditionalBlockParameters",
    "CurrentVersionParametersConditionalBlockParametersCondition",
    "DraftVersion",
    "DraftVersionParameters",
    "DraftVersionParametersConditionalBlockParameters",
    "DraftVersionParametersConditionalBlockParametersCondition",
]


class CurrentVersionParametersConditionalBlockParametersCondition(BaseModel):
    attribute: Optional[
        Literal[
            "MCC",
            "COUNTRY",
            "CURRENCY",
            "MERCHANT_ID",
            "DESCRIPTOR",
            "LIABILITY_SHIFT",
            "PAN_ENTRY_MODE",
            "TRANSACTION_AMOUNT",
            "RISK_SCORE",
        ]
    ] = None
    """The attribute to target"""

    operation: Optional[
        Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    ] = None
    """The operation to apply to the attribute"""

    value: Union[str, float, List[str], None] = None
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class CurrentVersionParametersConditionalBlockParameters(BaseModel):
    conditions: List[CurrentVersionParametersConditionalBlockParametersCondition]


CurrentVersionParameters: TypeAlias = Union[CurrentVersionParametersConditionalBlockParameters, VelocityLimitParams]


class CurrentVersion(BaseModel):
    parameters: CurrentVersionParameters
    """Parameters for the current version of the Auth Rule"""

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


class DraftVersionParametersConditionalBlockParametersCondition(BaseModel):
    attribute: Optional[
        Literal[
            "MCC",
            "COUNTRY",
            "CURRENCY",
            "MERCHANT_ID",
            "DESCRIPTOR",
            "LIABILITY_SHIFT",
            "PAN_ENTRY_MODE",
            "TRANSACTION_AMOUNT",
            "RISK_SCORE",
        ]
    ] = None
    """The attribute to target"""

    operation: Optional[
        Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    ] = None
    """The operation to apply to the attribute"""

    value: Union[str, float, List[str], None] = None
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class DraftVersionParametersConditionalBlockParameters(BaseModel):
    conditions: List[DraftVersionParametersConditionalBlockParametersCondition]


DraftVersionParameters: TypeAlias = Union[DraftVersionParametersConditionalBlockParameters, VelocityLimitParams]


class DraftVersion(BaseModel):
    parameters: DraftVersionParameters
    """Parameters for the current version of the Auth Rule"""

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


class AuthRuleMigrateV1ToV2Response(BaseModel):
    token: str

    account_tokens: List[str]
    """Account tokens to which the Auth Rule applies."""

    card_tokens: List[str]
    """Card tokens to which the Auth Rule applies."""

    current_version: Optional[CurrentVersion] = None

    draft_version: Optional[DraftVersion] = None

    program_level: bool
    """Whether the Auth Rule applies to all authorizations on the card program."""

    state: Literal["ACTIVE", "INACTIVE"]
    """The state of the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"]
    """The type of Auth Rule"""
