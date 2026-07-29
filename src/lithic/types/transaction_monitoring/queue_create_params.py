# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["QueueCreateParams"]


class QueueCreateParams(TypedDict, total=False):
    name: Required[str]
    """Human-readable name of the queue"""

    allowed_resolutions: Optional[SequenceNotStr[str]]
    """Resolutions that can be recorded on cases in this queue.

    Omit or send `null` to use the default list. Values are free-form labels and
    must be non-empty and unique
    """

    description: Optional[str]
    """Optional description of the queue"""
