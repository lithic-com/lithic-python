# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .case_status import CaseStatus
from .case_priority import CasePriority

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

    resolution: str
    """Resolution to record on the case.

    Must be one of the `allowed_resolutions` configured on the case's queue,
    otherwise the request is rejected with a `400`
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
