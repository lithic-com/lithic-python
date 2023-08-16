# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel
from .auth_rule import AuthRule

__all__ = ["AuthRuleApplyResponse"]


class AuthRuleApplyResponse(BaseModel):
    data: Optional[AuthRule] = None
