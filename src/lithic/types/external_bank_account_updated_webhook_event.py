# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .external_bank_account import ExternalBankAccount

__all__ = ["ExternalBankAccountUpdatedWebhookEvent"]


class ExternalBankAccountUpdatedWebhookEvent(ExternalBankAccount):
    event_type: Literal["external_bank_account.updated"]
    """The type of event that occurred."""
