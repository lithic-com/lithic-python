# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SpendLimit", "Account"]


class SpendLimit(BaseModel):
    daily: int
    """Daily spend limit (in cents)."""

    lifetime: int
    """Total spend limit over account lifetime (in cents)."""

    monthly: int
    """Monthly spend limit (in cents)."""


class Account(BaseModel):
    spend_limit: SpendLimit
    """
    Spend limit information for the user containing the daily, monthly, and lifetime
    spend limit of the account. Any charges to a card owned by this account will be
    declined once their transaction volume has surpassed the value in the applicable
    time limit (rolling). A lifetime limit of 0 indicates that the lifetime limit
    feature is disabled.
    """

    state: Literal["ACTIVE", "PAUSED"]
    """Account state:

    - `ACTIVE` - Active, account is able to transact and create new cards.
    - `PAUSED` - Paused, account will not be able to transact or create new cards.
    """

    token: str
    """Globally unique identifier for the account.

    This is the same as the account_token returned by the enroll endpoint. If using
    this parameter, do not include pagination.
    """

    auth_rule_tokens: Optional[List[str]]
    """List of identifiers for the Auth Rule(s) that are applied on the account."""
