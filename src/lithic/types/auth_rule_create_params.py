# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["AuthRuleCreateParams"]


class AuthRuleCreateParams(TypedDict, total=False):
    account_tokens: List[str]
    """Array of account_token(s) identifying the accounts that the Auth Rule applies
    to.

    Note that only this field or `card_tokens` can be provided for a given Auth
    Rule.
    """

    allowed_countries: List[str]
    """Countries in which the Auth Rule permits transactions.

    Note that Lithic maintains a list of countries in which all transactions are
    blocked; "allowing" those countries in an Auth Rule does not override the
    Lithic-wide restrictions.
    """

    allowed_mcc: List[str]
    """Merchant category codes for which the Auth Rule permits transactions."""

    blocked_countries: List[str]
    """Countries in which the Auth Rule automatically declines transactions."""

    blocked_mcc: List[str]
    """
    Merchant category codes for which the Auth Rule automatically declines
    transactions.
    """

    card_tokens: List[str]
    """Array of card_token(s) identifying the cards that the Auth Rule applies to.

    Note that only this field or `account_tokens` can be provided for a given Auth
    Rule.
    """

    program_level: bool
    """Boolean indicating whether the Auth Rule is applied at the program level."""
