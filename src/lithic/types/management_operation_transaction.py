# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ManagementOperationTransaction", "Event"]


class Event(BaseModel):
    token: str

    amount: int

    created: datetime

    detailed_results: List[Literal["APPROVED"]]

    effective_date: date

    memo: str

    result: Literal["APPROVED", "DECLINED"]

    type: Literal[
        "CASH_BACK",
        "CURRENCY_CONVERSION",
        "INTEREST",
        "LATE_PAYMENT",
        "BILLING_ERROR",
        "PROVISIONAL_CREDIT",
        "CASH_BACK_REVERSAL",
        "CURRENCY_CONVERSION_REVERSAL",
        "INTEREST_REVERSAL",
        "LATE_PAYMENT_REVERSAL",
        "BILLING_ERROR_REVERSAL",
        "PROVISIONAL_CREDIT_REVERSAL",
        "RETURNED_PAYMENT",
        "RETURNED_PAYMENT_REVERSAL",
    ]

    subtype: Optional[str] = None


class ManagementOperationTransaction(BaseModel):
    token: str

    category: Literal["MANAGEMENT_FEE", "MANAGEMENT_DISPUTE", "MANAGEMENT_REWARD", "MANAGEMENT_ADJUSTMENT"]

    created: datetime

    currency: str

    direction: Literal["CREDIT", "DEBIT"]

    events: List[Event]

    financial_account_token: str

    pending_amount: int

    result: Literal["APPROVED", "DECLINED"]

    settled_amount: int

    status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED"]

    updated: datetime

    user_defined_id: Optional[str] = None
