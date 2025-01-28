# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import TypeAlias, TypedDict

from .velocity_limit_params_param import VelocityLimitParamsParam
from .conditional_block_parameters_param import ConditionalBlockParametersParam

__all__ = ["V2DraftParams", "Parameters"]


class V2DraftParams(TypedDict, total=False):
    parameters: Optional[Parameters]
    """Parameters for the Auth Rule"""


Parameters: TypeAlias = Union[ConditionalBlockParametersParam, VelocityLimitParamsParam]
