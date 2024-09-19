# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..shared_params.velocity_limit_params import VelocityLimitParams

__all__ = [
    "V2DraftParams",
    "Parameters",
    "ParametersConditionalBlockParameters",
    "ParametersConditionalBlockParametersCondition",
]


class V2DraftParams(TypedDict, total=False):
    parameters: Optional[Parameters]
    """Parameters for the current version of the Auth Rule"""


class ParametersConditionalBlockParametersCondition(TypedDict, total=False):
    attribute: Literal[
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
    """The attribute to target"""

    operation: Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    """The operation to apply to the attribute"""

    value: Union[str, float, List[str]]
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class ParametersConditionalBlockParameters(TypedDict, total=False):
    conditions: Required[Iterable[ParametersConditionalBlockParametersCondition]]


Parameters: TypeAlias = Union[ParametersConditionalBlockParameters, VelocityLimitParams]
