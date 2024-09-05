# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ShippingAddress"]


class ShippingAddress(TypedDict, total=False):
    address1: Required[str]
    """Valid USPS routable address."""

    city: Required[str]
    """City"""

    country: Required[str]
    """Uppercase ISO 3166-1 alpha-3 three character abbreviation."""

    first_name: Required[str]
    """Customer's first name.

    This will be the first name printed on the physical card. The combined length of
    `first_name` and `last_name` may not exceed 25 characters.
    """

    last_name: Required[str]
    """Customer's surname (family name).

    This will be the last name printed on the physical card. The combined length of
    `first_name` and `last_name` may not exceed 25 characters.
    """

    postal_code: Required[str]
    """Postal code (formerly zipcode).

    For US addresses, either five-digit postal code or nine-digit postal code
    (ZIP+4) using the format 12345-1234.
    """

    state: Required[str]
    """Uppercase ISO 3166-2 two character abbreviation for US and CA.

    Optional with a limit of 24 characters for other countries.
    """

    address2: str
    """Unit number (if applicable)."""

    email: str
    """Email address to be contacted for expedited shipping process purposes.

    Required if `shipping_method` is `EXPEDITED`.
    """

    line2_text: str
    """Text to be printed on line two of the physical card.

    Use of this field requires additional permissions.
    """

    phone_number: str
    """
    Cardholder's phone number in E.164 format to be contacted for expedited shipping
    process purposes. Required if `shipping_method` is `EXPEDITED`.
    """
