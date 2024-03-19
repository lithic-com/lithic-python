# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AuthRuleRemoveResponse"]


class AuthRuleRemoveResponse(BaseModel):
    account_tokens: Optional[List[str]] = None

    card_tokens: Optional[List[str]] = None

    program_level: Optional[bool] = None
