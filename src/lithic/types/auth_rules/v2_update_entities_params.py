# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .auth_rule_entities_param import AuthRuleEntitiesParam

__all__ = ["V2UpdateEntitiesParams"]


class V2UpdateEntitiesParams(TypedDict, total=False):
    add: AuthRuleEntitiesParam
    """Entities to add to the rule's `include` and `exclude` lists"""

    remove: AuthRuleEntitiesParam
    """Entities to remove from the rule's `include` and `exclude` lists"""
