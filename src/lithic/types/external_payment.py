# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExternalPayment", "Event"]


class Event(BaseModel):
    token: str

    amount: int

    created: datetime

    detailed_results: List[Literal["APPROVED", "INSUFFICIENT_FUNDS"]]

    effective_date: date

    memo: str

    result: Literal["APPROVED", "DECLINED"]

    type: Literal[
        "EXTERNAL_WIRE_INITIATED",
        "EXTERNAL_WIRE_CANCELED",
        "EXTERNAL_WIRE_SETTLED",
        "EXTERNAL_WIRE_REVERSED",
        "EXTERNAL_WIRE_RELEASED",
        "EXTERNAL_ACH_INITIATED",
        "EXTERNAL_ACH_CANCELED",
        "EXTERNAL_ACH_SETTLED",
        "EXTERNAL_ACH_REVERSED",
        "EXTERNAL_ACH_RELEASED",
        "EXTERNAL_TRANSFER_INITIATED",
        "EXTERNAL_TRANSFER_CANCELED",
        "EXTERNAL_TRANSFER_SETTLED",
        "EXTERNAL_TRANSFER_REVERSED",
        "EXTERNAL_TRANSFER_RELEASED",
        "EXTERNAL_CHECK_INITIATED",
        "EXTERNAL_CHECK_CANCELED",
        "EXTERNAL_CHECK_SETTLED",
        "EXTERNAL_CHECK_REVERSED",
        "EXTERNAL_CHECK_RELEASED",
    ]


class ExternalPayment(BaseModel):
    token: str
    """Unique identifier for the transaction"""

    created: datetime
    """ISO 8601 timestamp of when the transaction was created"""

    family: Literal["CARD", "PAYMENT", "TRANSFER", "INTERNAL", "EXTERNAL_PAYMENT", "MANAGEMENT_OPERATION"]

    status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED"]
    """The status of the transaction"""

    updated: datetime
    """ISO 8601 timestamp of when the transaction was last updated"""

    category: Optional[Literal["EXTERNAL_WIRE", "EXTERNAL_ACH", "EXTERNAL_CHECK", "EXTERNAL_TRANSFER"]] = None

    currency: Optional[str] = None

    events: Optional[List[Event]] = None

    financial_account_token: Optional[str] = None

    payment_type: Optional[Literal["DEPOSIT", "WITHDRAWAL"]] = None

    pending_amount: Optional[int] = None

    result: Optional[Literal["APPROVED", "DECLINED"]] = None

    settled_amount: Optional[int] = None

    user_defined_id: Optional[str] = None
