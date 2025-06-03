# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .velocity_limit_params import VelocityLimitParams
from .conditional_block_parameters import ConditionalBlockParameters

__all__ = [
    "V2RetrieveResponse",
    "CurrentVersion",
    "CurrentVersionParameters",
    "CurrentVersionParametersMerchantLockParameters",
    "CurrentVersionParametersMerchantLockParametersMerchant",
    "CurrentVersionParametersConditional3DSActionParameters",
    "CurrentVersionParametersConditional3DsActionParametersCondition",
    "DraftVersion",
    "DraftVersionParameters",
    "DraftVersionParametersMerchantLockParameters",
    "DraftVersionParametersMerchantLockParametersMerchant",
    "DraftVersionParametersConditional3DSActionParameters",
    "DraftVersionParametersConditional3DsActionParametersCondition",
]


class CurrentVersionParametersMerchantLockParametersMerchant(BaseModel):
    comment: Optional[str] = None
    """
    A comment or explanation about the merchant, used internally for rule management
    purposes.
    """

    descriptor: Optional[str] = None
    """
    Short description of the merchant, often used to provide more human-readable
    context about the transaction merchant. This is typically the name or label
    shown on transaction summaries.
    """

    merchant_id: Optional[str] = None
    """Unique alphanumeric identifier for the payment card acceptor (merchant).

    This attribute specifies the merchant entity that will be locked or referenced
    for authorization rules.
    """


class CurrentVersionParametersMerchantLockParameters(BaseModel):
    merchants: List[CurrentVersionParametersMerchantLockParametersMerchant]
    """
    A list of merchant locks defining specific merchants or groups of merchants
    (based on descriptors or IDs) that the lock applies to.
    """


class CurrentVersionParametersConditional3DsActionParametersCondition(BaseModel):
    attribute: Optional[
        Literal[
            "MCC",
            "COUNTRY",
            "CURRENCY",
            "MERCHANT_ID",
            "DESCRIPTOR",
            "TRANSACTION_AMOUNT",
            "RISK_SCORE",
            "MESSAGE_CATEGORY",
        ]
    ] = None
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

    operation: Optional[
        Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    ] = None
    """The operation to apply to the attribute"""

    value: Union[str, int, List[str], None] = None
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class CurrentVersionParametersConditional3DSActionParameters(BaseModel):
    action: Literal["DECLINE", "CHALLENGE"]
    """The action to take if the conditions are met."""

    conditions: List[CurrentVersionParametersConditional3DsActionParametersCondition]


CurrentVersionParameters: TypeAlias = Union[
    ConditionalBlockParameters,
    VelocityLimitParams,
    CurrentVersionParametersMerchantLockParameters,
    CurrentVersionParametersConditional3DSActionParameters,
]


class CurrentVersion(BaseModel):
    parameters: CurrentVersionParameters
    """Parameters for the Auth Rule"""

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


class DraftVersionParametersMerchantLockParametersMerchant(BaseModel):
    comment: Optional[str] = None
    """
    A comment or explanation about the merchant, used internally for rule management
    purposes.
    """

    descriptor: Optional[str] = None
    """
    Short description of the merchant, often used to provide more human-readable
    context about the transaction merchant. This is typically the name or label
    shown on transaction summaries.
    """

    merchant_id: Optional[str] = None
    """Unique alphanumeric identifier for the payment card acceptor (merchant).

    This attribute specifies the merchant entity that will be locked or referenced
    for authorization rules.
    """


class DraftVersionParametersMerchantLockParameters(BaseModel):
    merchants: List[DraftVersionParametersMerchantLockParametersMerchant]
    """
    A list of merchant locks defining specific merchants or groups of merchants
    (based on descriptors or IDs) that the lock applies to.
    """


class DraftVersionParametersConditional3DsActionParametersCondition(BaseModel):
    attribute: Optional[
        Literal[
            "MCC",
            "COUNTRY",
            "CURRENCY",
            "MERCHANT_ID",
            "DESCRIPTOR",
            "TRANSACTION_AMOUNT",
            "RISK_SCORE",
            "MESSAGE_CATEGORY",
        ]
    ] = None
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

    operation: Optional[
        Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    ] = None
    """The operation to apply to the attribute"""

    value: Union[str, int, List[str], None] = None
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class DraftVersionParametersConditional3DSActionParameters(BaseModel):
    action: Literal["DECLINE", "CHALLENGE"]
    """The action to take if the conditions are met."""

    conditions: List[DraftVersionParametersConditional3DsActionParametersCondition]


DraftVersionParameters: TypeAlias = Union[
    ConditionalBlockParameters,
    VelocityLimitParams,
    DraftVersionParametersMerchantLockParameters,
    DraftVersionParametersConditional3DSActionParameters,
]


class DraftVersion(BaseModel):
    parameters: DraftVersionParameters
    """Parameters for the Auth Rule"""

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


class V2RetrieveResponse(BaseModel):
    token: str
    """Auth Rule Token"""

    account_tokens: List[str]
    """Account tokens to which the Auth Rule applies."""

    card_tokens: List[str]
    """Card tokens to which the Auth Rule applies."""

    current_version: Optional[CurrentVersion] = None

    draft_version: Optional[DraftVersion] = None

    event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"]
    """The type of event stream the Auth rule applies to."""

    name: Optional[str] = None
    """Auth Rule Name"""

    program_level: bool
    """Whether the Auth Rule applies to all authorizations on the card program."""

    state: Literal["ACTIVE", "INACTIVE"]
    """The state of the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_3DS_ACTION"]
    """The type of Auth Rule.

    Effectively determines the event stream during which it will be evaluated.

    - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
    - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
    - `MERCHANT_LOCK`: AUTHORIZATION event stream.
    - `CONDITIONAL_3DS_ACTION`: THREE_DS_AUTHENTICATION event stream.
    """

    excluded_card_tokens: Optional[List[str]] = None
    """Card tokens to which the Auth Rule does not apply."""
