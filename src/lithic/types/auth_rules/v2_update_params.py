# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .auth_rule_entities_param import AuthRuleEntitiesParam

__all__ = ["V2UpdateParams", "Rule", "AccountLevelRule", "CardLevelRule", "ProgramLevelRule"]


class Rule(TypedDict, total=False):
    entities: AuthRuleEntitiesParam
    """
    The entities an Auth Rule applies to (`include`) and does not apply to
    (`exclude`). An exclusion overrides an inclusion, so a card excluded here is
    skipped even when the program, its account or one of its tags is included.

    The rule's resulting entities must satisfy these constraints after any write:

    - `include` must contain at least one entity.
    - If `PROGRAM` is included, it must be the only included entity.
    - `PROGRAM` cannot be excluded.
    - An entity cannot appear in both `include` and `exclude`, or twice in the same
      list.
    - A rule can have at most 1,000 entities across `include` and `exclude`, not
      counting `PROGRAM`.
    - Entity types must be valid for the rule's event stream.
    - `CARD`, `ACCOUNT` and `BUSINESS_ACCOUNT` tokens must belong to your program.
    """

    name: Optional[str]
    """Auth Rule Name"""

    state: Literal["INACTIVE"]
    """The desired state of the Auth Rule.

    Note that only deactivating an Auth Rule through this endpoint is supported at
    this time. If you need to (re-)activate an Auth Rule the /promote endpoint
    should be used to promote a draft to the currently active version.
    """


class AccountLevelRule(TypedDict, total=False):
    account_tokens: SequenceNotStr[str]
    """Deprecated: Use `entities.include` with `ACCOUNT` entities instead.

    Account tokens to which the Auth Rule applies.
    """

    business_account_tokens: SequenceNotStr[str]
    """Deprecated: Use `entities.include` with `BUSINESS_ACCOUNT` entities instead.

    Business Account tokens to which the Auth Rule applies.
    """

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
    """Deprecated: Use `entities.include` with `CARD` entities instead.

    Card tokens to which the Auth Rule applies. Cards the rule applies to through a
    `CARD_TAG` entity are not listed.
    """

    name: Optional[str]
    """Auth Rule Name"""

    state: Literal["INACTIVE"]
    """The desired state of the Auth Rule.

    Note that only deactivating an Auth Rule through this endpoint is supported at
    this time. If you need to (re-)activate an Auth Rule the /promote endpoint
    should be used to promote a draft to the currently active version.
    """


class ProgramLevelRule(TypedDict, total=False):
    excluded_account_tokens: SequenceNotStr[str]
    """Deprecated: Use `entities.exclude` with `ACCOUNT` entities instead.

    Account tokens to which the Auth Rule does not apply.
    """

    excluded_business_account_tokens: SequenceNotStr[str]
    """Deprecated: Use `entities.exclude` with `BUSINESS_ACCOUNT` entities instead.

    Business account tokens to which the Auth Rule does not apply.
    """

    excluded_card_tokens: SequenceNotStr[str]
    """Deprecated: Use `entities.exclude` with `CARD` entities instead.

    Card tokens to which the Auth Rule does not apply. Cards excluded through a
    `CARD_TAG` entity are not listed.
    """

    name: Optional[str]
    """Auth Rule Name"""

    program_level: bool
    """Deprecated: Use `entities.include` with a `PROGRAM` entity instead.

    Whether the Auth Rule applies to all authorizations on the card program.
    """

    state: Literal["INACTIVE"]
    """The desired state of the Auth Rule.

    Note that only deactivating an Auth Rule through this endpoint is supported at
    this time. If you need to (re-)activate an Auth Rule the /promote endpoint
    should be used to promote a draft to the currently active version.
    """


V2UpdateParams: TypeAlias = Union[Rule, AccountLevelRule, CardLevelRule, ProgramLevelRule]
