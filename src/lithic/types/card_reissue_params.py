# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..types import shared_params

__all__ = ["CardReissueParams"]


class CardReissueParams(TypedDict, total=False):
    product_id: str
    """Specifies the configuration (e.g.

    physical card art) that the card should be manufactured with, and only applies
    to cards of type `PHYSICAL` [beta]. This must be configured with Lithic before
    use.
    """

    shipping_address: shared_params.ShippingAddress
    """If omitted, the previous shipping address will be used."""

    shipping_method: Literal["STANDARD", "STANDARD_WITH_TRACKING", "EXPEDITED"]
    """Shipping method for the card.

    Use of options besides `STANDARD` require additional permissions.

    - `STANDARD` - USPS regular mail or similar international option, with no
      tracking
    - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
      with tracking
    - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
      tracking
    """
