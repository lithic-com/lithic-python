# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .book_transfer_response import BookTransferResponse

__all__ = ["BookTransferTransactionCreatedWebhookEvent"]


class BookTransferTransactionCreatedWebhookEvent(BookTransferResponse):
    """Book transfer transaction"""

    event_type: Literal["book_transfer_transaction.created"]
    """The type of event that occurred."""
