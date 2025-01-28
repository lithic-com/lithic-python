# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .velocity_limit_params_param import VelocityLimitParamsParam
from .conditional_block_parameters_param import ConditionalBlockParametersParam

__all__ = [
    "V2CreateParams",
    "CreateAuthRuleRequestAccountTokens",
    "CreateAuthRuleRequestAccountTokensParameters",
    "CreateAuthRuleRequestCardTokens",
    "CreateAuthRuleRequestCardTokensParameters",
    "CreateAuthRuleRequestProgramLevel",
    "CreateAuthRuleRequestProgramLevelParameters",
]


class CreateAuthRuleRequestAccountTokens(TypedDict, total=False):
    account_tokens: Required[List[str]]
    """Account tokens to which the Auth Rule applies."""

    name: Optional[str]
    """Auth Rule Name"""

    parameters: CreateAuthRuleRequestAccountTokensParameters
    """Parameters for the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"]
    """The type of Auth Rule"""


CreateAuthRuleRequestAccountTokensParameters: TypeAlias = Union[
    ConditionalBlockParametersParam, VelocityLimitParamsParam
]


class CreateAuthRuleRequestCardTokens(TypedDict, total=False):
    card_tokens: Required[List[str]]
    """Card tokens to which the Auth Rule applies."""

    name: Optional[str]
    """Auth Rule Name"""

    parameters: CreateAuthRuleRequestCardTokensParameters
    """Parameters for the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"]
    """The type of Auth Rule"""


CreateAuthRuleRequestCardTokensParameters: TypeAlias = Union[ConditionalBlockParametersParam, VelocityLimitParamsParam]


class CreateAuthRuleRequestProgramLevel(TypedDict, total=False):
    program_level: Required[bool]
    """Whether the Auth Rule applies to all authorizations on the card program."""

    excluded_card_tokens: List[str]
    """Card tokens to which the Auth Rule does not apply."""

    name: Optional[str]
    """Auth Rule Name"""

    parameters: CreateAuthRuleRequestProgramLevelParameters
    """Parameters for the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"]
    """The type of Auth Rule"""


CreateAuthRuleRequestProgramLevelParameters: TypeAlias = Union[
    ConditionalBlockParametersParam, VelocityLimitParamsParam
]

V2CreateParams: TypeAlias = Union[
    CreateAuthRuleRequestAccountTokens, CreateAuthRuleRequestCardTokens, CreateAuthRuleRequestProgramLevel
]
