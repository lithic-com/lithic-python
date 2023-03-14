# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["DisputeInitiateEvidenceUploadResponse"]


class DisputeInitiateEvidenceUploadResponse(BaseModel):
    upload_url: Optional[str]
