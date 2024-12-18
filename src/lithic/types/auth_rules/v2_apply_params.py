# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "V2ApplyParams",
    "ApplyAuthRuleRequestAccountTokens",
    "ApplyAuthRuleRequestCardTokens",
    "ApplyAuthRuleRequestProgramLevel",
]


class ApplyAuthRuleRequestAccountTokens(TypedDict, total=False):
    account_tokens: Required[List[str]]
    """Account tokens to which the Auth Rule applies."""


class ApplyAuthRuleRequestCardTokens(TypedDict, total=False):
    card_tokens: Required[List[str]]
    """Card tokens to which the Auth Rule applies."""


class ApplyAuthRuleRequestProgramLevel(TypedDict, total=False):
    program_level: Required[bool]
    """Whether the Auth Rule applies to all authorizations on the card program."""

    excluded_card_tokens: List[str]
    """Card tokens to which the Auth Rule does not apply."""


V2ApplyParams: TypeAlias = Union[
    ApplyAuthRuleRequestAccountTokens, ApplyAuthRuleRequestCardTokens, ApplyAuthRuleRequestProgramLevel
]
