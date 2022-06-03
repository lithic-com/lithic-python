# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["FundingSourceListParams"]


class FundingSourceListParams(TypedDict, total=False):
    account_token: str

    page: float

    page_size: float
