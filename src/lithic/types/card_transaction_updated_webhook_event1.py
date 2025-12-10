# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .transaction import Transaction

__all__ = ["CardTransactionUpdatedWebhookEvent"]


class CardTransactionUpdatedWebhookEvent(Transaction):
    event_type: Literal["card_transaction.updated"]
    """The type of event that occurred."""
