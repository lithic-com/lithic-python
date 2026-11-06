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
            "CASH_BACK",
            "CURRENCY_CONVERSION",
            "INSTALLMENT_FEE",
            "LATE_PAYMENT",
            "BILLING_ERROR",
            "PROVISIONAL_CREDIT",
            "RETURNED_PAYMENT",
            "DISPUTE_WON",
            "DISBURSE",
            "ANNUAL",
            "QUARTERLY",
            "MONTHLY",
            "FEE",
        ]
    ]
    """Type of management operation to create.

    To reverse an existing management operation, use the reverse management
    operation endpoint
    """

    financial_account_token: Required[str]

    token: str
    """Client-provided token that will serve as an idempotency token.

    This token will become the transaction token.
    """

    memo: str

    on_closed_account: Literal["FAIL", "USE_SUSPENSE"]
    """What to do if the financial account is closed when posting an operation"""

    subtype: str

    user_defined_id: str
