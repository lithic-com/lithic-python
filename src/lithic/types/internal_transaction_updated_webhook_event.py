# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .internal_transaction import InternalTransaction

__all__ = ["InternalTransactionUpdatedWebhookEvent"]


class InternalTransactionUpdatedWebhookEvent(InternalTransaction):
    event_type: Literal["internal_transaction.updated"]
    """The type of event that occurred."""
