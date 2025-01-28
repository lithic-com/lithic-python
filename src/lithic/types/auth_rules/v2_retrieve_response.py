# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .velocity_limit_params import VelocityLimitParams
from .conditional_block_parameters import ConditionalBlockParameters

__all__ = ["V2RetrieveResponse", "CurrentVersion", "CurrentVersionParameters", "DraftVersion", "DraftVersionParameters"]

CurrentVersionParameters: TypeAlias = Union[ConditionalBlockParameters, VelocityLimitParams]


class CurrentVersion(BaseModel):
    parameters: CurrentVersionParameters
    """Parameters for the Auth Rule"""

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


DraftVersionParameters: TypeAlias = Union[ConditionalBlockParameters, VelocityLimitParams]


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

    name: Optional[str] = None
    """Auth Rule Name"""

    program_level: bool
    """Whether the Auth Rule applies to all authorizations on the card program."""

    state: Literal["ACTIVE", "INACTIVE"]
    """The state of the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT"]
    """The type of Auth Rule"""

    excluded_card_tokens: Optional[List[str]] = None
    """Card tokens to which the Auth Rule does not apply."""
