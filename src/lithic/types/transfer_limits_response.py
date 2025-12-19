# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "TransferLimitsResponse",
    "Data",
    "DataDailyLimit",
    "DataDailyLimitCredit",
    "DataDailyLimitDebit",
    "DataMonthlyLimit",
    "DataMonthlyLimitCredit",
    "DataMonthlyLimitDebit",
    "DataProgramLimitPerTransaction",
    "DataProgramLimitPerTransactionCredit",
    "DataProgramLimitPerTransactionDebit",
]


class DataDailyLimitCredit(BaseModel):
    """Credit limits"""

    limit: int
    """The limit amount"""

    amount_originated: Optional[int] = None
    """Amount originated towards limit"""


class DataDailyLimitDebit(BaseModel):
    """Debit limits"""

    limit: int
    """The limit amount"""

    amount_originated: Optional[int] = None
    """Amount originated towards limit"""


class DataDailyLimit(BaseModel):
    """Daily limits with progress"""

    credit: DataDailyLimitCredit
    """Credit limits"""

    debit: DataDailyLimitDebit
    """Debit limits"""


class DataMonthlyLimitCredit(BaseModel):
    """Credit limits"""

    limit: int
    """The limit amount"""

    amount_originated: Optional[int] = None
    """Amount originated towards limit"""


class DataMonthlyLimitDebit(BaseModel):
    """Debit limits"""

    limit: int
    """The limit amount"""

    amount_originated: Optional[int] = None
    """Amount originated towards limit"""


class DataMonthlyLimit(BaseModel):
    """Monthly limits with progress"""

    credit: DataMonthlyLimitCredit
    """Credit limits"""

    debit: DataMonthlyLimitDebit
    """Debit limits"""


class DataProgramLimitPerTransactionCredit(BaseModel):
    """Credit limits"""

    limit: int
    """The limit amount"""

    amount_originated: Optional[int] = None
    """Amount originated towards limit"""


class DataProgramLimitPerTransactionDebit(BaseModel):
    """Debit limits"""

    limit: int
    """The limit amount"""

    amount_originated: Optional[int] = None
    """Amount originated towards limit"""


class DataProgramLimitPerTransaction(BaseModel):
    """Program transaction limits"""

    credit: DataProgramLimitPerTransactionCredit
    """Credit limits"""

    debit: DataProgramLimitPerTransactionDebit
    """Debit limits"""


class Data(BaseModel):
    company_id: str
    """Company ID"""

    daily_limit: DataDailyLimit
    """Daily limits with progress"""

    date: datetime.date
    """The date for the limit view (ISO format)"""

    is_fbo: bool
    """Whether the company is a FBO; based on the company ID prefix"""

    monthly_limit: DataMonthlyLimit
    """Monthly limits with progress"""

    program_limit_per_transaction: DataProgramLimitPerTransaction
    """Program transaction limits"""


class TransferLimitsResponse(BaseModel):
    data: List[Data]
    """List of transfer limits"""

    has_more: bool
    """Whether there are more transfer limits"""
