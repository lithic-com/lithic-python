# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..shared_params.velocity_limit_params import VelocityLimitParams

__all__ = [
    "V2CreateParams",
    "CreateAuthRuleRequestAccountTokens",
    "CreateAuthRuleRequestAccountTokensParameters",
    "CreateAuthRuleRequestAccountTokensParametersConditionalBlockParameters",
    "CreateAuthRuleRequestAccountTokensParametersConditionalBlockParametersCondition",
    "CreateAuthRuleRequestCardTokens",
    "CreateAuthRuleRequestCardTokensParameters",
    "CreateAuthRuleRequestCardTokensParametersConditionalBlockParameters",
    "CreateAuthRuleRequestCardTokensParametersConditionalBlockParametersCondition",
    "CreateAuthRuleRequestProgramLevel",
    "CreateAuthRuleRequestProgramLevelParameters",
    "CreateAuthRuleRequestProgramLevelParametersConditionalBlockParameters",
    "CreateAuthRuleRequestProgramLevelParametersConditionalBlockParametersCondition",
]


class CreateAuthRuleRequestAccountTokens(TypedDict, total=False):
    account_tokens: Required[List[str]]
    """Account tokens to which the Auth Rule applies."""

    parameters: CreateAuthRuleRequestAccountTokensParameters
    """Parameters for the current version of the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"]
    """The type of Auth Rule"""


class CreateAuthRuleRequestAccountTokensParametersConditionalBlockParametersCondition(TypedDict, total=False):
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
    ]
    """The attribute to target"""

    operation: Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    """The operation to apply to the attribute"""

    value: Union[str, float, List[str]]
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class CreateAuthRuleRequestAccountTokensParametersConditionalBlockParameters(TypedDict, total=False):
    conditions: Required[Iterable[CreateAuthRuleRequestAccountTokensParametersConditionalBlockParametersCondition]]


CreateAuthRuleRequestAccountTokensParameters: TypeAlias = Union[
    CreateAuthRuleRequestAccountTokensParametersConditionalBlockParameters, VelocityLimitParams
]


class CreateAuthRuleRequestCardTokens(TypedDict, total=False):
    card_tokens: Required[List[str]]
    """Card tokens to which the Auth Rule applies."""

    parameters: CreateAuthRuleRequestCardTokensParameters
    """Parameters for the current version of the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"]
    """The type of Auth Rule"""


class CreateAuthRuleRequestCardTokensParametersConditionalBlockParametersCondition(TypedDict, total=False):
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
    ]
    """The attribute to target"""

    operation: Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    """The operation to apply to the attribute"""

    value: Union[str, float, List[str]]
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class CreateAuthRuleRequestCardTokensParametersConditionalBlockParameters(TypedDict, total=False):
    conditions: Required[Iterable[CreateAuthRuleRequestCardTokensParametersConditionalBlockParametersCondition]]


CreateAuthRuleRequestCardTokensParameters: TypeAlias = Union[
    CreateAuthRuleRequestCardTokensParametersConditionalBlockParameters, VelocityLimitParams
]


class CreateAuthRuleRequestProgramLevel(TypedDict, total=False):
    program_level: Required[bool]
    """Whether the Auth Rule applies to all authorizations on the card program."""

    parameters: CreateAuthRuleRequestProgramLevelParameters
    """Parameters for the current version of the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"]
    """The type of Auth Rule"""


class CreateAuthRuleRequestProgramLevelParametersConditionalBlockParametersCondition(TypedDict, total=False):
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
    ]
    """The attribute to target"""

    operation: Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    """The operation to apply to the attribute"""

    value: Union[str, float, List[str]]
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class CreateAuthRuleRequestProgramLevelParametersConditionalBlockParameters(TypedDict, total=False):
    conditions: Required[Iterable[CreateAuthRuleRequestProgramLevelParametersConditionalBlockParametersCondition]]


CreateAuthRuleRequestProgramLevelParameters: TypeAlias = Union[
    CreateAuthRuleRequestProgramLevelParametersConditionalBlockParameters, VelocityLimitParams
]

V2CreateParams: TypeAlias = Union[
    CreateAuthRuleRequestAccountTokens, CreateAuthRuleRequestCardTokens, CreateAuthRuleRequestProgramLevel
]
