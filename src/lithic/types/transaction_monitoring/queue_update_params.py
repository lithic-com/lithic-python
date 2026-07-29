# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["QueueUpdateParams"]


class QueueUpdateParams(TypedDict, total=False):
    allowed_resolutions: Optional[SequenceNotStr[str]]
    """
    New list of resolutions that can be recorded on cases in this queue, or `null`
    to revert to the default list. Values are free-form labels and must be non-empty
    and unique. Changing the list only affects what is selectable going forward; the
    `resolution` already stored on a case is preserved as-is
    """

    description: Optional[str]
    """New description for the queue, or `null` to clear it"""

    name: str
    """New name for the queue"""
