# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Address"]


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
