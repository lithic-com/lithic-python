# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["KYBBusinessEntity", "Address"]


class Address(BaseModel):
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


class KYBBusinessEntity(BaseModel):
    address: Address
    """
    Business''s physical address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable.
    """

    government_id: str
    """Government-issued identification number.

    US Federal Employer Identification Numbers (EIN) are currently supported,
    entered as full nine-digits, with or without hyphens.
    """

    legal_business_name: str
    """Legal (formal) business name."""

    phone_numbers: List[str]
    """
    One or more of the business's phone number(s), entered as a list in E.164
    format.
    """

    dba_business_name: Optional[str] = None
    """
    Any name that the business operates under that is not its legal business name
    (if applicable).
    """

    parent_company: Optional[str] = None
    """Parent company name (if applicable)."""
