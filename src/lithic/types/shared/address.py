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
    """Valid country code.

    USA and CAN are supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: str
    """Valid postal code."""

    state: str
    """Valid state code."""

    address2: Optional[str] = None
    """Unit or apartment number (if applicable)."""
