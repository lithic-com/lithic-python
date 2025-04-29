# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .velocity_limit_params_param import VelocityLimitParamsParam
from .conditional_block_parameters_param import ConditionalBlockParametersParam

__all__ = [
    "V2DraftParams",
    "Parameters",
    "ParametersMerchantLockParameters",
    "ParametersMerchantLockParametersMerchant",
]


class V2DraftParams(TypedDict, total=False):
    parameters: Optional[Parameters]
    """Parameters for the Auth Rule"""


class ParametersMerchantLockParametersMerchant(TypedDict, total=False):
    comment: str
    """
    A comment or explanation about the merchant, used internally for rule management
    purposes.
    """

    descriptor: str
    """
    Short description of the merchant, often used to provide more human-readable
    context about the transaction merchant. This is typically the name or label
    shown on transaction summaries.
    """

    merchant_id: str
    """Unique alphanumeric identifier for the payment card acceptor (merchant).

    This attribute specifies the merchant entity that will be locked or referenced
    for authorization rules.
    """


class ParametersMerchantLockParameters(TypedDict, total=False):
    merchants: Required[Iterable[ParametersMerchantLockParametersMerchant]]
    """
    A list of merchant locks defining specific merchants or groups of merchants
    (based on descriptors or IDs) that the lock applies to.
    """


Parameters: TypeAlias = Union[
    ConditionalBlockParametersParam, VelocityLimitParamsParam, ParametersMerchantLockParameters
]
