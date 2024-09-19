# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypedDict

from .velocity_limit_params_period_window import VelocityLimitParamsPeriodWindow
from ..shared.velocity_limit_params_period_window import VelocityLimitParamsPeriodWindow

__all__ = ["VelocityLimitParams", "Filters"]


class Filters(TypedDict, total=False):
    include_countries: Optional[List[str]]
    """ISO-3166-1 alpha-3 Country Codes to include in the velocity calculation.

    Transactions not matching any of the provided will not be included in the
    calculated velocity.
    """

    include_mccs: Optional[List[str]]
    """Merchant Category Codes to include in the velocity calculation.

    Transactions not matching this MCC will not be included in the calculated
    velocity.
    """


class VelocityLimitParams(TypedDict, total=False):
    filters: Required[Filters]

    period: Required[Union[float, VelocityLimitParamsPeriodWindow]]
    """The size of the trailing window to calculate Spend Velocity over in seconds."""

    scope: Required[Literal["CARD", "ACCOUNT"]]

    limit_amount: Optional[float]
    """
    The maximum amount of spend velocity allowed in the period in minor units (the
    smallest unit of a currency, e.g. cents for USD). Transactions exceeding this
    limit will be declined.
    """

    limit_count: Optional[float]
    """
    The number of spend velocity impacting transactions may not exceed this limit in
    the period. Transactions exceeding this limit will be declined. A spend velocity
    impacting transaction is a transaction that has been authorized, and optionally
    settled, or a force post (a transaction that settled without prior
    authorization).
    """
