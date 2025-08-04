# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel
from .external_resource import ExternalResource

__all__ = ["ManagementOperationTransaction", "Event", "TransactionSeries"]


class Event(BaseModel):
    token: str

    amount: int

    created: datetime

    detailed_results: List[Literal["APPROVED", "INSUFFICIENT_FUNDS"]]

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
    """Unique identifier for the transaction"""

    created: datetime
    """ISO 8601 timestamp of when the transaction was created"""

    family: Literal["CARD", "PAYMENT", "TRANSFER", "INTERNAL", "EXTERNAL_PAYMENT", "MANAGEMENT_OPERATION"]

    status: Literal["PENDING", "SETTLED", "DECLINED", "REVERSED", "CANCELED"]
    """The status of the transaction"""

    updated: datetime
    """ISO 8601 timestamp of when the transaction was last updated"""

    category: Optional[
        Literal[
            "MANAGEMENT_FEE",
            "MANAGEMENT_DISPUTE",
            "MANAGEMENT_REWARD",
            "MANAGEMENT_ADJUSTMENT",
            "MANAGEMENT_DISBURSEMENT",
        ]
    ] = None

    currency: Optional[str] = None

    direction: Optional[Literal["CREDIT", "DEBIT"]] = None

    events: Optional[List[Event]] = None

    external_resource: Optional[ExternalResource] = None
    """External resource associated with the management operation"""

    financial_account_token: Optional[str] = None

    pending_amount: Optional[int] = None

    result: Optional[Literal["APPROVED", "DECLINED"]] = None

    settled_amount: Optional[int] = None

    transaction_series: Optional[TransactionSeries] = None

    user_defined_id: Optional[str] = None
