# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .shared_params.carrier import Carrier
from .shared_params.shipping_address import ShippingAddress

__all__ = ["CardRenewParams"]


class CardRenewParams(TypedDict, total=False):
    shipping_address: Required[ShippingAddress]
    """The shipping address this card will be sent to."""

    carrier: Carrier
    """If omitted, the previous carrier will be used."""

    exp_month: str
    """Two digit (MM) expiry month.

    If neither `exp_month` nor `exp_year` is provided, an expiration date six years
    in the future will be generated.
    """

    exp_year: str
    """Four digit (yyyy) expiry year.

    If neither `exp_month` nor `exp_year` is provided, an expiration date six years
    in the future will be generated.
    """

    product_id: str
    """Specifies the configuration (e.g.

    physical card art) that the card should be manufactured with, and only applies
    to cards of type `PHYSICAL`. This must be configured with Lithic before use.
    """

    shipping_method: Literal["2-DAY", "EXPEDITED", "EXPRESS", "PRIORITY", "STANDARD", "STANDARD_WITH_TRACKING"]
    """Shipping method for the card.

    Use of options besides `STANDARD` require additional permissions.

    - `STANDARD` - USPS regular mail or similar international option, with no
      tracking
    - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
      with tracking
    - `PRIORITY` - USPS Priority, 1-3 day shipping, with tracking
    - `EXPRESS` - FedEx Express, 3-day shipping, with tracking
    - `2_DAY` - FedEx 2-day shipping, with tracking
    - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
      tracking
    """
