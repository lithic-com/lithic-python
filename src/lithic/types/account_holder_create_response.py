# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountHolderCreateResponse"]


class AccountHolderCreateResponse(BaseModel):
    token: str
    """Globally unique identifier for the account holder."""

    account_token: str
    """Globally unique identifier for the account."""

    status: Literal["ACCEPTED", "PENDING_REVIEW", "PENDING_DOCUMENT", "PENDING_RESUBMIT", "REJECTED"]
    """KYC and KYB evaluation states.

    Note:

    - `PENDING_RESUBMIT` and `PENDING_DOCUMENT` are only applicable for the
      `KYC_ADVANCED` workflow.
    - `PENDING_REVIEW` is only applicable for the `KYB_BASIC` workflow.
    """

    status_reasons: List[
        Literal[
            "ADDRESS_VERIFICATION_FAILURE",
            "AGE_THRESHOLD_FAILURE",
            "COMPLETE_VERIFICATION_FAILURE",
            "DOB_VERIFICATION_FAILURE",
            "ID_VERIFICATION_FAILURE",
            "MAX_DOCUMENT_ATTEMPTS",
            "MAX_RESUBMISSION_ATTEMPTS",
            "NAME_VERIFICATION_FAILURE",
            "OTHER_VERIFICATION_FAILURE",
            "RISK_THRESHOLD_FAILURE",
            "WATCHLIST_ALERT_FAILURE",
        ]
    ]
    """Reason for the evaluation status."""

    created: Optional[datetime] = None
    """Timestamp of when the account holder was created."""

    external_id: Optional[str] = None
    """
    Customer-provided token that indicates a relationship with an object outside of
    the Lithic ecosystem.
    """
