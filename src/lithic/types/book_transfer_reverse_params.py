# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["BookTransferReverseParams"]


class BookTransferReverseParams(TypedDict, total=False):
    memo: str
    """Optional descriptor for the reversal."""
