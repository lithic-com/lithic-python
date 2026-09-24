# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .auth_rule_condition_param import AuthRuleConditionParam

__all__ = ["ConditionalAuthorizationActionParametersParam"]


class ConditionalAuthorizationActionParametersParam(TypedDict, total=False):
    action: Required[Literal["DECLINE", "CHALLENGE"]]
    """The action to take if the conditions are met."""

    conditions: Required[Iterable[AuthRuleConditionParam]]
