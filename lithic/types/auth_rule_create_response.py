# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Any
from typing_extensions import Literal
from .._models import StringModel, NoneModel, BaseModel
from ..types import auth_rule


__all__ = ["AuthRuleCreateResponse"]


class AuthRuleCreateResponse(BaseModel):
    data: Optional[auth_rule.AuthRule]
