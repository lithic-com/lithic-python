# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .rule_feature import RuleFeature

__all__ = ["TypescriptCodeParameters"]


class TypescriptCodeParameters(BaseModel):
    """Parameters for defining a TypeScript code rule"""

    code: str
    """The TypeScript source code of the rule.

    Must define a `rule()` function that accepts the declared features as positional
    arguments (in the same order as the `features` array) and returns an array of
    actions.
    """

    features: List[RuleFeature]
    """Features available to the TypeScript code at evaluation time"""
