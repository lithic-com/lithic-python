# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .velocity_limit_params_param import VelocityLimitParamsParam
from .conditional_block_parameters_param import ConditionalBlockParametersParam

__all__ = [
    "V2CreateParams",
    "CreateAuthRuleRequestAccountTokens",
    "CreateAuthRuleRequestAccountTokensParameters",
    "CreateAuthRuleRequestAccountTokensParametersMerchantLockParameters",
    "CreateAuthRuleRequestAccountTokensParametersMerchantLockParametersMerchant",
    "CreateAuthRuleRequestCardTokens",
    "CreateAuthRuleRequestCardTokensParameters",
    "CreateAuthRuleRequestCardTokensParametersMerchantLockParameters",
    "CreateAuthRuleRequestCardTokensParametersMerchantLockParametersMerchant",
    "CreateAuthRuleRequestProgramLevel",
    "CreateAuthRuleRequestProgramLevelParameters",
    "CreateAuthRuleRequestProgramLevelParametersMerchantLockParameters",
    "CreateAuthRuleRequestProgramLevelParametersMerchantLockParametersMerchant",
]


class CreateAuthRuleRequestAccountTokens(TypedDict, total=False):
    account_tokens: Required[List[str]]
    """Account tokens to which the Auth Rule applies."""

    name: Optional[str]
    """Auth Rule Name"""

    parameters: CreateAuthRuleRequestAccountTokensParameters
    """Parameters for the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK"]
    """The type of Auth Rule"""


class CreateAuthRuleRequestAccountTokensParametersMerchantLockParametersMerchant(TypedDict, total=False):
    comment: str
    """
    A comment or explanation about the merchant, used internally for rule management
    purposes.
    """

    descriptor: str
    """
    Short description of the merchant, often used to provide more human-readable
    context about the transaction merchant. This is typically the name or label
    shown on transaction summaries.
    """

    merchant_id: str
    """Unique alphanumeric identifier for the payment card acceptor (merchant).

    This attribute specifies the merchant entity that will be locked or referenced
    for authorization rules.
    """


class CreateAuthRuleRequestAccountTokensParametersMerchantLockParameters(TypedDict, total=False):
    merchants: Required[Iterable[CreateAuthRuleRequestAccountTokensParametersMerchantLockParametersMerchant]]
    """
    A list of merchant locks defining specific merchants or groups of merchants
    (based on descriptors or IDs) that the lock applies to.
    """


CreateAuthRuleRequestAccountTokensParameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    CreateAuthRuleRequestAccountTokensParametersMerchantLockParameters,
]


class CreateAuthRuleRequestCardTokens(TypedDict, total=False):
    card_tokens: Required[List[str]]
    """Card tokens to which the Auth Rule applies."""

    name: Optional[str]
    """Auth Rule Name"""

    parameters: CreateAuthRuleRequestCardTokensParameters
    """Parameters for the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK"]
    """The type of Auth Rule"""


class CreateAuthRuleRequestCardTokensParametersMerchantLockParametersMerchant(TypedDict, total=False):
    comment: str
    """
    A comment or explanation about the merchant, used internally for rule management
    purposes.
    """

    descriptor: str
    """
    Short description of the merchant, often used to provide more human-readable
    context about the transaction merchant. This is typically the name or label
    shown on transaction summaries.
    """

    merchant_id: str
    """Unique alphanumeric identifier for the payment card acceptor (merchant).

    This attribute specifies the merchant entity that will be locked or referenced
    for authorization rules.
    """


class CreateAuthRuleRequestCardTokensParametersMerchantLockParameters(TypedDict, total=False):
    merchants: Required[Iterable[CreateAuthRuleRequestCardTokensParametersMerchantLockParametersMerchant]]
    """
    A list of merchant locks defining specific merchants or groups of merchants
    (based on descriptors or IDs) that the lock applies to.
    """


CreateAuthRuleRequestCardTokensParameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    CreateAuthRuleRequestCardTokensParametersMerchantLockParameters,
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

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK"]
    """The type of Auth Rule"""


class CreateAuthRuleRequestProgramLevelParametersMerchantLockParametersMerchant(TypedDict, total=False):
    comment: str
    """
    A comment or explanation about the merchant, used internally for rule management
    purposes.
    """

    descriptor: str
    """
    Short description of the merchant, often used to provide more human-readable
    context about the transaction merchant. This is typically the name or label
    shown on transaction summaries.
    """

    merchant_id: str
    """Unique alphanumeric identifier for the payment card acceptor (merchant).

    This attribute specifies the merchant entity that will be locked or referenced
    for authorization rules.
    """


class CreateAuthRuleRequestProgramLevelParametersMerchantLockParameters(TypedDict, total=False):
    merchants: Required[Iterable[CreateAuthRuleRequestProgramLevelParametersMerchantLockParametersMerchant]]
    """
    A list of merchant locks defining specific merchants or groups of merchants
    (based on descriptors or IDs) that the lock applies to.
    """


CreateAuthRuleRequestProgramLevelParameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    CreateAuthRuleRequestProgramLevelParametersMerchantLockParameters,
]

V2CreateParams: TypeAlias = Union[
    CreateAuthRuleRequestAccountTokens, CreateAuthRuleRequestCardTokens, CreateAuthRuleRequestProgramLevel
]
