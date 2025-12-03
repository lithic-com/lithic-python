# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardBulkOrderUpdateParams"]


class CardBulkOrderUpdateParams(TypedDict, total=False):
    status: Required[Literal["LOCKED"]]
    """Status to update the bulk order to. Use LOCKED to finalize the order"""
