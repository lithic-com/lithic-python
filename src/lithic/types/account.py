# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Account", "SpendLimit", "AccountHolder", "VerificationAddress"]


class SpendLimit(BaseModel):
    daily: int
    """Daily spend limit (in cents)."""

    lifetime: int
    """Total spend limit over account lifetime (in cents)."""

    monthly: int
    """Monthly spend limit (in cents)."""


class AccountHolder(BaseModel):
    token: str
    """Globally unique identifier for the account holder."""

    business_account_token: str
    """
    Only applicable for customers using the KYC-Exempt workflow to enroll authorized
    users of businesses. Account_token of the enrolled business associated with an
    enrolled AUTHORIZED_USER individual.
    """

    email: str
    """Email address."""

    phone_number: str
    """Phone number of the individual."""


class VerificationAddress(BaseModel):
    address1: str
    """Valid deliverable address (no PO boxes)."""

    city: str
    """City name."""

    country: str
    """Country name. Only USA is currently supported."""

    postal_code: str
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: str
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: Optional[str] = None
    """Unit or apartment number (if applicable)."""


class Account(BaseModel):
    token: str
    """Globally unique identifier for the account.

    This is the same as the account_token returned by the enroll endpoint. If using
    this parameter, do not include pagination.
    """

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

    - `ACTIVE` - Account is able to transact and create new cards.
    - `PAUSED` - Account will not be able to transact or create new cards. It can be
      set back to `ACTIVE`.
    """

    account_holder: Optional[AccountHolder] = None

    auth_rule_tokens: Optional[List[str]] = None
    """List of identifiers for the Auth Rule(s) that are applied on the account."""

    verification_address: Optional[VerificationAddress] = None
