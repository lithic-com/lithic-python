# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DisputeUpdateParams"]


class DisputeUpdateParams(TypedDict, total=False):
    amount: int
    """Amount to dispute"""

    customer_filed_date: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date the customer filed the dispute"""

    customer_note: str
    """Customer description of dispute"""

    reason: Literal[
        "ATM_CASH_MISDISPENSE",
        "CANCELLED",
        "DUPLICATED",
        "FRAUD_CARD_NOT_PRESENT",
        "FRAUD_CARD_PRESENT",
        "FRAUD_OTHER",
        "GOODS_SERVICES_NOT_AS_DESCRIBED",
        "GOODS_SERVICES_NOT_RECEIVED",
        "INCORRECT_AMOUNT",
        "MISSING_AUTH",
        "OTHER",
        "PROCESSING_ERROR",
        "RECURRING_TRANSACTION_NOT_CANCELLED",
        "REFUND_NOT_PROCESSED",
    ]
    """Reason for dispute"""
