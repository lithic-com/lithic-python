# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["HoldEvent"]


class HoldEvent(BaseModel):
    """Event representing a lifecycle change to a hold"""

    token: str

    amount: int
    """Amount in cents"""

    created: datetime

    detailed_results: List[Literal["APPROVED", "INSUFFICIENT_FUNDS"]]

    memo: Optional[str] = None

    result: Literal["APPROVED", "DECLINED"]

    settling_transaction_token: Optional[str] = None
    """
    Transaction token of the payment that settled this hold (only populated for
    HOLD_SETTLED events)
    """

    type: Literal["HOLD_INITIATED", "HOLD_VOIDED", "HOLD_EXPIRED", "HOLD_SETTLED"]
    """Type of hold lifecycle event"""
