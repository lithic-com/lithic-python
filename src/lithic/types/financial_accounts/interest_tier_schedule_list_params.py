# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InterestTierScheduleListParams"]


class InterestTierScheduleListParams(TypedDict, total=False):
    after_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Return schedules with effective_date >= after_date (ISO format YYYY-MM-DD)"""

    before_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Return schedules with effective_date <= before_date (ISO format YYYY-MM-DD)"""

    for_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """Return schedule with effective_date == for_date (ISO format YYYY-MM-DD)"""
