# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List

from ..._models import BaseModel
from .report_stats import ReportStats

__all__ = ["V2RetrieveReportResponse", "DailyStatistic"]


class DailyStatistic(BaseModel):
    date: datetime.date
    """The date (UTC) for which the statistics are reported."""

    versions: List[ReportStats]
    """
    Statistics for each version of the rule that was evaluated during the reported
    day.
    """


class V2RetrieveReportResponse(BaseModel):
    auth_rule_token: str
    """Auth Rule Token"""

    begin: datetime.date
    """The start date (UTC) of the report."""

    daily_statistics: List[DailyStatistic]
    """Daily evaluation statistics for the Auth Rule."""

    end: datetime.date
    """The end date (UTC) of the report."""
