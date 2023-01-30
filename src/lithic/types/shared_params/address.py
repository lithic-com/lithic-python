# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["Address"]


class Address(TypedDict, total=False):
    address1: Required[str]
    """Valid deliverable address (no PO boxes)."""

    city: Required[str]
    """Name of city."""

    country: Required[str]
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: Required[str]
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: Required[str]
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: str
    """Unit or apartment number (if applicable)."""
