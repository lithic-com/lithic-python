# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DisputeEvidence"]


class DisputeEvidence(BaseModel):
    token: str
    """Globally unique identifier."""

    created: datetime
    """Timestamp of when dispute evidence was created."""

    dispute_token: str
    """Dispute token evidence is attached to."""

    upload_status: Literal["DELETED", "ERROR", "PENDING", "REJECTED", "UPLOADED"]
    """Upload status types:

    - `DELETED` - Evidence was deleted.
    - `ERROR` - Evidence upload failed.
    - `PENDING` - Evidence is pending upload.
    - `REJECTED` - Evidence was rejected.
    - `UPLOADED` - Evidence was uploaded.
    """

    download_url: Optional[str] = None
    """URL to download evidence. Only shown when `upload_status` is `UPLOADED`."""

    filename: Optional[str] = None
    """File name of evidence.

    Recommended to give the dispute evidence a human-readable identifier.
    """

    upload_url: Optional[str] = None
    """URL to upload evidence. Only shown when `upload_status` is `PENDING`."""
