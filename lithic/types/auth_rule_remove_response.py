# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Union, Optional

from typing_extensions import Literal

from ..types import auth_rule
from .._models import BaseModel, NoneModel, StringModel

__all__ = ["AuthRuleRemoveResponse"]


class AuthRuleRemoveResponse(BaseModel):
    account_tokens: Optional[List[str]]

    card_tokens: Optional[List[str]]

    previous_auth_rule_tokens: Optional[List[str]]

    program_level: Optional[bool]
