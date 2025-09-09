# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["V2UpdateParams", "Variant0", "Variant1", "CardLevelRule", "ProgramLevelRule"]


class Variant0(TypedDict, total=False):
    name: Optional[str]
    """Auth Rule Name"""

    state: Literal["INACTIVE"]
    """The desired state of the Auth Rule.

    Note that only deactivating an Auth Rule through this endpoint is supported at
    this time. If you need to (re-)activate an Auth Rule the /promote endpoint
    should be used to promote a draft to the currently active version.
    """


class Variant1(TypedDict, total=False):
    name: Optional[str]
    """Auth Rule Name"""

    state: Literal["INACTIVE"]
    """The desired state of the Auth Rule.

    Note that only deactivating an Auth Rule through this endpoint is supported at
    this time. If you need to (re-)activate an Auth Rule the /promote endpoint
    should be used to promote a draft to the currently active version.
    """


class CardLevelRule(TypedDict, total=False):
    card_tokens: SequenceNotStr[str]
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
    excluded_card_tokens: SequenceNotStr[str]
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


V2UpdateParams: TypeAlias = Union[Variant0, Variant1, CardLevelRule, ProgramLevelRule]
