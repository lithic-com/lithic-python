# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InternalTransaction", "Event"]


class Event(BaseModel):
    token: str

    amount: int

    created: datetime

    result: Literal["APPROVED", "DECLINED"]

    type: Literal["INTERNAL_ADJUSTMENT"]


class InternalTransaction(BaseModel):
    token: str

    category: Literal["INTERNAL"]

    created: datetime

    currency: str

    descriptor: str

    events: List[Event]

    pending_amount: int

    result: Literal["APPROVED", "DECLINED"]

    settled_amount: int

    status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED", "RETURNED"]

    updated: datetime
