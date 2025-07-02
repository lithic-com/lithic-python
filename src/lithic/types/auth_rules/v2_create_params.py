# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .velocity_limit_params_param import VelocityLimitParamsParam
from .merchant_lock_parameters_param import MerchantLockParametersParam
from .conditional_block_parameters_param import ConditionalBlockParametersParam
from .conditional_3ds_action_parameters_param import Conditional3DSActionParametersParam

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

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_3DS_ACTION"]
    """The type of Auth Rule.

    Effectively determines the event stream during which it will be evaluated.

    - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
    - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
    - `MERCHANT_LOCK`: AUTHORIZATION event stream.
    - `CONDITIONAL_3DS_ACTION`: THREE_DS_AUTHENTICATION event stream.
    """


CreateAuthRuleRequestAccountTokensParameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    MerchantLockParametersParam,
    Conditional3DSActionParametersParam,
]


class CreateAuthRuleRequestCardTokens(TypedDict, total=False):
    card_tokens: Required[List[str]]
    """Card tokens to which the Auth Rule applies."""

    name: Optional[str]
    """Auth Rule Name"""

    parameters: CreateAuthRuleRequestCardTokensParameters
    """Parameters for the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_3DS_ACTION"]
    """The type of Auth Rule.

    Effectively determines the event stream during which it will be evaluated.

    - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
    - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
    - `MERCHANT_LOCK`: AUTHORIZATION event stream.
    - `CONDITIONAL_3DS_ACTION`: THREE_DS_AUTHENTICATION event stream.
    """


CreateAuthRuleRequestCardTokensParameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    MerchantLockParametersParam,
    Conditional3DSActionParametersParam,
]


class CreateAuthRuleRequestProgramLevel(TypedDict, total=False):
    program_level: Required[bool]
    """Whether the Auth Rule applies to all authorizations on the card program."""

    excluded_card_tokens: List[str]
    """Card tokens to which the Auth Rule does not apply."""

    name: Optional[str]
    """Auth Rule Name"""

    parameters: CreateAuthRuleRequestProgramLevelParameters
    """Parameters for the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_3DS_ACTION"]
    """The type of Auth Rule.

    Effectively determines the event stream during which it will be evaluated.

    - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
    - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
    - `MERCHANT_LOCK`: AUTHORIZATION event stream.
    - `CONDITIONAL_3DS_ACTION`: THREE_DS_AUTHENTICATION event stream.
    """


CreateAuthRuleRequestProgramLevelParameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    MerchantLockParametersParam,
    Conditional3DSActionParametersParam,
]

V2CreateParams: TypeAlias = Union[
    CreateAuthRuleRequestAccountTokens, CreateAuthRuleRequestCardTokens, CreateAuthRuleRequestProgramLevel
]
