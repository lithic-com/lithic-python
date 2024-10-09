# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountHolderSimulateEnrollmentDocumentReviewParams"]


class AccountHolderSimulateEnrollmentDocumentReviewParams(TypedDict, total=False):
    document_upload_token: Required[str]
    """The account holder document upload which to perform the simulation upon."""

    status: Required[Literal["UPLOADED", "ACCEPTED", "REJECTED", "PARTIAL_APPROVAL"]]
    """An account holder document's upload status for use within the simulation."""

    accepted_entity_status_reasons: List[str]
    """A list of status reasons associated with a KYB account holder in PENDING_REVIEW"""

    status_reason: Literal[
        "DOCUMENT_MISSING_REQUIRED_DATA",
        "DOCUMENT_UPLOAD_TOO_BLURRY",
        "FILE_SIZE_TOO_LARGE",
        "INVALID_DOCUMENT_TYPE",
        "INVALID_DOCUMENT_UPLOAD",
        "INVALID_ENTITY",
        "DOCUMENT_EXPIRED",
        "DOCUMENT_ISSUED_GREATER_THAN_30_DAYS",
        "DOCUMENT_TYPE_NOT_SUPPORTED",
        "UNKNOWN_FAILURE_REASON",
        "UNKNOWN_ERROR",
    ]
    """Status reason that will be associated with the simulated account holder status.

    Only required for a `REJECTED` status or `PARTIAL_APPROVAL` status.
    """
