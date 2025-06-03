# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .velocity_limit_params_param import VelocityLimitParamsParam
from .conditional_block_parameters_param import ConditionalBlockParametersParam

__all__ = [
    "V2DraftParams",
    "Parameters",
    "ParametersMerchantLockParameters",
    "ParametersMerchantLockParametersMerchant",
    "ParametersConditional3DSActionParameters",
    "ParametersConditional3DsActionParametersCondition",
]


class V2DraftParams(TypedDict, total=False):
    parameters: Optional[Parameters]
    """Parameters for the Auth Rule"""


class ParametersMerchantLockParametersMerchant(TypedDict, total=False):
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


class ParametersMerchantLockParameters(TypedDict, total=False):
    merchants: Required[Iterable[ParametersMerchantLockParametersMerchant]]
    """
    A list of merchant locks defining specific merchants or groups of merchants
    (based on descriptors or IDs) that the lock applies to.
    """


class ParametersConditional3DsActionParametersCondition(TypedDict, total=False):
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


class ParametersConditional3DSActionParameters(TypedDict, total=False):
    action: Required[Literal["DECLINE", "CHALLENGE"]]
    """The action to take if the conditions are met."""

    conditions: Required[Iterable[ParametersConditional3DsActionParametersCondition]]


Parameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    ParametersMerchantLockParameters,
    ParametersConditional3DSActionParameters,
]
