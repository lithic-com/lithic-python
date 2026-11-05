# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .auth_rule_condition_param import AuthRuleConditionParam

__all__ = ["ConditionalAuthorizationActionParametersParam", "Action", "ActionHoldAdjustmentAction"]


class ActionHoldAdjustmentAction(TypedDict, total=False):
    """The hold adjustment to apply if the conditions are met."""

    mode: Required[Literal["REPLACE_WITH_AMOUNT", "ADD_PERCENTAGE", "ADD_AMOUNT"]]
    """The mode of the hold adjustment, determining how the value is interpreted:

    - `REPLACE_WITH_AMOUNT`: The value is the approved hold amount in cents.
    - `ADD_PERCENTAGE`: The value adjusts the hold amount by a percentage. 1000
      represents a 10% increase, 0 represents no change.
    - `ADD_AMOUNT`: The value is added to the hold amount in cents.
    """

    type: Required[Literal["HOLD_ADJUSTMENT"]]
    """The type of adjustment to apply"""

    value: Required[int]
    """The value used for the hold adjustment, interpreted based on the mode"""


Action: TypeAlias = Union[Literal["DECLINE", "CHALLENGE"], ActionHoldAdjustmentAction]


class ConditionalAuthorizationActionParametersParam(TypedDict, total=False):
    action: Required[Action]
    """The action to take if the conditions are met."""

    conditions: Required[Iterable[AuthRuleConditionParam]]
