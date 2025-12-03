# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TokenizationRuleResult"]


class TokenizationRuleResult(BaseModel):
    auth_rule_token: Optional[str] = None
    """The Auth Rule Token associated with the rule.

    If this is set to null, then the result was not associated with a
    customer-configured rule. This may happen in cases where a tokenization is
    declined or requires TFA due to a Lithic-configured security or compliance rule,
    for example.
    """

    explanation: Optional[str] = None
    """A human-readable explanation outlining the motivation for the rule's result"""

    name: Optional[str] = None
    """The name for the rule, if any was configured"""

    result: Literal["APPROVED", "DECLINED", "REQUIRE_TFA", "ERROR"]
    """The result associated with this rule"""
