# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .velocity_limit_params import VelocityLimitParams
from .merchant_lock_parameters import MerchantLockParameters
from .typescript_code_parameters import TypescriptCodeParameters
from .conditional_block_parameters import ConditionalBlockParameters
from .conditional_3ds_action_parameters import Conditional3DSActionParameters
from .conditional_ach_action_parameters import ConditionalACHActionParameters
from .conditional_tokenization_action_parameters import ConditionalTokenizationActionParameters
from .conditional_authorization_action_parameters import ConditionalAuthorizationActionParameters

__all__ = ["AuthRuleVersion", "Parameters"]

Parameters: TypeAlias = Union[
    ConditionalBlockParameters,
    VelocityLimitParams,
    MerchantLockParameters,
    Conditional3DSActionParameters,
    ConditionalAuthorizationActionParameters,
    ConditionalACHActionParameters,
    ConditionalTokenizationActionParameters,
    TypescriptCodeParameters,
]


class AuthRuleVersion(BaseModel):
    created: datetime
    """Timestamp of when this version was created."""

    parameters: Parameters
    """Parameters for the Auth Rule"""

    state: Literal["ACTIVE", "SHADOW", "INACTIVE"]
    """The current state of this version."""

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """
