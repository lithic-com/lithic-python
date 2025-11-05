# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentSimulateActionParams"]


class PaymentSimulateActionParams(TypedDict, total=False):
    event_type: Required[
        Literal[
            "ACH_ORIGINATION_REVIEWED",
            "ACH_ORIGINATION_RELEASED",
            "ACH_ORIGINATION_PROCESSED",
            "ACH_ORIGINATION_SETTLED",
            "ACH_RECEIPT_SETTLED",
            "ACH_RECEIPT_RELEASED",
            "ACH_RETURN_INITIATED",
            "ACH_RETURN_PROCESSED",
            "ACH_RETURN_SETTLED",
        ]
    ]
    """Event Type"""

    date_of_death: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Date of Death for ACH Return"""

    decline_reason: Literal[
        "PROGRAM_TRANSACTION_LIMIT_EXCEEDED", "PROGRAM_DAILY_LIMIT_EXCEEDED", "PROGRAM_MONTHLY_LIMIT_EXCEEDED"
    ]
    """Decline reason"""

    return_addenda: str
    """Return Addenda"""

    return_reason_code: str
    """Return Reason Code"""
