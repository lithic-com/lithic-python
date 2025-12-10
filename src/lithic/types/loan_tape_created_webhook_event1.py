# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .financial_accounts.loan_tape import LoanTape

__all__ = ["LoanTapeCreatedWebhookEvent"]


class LoanTapeCreatedWebhookEvent(LoanTape):
    event_type: Literal["loan_tape.created"]
    """The type of event that occurred."""
