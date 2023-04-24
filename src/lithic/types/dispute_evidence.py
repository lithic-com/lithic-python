# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DisputeEvidence"]


class DisputeEvidence(BaseModel):
    created: datetime
    """Timestamp of when first Dispute was reported."""

    dispute_token: str
    """Dispute token evidence is attached to."""

    token: str
    """Globally unique identifier."""

    upload_status: Literal["DELETED", "ERROR", "PENDING", "REJECTED", "UPLOADED"]
    """Upload status types:

    - `DELETED` - Evidence was deleted.
    - `ERROR` - Evidence upload failed.
    - `PENDING` - Evidence is pending upload.
    - `REJECTED` - Evidence was rejected.
    - `UPLOADED` - Evidence was uploaded.
    """

    download_url: Optional[str]
    """URL to download evidence. Only shown when `upload_status` is `UPLOADED`."""

    upload_url: Optional[str]
    """URL to upload evidence. Only shown when `upload_status` is `PENDING`."""
