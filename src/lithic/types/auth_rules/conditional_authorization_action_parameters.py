# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .auth_rule_condition import AuthRuleCondition

__all__ = ["ConditionalAuthorizationActionParameters", "Action", "ActionHoldAdjustmentAction"]


class ActionHoldAdjustmentAction(BaseModel):
    """The hold adjustment to apply if the conditions are met."""

    mode: Literal["REPLACE_WITH_AMOUNT", "ADD_PERCENTAGE", "ADD_AMOUNT"]
    """The mode of the hold adjustment, determining how the value is interpreted:

    - `REPLACE_WITH_AMOUNT`: The value is the approved hold amount in cents.
    - `ADD_PERCENTAGE`: The value adjusts the hold amount by a percentage. 1000
      represents a 10% increase, 0 represents no change.
    - `ADD_AMOUNT`: The value is added to the hold amount in cents.
    """

    type: Literal["HOLD_ADJUSTMENT"]
    """The type of adjustment to apply"""

    value: int
    """The value used for the hold adjustment, interpreted based on the mode"""


Action: TypeAlias = Union[Literal["DECLINE", "CHALLENGE"], ActionHoldAdjustmentAction]


class ConditionalAuthorizationActionParameters(BaseModel):
    action: Action
    """The action to take if the conditions are met."""

    conditions: List[AuthRuleCondition]
