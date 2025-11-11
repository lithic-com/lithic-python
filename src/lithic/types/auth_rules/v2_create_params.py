# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .velocity_limit_params_param import VelocityLimitParamsParam
from .merchant_lock_parameters_param import MerchantLockParametersParam
from .conditional_block_parameters_param import ConditionalBlockParametersParam
from .conditional_3ds_action_parameters_param import Conditional3DSActionParametersParam
from .conditional_authorization_action_parameters_param import ConditionalAuthorizationActionParametersParam

__all__ = [
    "V2CreateParams",
    "AccountLevelRule",
    "AccountLevelRuleParameters",
    "CardLevelRule",
    "CardLevelRuleParameters",
    "ProgramLevelRule",
    "ProgramLevelRuleParameters",
]


class AccountLevelRule(TypedDict, total=False):
    parameters: Required[AccountLevelRuleParameters]
    """Parameters for the Auth Rule"""

    type: Required[Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION"]]
    """The type of Auth Rule.

    For certain rule types, this determines the event stream during which it will be
    evaluated. For rules that can be applied to one of several event streams, the
    effective one is defined by the separate `event_stream` field.

    - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
    - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
    - `MERCHANT_LOCK`: AUTHORIZATION event stream.
    - `CONDITIONAL_ACTION`: AUTHORIZATION or THREE_DS_AUTHENTICATION event stream.
    """

    account_tokens: SequenceNotStr[str]
    """Account tokens to which the Auth Rule applies."""

    business_account_tokens: SequenceNotStr[str]
    """Business Account tokens to which the Auth Rule applies."""

    event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"]
    """The event stream during which the rule will be evaluated."""

    name: Optional[str]
    """Auth Rule Name"""


AccountLevelRuleParameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    MerchantLockParametersParam,
    Conditional3DSActionParametersParam,
    ConditionalAuthorizationActionParametersParam,
]


class CardLevelRule(TypedDict, total=False):
    card_tokens: Required[SequenceNotStr[str]]
    """Card tokens to which the Auth Rule applies."""

    parameters: Required[CardLevelRuleParameters]
    """Parameters for the Auth Rule"""

    type: Required[Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION"]]
    """The type of Auth Rule.

    For certain rule types, this determines the event stream during which it will be
    evaluated. For rules that can be applied to one of several event streams, the
    effective one is defined by the separate `event_stream` field.

    - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
    - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
    - `MERCHANT_LOCK`: AUTHORIZATION event stream.
    - `CONDITIONAL_ACTION`: AUTHORIZATION or THREE_DS_AUTHENTICATION event stream.
    """

    event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"]
    """The event stream during which the rule will be evaluated."""

    name: Optional[str]
    """Auth Rule Name"""


CardLevelRuleParameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    MerchantLockParametersParam,
    Conditional3DSActionParametersParam,
    ConditionalAuthorizationActionParametersParam,
]


class ProgramLevelRule(TypedDict, total=False):
    parameters: Required[ProgramLevelRuleParameters]
    """Parameters for the Auth Rule"""

    program_level: Required[bool]
    """Whether the Auth Rule applies to all authorizations on the card program."""

    type: Required[Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION"]]
    """The type of Auth Rule.

    For certain rule types, this determines the event stream during which it will be
    evaluated. For rules that can be applied to one of several event streams, the
    effective one is defined by the separate `event_stream` field.

    - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
    - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
    - `MERCHANT_LOCK`: AUTHORIZATION event stream.
    - `CONDITIONAL_ACTION`: AUTHORIZATION or THREE_DS_AUTHENTICATION event stream.
    """

    event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"]
    """The event stream during which the rule will be evaluated."""

    excluded_card_tokens: SequenceNotStr[str]
    """Card tokens to which the Auth Rule does not apply."""

    name: Optional[str]
    """Auth Rule Name"""


ProgramLevelRuleParameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    MerchantLockParametersParam,
    Conditional3DSActionParametersParam,
    ConditionalAuthorizationActionParametersParam,
]

V2CreateParams: TypeAlias = Union[AccountLevelRule, CardLevelRule, ProgramLevelRule]
