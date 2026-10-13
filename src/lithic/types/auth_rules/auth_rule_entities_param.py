# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .auth_rule_entity_param import AuthRuleEntityParam

__all__ = ["AuthRuleEntitiesParam"]


class AuthRuleEntitiesParam(TypedDict, total=False):
    """
    The entities an Auth Rule applies to (`include`) and does not apply to (`exclude`). An exclusion overrides an inclusion, so a card excluded here is skipped even when the program, its account or one of its tags is included.

    The rule's resulting entities must satisfy these constraints after any write:

    - `include` must contain at least one entity.
    - If `PROGRAM` is included, it must be the only included entity.
    - `PROGRAM` cannot be excluded.
    - An entity cannot appear in both `include` and `exclude`, or twice in the same list.
    - A rule can have at most 1,000 entities across `include` and `exclude`, not counting `PROGRAM`.
    - Entity types must be valid for the rule's event stream.
    - `CARD`, `ACCOUNT` and `BUSINESS_ACCOUNT` tokens must belong to your program.
    """

    exclude: Iterable[AuthRuleEntityParam]
    """Entities the Auth Rule does not apply to.

    Defaults to an empty list in requests.
    """

    include: Iterable[AuthRuleEntityParam]
    """Entities the Auth Rule applies to. Defaults to an empty list in requests."""
