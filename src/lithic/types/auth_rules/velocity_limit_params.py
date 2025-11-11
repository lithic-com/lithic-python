# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .velocity_limit_period import VelocityLimitPeriod

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

    include_pan_entry_modes: Optional[
        List[
            Literal[
                "AUTO_ENTRY",
                "BAR_CODE",
                "CONTACTLESS",
                "CREDENTIAL_ON_FILE",
                "ECOMMERCE",
                "ERROR_KEYED",
                "ERROR_MAGNETIC_STRIPE",
                "ICC",
                "KEY_ENTERED",
                "MAGNETIC_STRIPE",
                "MANUAL",
                "OCR",
                "SECURE_CARDLESS",
                "UNSPECIFIED",
                "UNKNOWN",
            ]
        ]
    ] = None
    """PAN entry modes to include in the velocity calculation.

    Transactions not matching any of the provided will not be included in the
    calculated velocity.
    """


class VelocityLimitParams(BaseModel):
    filters: Filters

    period: VelocityLimitPeriod
    """Velocity over the current day since 00:00 / 12 AM in Eastern Time"""

    scope: Literal["CARD", "ACCOUNT"]
    """The scope the velocity is calculated for"""

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
