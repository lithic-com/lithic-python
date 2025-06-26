# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from ..._models import BaseModel
from .rule_stats import RuleStats

__all__ = ["V2RetrieveReportResponse", "DailyStatistic"]


class DailyStatistic(BaseModel):
    current_version_statistics: Optional[RuleStats] = None
    """Detailed statistics for the current version of the rule."""

    date: datetime.date
    """The date (UTC) for which the statistics are reported."""

    draft_version_statistics: Optional[RuleStats] = None
    """Detailed statistics for the draft version of the rule."""


class V2RetrieveReportResponse(BaseModel):
    auth_rule_token: str
    """Auth Rule Token"""

    begin: datetime.date
    """The start date (UTC) of the report."""

    daily_statistics: List[DailyStatistic]
    """Daily evaluation statistics for the Auth Rule."""

    end: datetime.date
    """The end date (UTC) of the report."""
