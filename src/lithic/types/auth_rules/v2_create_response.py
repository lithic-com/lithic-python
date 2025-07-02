# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .velocity_limit_params import VelocityLimitParams
from .merchant_lock_parameters import MerchantLockParameters
from .conditional_block_parameters import ConditionalBlockParameters
from .conditional_3ds_action_parameters import Conditional3DSActionParameters

__all__ = ["V2CreateResponse", "CurrentVersion", "CurrentVersionParameters", "DraftVersion", "DraftVersionParameters"]

CurrentVersionParameters: TypeAlias = Union[
    ConditionalBlockParameters, VelocityLimitParams, MerchantLockParameters, Conditional3DSActionParameters
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
    ConditionalBlockParameters, VelocityLimitParams, MerchantLockParameters, Conditional3DSActionParameters
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
