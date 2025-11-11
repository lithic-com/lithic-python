# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .velocity_limit_params import VelocityLimitParams
from .merchant_lock_parameters import MerchantLockParameters
from .conditional_block_parameters import ConditionalBlockParameters
from .conditional_3ds_action_parameters import Conditional3DSActionParameters
from .conditional_authorization_action_parameters import ConditionalAuthorizationActionParameters

__all__ = ["V2RetrieveResponse", "CurrentVersion", "CurrentVersionParameters", "DraftVersion", "DraftVersionParameters"]

CurrentVersionParameters: TypeAlias = Union[
    ConditionalBlockParameters,
    VelocityLimitParams,
    MerchantLockParameters,
    Conditional3DSActionParameters,
    ConditionalAuthorizationActionParameters,
]


class CurrentVersion(BaseModel):
    parameters: CurrentVersionParameters
    """Parameters for the Auth Rule"""

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


DraftVersionParameters: TypeAlias = Union[
    ConditionalBlockParameters,
    VelocityLimitParams,
    MerchantLockParameters,
    Conditional3DSActionParameters,
    ConditionalAuthorizationActionParameters,
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

    business_account_tokens: List[str]
    """Business Account tokens to which the Auth Rule applies."""

    card_tokens: List[str]
    """Card tokens to which the Auth Rule applies."""

    current_version: Optional[CurrentVersion] = None

    draft_version: Optional[DraftVersion] = None

    event_stream: Literal["AUTHORIZATION", "THREE_DS_AUTHENTICATION"]
    """The event stream during which the rule will be evaluated."""

    lithic_managed: bool
    """Indicates whether this auth rule is managed by Lithic.

    If true, the rule cannot be modified or deleted by the user
    """

    name: Optional[str] = None
    """Auth Rule Name"""

    program_level: bool
    """Whether the Auth Rule applies to all authorizations on the card program."""

    state: Literal["ACTIVE", "INACTIVE"]
    """The state of the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION"]
    """The type of Auth Rule.

    For certain rule types, this determines the event stream during which it will be
    evaluated. For rules that can be applied to one of several event streams, the
    effective one is defined by the separate `event_stream` field.

    - `CONDITIONAL_BLOCK`: AUTHORIZATION event stream.
    - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
    - `MERCHANT_LOCK`: AUTHORIZATION event stream.
    - `CONDITIONAL_ACTION`: AUTHORIZATION or THREE_DS_AUTHENTICATION event stream.
    """

    excluded_card_tokens: Optional[List[str]] = None
    """Card tokens to which the Auth Rule does not apply."""
