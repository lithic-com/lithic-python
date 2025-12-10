# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .financial_accounts.statement import Statement

__all__ = ["StatementsCreatedWebhookEvent"]


class StatementsCreatedWebhookEvent(Statement):
    event_type: Literal["statements.created"]
    """The type of event that occurred."""
