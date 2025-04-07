# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["FinancialAccountUpdateStatusParams"]


class FinancialAccountUpdateStatusParams(TypedDict, total=False):
    status: Required[Literal["OPEN", "CLOSED", "SUSPENDED", "PENDING"]]
    """Status of the financial account"""

    substatus: Required[
        Optional[Literal["CHARGED_OFF_FRAUD", "END_USER_REQUEST", "BANK_REQUEST", "CHARGED_OFF_DELINQUENT"]]
    ]
    """Substatus for the financial account"""
