# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["UploadConstraints"]


class UploadConstraints(BaseModel):
    """
    Constraints applied to a file upload, returned alongside the upload URL so clients can validate before uploading
    """

    accepted_mime_types: List[str]
    """MIME types accepted for the upload"""

    max_size_bytes: int
    """Maximum accepted file size, in bytes"""
