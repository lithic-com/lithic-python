# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "V2ApplyParams",
    "ApplyAuthRuleRequestAccountTokens",
    "ApplyAuthRuleRequestCardTokens",
    "ApplyAuthRuleRequestProgramLevel",
]


class ApplyAuthRuleRequestAccountTokens(TypedDict, total=False):
    account_tokens: SequenceNotStr[str]
    """Account tokens to which the Auth Rule applies."""

    business_account_tokens: SequenceNotStr[str]
    """Business Account tokens to which the Auth Rule applies."""


class ApplyAuthRuleRequestCardTokens(TypedDict, total=False):
    card_tokens: Required[SequenceNotStr[str]]
    """Card tokens to which the Auth Rule applies."""


class ApplyAuthRuleRequestProgramLevel(TypedDict, total=False):
    program_level: Required[bool]
    """Whether the Auth Rule applies to all authorizations on the card program."""

    excluded_card_tokens: SequenceNotStr[str]
    """Card tokens to which the Auth Rule does not apply."""


V2ApplyParams: TypeAlias = Union[
    ApplyAuthRuleRequestAccountTokens, ApplyAuthRuleRequestCardTokens, ApplyAuthRuleRequestProgramLevel
]
