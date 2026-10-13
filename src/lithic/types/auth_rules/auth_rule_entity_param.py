# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "AuthRuleEntityParam",
    "AuthRuleProgramEntity",
    "AuthRuleCardEntity",
    "AuthRuleAccountEntity",
    "AuthRuleBusinessAccountEntity",
    "AuthRuleCardTagEntity",
]


class AuthRuleProgramEntity(TypedDict, total=False):
    """The entire card program. Takes no other fields."""

    type: Required[Literal["PROGRAM"]]


class AuthRuleCardEntity(TypedDict, total=False):
    """A single card."""

    token: Required[str]
    """Token of the card"""

    type: Required[Literal["CARD"]]


class AuthRuleAccountEntity(TypedDict, total=False):
    """A single account."""

    token: Required[str]
    """Token of the account"""

    type: Required[Literal["ACCOUNT"]]


class AuthRuleBusinessAccountEntity(TypedDict, total=False):
    """A single business account."""

    token: Required[str]
    """Token of the business account"""

    type: Required[Literal["BUSINESS_ACCOUNT"]]


class AuthRuleCardTagEntity(TypedDict, total=False):
    """Every card whose `tags` contain `key` set to `value`."""

    key: Required[str]
    """Tag key.

    Keys starting with `lithic.` (case-insensitive) are reserved and rejected.
    """

    type: Required[Literal["CARD_TAG"]]

    value: Required[str]
    """Tag value"""


AuthRuleEntityParam: TypeAlias = Union[
    AuthRuleProgramEntity,
    AuthRuleCardEntity,
    AuthRuleAccountEntity,
    AuthRuleBusinessAccountEntity,
    AuthRuleCardTagEntity,
]
