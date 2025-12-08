# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "VelocityLimitPeriodParam",
    "TrailingWindowObject",
    "FixedWindowDay",
    "FixedWindowWeek",
    "FixedWindowMonth",
    "FixedWindowYear",
]


class TrailingWindowObject(TypedDict, total=False):
    duration: Required[int]
    """The size of the trailing window to calculate Spend Velocity over in seconds.

    The minimum value is 10 seconds, and the maximum value is 2678400 seconds (31
    days).
    """

    type: Required[Literal["CUSTOM"]]


class FixedWindowDay(TypedDict, total=False):
    """Velocity over the current day since 00:00 / 12 AM in Eastern Time"""

    type: Required[Literal["DAY"]]


class FixedWindowWeek(TypedDict, total=False):
    """
    Velocity over the current week since 00:00 / 12 AM in Eastern Time on specified `day_of_week`
    """

    type: Required[Literal["WEEK"]]

    day_of_week: int
    """The day of the week to start the week from.

    Following ISO-8601, 1 is Monday and 7 is Sunday. Defaults to Monday if not
    specified.
    """


class FixedWindowMonth(TypedDict, total=False):
    """
    Velocity over the current month since 00:00 / 12 AM in Eastern Time on specified `day_of_month`.
    """

    type: Required[Literal["MONTH"]]

    day_of_month: int
    """The day of the month to start from.

    Accepts values from 1 to 31, and will reset at the end of the month if the day
    exceeds the number of days in the month. Defaults to the 1st of the month if not
    specified.
    """


class FixedWindowYear(TypedDict, total=False):
    """
    Velocity over the current year since 00:00 / 12 AM in Eastern Time on specified `month` and `day_of_month`. This validates the month and day of the year to start from is a real date. In the event that February 29th is selected, in non-leap years, the window will start from February 28th.
    """

    type: Required[Literal["YEAR"]]

    day_of_month: int
    """The day of the month to start from.

    Defaults to the 1st of the month if not specified.
    """

    month: int
    """The month to start from.

    1 is January and 12 is December. Defaults to January if not specified.
    """


VelocityLimitPeriodParam: TypeAlias = Union[
    TrailingWindowObject, FixedWindowDay, FixedWindowWeek, FixedWindowMonth, FixedWindowYear
]
