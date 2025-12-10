# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .dispute_evidence import DisputeEvidence

__all__ = ["DisputeEvidenceUploadFailedWebhookEvent"]


class DisputeEvidenceUploadFailedWebhookEvent(DisputeEvidence):
    """Dispute evidence."""

    event_type: Literal["dispute_evidence.upload_failed"]
    """The type of event that occurred."""
