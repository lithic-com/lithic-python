# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .financial_account import FinancialAccount

__all__ = ["FinancialAccountUpdatedWebhookEvent"]


class FinancialAccountUpdatedWebhookEvent(FinancialAccount):
    event_type: Literal["financial_account.updated"]
    """The type of event that occurred."""
