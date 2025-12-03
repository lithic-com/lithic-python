# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardBulkOrderCreateParams"]


class CardBulkOrderCreateParams(TypedDict, total=False):
    customer_product_id: Required[str]
    """Customer-specified product configuration for physical card manufacturing.

    This must be configured with Lithic before use
    """

    shipping_address: Required[object]
    """Shipping address for all cards in this bulk order"""

    shipping_method: Required[Literal["BULK_EXPEDITED"]]
    """Shipping method for all cards in this bulk order"""
