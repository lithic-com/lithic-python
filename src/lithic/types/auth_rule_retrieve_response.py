# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel
from .auth_rule import AuthRule

__all__ = ["AuthRuleRetrieveResponse"]


class AuthRuleRetrieveResponse(BaseModel):
    data: Optional[List[AuthRule]] = None
