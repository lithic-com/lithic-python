# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["VelocityLimitFiltersParam"]


class VelocityLimitFiltersParam(TypedDict, total=False):
    exclude_countries: Optional[SequenceNotStr[str]]
    """ISO-3166-1 alpha-3 Country Codes to exclude from the velocity calculation.

    Transactions matching any of the provided will be excluded from the calculated
    velocity.
    """

    exclude_mccs: Optional[SequenceNotStr[str]]
    """Merchant Category Codes to exclude from the velocity calculation.

    Transactions matching this MCC will be excluded from the calculated velocity.
    """

    include_countries: Optional[SequenceNotStr[str]]
    """ISO-3166-1 alpha-3 Country Codes to include in the velocity calculation.

    Transactions not matching any of the provided will not be included in the
    calculated velocity.
    """

    include_mccs: Optional[SequenceNotStr[str]]
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
    ]
    """PAN entry modes to include in the velocity calculation.

    Transactions not matching any of the provided will not be included in the
    calculated velocity.
    """
