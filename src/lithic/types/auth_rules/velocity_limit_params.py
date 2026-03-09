# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .velocity_limit_period import VelocityLimitPeriod
from .velocity_limit_filters import VelocityLimitFilters

__all__ = ["VelocityLimitParams"]


class VelocityLimitParams(BaseModel):
    period: VelocityLimitPeriod
    """Velocity over the current day since 00:00 / 12 AM in Eastern Time"""

    scope: Literal["CARD", "ACCOUNT"]
    """The scope the velocity is calculated for"""

    filters: Optional[VelocityLimitFilters] = None

    limit_amount: Optional[int] = None
    """
    The maximum amount of spend velocity allowed in the period in minor units (the
    smallest unit of a currency, e.g. cents for USD). Transactions exceeding this
    limit will be declined.
    """

    limit_count: Optional[int] = None
    """
    The number of spend velocity impacting transactions may not exceed this limit in
    the period. Transactions exceeding this limit will be declined. A spend velocity
    impacting transaction is a transaction that has been authorized, and optionally
    settled, or a force post (a transaction that settled without prior
    authorization).
    """
