# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExternalPaymentCreateParams"]


class ExternalPaymentCreateParams(TypedDict, total=False):
    amount: Required[int]

    category: Required[Literal["EXTERNAL_WIRE", "EXTERNAL_ACH", "EXTERNAL_CHECK", "EXTERNAL_TRANSFER"]]

    effective_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]

    financial_account_token: Required[str]

    payment_type: Required[Literal["DEPOSIT", "WITHDRAWAL"]]

    token: str

    memo: str

    progress_to: Literal["SETTLED", "RELEASED"]

    user_defined_id: str
