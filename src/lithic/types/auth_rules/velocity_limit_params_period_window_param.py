# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypeAlias, TypedDict

__all__ = [
    "VelocityLimitParamsPeriodWindowParam",
    "TrailingWindowObject",
    "FixedWindowDay",
    "FixedWindowWeek",
    "FixedWindowMonth",
    "FixedWindowYear",
]


class TrailingWindowObject(TypedDict, total=False):
    duration: int
    """The size of the trailing window to calculate Spend Velocity over in seconds.

    The minimum value is 10 seconds, and the maximum value is 2678400 seconds (31
    days).
    """

    type: Literal["CUSTOM"]


class FixedWindowDay(TypedDict, total=False):
    type: Literal["DAY"]


class FixedWindowWeek(TypedDict, total=False):
    day_of_week: int
    """The day of the week to start the week from.

    Following ISO-8601, 1 is Monday and 7 is Sunday. Defaults to Monday if not
    specified.
    """

    type: Literal["WEEK"]


class FixedWindowMonth(TypedDict, total=False):
    day_of_month: int
    """The day of the month to start from.

    Accepts values from 1 to 31, and will reset at the end of the month if the day
    exceeds the number of days in the month. Defaults to the 1st of the month if not
    specified.
    """

    type: Literal["MONTH"]


class FixedWindowYear(TypedDict, total=False):
    day_of_month: int
    """The day of the month to start from.

    Defaults to the 1st of the month if not specified.
    """

    month: int
    """The month to start from.

    1 is January and 12 is December. Defaults to January if not specified.
    """

    type: Literal["YEAR"]


VelocityLimitParamsPeriodWindowParam: TypeAlias = Union[
    int,
    Literal["DAY", "WEEK", "MONTH", "YEAR"],
    TrailingWindowObject,
    FixedWindowDay,
    FixedWindowWeek,
    FixedWindowMonth,
    FixedWindowYear,
]
