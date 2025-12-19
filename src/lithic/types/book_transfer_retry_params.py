# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BookTransferRetryParams"]


class BookTransferRetryParams(TypedDict, total=False):
    retry_token: Required[str]
    """Globally unique identifier for the retry."""
