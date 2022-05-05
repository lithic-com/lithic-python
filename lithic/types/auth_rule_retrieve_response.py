# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Any
from typing_extensions import Literal
from .._models import StringModel, NoneModel, BaseModel
from ..types import auth_rule


__all__ = ["AuthRuleRetrieveResponse"]


class AuthRuleRetrieveResponse(BaseModel):
    data: Optional[List[auth_rule.AuthRule]]
