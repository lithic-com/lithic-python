# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PaymentCreateParams", "MethodAttributes"]


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

    memo: str

    user_defined_id: str


class MethodAttributes(TypedDict, total=False):
    sec_code: Required[Literal["CCD", "PPD", "WEB"]]
