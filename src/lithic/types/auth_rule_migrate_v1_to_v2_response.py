# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.velocity_limit_params import VelocityLimitParams

__all__ = [
    "AuthRuleMigrateV1ToV2Response",
    "AuthRuleMigrateV1ToV2ResponseItem",
    "AuthRuleMigrateV1ToV2ResponseItemCurrentVersion",
    "AuthRuleMigrateV1ToV2ResponseItemCurrentVersionParameters",
    "AuthRuleMigrateV1ToV2ResponseItemCurrentVersionParametersConditionalBlockParameters",
    "AuthRuleMigrateV1ToV2ResponseItemCurrentVersionParametersConditionalBlockParametersCondition",
    "AuthRuleMigrateV1ToV2ResponseItemDraftVersion",
    "AuthRuleMigrateV1ToV2ResponseItemDraftVersionParameters",
    "AuthRuleMigrateV1ToV2ResponseItemDraftVersionParametersConditionalBlockParameters",
    "AuthRuleMigrateV1ToV2ResponseItemDraftVersionParametersConditionalBlockParametersCondition",
]


class AuthRuleMigrateV1ToV2ResponseItemCurrentVersionParametersConditionalBlockParametersCondition(BaseModel):
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


class AuthRuleMigrateV1ToV2ResponseItemCurrentVersionParametersConditionalBlockParameters(BaseModel):
    conditions: List[AuthRuleMigrateV1ToV2ResponseItemCurrentVersionParametersConditionalBlockParametersCondition]


AuthRuleMigrateV1ToV2ResponseItemCurrentVersionParameters: TypeAlias = Union[
    AuthRuleMigrateV1ToV2ResponseItemCurrentVersionParametersConditionalBlockParameters, VelocityLimitParams
]


class AuthRuleMigrateV1ToV2ResponseItemCurrentVersion(BaseModel):
    parameters: AuthRuleMigrateV1ToV2ResponseItemCurrentVersionParameters
    """Parameters for the current version of the Auth Rule"""

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


class AuthRuleMigrateV1ToV2ResponseItemDraftVersionParametersConditionalBlockParametersCondition(BaseModel):
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


class AuthRuleMigrateV1ToV2ResponseItemDraftVersionParametersConditionalBlockParameters(BaseModel):
    conditions: List[AuthRuleMigrateV1ToV2ResponseItemDraftVersionParametersConditionalBlockParametersCondition]


AuthRuleMigrateV1ToV2ResponseItemDraftVersionParameters: TypeAlias = Union[
    AuthRuleMigrateV1ToV2ResponseItemDraftVersionParametersConditionalBlockParameters, VelocityLimitParams
]


class AuthRuleMigrateV1ToV2ResponseItemDraftVersion(BaseModel):
    parameters: AuthRuleMigrateV1ToV2ResponseItemDraftVersionParameters
    """Parameters for the current version of the Auth Rule"""

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


class AuthRuleMigrateV1ToV2ResponseItem(BaseModel):
    token: str

    account_tokens: List[str]
    """Account tokens to which the Auth Rule applies."""

    card_tokens: List[str]
    """Card tokens to which the Auth Rule applies."""

    current_version: Optional[AuthRuleMigrateV1ToV2ResponseItemCurrentVersion] = None

    draft_version: Optional[AuthRuleMigrateV1ToV2ResponseItemDraftVersion] = None

    program_level: bool
    """Whether the Auth Rule applies to all authorizations on the card program."""

    state: Literal["ACTIVE", "INACTIVE"]
    """The state of the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"]
    """The type of Auth Rule"""


AuthRuleMigrateV1ToV2Response: TypeAlias = List[AuthRuleMigrateV1ToV2ResponseItem]
