# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["PaymentCreateParams", "MethodAttributes", "Hold"]


class PaymentCreateParams(TypedDict, total=False):
    amount: Required[int]

    external_bank_account_token: Required[str]

    financial_account_token: Required[str]

    method: Required[Literal["ACH_NEXT_DAY", "ACH_SAME_DAY"]]

    method_attributes: Required[MethodAttributes]

    type: Required[Literal["COLLECTION", "PAYMENT"]]

    token: str
    """Customer-provided token that will serve as an idempotency token.

    This token will become the transaction token.
    """

    hold: Hold
    """Optional hold to settle when this payment is initiated."""

    memo: str

    user_defined_id: str


class MethodAttributes(TypedDict, total=False):
    sec_code: Required[Literal["CCD", "PPD", "WEB"]]

    ach_hold_period: int
    """Number of days to hold the ACH payment"""

    addenda: Optional[str]


class Hold(TypedDict, total=False):
    """Optional hold to settle when this payment is initiated."""

    token: Required[str]
    """Token of the hold to settle when this payment is initiated."""
