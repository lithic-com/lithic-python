# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .velocity_limit_params_param import VelocityLimitParamsParam
from .merchant_lock_parameters_param import MerchantLockParametersParam
from .conditional_block_parameters_param import ConditionalBlockParametersParam
from .conditional_3ds_action_parameters_param import Conditional3DSActionParametersParam

__all__ = ["V2DraftParams", "Parameters"]


class V2DraftParams(TypedDict, total=False):
    parameters: Optional[Parameters]
    """Parameters for the Auth Rule"""


Parameters: TypeAlias = Union[
    ConditionalBlockParametersParam,
    VelocityLimitParamsParam,
    MerchantLockParametersParam,
    Conditional3DSActionParametersParam,
]
