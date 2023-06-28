# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountHolder"]


class AccountHolder(BaseModel):
    token: Optional[str]
    """Globally unique identifier for the account holder."""

    account_token: Optional[str]
    """Globally unique identifier for the account."""

    business_account_token: Optional[str]
    """
    Only applicable for customers using the KYC-Exempt workflow to enroll authorized
    users of businesses. Pass the account_token of the enrolled business associated
    with the AUTHORIZED_USER in this field.
    """

    status: Optional[Literal["ACCEPTED", "REJECTED", "PENDING_RESUBMIT", "PENDING_DOCUMENT"]]
    """KYC and KYB evaluation states.

    Note: `PENDING_RESUBMIT` and `PENDING_DOCUMENT` are only applicable for the
    `ADVANCED` workflow.
    """

    status_reasons: Optional[
        List[
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
    ]
    """Reason for the evaluation status."""
