# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .velocity_limit_period import VelocityLimitPeriod
from .velocity_limit_filters import VelocityLimitFilters

__all__ = ["V2RetrieveFeaturesResponse", "Feature", "FeatureValue"]


class FeatureValue(BaseModel):
    amount: int
    """
    Amount (in cents) for the given Auth Rule that is used as input for calculating
    the rule. For Velocity Limit rules this would be the calculated Velocity. For
    Conditional Rules using CARD*TRANSACTION_COUNT*\\** this will be 0
    """

    count: int
    """
    Number of velocity impacting transactions matching the given scope, period and
    filters
    """


class Feature(BaseModel):
    filters: VelocityLimitFilters

    period: VelocityLimitPeriod
    """Velocity over the current day since 00:00 / 12 AM in Eastern Time"""

    scope: Literal["CARD", "ACCOUNT"]
    """The scope the velocity is calculated for"""

    value: FeatureValue


class V2RetrieveFeaturesResponse(BaseModel):
    evaluated: datetime
    """Timestamp at which the Features were evaluated"""

    features: List[Feature]
    """Calculated Features used for evaluation of the provided Auth Rule"""
