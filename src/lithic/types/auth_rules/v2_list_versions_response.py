# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .auth_rule_version import AuthRuleVersion

__all__ = ["V2ListVersionsResponse"]


class V2ListVersionsResponse(BaseModel):
    data: List[AuthRuleVersion]
