# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .hold_event import HoldEvent

__all__ = ["Hold"]


class Hold(BaseModel):
    """A hold transaction representing reserved funds on a financial account.

    Holds move funds from available to pending balance in anticipation of future payments. They can be resolved via settlement (linked to payment), manual release, or expiration.
    """

    token: str
    """Unique identifier for the transaction"""

    created: datetime
    """ISO 8601 timestamp of when the transaction was created"""

    status: Literal["PENDING", "SETTLED", "EXPIRED", "VOIDED", "DECLINED", "REVERSED", "CANCELED", "RETURNED"]
    """Status of a hold transaction"""

    updated: datetime
    """ISO 8601 timestamp of when the transaction was last updated"""

    currency: Optional[str] = None

    events: Optional[List[HoldEvent]] = None

    expiration_datetime: Optional[datetime] = None
    """When the hold will auto-expire if not resolved"""

    family: Optional[Literal["HOLD"]] = None
    """HOLD - Hold Transaction"""

    financial_account_token: Optional[str] = None

    pending_amount: Optional[int] = None
    """Current pending amount (0 when resolved)"""

    result: Optional[Literal["APPROVED", "DECLINED"]] = None

    user_defined_id: Optional[str] = None
