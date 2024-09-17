# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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

    USA and CAN are supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: Required[str]
    """Valid postal code."""

    state: Required[str]
    """Valid state code."""

    address2: str
    """Unit or apartment number (if applicable)."""
