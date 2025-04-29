# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .velocity_limit_params import VelocityLimitParams
from .conditional_block_parameters import ConditionalBlockParameters

__all__ = [
    "V2CreateResponse",
    "CurrentVersion",
    "CurrentVersionParameters",
    "CurrentVersionParametersMerchantLockParameters",
    "CurrentVersionParametersMerchantLockParametersMerchant",
    "DraftVersion",
    "DraftVersionParameters",
    "DraftVersionParametersMerchantLockParameters",
    "DraftVersionParametersMerchantLockParametersMerchant",
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


CurrentVersionParameters: TypeAlias = Union[
    ConditionalBlockParameters, VelocityLimitParams, CurrentVersionParametersMerchantLockParameters
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


DraftVersionParameters: TypeAlias = Union[
    ConditionalBlockParameters, VelocityLimitParams, DraftVersionParametersMerchantLockParameters
]


class DraftVersion(BaseModel):
    parameters: DraftVersionParameters
    """Parameters for the Auth Rule"""

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


class V2CreateResponse(BaseModel):
    token: str
    """Auth Rule Token"""

    account_tokens: List[str]
    """Account tokens to which the Auth Rule applies."""

    card_tokens: List[str]
    """Card tokens to which the Auth Rule applies."""

    current_version: Optional[CurrentVersion] = None

    draft_version: Optional[DraftVersion] = None

    name: Optional[str] = None
    """Auth Rule Name"""

    program_level: bool
    """Whether the Auth Rule applies to all authorizations on the card program."""

    state: Literal["ACTIVE", "INACTIVE"]
    """The state of the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK"]
    """The type of Auth Rule"""

    excluded_card_tokens: Optional[List[str]] = None
    """Card tokens to which the Auth Rule does not apply."""
