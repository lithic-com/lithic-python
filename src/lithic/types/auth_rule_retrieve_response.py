# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..types import auth_rule
from .._models import BaseModel

__all__ = ["AuthRuleRetrieveResponse"]


class AuthRuleRetrieveResponse(BaseModel):
    data: Optional[List[auth_rule.AuthRule]]
