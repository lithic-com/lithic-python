# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .auth_rule_entity import AuthRuleEntity

__all__ = ["AuthRuleEntitiesResponse"]


class AuthRuleEntitiesResponse(BaseModel):
    """
    The entities the Auth Rule applies to (`include`) and does not apply to (`exclude`). An exclusion overrides an inclusion.
    """

    exclude: List[AuthRuleEntity]
    """Entities the Auth Rule does not apply to"""

    include: List[AuthRuleEntity]
    """Entities the Auth Rule applies to"""
