# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FinancialAccountCreateParams"]


class FinancialAccountCreateParams(TypedDict, total=False):
    nickname: Required[str]

    type: Required[Literal["OPERATING"]]

    account_token: str
