# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["HoldCreateParams"]


class HoldCreateParams(TypedDict, total=False):
    amount: Required[int]
    """Amount to hold in cents"""

    token: str
    """Customer-provided token for idempotency. Becomes the hold token."""

    expiration_datetime: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """When the hold should auto-expire"""

    memo: Optional[str]
    """Reason for the hold"""

    user_defined_id: str
    """User-provided identifier for the hold"""
