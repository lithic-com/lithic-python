# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AccountHolderEntity", "Address"]


class Address(BaseModel):
    """Individual's current address"""

    address1: str
    """Valid deliverable address (no PO boxes)."""

    city: str
    """Name of city."""

    country: str
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

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


class AccountHolderEntity(BaseModel):
    """Information about an entity associated with an account holder"""

    token: str
    """Globally unique identifier for the entity"""

    account_holder_token: str
    """Globally unique identifier for the account holder"""

    address: Address
    """Individual's current address"""

    dob: Optional[str] = None
    """Individual's date of birth, as an RFC 3339 date"""

    email: Optional[str] = None
    """Individual's email address"""

    first_name: Optional[str] = None
    """Individual's first name, as it appears on government-issued identity documents"""

    last_name: Optional[str] = None
    """Individual's last name, as it appears on government-issued identity documents"""

    phone_number: Optional[str] = None
    """Individual's phone number, entered in E.164 format"""

    status: Literal["ACCEPTED", "INACTIVE", "PENDING_REVIEW", "REJECTED"]
    """The status of the entity"""

    type: Literal["BENEFICIAL_OWNER_INDIVIDUAL", "CONTROL_PERSON"]
    """The type of entity"""
