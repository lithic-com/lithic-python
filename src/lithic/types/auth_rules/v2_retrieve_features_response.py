# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .velocity_limit_period import VelocityLimitPeriod

__all__ = ["V2RetrieveFeaturesResponse", "Feature", "FeatureFilters", "FeatureValue"]


class FeatureFilters(BaseModel):
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
    filters: FeatureFilters

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
