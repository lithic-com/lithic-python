# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["AuthRuleRemoveParams"]


class AuthRuleRemoveParams(TypedDict, total=False):
    account_tokens: List[str]
    """
    Array of account_token(s) identifying the accounts that the Auth Rule applies
    to. Note that only this field or `card_tokens` can be provided for a given Auth
    Rule.
    """

    card_tokens: List[str]
    """
    Array of card_token(s) identifying the cards that the Auth Rule applies to. Note
    that only this field or `account_tokens` can be provided for a given Auth Rule.
    """

    program_level: bool
    """Boolean indicating whether the Auth Rule is applied at the program level."""
