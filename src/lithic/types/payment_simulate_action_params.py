# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PaymentSimulateActionParams"]


class PaymentSimulateActionParams(TypedDict, total=False):
    event_type: Required[
        Literal[
            "ACH_ORIGINATION_REVIEWED",
            "ACH_ORIGINATION_RELEASED",
            "ACH_ORIGINATION_PROCESSED",
            "ACH_ORIGINATION_SETTLED",
            "ACH_RECEIPT_SETTLED",
            "ACH_RETURN_INITIATED",
            "ACH_RETURN_PROCESSED",
            "ACH_RETURN_SETTLED",
        ]
    ]
    """Event Type"""

    decline_reason: Literal[
        "PROGRAM_TRANSACTION_LIMIT_EXCEEDED", "PROGRAM_DAILY_LIMIT_EXCEEDED", "PROGRAM_MONTHLY_LIMIT_EXCEEDED"
    ]
    """Decline reason"""

    return_reason_code: str
    """Return Reason Code"""
