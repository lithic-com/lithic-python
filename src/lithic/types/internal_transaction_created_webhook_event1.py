# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .internal_transaction import InternalTransaction

__all__ = ["InternalTransactionCreatedWebhookEvent"]


class InternalTransactionCreatedWebhookEvent(InternalTransaction):
    event_type: Literal["internal_transaction.created"]
    """The type of event that occurred."""
