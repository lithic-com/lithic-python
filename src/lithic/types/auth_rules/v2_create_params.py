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
    "CreateAuthRuleRequestAccountTokensParametersConditional3DSActionParameters",
    "CreateAuthRuleRequestAccountTokensParametersConditional3DsActionParametersCondition",
    "CreateAuthRuleRequestCardTokens",
    "CreateAuthRuleRequestCardTokensParameters",
    "CreateAuthRuleRequestCardTokensParametersMerchantLockParameters",
    "CreateAuthRuleRequestCardTokensParametersMerchantLockParametersMerchant",
    "CreateAuthRuleRequestCardTokensParametersConditional3DSActionParameters",
    "CreateAuthRuleRequestCardTokensParametersConditional3DsActionParametersCondition",
    "CreateAuthRuleRequestProgramLevel",
    "CreateAuthRuleRequestProgramLevelParameters",
    "CreateAuthRuleRequestProgramLevelParametersMerchantLockParameters",
    "CreateAuthRuleRequestProgramLevelParametersMerchantLockParametersMerchant",
    "CreateAuthRuleRequestProgramLevelParametersConditional3DSActionParameters",
    "CreateAuthRuleRequestProgramLevelParametersConditional3DsActionParametersCondition",
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


class CreateAuthRuleRequestAccountTokensParametersConditional3DsActionParametersCondition(TypedDict, total=False):
    attribute: Literal[
        "MCC",
        "COUNTRY",
        "CURRENCY",
        "MERCHANT_ID",
        "DESCRIPTOR",
        "TRANSACTION_AMOUNT",
        "RISK_SCORE",
        "MESSAGE_CATEGORY",
    ]
    """The attribute to target.

    The following attributes may be targeted:

    - `MCC`: A four-digit number listed in ISO 18245. An MCC is used to classify a
      business by the types of goods or services it provides.
    - `COUNTRY`: Country of entity of card acceptor. Possible values are: (1) all
      ISO 3166-1 alpha-3 country codes, (2) QZZ for Kosovo, and (3) ANT for
      Netherlands Antilles.
    - `CURRENCY`: 3-character alphabetic ISO 4217 code for the merchant currency of
      the transaction.
    - `MERCHANT_ID`: Unique alphanumeric identifier for the payment card acceptor
      (merchant).
    - `DESCRIPTOR`: Short description of card acceptor.
    - `TRANSACTION_AMOUNT`: The base transaction amount (in cents) plus the acquirer
      fee field in the settlement/cardholder billing currency. This is the amount
      the issuer should authorize against unless the issuer is paying the acquirer
      fee on behalf of the cardholder.
    - `RISK_SCORE`: Network-provided score assessing risk level associated with a
      given authentication. Scores are on a range of 0-999, with 0 representing the
      lowest risk and 999 representing the highest risk. For Visa transactions,
      where the raw score has a range of 0-99, Lithic will normalize the score by
      multiplying the raw score by 10x.
    - `MESSAGE_CATEGORY`: The category of the authentication being processed.
    """

    operation: Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    """The operation to apply to the attribute"""

    value: Union[str, int, List[str]]
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class CreateAuthRuleRequestAccountTokensParametersConditional3DSActionParameters(TypedDict, total=False):
    action: Required[Literal["DECLINE", "CHALLENGE"]]
    """The action to take if the conditions are met."""

    conditions: Required[Iterable[CreateAuthRuleRequestAccountTokensParametersConditional3DsActionParametersCondition]]


CreateAuthRuleRequestAccountTokensParameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    CreateAuthRuleRequestAccountTokensParametersMerchantLockParameters,
    CreateAuthRuleRequestAccountTokensParametersConditional3DSActionParameters,
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


