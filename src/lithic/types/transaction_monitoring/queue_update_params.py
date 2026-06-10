# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["QueueUpdateParams"]


class QueueUpdateParams(TypedDict, total=False):
    description: Optional[str]
    """New description for the queue, or `null` to clear it"""

    name: str
    """New name for the queue"""
