# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .payment import Payment

__all__ = ["PaymentTransactionCreatedWebhookEvent"]


class PaymentTransactionCreatedWebhookEvent(Payment):
    """Payment transaction"""

    event_type: Literal["payment_transaction.created"]
    """The type of event that occurred."""
