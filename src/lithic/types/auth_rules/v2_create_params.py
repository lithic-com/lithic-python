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
    """The attribute to target.

    The following attributes may be targeted:

    - `MCC`: A four-digit number listed in ISO 18245. An MCC is used to classify a
      business by the types of goods or services it provides.
    - `COUNTRY`: Country of entity of card acceptor. Possible values are: (1) all
      ISO 3166-1 alpha-3 country codes, (2) QZZ for Kosovo, and (3) ANT for
      Netherlands Antilles.
    - `CURRENCY`: 3-digit alphabetic ISO 4217 code for the merchant currency of the
      transaction.
    - `MERCHANT_ID`: Unique alphanumeric identifier for the payment card acceptor
      (merchant).
    - `DESCRIPTOR`: Short description of card acceptor.
    - `LIABILITY_SHIFT`: Indicates whether chargeback liability shift to the issuer
      applies to the transaction. Valid values are `NONE`, `3DS_AUTHENTICATED`, or
      `TOKEN_AUTHENTICATED`.
    - `PAN_ENTRY_MODE`: The method by which the cardholder's primary account number
      (PAN) was entered. Valid values are `AUTO_ENTRY`, `BAR_CODE`, `CONTACTLESS`,
      `ECOMMERCE`, `ERROR_KEYED`, `ERROR_MAGNETIC_STRIPE`, `ICC`, `KEY_ENTERED`,
      `MAGNETIC_STRIPE`, `MANUAL`, `OCR`, `SECURE_CARDLESS`, `UNSPECIFIED`,
      `UNKNOWN`, `CREDENTIAL_ON_FILE`, or `ECOMMERCE`.
    - `TRANSACTION_AMOUNT`: The base transaction amount (in cents) plus the acquirer
      fee field in the settlement/cardholder billing currency. This is the amount
      the issuer should authorize against unless the issuer is paying the acquirer
      fee on behalf of the cardholder.
    - `RISK_SCORE`: Network-provided score assessing risk level associated with a
      given authorization. Scores are on a range of 0-999, with 0 representing the
      lowest risk and 999 representing the highest risk. For Visa transactions,
      where the raw score has a range of 0-99, Lithic will normalize the score by
      multiplying the raw score by 10x.
    """

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
    """The attribute to target.

    The following attributes may be targeted:

    - `MCC`: A four-digit number listed in ISO 18245. An MCC is used to classify a
      business by the types of goods or services it provides.
    - `COUNTRY`: Country of entity of card acceptor. Possible values are: (1) all
      ISO 3166-1 alpha-3 country codes, (2) QZZ for Kosovo, and (3) ANT for
      Netherlands Antilles.
    - `CURRENCY`: 3-digit alphabetic ISO 4217 code for the merchant currency of the
      transaction.
    - `MERCHANT_ID`: Unique alphanumeric identifier for the payment card acceptor
      (merchant).
    - `DESCRIPTOR`: Short description of card acceptor.
    - `LIABILITY_SHIFT`: Indicates whether chargeback liability shift to the issuer
      applies to the transaction. Valid values are `NONE`, `3DS_AUTHENTICATED`, or
      `TOKEN_AUTHENTICATED`.
    - `PAN_ENTRY_MODE`: The method by which the cardholder's primary account number
      (PAN) was entered. Valid values are `AUTO_ENTRY`, `BAR_CODE`, `CONTACTLESS`,
      `ECOMMERCE`, `ERROR_KEYED`, `ERROR_MAGNETIC_STRIPE`, `ICC`, `KEY_ENTERED`,
      `MAGNETIC_STRIPE`, `MANUAL`, `OCR`, `SECURE_CARDLESS`, `UNSPECIFIED`,
      `UNKNOWN`, `CREDENTIAL_ON_FILE`, or `ECOMMERCE`.
    - `TRANSACTION_AMOUNT`: The base transaction amount (in cents) plus the acquirer
      fee field in the settlement/cardholder billing currency. This is the amount
      the issuer should authorize against unless the issuer is paying the acquirer
      fee on behalf of the cardholder.
    - `RISK_SCORE`: Network-provided score assessing risk level associated with a
      given authorization. Scores are on a range of 0-999, with 0 representing the
      lowest risk and 999 representing the highest risk. For Visa transactions,
      where the raw score has a range of 0-99, Lithic will normalize the score by
      multiplying the raw score by 10x.
    """

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
    """The attribute to target.

    The following attributes may be targeted:

    - `MCC`: A four-digit number listed in ISO 18245. An MCC is used to classify a
      business by the types of goods or services it provides.
    - `COUNTRY`: Country of entity of card acceptor. Possible values are: (1) all
      ISO 3166-1 alpha-3 country codes, (2) QZZ for Kosovo, and (3) ANT for
      Netherlands Antilles.
    - `CURRENCY`: 3-digit alphabetic ISO 4217 code for the merchant currency of the
      transaction.
    - `MERCHANT_ID`: Unique alphanumeric identifier for the payment card acceptor
      (merchant).
    - `DESCRIPTOR`: Short description of card acceptor.
    - `LIABILITY_SHIFT`: Indicates whether chargeback liability shift to the issuer
      applies to the transaction. Valid values are `NONE`, `3DS_AUTHENTICATED`, or
      `TOKEN_AUTHENTICATED`.
    - `PAN_ENTRY_MODE`: The method by which the cardholder's primary account number
      (PAN) was entered. Valid values are `AUTO_ENTRY`, `BAR_CODE`, `CONTACTLESS`,
      `ECOMMERCE`, `ERROR_KEYED`, `ERROR_MAGNETIC_STRIPE`, `ICC`, `KEY_ENTERED`,
      `MAGNETIC_STRIPE`, `MANUAL`, `OCR`, `SECURE_CARDLESS`, `UNSPECIFIED`,
      `UNKNOWN`, `CREDENTIAL_ON_FILE`, or `ECOMMERCE`.
    - `TRANSACTION_AMOUNT`: The base transaction amount (in cents) plus the acquirer
      fee field in the settlement/cardholder billing currency. This is the amount
      the issuer should authorize against unless the issuer is paying the acquirer
      fee on behalf of the cardholder.
    - `RISK_SCORE`: Network-provided score assessing risk level associated with a
      given authorization. Scores are on a range of 0-999, with 0 representing the
      lowest risk and 999 representing the highest risk. For Visa transactions,
      where the raw score has a range of 0-99, Lithic will normalize the score by
      multiplying the raw score by 10x.
    """

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
