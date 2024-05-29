# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PaymentSimulateReceiptParams"]


class PaymentSimulateReceiptParams(TypedDict, total=False):
    token: Required[str]
    """Payment token"""

    amount: Required[int]
    """Amount"""

    financial_account_token: Required[str]
    """Financial Account Token"""

    receipt_type: Required[Literal["RECEIPT_CREDIT", "RECEIPT_DEBIT"]]
    """Receipt Type"""

    memo: str
    """Memo"""
