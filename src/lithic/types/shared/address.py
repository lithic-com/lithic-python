# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Address"]


class Address(BaseModel):
    address1: str
    """Valid deliverable address (no PO boxes)."""

    city: str
    """Name of city."""

    country: str
    """
    Valid country code, entered in uppercase ISO 3166-1 alpha-3 three-character
    format. Only USA is currently supported for all workflows. KYC_EXEMPT supports
    CAN additionally.
    """

    postal_code: str
    """Valid postal code.

    USA postal codes (ZIP codes) are supported, entered as a five-digit postal code
    or nine-digit postal code (ZIP+4) using the format 12345-1234. KYC_EXEMPT
    supports Canadian postal codes.
    """

    state: str
    """Valid state code.

    USA state codes are supported, entered in uppercase ISO 3166-2 two-character
    format. KYC_EXEMPT supports Canadian province codes.
    """

    address2: Optional[str] = None
    """Unit or apartment number (if applicable)."""
