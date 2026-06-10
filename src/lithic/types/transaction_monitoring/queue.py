# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Queue", "CaseCounts"]


class CaseCounts(BaseModel):
    """Number of cases in the queue, broken down by status.

    A status is omitted
    when the queue has no cases in that status
    """

    assigned: Optional[int] = FieldInfo(alias="ASSIGNED", default=None)
    """Number of cases in the queue with status `ASSIGNED`"""

    closed: Optional[int] = FieldInfo(alias="CLOSED", default=None)
    """Number of cases in the queue with status `CLOSED`"""

    escalated: Optional[int] = FieldInfo(alias="ESCALATED", default=None)
    """Number of cases in the queue with status `ESCALATED`"""

    in_review: Optional[int] = FieldInfo(alias="IN_REVIEW", default=None)
    """Number of cases in the queue with status `IN_REVIEW`"""

    open: Optional[int] = FieldInfo(alias="OPEN", default=None)
    """Number of cases in the queue with status `OPEN`"""

    resolved: Optional[int] = FieldInfo(alias="RESOLVED", default=None)
    """Number of cases in the queue with status `RESOLVED`"""


class Queue(BaseModel):
    """A queue that groups transaction monitoring cases for review"""

    token: str
    """Globally unique identifier for the queue"""

    case_counts: CaseCounts
    """Number of cases in the queue, broken down by status.

    A status is omitted when the queue has no cases in that status
    """

    created: datetime
    """Date and time at which the queue was created"""

    description: Optional[str] = None
    """Optional description of the queue"""

    name: str
    """Human-readable name of the queue"""

    updated: datetime
    """Date and time at which the queue was last updated"""
