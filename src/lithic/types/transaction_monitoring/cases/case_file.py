# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel
from .file_status import FileStatus
from .upload_constraints import UploadConstraints

__all__ = ["CaseFile"]


class CaseFile(BaseModel):
    """A file attached to a case.

    Status-dependent fields are always present but may be `null`:
      - `upload_url`, `upload_url_expires`, and `upload_constraints` are populated when `status` is `PENDING` or `REJECTED`
      - `download_url` and `download_url_expires` are populated when `status` is `READY`
      - `failure_reason` is populated when `status` is `REJECTED`
    """

    token: str
    """Globally unique identifier for the file"""

    created: datetime
    """Date and time at which the file record was created"""

    download_url: Optional[str] = None
    """Presigned URL the client uses to download the file"""

    download_url_expires: Optional[datetime] = None
    """Date and time at which the download URL expires"""

    failure_reason: Optional[str] = None
    """Reason the file was rejected, when applicable"""

    mime_type: Optional[str] = None
    """MIME type of the file, available once the file is ready"""

    name: str
    """Name of the file"""

    size_bytes: Optional[int] = None
    """Size of the file in bytes, available once the file is ready"""

    status: FileStatus
    """Lifecycle status of a case file:

    - `PENDING` - An upload URL has been issued and the file is awaiting upload
    - `READY` - The file has been uploaded and validated; a download URL is
      available
    - `REJECTED` - File validation failed; see `failure_reason` for details
    """

    updated: datetime
    """Date and time at which the file record was last updated"""

    upload_constraints: Optional[UploadConstraints] = None
    """
    Constraints applied to a file upload, returned alongside the upload URL so
    clients can validate before uploading
    """

    upload_url: Optional[str] = None
    """Presigned URL the client uses to upload the file"""

    upload_url_expires: Optional[datetime] = None
    """Date and time at which the upload URL expires"""
