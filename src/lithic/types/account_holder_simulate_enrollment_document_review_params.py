# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["AccountHolderSimulateEnrollmentDocumentReviewParams"]


class AccountHolderSimulateEnrollmentDocumentReviewParams(TypedDict, total=False):
    document_upload_token: str
    """The account holder document upload which to perform the simulation upon."""

    status: Literal["UPLOADED", "ACCEPTED", "REJECTED"]
    """An account holder document's upload status for use within the simulation."""

    status_reasons: List[
        Literal["DOCUMENT_MISSING_REQUIRED_DATA", "DOCUMENT_UPLOAD_TOO_BLURRY", "INVALID_DOCUMENT_TYPE"]
    ]
    """Status reason that will be associated with the simulated account holder status.

    Only required for a `REJECTED` status.
    """
