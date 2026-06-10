# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from ..._models import BaseModel
from .case_entity import CaseEntity
from .case_status import CaseStatus
from .case_priority import CasePriority
from .resolution_outcome import ResolutionOutcome

__all__ = ["MonitoringCase"]


class MonitoringCase(BaseModel):
    """A transaction monitoring case"""

    token: str
    """Globally unique identifier for the case"""

    assignee: Optional[str] = None
    """Identifier of the user the case is currently assigned to"""

    collection_stopped: Optional[datetime] = None
    """Date and time at which transaction collection stopped for the case"""

    created: datetime
    """Date and time at which the case was created"""

    entity: Optional[CaseEntity] = None
    """The entity a case is associated with"""

    pending_transactions: bool
    """Whether the case still has transaction scopes pending resolution"""

    priority: CasePriority
    """Priority level of a case, controlling queue ordering and SLA urgency"""

    queue_token: str
    """Token of the queue the case belongs to"""

    resolution: Optional[ResolutionOutcome] = None
    """Outcome recorded when a case is resolved:

    - `CONFIRMED_FRAUD` - The reviewed activity was confirmed to be fraudulent
    - `SUSPICIOUS_ACTIVITY` - The activity is suspicious but not confirmed fraud
    - `FALSE_POSITIVE` - The activity was legitimate and the alert was a false
      positive
    - `NO_ACTION_REQUIRED` - No further action is required
    - `ESCALATED_EXTERNAL` - The case was escalated to an external party
    """

    resolution_notes: Optional[str] = None
    """Free-form notes describing the resolution"""

    resolved: Optional[datetime] = None
    """Date and time at which the case was resolved"""

    rule_token: Optional[str] = None
    """Token of the transaction monitoring rule that triggered the case"""

    sla_deadline: Optional[datetime] = None
    """Deadline by which the case is expected to be resolved"""

    status: CaseStatus
    """Status of a case as it progresses through the review workflow:

    - `OPEN` - The case has been created and is still collecting matching
      transactions
    - `ASSIGNED` - An analyst has been assigned and transaction collection has
      stopped
    - `IN_REVIEW` - The case is actively being investigated
    - `ESCALATED` - The case has been reviewed and requires additional oversight
    - `RESOLVED` - A determination has been made and a resolution recorded
    - `CLOSED` - The case is finalized
    """

    tags: Dict[str, str]
    """Arbitrary key-value metadata associated with the case"""

    title: Optional[str] = None
    """Short, human-readable summary of the case"""

    updated: datetime
    """Date and time at which the case was last updated"""
