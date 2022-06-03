# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AuthRuleRemoveResponse"]


class AuthRuleRemoveResponse(BaseModel):
    account_tokens: Optional[List[str]]

    card_tokens: Optional[List[str]]

    previous_auth_rule_tokens: Optional[List[str]]

    program_level: Optional[bool]
