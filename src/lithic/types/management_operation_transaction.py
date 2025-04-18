# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ManagementOperationTransaction", "Event", "TransactionSeries"]


class Event(BaseModel):
    token: str

    amount: int

    created: datetime

    detailed_results: List[Literal["APPROVED"]]

    effective_date: date

    memo: str

    result: Literal["APPROVED", "DECLINED"]

    type: Literal[
        "LOSS_WRITE_OFF",
        "CASH_BACK",
        "CASH_BACK_REVERSAL",
        "CURRENCY_CONVERSION",
        "CURRENCY_CONVERSION_REVERSAL",
        "INTEREST",
        "INTEREST_REVERSAL",
        "LATE_PAYMENT",
        "LATE_PAYMENT_REVERSAL",
        "BILLING_ERROR",
        "BILLING_ERROR_REVERSAL",
        "PROVISIONAL_CREDIT",
        "PROVISIONAL_CREDIT_REVERSAL",
        "RETURNED_PAYMENT",
        "RETURNED_PAYMENT_REVERSAL",
        "DISPUTE_WON",
        "DISPUTE_WON_REVERSAL",
        "DISBURSE",
        "DISBURSE_REVERSAL",
    ]

    subtype: Optional[str] = None


class TransactionSeries(BaseModel):
    related_transaction_event_token: Optional[str] = None

    related_transaction_token: Optional[str] = None

    type: str


class ManagementOperationTransaction(BaseModel):
    token: str

    category: Literal[
        "MANAGEMENT_FEE", "MANAGEMENT_DISPUTE", "MANAGEMENT_REWARD", "MANAGEMENT_ADJUSTMENT", "MANAGEMENT_DISBURSEMENT"
    ]

    created: datetime

    currency: str

    direction: Literal["CREDIT", "DEBIT"]

    events: List[Event]

    financial_account_token: str

    pending_amount: int

    result: Literal["APPROVED", "DECLINED"]

    settled_amount: int

    status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED"]

    transaction_series: Optional[TransactionSeries] = None

    updated: datetime

    user_defined_id: Optional[str] = None
