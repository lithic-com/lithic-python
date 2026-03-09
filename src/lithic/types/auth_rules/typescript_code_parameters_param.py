# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .rule_feature_param import RuleFeatureParam

__all__ = ["TypescriptCodeParametersParam"]


class TypescriptCodeParametersParam(TypedDict, total=False):
    """Parameters for defining a TypeScript code rule"""

    code: Required[str]
    """The TypeScript source code of the rule.

    Must define a `rule()` function that accepts the declared features as positional
    arguments (in the same order as the `features` array) and returns an array of
    actions.
    """

    features: Required[Iterable[RuleFeatureParam]]
    """Features available to the TypeScript code at evaluation time"""
