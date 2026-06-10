# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .case_status import CaseStatus
from .case_priority import CasePriority
from .resolution_outcome import ResolutionOutcome

__all__ = ["CaseUpdateParams"]


class CaseUpdateParams(TypedDict, total=False):
    actor_token: str
    """
    Optional client-provided identifier for the actor performing this action,
    recorded on the resulting activity entry. This value is supplied by the client
    (for example, your own internal user ID) and is not authenticated by Lithic
    """

    assignee: Optional[str]
    """New assignee for the case, or `null` to unassign"""

    priority: CasePriority
    """Priority level of a case, controlling queue ordering and SLA urgency"""

    resolution: ResolutionOutcome
    """Outcome recorded when a case is resolved:

    - `CONFIRMED_FRAUD` - The reviewed activity was confirmed to be fraudulent
    - `SUSPICIOUS_ACTIVITY` - The activity is suspicious but not confirmed fraud
    - `FALSE_POSITIVE` - The activity was legitimate and the alert was a false
      positive
    - `NO_ACTION_REQUIRED` - No further action is required
    - `ESCALATED_EXTERNAL` - The case was escalated to an external party
    """

    resolution_notes: str
    """Notes describing the resolution"""

    sla_deadline: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """New SLA deadline for the case, or `null` to clear it"""

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
    """Arbitrary key-value metadata to set on the case"""

    title: Optional[str]
    """New title for the case, or `null` to clear it"""
