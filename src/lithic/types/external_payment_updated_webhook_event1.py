# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .external_payment import ExternalPayment

__all__ = ["ExternalPaymentUpdatedWebhookEvent"]


class ExternalPaymentUpdatedWebhookEvent(ExternalPayment):
    event_type: Literal["external_payment.updated"]
    """The type of event that occurred."""
