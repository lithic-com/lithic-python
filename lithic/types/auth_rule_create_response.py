# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Union, Optional

from typing_extensions import Literal

from ..types import auth_rule
from .._models import BaseModel, NoneModel, StringModel

__all__ = ["AuthRuleCreateResponse"]


class AuthRuleCreateResponse(BaseModel):
    data: Optional[auth_rule.AuthRule]
