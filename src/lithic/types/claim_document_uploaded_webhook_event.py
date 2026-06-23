# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ClaimDocumentUploadedWebhookEvent", "UploadConstraints"]


class UploadConstraints(BaseModel):
    """Constraints that an uploaded file must satisfy."""

    accepted_mime_types: List[str]
    """MIME types accepted for upload"""

    max_size_bytes: Optional[int] = None
    """Maximum file size in bytes. Null if there is no enforced size limit"""


class ClaimDocumentUploadedWebhookEvent(BaseModel):
    token: str
    """Unique identifier for the document, in UUID format"""

    created: datetime
    """When the document was created"""

    download_url: Optional[str] = None
    """Presigned URL for downloading the uploaded document.

    Available once the document is being validated or has been accepted
    (`VALIDATING` or `ACCEPTED`)
    """

    download_url_expires_at: Optional[datetime] = None
    """When the download URL expires"""

    event_type: Literal["claim_document.uploaded"]
    """The type of event that occurred."""

    failure_reason: Optional[Literal["INVALID_MIME_TYPE", "FILE_TOO_LARGE", "FILE_EMPTY", "CORRUPT_FILE", "OTHER"]] = (
        None
    )
    """Reason the document failed validation. Null unless `status` is `REJECTED`"""

    name: str
    """Name provided when the upload intent was created"""

    requirement_id: Optional[str] = None
    """Identifier of the document requirement this document satisfies.

    Null for supplemental documents not tied to a specific requirement
    """

    status: Literal["PENDING", "VALIDATING", "ACCEPTED", "REJECTED"]
    """Current validation status of the document"""

    updated: datetime
    """When the document was last updated"""

    upload_constraints: Optional[UploadConstraints] = None
    """Constraints that an uploaded file must satisfy."""

    upload_url: Optional[str] = None
    """Presigned URL for uploading the file via HTTP PUT.

    Null after the upload window expires or after the document has been validated
    """

    upload_url_expires_at: Optional[datetime] = None
    """When the upload URL expires"""
