# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["BookTransferRetryParams"]


class BookTransferRetryParams(TypedDict, total=False):
    retry_token: Required[str]
    """Customer-provided token that will serve as an idempotency token.

    This token will become the transaction token.
    """
