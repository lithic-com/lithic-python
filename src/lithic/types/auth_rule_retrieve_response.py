# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .auth_rule import AuthRule

__all__ = ["AuthRuleRetrieveResponse"]


class AuthRuleRetrieveResponse(BaseModel):
    data: Optional[List[AuthRule]] = None
