# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CardBulkOrder"]


class CardBulkOrder(BaseModel):
    """Represents a bulk order for physical card shipments"""

    token: str
    """Globally unique identifier for the bulk order"""

    card_tokens: List[str]
    """List of card tokens associated with this bulk order"""

    created: datetime
    """An RFC 3339 timestamp for when the bulk order was created. UTC time zone"""

    customer_product_id: Optional[str] = None
    """Customer-specified product configuration for physical card manufacturing.

    This must be configured with Lithic before use
    """

    shipping_address: object
    """Shipping address for all cards in this bulk order"""

    shipping_method: Literal["BULK_EXPEDITED"]
    """Shipping method for all cards in this bulk order"""

    status: Literal["OPEN", "LOCKED"]
    """Status of the bulk order.

    OPEN indicates the order is accepting cards. LOCKED indicates the order is
    finalized and no more cards can be added
    """

    updated: datetime
    """An RFC 3339 timestamp for when the bulk order was last updated. UTC time zone"""
