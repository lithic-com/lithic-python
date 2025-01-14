# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .auth_rule_condition_param import AuthRuleConditionParam

__all__ = ["ConditionalBlockParametersParam"]


class ConditionalBlockParametersParam(TypedDict, total=False):
    conditions: Required[Iterable[AuthRuleConditionParam]]
