# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .auth_rule_condition import AuthRuleCondition

__all__ = ["ConditionalBlockParameters"]


class ConditionalBlockParameters(BaseModel):
    """Deprecated: Use CONDITIONAL_ACTION instead."""

    conditions: List[AuthRuleCondition]
