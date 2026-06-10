# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .case_activity_type import CaseActivityType

__all__ = ["CaseActivityEntry"]


class CaseActivityEntry(BaseModel):
    """A single entry in a case's activity feed"""

    token: str
    """Globally unique identifier for the activity entry"""

    actor_token: Optional[str] = None
    """Identifier of the actor that produced the activity entry"""

    created: datetime
    """Date and time at which the activity entry was created"""

    entry_type: CaseActivityType
    """The case field that changed, or the action that was taken, in an activity entry:

    - `STATUS` - The case status changed
    - `TITLE` - The case title changed
    - `ASSIGNED_TO` - The case assignee changed
    - `RESOLUTION_OUTCOME` - The resolution outcome was set or changed
    - `RESOLUTION_NOTES` - The resolution notes were set or changed
    - `TAGS` - The case tags changed
    - `PRIORITY` - The case priority changed
    - `COMMENT` - A comment was added or edited
    - `FILE` - A file was attached to the case
    """

    new_value: Optional[str] = None
    """New value of the changed field, when applicable"""

    previous_value: Optional[str] = None
    """Previous value of the changed field, when applicable"""
