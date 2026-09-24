# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .auth_rule_condition import AuthRuleCondition

__all__ = ["ConditionalAuthorizationActionParameters"]


class ConditionalAuthorizationActionParameters(BaseModel):
    action: Literal["DECLINE", "CHALLENGE"]
    """The action to take if the conditions are met."""

    conditions: List[AuthRuleCondition]
