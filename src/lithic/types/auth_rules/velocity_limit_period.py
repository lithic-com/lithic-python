# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "VelocityLimitPeriod",
    "TrailingWindowObject",
    "FixedWindowDay",
    "FixedWindowWeek",
    "FixedWindowMonth",
    "FixedWindowYear",
]


class TrailingWindowObject(BaseModel):
    duration: int
    """The size of the trailing window to calculate Spend Velocity over in seconds.

    The minimum value is 10 seconds, and the maximum value is 2678400 seconds (31
    days).
    """

    type: Literal["CUSTOM"]


class FixedWindowDay(BaseModel):
    type: Literal["DAY"]


class FixedWindowWeek(BaseModel):
    type: Literal["WEEK"]

    day_of_week: Optional[int] = None
    """The day of the week to start the week from.

    Following ISO-8601, 1 is Monday and 7 is Sunday. Defaults to Monday if not
    specified.
    """


class FixedWindowMonth(BaseModel):
    type: Literal["MONTH"]

    day_of_month: Optional[int] = None
    """The day of the month to start from.

    Accepts values from 1 to 31, and will reset at the end of the month if the day
    exceeds the number of days in the month. Defaults to the 1st of the month if not
    specified.
    """


class FixedWindowYear(BaseModel):
    type: Literal["YEAR"]

    day_of_month: Optional[int] = None
    """The day of the month to start from.

    Defaults to the 1st of the month if not specified.
    """

    month: Optional[int] = None
    """The month to start from.

    1 is January and 12 is December. Defaults to January if not specified.
    """


VelocityLimitPeriod: TypeAlias = Union[
    TrailingWindowObject, FixedWindowDay, FixedWindowWeek, FixedWindowMonth, FixedWindowYear
]