class CreateAuthRuleRequestCardTokensParametersConditional3DsActionParametersCondition(TypedDict, total=False):
    attribute: Literal[
        "MCC",
        "COUNTRY",
        "CURRENCY",
        "MERCHANT_ID",
        "DESCRIPTOR",
        "TRANSACTION_AMOUNT",
        "RISK_SCORE",
        "MESSAGE_CATEGORY",
    ]
    """The attribute to target.

    The following attributes may be targeted:

    - `MCC`: A four-digit number listed in ISO 18245. An MCC is used to classify a
      business by the types of goods or services it provides.
    - `COUNTRY`: Country of entity of card acceptor. Possible values are: (1) all
      ISO 3166-1 alpha-3 country codes, (2) QZZ for Kosovo, and (3) ANT for
      Netherlands Antilles.
    - `CURRENCY`: 3-character alphabetic ISO 4217 code for the merchant currency of
      the transaction.
    - `MERCHANT_ID`: Unique alphanumeric identifier for the payment card acceptor
      (merchant).
    - `DESCRIPTOR`: Short description of card acceptor.
    - `TRANSACTION_AMOUNT`: The base transaction amount (in cents) plus the acquirer
      fee field in the settlement/cardholder billing currency. This is the amount
      the issuer should authorize against unless the issuer is paying the acquirer
      fee on behalf of the cardholder.
    - `RISK_SCORE`: Network-provided score assessing risk level associated with a
      given authentication. Scores are on a range of 0-999, with 0 representing the
      lowest risk and 999 representing the highest risk. For Visa transactions,
      where the raw score has a range of 0-99, Lithic will normalize the score by
      multiplying the raw score by 10x.
    - `MESSAGE_CATEGORY`: The category of the authentication being processed.
    """

    operation: Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    """The operation to apply to the attribute"""

    value: Union[str, int, List[str]]
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class CreateAuthRuleRequestCardTokensParametersConditional3DSActionParameters(TypedDict, total=False):
    action: Required[Literal["DECLINE", "CHALLENGE"]]
    """The action to take if the conditions are met."""

    conditions: Required[Iterable[CreateAuthRuleRequestCardTokensParametersConditional3DsActionParametersCondition]]


CreateAuthRuleRequestCardTokensParameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    CreateAuthRuleRequestCardTokensParametersMerchantLockParameters,
    CreateAuthRuleRequestCardTokensParametersConditional3DSActionParameters,
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


class CreateAuthRuleRequestProgramLevelParametersConditional3DsActionParametersCondition(TypedDict, total=False):
    attribute: Literal[
        "MCC",
        "COUNTRY",
        "CURRENCY",
        "MERCHANT_ID",
        "DESCRIPTOR",
        "TRANSACTION_AMOUNT",
        "RISK_SCORE",
        "MESSAGE_CATEGORY",
    ]
    """The attribute to target.

    The following attributes may be targeted:

    - `MCC`: A four-digit number listed in ISO 18245. An MCC is used to classify a
      business by the types of goods or services it provides.
    - `COUNTRY`: Country of entity of card acceptor. Possible values are: (1) all
      ISO 3166-1 alpha-3 country codes, (2) QZZ for Kosovo, and (3) ANT for
      Netherlands Antilles.
    - `CURRENCY`: 3-character alphabetic ISO 4217 code for the merchant currency of
      the transaction.
    - `MERCHANT_ID`: Unique alphanumeric identifier for the payment card acceptor
      (merchant).
    - `DESCRIPTOR`: Short description of card acceptor.
    - `TRANSACTION_AMOUNT`: The base transaction amount (in cents) plus the acquirer
      fee field in the settlement/cardholder billing currency. This is the amount
      the issuer should authorize against unless the issuer is paying the acquirer
      fee on behalf of the cardholder.
    - `RISK_SCORE`: Network-provided score assessing risk level associated with a
      given authentication. Scores are on a range of 0-999, with 0 representing the
      lowest risk and 999 representing the highest risk. For Visa transactions,
      where the raw score has a range of 0-99, Lithic will normalize the score by
      multiplying the raw score by 10x.
    - `MESSAGE_CATEGORY`: The category of the authentication being processed.
    """

    operation: Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    """The operation to apply to the attribute"""

    value: Union[str, int, List[str]]
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class CreateAuthRuleRequestProgramLevelParametersConditional3DSActionParameters(TypedDict, total=False):
    action: Required[Literal["DECLINE", "CHALLENGE"]]
    """The action to take if the conditions are met."""

    conditions: Required[Iterable[CreateAuthRuleRequestProgramLevelParametersConditional3DsActionParametersCondition]]


CreateAuthRuleRequestProgramLevelParameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    CreateAuthRuleRequestProgramLevelParametersMerchantLockParameters,
    CreateAuthRuleRequestProgramLevelParametersConditional3DSActionParameters,
]

V2CreateParams: TypeAlias = Union[
    CreateAuthRuleRequestAccountTokens, CreateAuthRuleRequestCardTokens, CreateAuthRuleRequestProgramLevel
]
