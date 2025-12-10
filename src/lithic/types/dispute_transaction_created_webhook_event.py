# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .dispute_v2 import DisputeV2

__all__ = ["DisputeTransactionCreatedWebhookEvent"]


class DisputeTransactionCreatedWebhookEvent(DisputeV2):
    """
    The Dispute object tracks the progression of a dispute throughout its lifecycle.
    """

    event_type: Literal["dispute_transaction.created"]
    """The type of event that occurred."""
