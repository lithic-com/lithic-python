# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = ["V2UpdateParams", "AccountLevelRule", "CardLevelRule", "ProgramLevelRule"]


class AccountLevelRule(TypedDict, total=False):
    account_tokens: List[str]
    """Account tokens to which the Auth Rule applies."""

    name: Optional[str]
    """Auth Rule Name"""

    state: Literal["INACTIVE"]
    """The desired state of the Auth Rule.

    Note that only deactivating an Auth Rule through this endpoint is supported at
    this time. If you need to (re-)activate an Auth Rule the /promote endpoint
    should be used to promote a draft to the currently active version.
    """


class CardLevelRule(TypedDict, total=False):
    card_tokens: List[str]
    """Card tokens to which the Auth Rule applies."""

    name: Optional[str]
    """Auth Rule Name"""

    state: Literal["INACTIVE"]
    """The desired state of the Auth Rule.

    Note that only deactivating an Auth Rule through this endpoint is supported at
    this time. If you need to (re-)activate an Auth Rule the /promote endpoint
    should be used to promote a draft to the currently active version.
    """


class ProgramLevelRule(TypedDict, total=False):
    excluded_card_tokens: List[str]
    """Card tokens to which the Auth Rule does not apply."""

    name: Optional[str]
    """Auth Rule Name"""

    program_level: bool
    """Whether the Auth Rule applies to all authorizations on the card program."""

    state: Literal["INACTIVE"]
    """The desired state of the Auth Rule.

    Note that only deactivating an Auth Rule through this endpoint is supported at
    this time. If you need to (re-)activate an Auth Rule the /promote endpoint
    should be used to promote a draft to the currently active version.
    """


V2UpdateParams: TypeAlias = Union[AccountLevelRule, CardLevelRule, ProgramLevelRule]
