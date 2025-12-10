# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .transactions.events.enhanced_data import EnhancedData

__all__ = ["CardTransactionEnhancedDataUpdatedWebhookEvent"]


class CardTransactionEnhancedDataUpdatedWebhookEvent(EnhancedData):
    event_type: Literal["card_transaction.enhanced_data.updated"]
    """The type of event that occurred."""
