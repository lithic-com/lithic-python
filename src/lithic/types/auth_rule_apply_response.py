# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..types import auth_rule
from .._models import BaseModel

__all__ = ["AuthRuleApplyResponse"]


class AuthRuleApplyResponse(BaseModel):
    data: Optional[auth_rule.AuthRule]
