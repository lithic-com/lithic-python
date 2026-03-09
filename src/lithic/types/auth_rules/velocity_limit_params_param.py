# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .velocity_limit_period_param import VelocityLimitPeriodParam
from .velocity_limit_filters_param import VelocityLimitFiltersParam

__all__ = ["VelocityLimitParamsParam"]


class VelocityLimitParamsParam(TypedDict, total=False):
    period: Required[VelocityLimitPeriodParam]
    """Velocity over the current day since 00:00 / 12 AM in Eastern Time"""

    scope: Required[Literal["CARD", "ACCOUNT"]]
    """The scope the velocity is calculated for"""

    filters: VelocityLimitFiltersParam

    limit_amount: Optional[int]
    """
    The maximum amount of spend velocity allowed in the period in minor units (the
    smallest unit of a currency, e.g. cents for USD). Transactions exceeding this
    limit will be declined.
    """

    limit_count: Optional[int]
    """
    The number of spend velocity impacting transactions may not exceed this limit in
    the period. Transactions exceeding this limit will be declined. A spend velocity
    impacting transaction is a transaction that has been authorized, and optionally
    settled, or a force post (a transaction that settled without prior
    authorization).
    """
