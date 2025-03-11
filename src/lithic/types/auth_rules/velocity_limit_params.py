# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .velocity_limit_params_period_window import VelocityLimitParamsPeriodWindow

__all__ = ["VelocityLimitParams", "Filters"]


class Filters(BaseModel):
    exclude_countries: Optional[List[str]] = None
    """ISO-3166-1 alpha-3 Country Codes to exclude from the velocity calculation.

    Transactions matching any of the provided will be excluded from the calculated
    velocity.
    """

    exclude_mccs: Optional[List[str]] = None
    """Merchant Category Codes to exclude from the velocity calculation.

    Transactions matching this MCC will be excluded from the calculated velocity.
    """

    include_countries: Optional[List[str]] = None
    """ISO-3166-1 alpha-3 Country Codes to include in the velocity calculation.

    Transactions not matching any of the provided will not be included in the
    calculated velocity.
    """

    include_mccs: Optional[List[str]] = None
    """Merchant Category Codes to include in the velocity calculation.

    Transactions not matching this MCC will not be included in the calculated
    velocity.
    """


class VelocityLimitParams(BaseModel):
    filters: Filters

    period: Union[int, VelocityLimitParamsPeriodWindow]
    """The size of the trailing window to calculate Spend Velocity over in seconds.

    The minimum value is 10 seconds, and the maximum value is 2678400 seconds (31
    days).
    """

    scope: Literal["CARD", "ACCOUNT"]

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
