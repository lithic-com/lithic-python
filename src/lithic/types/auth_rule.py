# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuthRule"]


class AuthRule(BaseModel):
    token: str
    """Globally unique identifier."""

    state: Literal["ACTIVE", "INACTIVE"]
    """Indicates whether the Auth Rule is ACTIVE or INACTIVE"""

    account_tokens: Optional[List[str]] = None
    """Array of account_token(s) identifying the accounts that the Auth Rule applies
    to.

    Note that only this field or `card_tokens` can be provided for a given Auth
    Rule.
    """

    allowed_countries: Optional[List[str]] = None
    """Countries in which the Auth Rule permits transactions.

    Note that Lithic maintains a list of countries in which all transactions are
    blocked; "allowing" those countries in an Auth Rule does not override the
    Lithic-wide restrictions.
    """

    allowed_mcc: Optional[List[str]] = None
    """Merchant category codes for which the Auth Rule permits transactions."""

    blocked_countries: Optional[List[str]] = None
    """Countries in which the Auth Rule automatically declines transactions."""

    blocked_mcc: Optional[List[str]] = None
    """
    Merchant category codes for which the Auth Rule automatically declines
    transactions.
    """

    card_tokens: Optional[List[str]] = None
    """Array of card_token(s) identifying the cards that the Auth Rule applies to.

    Note that only this field or `account_tokens` can be provided for a given Auth
    Rule.
    """

    program_level: Optional[bool] = None
    """Boolean indicating whether the Auth Rule is applied at the program level."""
