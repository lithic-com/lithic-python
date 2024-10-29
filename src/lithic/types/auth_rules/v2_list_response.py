# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..shared.velocity_limit_params import VelocityLimitParams

__all__ = [
    "V2ListResponse",
    "CurrentVersion",
    "CurrentVersionParameters",
    "CurrentVersionParametersConditionalBlockParameters",
    "CurrentVersionParametersConditionalBlockParametersCondition",
    "DraftVersion",
    "DraftVersionParameters",
    "DraftVersionParametersConditionalBlockParameters",
    "DraftVersionParametersConditionalBlockParametersCondition",
]


class CurrentVersionParametersConditionalBlockParametersCondition(BaseModel):
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

    operation: Optional[
        Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    ] = None
    """The operation to apply to the attribute"""

    value: Union[str, float, List[str], None] = None
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class CurrentVersionParametersConditionalBlockParameters(BaseModel):
    conditions: List[CurrentVersionParametersConditionalBlockParametersCondition]


CurrentVersionParameters: TypeAlias = Union[CurrentVersionParametersConditionalBlockParameters, VelocityLimitParams]


class CurrentVersion(BaseModel):
    parameters: CurrentVersionParameters
    """Parameters for the current version of the Auth Rule"""

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


class DraftVersionParametersConditionalBlockParametersCondition(BaseModel):
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

    operation: Optional[
        Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    ] = None
    """The operation to apply to the attribute"""

    value: Union[str, float, List[str], None] = None
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class DraftVersionParametersConditionalBlockParameters(BaseModel):
    conditions: List[DraftVersionParametersConditionalBlockParametersCondition]


DraftVersionParameters: TypeAlias = Union[DraftVersionParametersConditionalBlockParameters, VelocityLimitParams]


class DraftVersion(BaseModel):
    parameters: DraftVersionParameters
    """Parameters for the current version of the Auth Rule"""

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


class V2ListResponse(BaseModel):
    token: str

    account_tokens: List[str]
    """Account tokens to which the Auth Rule applies."""

    card_tokens: List[str]
    """Card tokens to which the Auth Rule applies."""

    current_version: Optional[CurrentVersion] = None

    draft_version: Optional[DraftVersion] = None

    program_level: bool
    """Whether the Auth Rule applies to all authorizations on the card program."""

    state: Literal["ACTIVE", "INACTIVE"]
    """The state of the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"]
    """The type of Auth Rule"""
