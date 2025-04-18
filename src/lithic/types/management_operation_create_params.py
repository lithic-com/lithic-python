# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ManagementOperationCreateParams"]


class ManagementOperationCreateParams(TypedDict, total=False):
    amount: Required[int]

    category: Required[
        Literal[
            "MANAGEMENT_FEE",
            "MANAGEMENT_DISPUTE",
            "MANAGEMENT_REWARD",
            "MANAGEMENT_ADJUSTMENT",
            "MANAGEMENT_DISBURSEMENT",
        ]
    ]

    direction: Required[Literal["CREDIT", "DEBIT"]]

    effective_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    event_type: Required[
        Literal[
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
    ]

    financial_account_token: Required[str]

    token: str

    memo: str

    subtype: str

    user_defined_id: str
