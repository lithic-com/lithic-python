# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .financial_account import FinancialAccount

__all__ = ["FinancialAccountCreatedWebhookEvent"]


class FinancialAccountCreatedWebhookEvent(FinancialAccount):
    event_type: Literal["financial_account.created"]
    """The type of event that occurred."""
