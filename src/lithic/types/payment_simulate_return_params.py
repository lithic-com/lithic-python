# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PaymentSimulateReturnParams"]


class PaymentSimulateReturnParams(TypedDict, total=False):
    payment_token: Required[str]
    """Payment Token"""

    return_reason_code: str
    """Return Reason Code"""
